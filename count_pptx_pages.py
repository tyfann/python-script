#!/usr/bin/env python3
import os
import pptx
import argparse
from os.path import exists, join, isdir

total = 0
def get_total_pages(folder, recursive=False):
	if not exists(folder):
		return "Error: No such file or directory: {}".format(folder)
	global total

	for subPath in os.listdir(folder):
		subPath = join(folder, subPath)
		if recursive:
			if isdir(subPath):
				get_total_pages(subPath, recursive)
		else:
			if subPath.endswith('.pptx'):
				presentation = pptx.Presentation(subPath)
				total += len(presentation.slides)
	return total

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('folder', type=str, help='path to the folder where pptx files are stored.')
	parser.add_argument('--recursive', '-r', action='store_true', help='search pptx files in the <folder> recursively.')
	args = parser.parse_args()
	total_pages = get_total_pages(args.folder, recursive=args.recursive)
	print("=======================================\nTotal pages in '%s': %d" % (args.folder, total_pages))
