import logging
from pathlib import Path
from shutil import copyfile
import sys
from threading import Thread


folders = []


def scan_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            scan_folder(el)


def copy_file(path: Path, output) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:].upper()
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
            except OSError as err:
                logging.error(err)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")
    while True:
        source = input("Source_folder >>> ")
        output = input("Destination_folder >>> ")
        source_path = Path(source)
        output_path = Path(output)
        if source_path.exists():
            if not source_path.is_dir():
                print(f"{source} isn't a directory")
            else:
                folders.append(source_path)
                scan_folder(source_path)
                threads = []
                for folder in folders:
                    th = Thread(target=copy_file, args=(folder, output_path))
                    th.start()
                    threads.append(th)
                [th.join() for th in threads]
                print(f"The directory {source_path} may be deleted.")
                break
        else:
            print(f"{source_path} doesn't exist")
            q = input("Y - for try again, other keys for exit! >>> ")
            if q == 'Y' or q == 'y':
                continue
            else:
                break
 