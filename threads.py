import sys
from pathlib import Path
from shutil import copyfile
from threading import Thread


folders = []

def folder_collect(path: Path) -> None:
    for item in path.iterdir():
        if item.is_dir():
            folders.append(item)
            folder_collect(item)

def copy_file(path: Path) -> None:
    for item in path.iterdir():
        if item.is_file():
            extension = item.suffix[1:]
            dest_folder = Path(sys.argv[2]) / extension
            try:
                dest_folder.mkdir(exist_ok=True, parents=True)
                copyfile(item, dest_folder / item.name)
            except OSError:
                print("Can not copy file.")

def main(*args):
    if len(sys.argv) != 3:
        print("It has to be source path and a destination path.")
    
    source = Path(sys.argv[1])
    folders.append(source)
    folder_collect(source)

    threads = []
    for folder in folders:
        thread = Thread(target=copy_file, args=(folder,))
        thread.start()
        threads.append(thread)

    [thread.join() for thread in threads]


if __name__ == "__main__":
    main()
