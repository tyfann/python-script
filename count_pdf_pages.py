#!/usr/bin/env python3
import argparse
from glob import glob
from os.path import exists, join
from PyPDF2 import PdfFileReader


def get_total_pages(folder, recursive=False):
    if not exists(folder):
        return "Error: No such file or directory: {}".format(folder)
    if recursive:
        pdf_list = glob(join(folder, "**/*.pdf"), recursive=True)
    else:
        pdf_list = glob(join(folder, "*.pdf"), recursive=False)

    pages = []
    for pdf in pdf_list:
        reader = PdfFileReader(pdf)
        num_page = reader.getNumPages()
        # print("%d pages <-- '%s'" % (num_page, pdf))
        pages.append(num_page)
    return sum(pages)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', type=str, help='path to the folder where PDF files are stored.')
    parser.add_argument('--recursive', '-r', action='store_true', help='search PDF files in the <folder> recursively.')
    args = parser.parse_args()
    total_pages = get_total_pages(args.folder, recursive=args.recursive)
    print("===============================\nTotal pages in '%s': %d" % (args.folder, total_pages))