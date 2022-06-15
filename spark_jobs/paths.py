import os


def get_path(file=__file__):
    return os.path.join(os.getcwd(),file)