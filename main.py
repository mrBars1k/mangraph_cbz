import os
import re
import zipfile

title = input("Введите название манги: ")

path = os.path.expanduser(f"~/mnt/khaine/manga/{title}")
output_path = os.path.expanduser(f"~/mnt/khaine/output/{title}")
os.makedirs(output_path, exist_ok=True)

pattern = r'^(\d+(?:\.\d+)?)'
num_re = re.compile(pattern)

chapters = os.listdir(path)
chapters.sort(key=lambda ch: float(num_re.match(ch).group(1)))

for ch in chapters:
    pages_path = os.path.join(path, ch)

    if not os.path.isdir(pages_path):
        continue

    pages = os.listdir(pages_path)
    pages.sort(key=lambda p: float(os.path.splitext(p)[0]))

    filename = os.path.join(output_path, f"{ch}.cbz")

    with zipfile.ZipFile(filename, 'w') as cbz:
        for p in pages:
            page_path = os.path.join(pages_path, p)
            cbz.write(page_path, arcname=p)

    print(filename)

for name in os.listdir(output_path):
    if not name.endswith(".cbz"):
        continue

    m = num_re.match(name)
    if not m:
        continue

    new_name = f"{m.group(1)}.cbz"

    old_path = os.path.join(output_path, name)
    new_path = os.path.join(output_path, new_name)

    if old_path != new_path:
        os.rename(old_path, new_path)
        print(f"{name} --> {new_name}")

print("\nРабота завершена.")
