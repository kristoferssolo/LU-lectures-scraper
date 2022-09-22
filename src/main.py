"""
Utility to collect time and place of lectures for each individual first year student.
"""
from pathlib import Path
from handling import read_file, write_xlsx
from dowloader import download_file, convert_file

BASE_DIR = Path(__file__).resolve().parent.parent
DOWNLOADS_DIR = Path(BASE_DIR, "downloads")
URL = "https://www.df.lu.lv/fileadmin/user_upload/LU.LV/Apaksvietnes/Fakultates/www.df.lu.lv/Studijas/Pamatstudijas/Informacija_studentiem/1kurss_2022R_sad_gr_07_publ.pdf"
FILE_NAME = URL.rsplit("/", maxsplit=1)[-1].rsplit(".", maxsplit=1)[0]


def main() -> None:
    """Main function to run"""
    download_file(url=URL, file_name=FILE_NAME, directory=DOWNLOADS_DIR)
    convert_file(directory=DOWNLOADS_DIR)
    write_xlsx(read_file(directory=DOWNLOADS_DIR,
               file_name=FILE_NAME), file_name=FILE_NAME, directory=DOWNLOADS_DIR)


if __name__ == "__main__":
    main()
