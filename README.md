## How to use:

1. Specify the directory with the manga and the resulting one in the `config.py`;
2. Run `main.py` and enter the name of the directory with the required manga;
3. Wait until the script finishes running.

## How does it work:
The script takes the names of all directories in the specified location and then sorts them in ascending order, using only the number at the beginning of the folder name, ignoring any letters that come after.

Then, starting from the first chapter (its folder), the script begins to sort the pages, separating the file extension from the name, using only the number.

After these steps, each page is packed into a cbz archive until all pages are finished, after which the work moves on to the next chapter. 
This continues until all chapters are finished.

> [!WARNING]
> For the most accurate and predictable results, all folders and page files should be named with a number.

## Libraries used:
- re
- pathlib
- zipfile
