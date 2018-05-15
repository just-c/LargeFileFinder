import os

from crawler import Crawler


def main():
    folder = input("Please specify the folder to check (i.e. C://Users/Me/Documents/): ")
    min_size = input("Please input the minimum file size to search for (MB): ")

    if folder and check_size_input(min_size):
        c = Crawler(min_size)
        c.crawl_dir(folder)
        c.print_results()


def check_crawl_folder(folder):
    try:
        os.path.isdir(folder)
        return True
    except:
        print(folder + " is not a valid folder.")
        return False


def check_size_input(size):
    try:
        float(size)
        return True
    except ValueError:
        print(size + " is not a valid size.")
        return False

main()
