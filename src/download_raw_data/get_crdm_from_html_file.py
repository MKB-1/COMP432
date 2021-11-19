import re
import time
import requests
from bs4 import BeautifulSoup
from env import DIR


def get_crdm_from_file():
    cr_data_models = {"classification": {}, "regression": {}}
    with open(
        f"{DIR.rel_path(['info', 'default_project.html'])}", mode="rb"
    ) as default_project_html_file:
        # Make soup
        soup = BeautifulSoup(default_project_html_file, "html.parser")

        # Find ordered list with "uri_datalist" as className (make sure to add in default_project.html)
        ols = soup.find_all(attrs={"class": "uri_datalist"})

        # Iterate through classification and regression lists
        for idx, ol in enumerate(ols):
            for index, (uci_url, display_name) in enumerate(
                [
                    (elem["href"], "".join(elem.children))
                    for elem in ol.find_all("a", href=True)
                ]
            ):
                # Make key by modifying value to python casing
                key = re.sub(r"[\s|-]", "_", re.sub(r"[(|)]", "", display_name)).lower()
                key = f"{index}_{key}"
                # Append to dict with key: {uci_url, display_name}
                cr_data_models[list(cr_data_models.keys())[idx]][key] = {
                    "uci_url": uci_url,
                    "display_name": display_name,
                }
    return cr_data_models


def append_data_folder_url_to_crdm(crdm):
    copy = crdm.copy()
    for key, val in crdm.items():
        for key, dataset_model in val.items():
            print(key, dataset_model)
            r = requests.get(dataset_model["uci_url"], allow_redirects=True)
            soup = BeautifulSoup(str(r.content), "html.parser")
            match = soup.find("a", string="Data Folder")
            time.sleep(0.5)
            val[key][
                "data_folder_url"
            ] = f"https://archive.ics.uci.edu/ml/{match['href'].replace('../','')}"
    return copy


# cr_data_models = get_crdm_from_file()
# cr_data_models = append_data_folder_url_to_crdm(cr_data_models)
# print(cr_data_models)
