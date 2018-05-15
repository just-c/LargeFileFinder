import os

byte_size = 1024


def convert_to(size, unit="MB"):
    units = {"KB": 1, "MB": 2, "GB": 3}

    for i in range(units[unit]):
        size = size / byte_size

    return size


def get_file_size(file, unit="MB"):
    return convert_to(os.path.getsize(file), unit)


def normalize_path(file):
    return file.replace("/", "\\")
