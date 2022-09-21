"""
PDF file download module
"""

from pathlib import Path
from requests import get


def download_file(url, base_path) -> None:
    """Downloads file from given url"""
    downloads_dir = Path(base_path, "downloads")
    create_dir(downloads_dir)
    response = get(url)
    with open(Path(downloads_dir, url.split("/")[-1]), "wb") as file:
        file.write(response.content)


def create_dir(path) -> None:
    """Created directory if doesn't exist"""
    Path(path).mkdir(exist_ok=True)
