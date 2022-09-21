"""
PDF file download module
"""

from pathlib import Path
from requests import get


def download_file(url, path) -> None:
    """Downloads file from given url"""
    response = get(url)
    with open(Path(path, "downloads", url.split("/")[-1]), "wb") as file:
        file.write(response.content)
