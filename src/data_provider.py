import mimetypes
import os
from scipy.io.arff import loadarff
from env import DIR


def get_file_type(filename):
    real_ext = os.path.splitext(filename)
    return real_ext[1] if len(real_ext) == 2 else mimetypes.guess_extension(filename)


def raw_data_to_numpy(filename):
    file_type = get_file_type(filename).replace(".", "")
    if file_type == "arff":
        return


class RawDataToNumpy(object):
    # Raw file to numpy transformers
    def arff(self, filename):
        return loadarff(filename)

    def __init__(self):
        self.instance = {}
        for dirname in os.listdir(DIR.rel_path(["data", "classification"])):
            if dirname != ".DS_Store":
                self.instance[dirname] = {}
                for filename in os.listdir(
                    DIR.rel_path(["data", "classification", dirname])
                ):
                    print(filename, get_file_type(filename))

        # 0_diabetic_retinopathy
        f_name = DIR.rel_path(
            [
                "data",
                "classification",
                "0_diabetic_retinopathy",
                "messidor_features.arff",
            ]
        )
        ext = get_file_type(f_name)
        content = getattr(self, ext.replace(".", ""))(f_name)
        print(content)


dp_classification = RawDataToNumpy()
print(vars(dp_classification))
