"""
Utility to collect time and place of lectures for each individual first year student.
"""
from pathlib import Path
from dowloader import download_file

BASE_DIR = Path(__file__).resolve().parent.parent
URL = "https://www.df.lu.lv/fileadmin/user_upload/LU.LV/Apaksvietnes/Fakultates/www.df.lu.lv/Studijas/Pamatstudijas/Informacija_studentiem/1kurss_2022R_sad_gr_07_publ.pdf"


def main() -> None:
    """Main function to run"""
    download_file(url=URL, path=BASE_DIR)


if __name__ == "__main__":
    main()
