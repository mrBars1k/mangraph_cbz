import os
import re
import zipfile
from config import MANGA_FOLDER, OUTPUT_FOLDER


def format_chapter_number(chapter: str) -> str:
    number = extract_num(chapter)

    if number.is_integer():
        return str(int(number))
    return str(number)


def extract_num(title: str) -> float:
    number = num_re.match(title)
    if not number:
        raise ValueError(f"Inappropriate name: {title}")
    return float(number.group(1))


pattern = r'^(\d+(?:\.\d+)?)'
num_re = re.compile(pattern)


def main():
    title = input("Enter the manga title (folder name): ")

    manga_path = os.path.expanduser(f"{MANGA_FOLDER}/{title}")
    output_path = os.path.expanduser(f"{OUTPUT_FOLDER}/{title}")

    os.makedirs(output_path, exist_ok=True)

    chapters = os.listdir(manga_path)
    chapters.sort(key=extract_num)

    for ch in chapters:
        pages_path = os.path.join(manga_path, ch)

        if not os.path.isdir(pages_path):
            continue

        pages = os.listdir(pages_path)
        pages.sort(key=lambda p: float(os.path.splitext(p)[0]))

        chapter_num = format_chapter_number(ch)
        filename = os.path.join(output_path, f"{chapter_num}.cbz")

        with zipfile.ZipFile(filename, 'w') as cbz:
            for p in pages:
                page_path = os.path.join(pages_path, p)
                cbz.write(page_path, arcname=p)

        print(filename)

    print("\nDone.")


if __name__ == "__main__":
    main()