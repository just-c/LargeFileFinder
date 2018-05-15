import os

byte_size = 1024


def convert_to(size, unit="MB"):
    units = {"KB": 1, "MB": 2, "GB": 3}

    for i in range(2):
        size = size / byte_size

    return size


def get_file_size_mb(file):
    return convert_to(os.path.getsize(file), "MB")


def normalize_path(file):
    return file.replace("/", "\\")
