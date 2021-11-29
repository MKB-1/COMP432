import get_crdm_from_html_file as get_crdm
import download_data_from_crdm as download_data


if __name__ == '__main__':
    cr_data_models = get_crdm.get_crdm_from_file()
    cr_data_models = get_crdm.append_data_folder_url_to_crdm(cr_data_models)
    crdm_new = download_data.append_download_links_to_crdm(download_data.crdm)
    download_data.create_folder_download_files(crdm_new)