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
                    file_size = os.path.getsize(file_path) / (1024 * 1024)
                    if file_size > 1:
                        old_files.append((file_path, file_size))
            except (FileNotFoundError, PermissionError):
                continue
    
    print()
    print("Directory:", directory)
    print("Threshold:", months, "months")
    print()
    print("Old Files:")
    if len(old_files) == 0:
        print("No old files")
    else:
        for old_file in old_files:
            print(f"SIZE: {old_file[1]:.2f} MB              Path: {old_file[0]}")
    print()


def main():
    parser = argparse.ArgumentParser(description = "Search for files that haven't been accessed in a long time")
    parser.add_argument("-d", "--directory", nargs = "?", type=str, default = "~", help="Directory to search in")
    parser.add_argument("-m", "--months", nargs = "?", type=float, default = "12", help="Threshold in months")
    args = parser.parse_args()

    search(args.directory, args.months)

if __name__ == '__main__':
    main()