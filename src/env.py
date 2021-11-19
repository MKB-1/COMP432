import os
from types import SimpleNamespace
from typing import Any


class Dir(SimpleNamespace):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.ROOT = os.path.dirname(os.path.abspath(__file__))

    def rel_path(self, path_arr):
        return os.path.join(self.ROOT, *path_arr)


DIR = Dir()

name = "hey"
