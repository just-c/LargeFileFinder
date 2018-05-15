import os
import operator

from os.path import isfile, join
from convert import get_file_size_mb, normalize_path


class Crawler:
    # dictionary to store file names and sizes
    listing = {}

    # constructor
    def __init__(self, min_size=25):
        self.min_size = float(min_size)

    # recursively crawls the directory structure storing file names and sizes in an unordered dictionary.
    def crawl_dir(self, dir_to_crawl):
        read_write = os.access(dir_to_crawl, os.R_OK) and os.access(dir_to_crawl, os.W_OK)
        if read_write:
            try:
                for f in os.listdir(dir_to_crawl):
                    file = join(normalize_path(dir_to_crawl), f)
                    if isfile(file) and get_file_size_mb(file) > self.min_size:
                        # store the file name and size in a dictionary
                        self.listing[file] = get_file_size_mb(file)
                    else:
                        # recursively crawl the folders
                        self.crawl_dir(file)
            except WindowsError:
                pass

    def print_results(self):
        # sort the results from lowest to highest
        sorted_results = sorted(self.listing.items(), key=operator.itemgetter(1))

        # print em' out.
        for file_name, file_size in sorted_results:
            print(file_name + " - " + str(file_size) + "MB")
