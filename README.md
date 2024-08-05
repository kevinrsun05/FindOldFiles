# Find Old Files
Python Script that searches for old files given a directory path and threshold. Displays file size + path name

Run the script with the following parameters (optional)

  1) directory path (-d argument)
  2) threshold in months (-m argument)

The default values are your HOME directory and 12 months

**Example running the script**

Windows: ```Python findOldFiles.py -d "~\Desktop" -m 12```

Linux: ```./findOldFiles.py -d "~/Desktop" -m 12```

**Note:** The script is currently ignoring files under 1 MB, so you can change that in the script where it says
```
if file_size > 1:
    old_files.append((file_path, file_size))
```
