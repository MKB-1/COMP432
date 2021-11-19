import os
import requests
from bs4 import BeautifulSoup

from src.download_raw_data.classification_regression_datamodels import crdm
from src.env import DIR


def create_directory_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)


def append_download_links_to_crdm(crdm):
    copy = crdm.copy()
    for key, val in crdm.items():
        # Create classification and regression folders if not exists
        create_directory_if_not_exists(DIR.rel_path(["download_raw_data", key]))

        for dataset_name, dataset_model in val.items():
            # Create dataset content folder if not exists
            create_directory_if_not_exists(
                DIR.rel_path(["download_raw_data", key, dataset_name])
            )

            # Create soup with download_raw_data directory
            r = requests.get(dataset_model["data_folder_url"], allow_redirects=True)
            soup = BeautifulSoup(str(r.content), "html.parser")

            # Retrieve download links for all files
            download_links = soup.find_all(
                "a", string=lambda x: "Parent Directory" not in x
            )

            copy[key][dataset_name]["data_download_links"] = [
                f"{dataset_model['data_folder_url']}{link['href']}"
                for link in download_links
            ]
    return copy


def create_folder_download_files(crdm):
    for key, val in crdm.items():
        # Create classification and regression folders if not exists
        create_directory_if_not_exists(DIR.rel_path(["download_raw_data", key]))

        for dataset_name, dataset_model in val.items():
            print(f"Downloading dataset {key} - {dataset_name}")

            # Create dataset content folder if not exists
            create_directory_if_not_exists(
                DIR.rel_path(["download_raw_data", key, dataset_name])
            )

            # Create soup with download_raw_data directory
            for url in dataset_model["data_download_links"]:
                f_target = requests.get(url, allow_redirects=True)
                with open(
                    DIR.rel_path(
                        [
                            "download_raw_data",
                            key,
                            dataset_name,
                            str(url).split("/")[-1],
                        ]
                    ),
                    "wb",
                ) as file:
                    for chunk in f_target.iter_content(chunk_size=1024):
                        file.write(chunk)


crdm_new = append_download_links_to_crdm(crdm)

create_folder_download_files(crdm_new)
