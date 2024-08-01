#!/usr/bin/env python3

import argparse
import os
import time
from datetime import datetime, timedelta

def search(directory, months):
    threshold = time.time() - (months * 30 * 24 * 60 * 60)
    old_files = []
    old_dirs = []
    directory = os.path.expanduser(directory)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.getatime(file_path) < threshold:
                    old_files.append(file_path)
            except (FileNotFoundError, PermissionError):
                continue
    
    print("Threshold:", months, "months")
    print()
    print("Old Files:")
    if len(old_files) == 0:
        print("No old files")
    else:
        for old_file in old_files:
            print(old_file)


def main():
    parser = argparse.ArgumentParser(description = "Search for files that haven't been accessed in a long time")
    parser.add_argument("directory", type=str, help="Directory to search in")
    parser.add_argument("months", type=float, help="Threshold in months")
    args = parser.parse_args()

    if len(vars(args)) != 2:
        parser.error("Please only pass in the number of months and directory to search in")

    search(args.directory, args.months)

if __name__ == '__main__':
    main()