import re
import zipfile
from pathlib import Path
from config import MANGA_FOLDER, OUTPUT_FOLDER


def extract_num(title: str) -> float:
    number = num_re.match(title)
    if not number:
        raise ValueError(f"Inappropriate name: {title}")
    return float(number.group(1))


def format_chapter_number(chapter: str) -> str:
    number = extract_num(chapter)

    if number.is_integer():
        return str(int(number))
    return str(number)


pattern = r'^(\d+(?:\.\d+)?)'
num_re = re.compile(pattern)


def main():
    title = input("Enter the manga title (folder name): ")

    manga_path = (Path(MANGA_FOLDER) / title).expanduser()
    output_path = (Path(OUTPUT_FOLDER) / title).expanduser()

    if not manga_path.exists():
        raise ValueError(f"Manga folder doesn't exists: {manga_path}")

    output_path.mkdir(parents=True, exist_ok=True)

    chapters = [i.name for i in manga_path.iterdir() if i.is_dir()]
    chapters.sort(key=extract_num)

    for ch in chapters:
        pages_path = manga_path / ch

        pages = [p for p in pages_path.iterdir() if p.is_file()]
        pages.sort(key=lambda p: int(p.stem))

        chapter_num = format_chapter_number(ch)
        archive = output_path / f"{chapter_num}.cbz"

        with zipfile.ZipFile(archive, 'w') as cbz:
            for page in pages:
                cbz.write(page, arcname=page.name)

        print(archive_path)

    print("\nDone.")


if __name__ == "__main__":
    main()