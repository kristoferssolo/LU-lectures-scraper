"""
PDF file download module
"""

from pathlib import Path
import requests
import tabula


def download_file(url, file_name, directory) -> None:
    """Downloads file from given url"""
    create_dir(directory)
    response = requests.get(url)
    with open(Path(directory, "PDFs", f"{file_name}.pdf"), "wb") as file:
        file.write(response.content)
    print(f"Downloaded {file_name}.pdf file")


def create_dir(path) -> None:
    """Created directory if doesn't exist"""
    directories = ["", "CSVs", "PDFs", "XLSXs"]
    for directory in directories:
        directory = Path(path, directory)
        if not directory.is_dir():
            Path(path, directory).mkdir()
            print(f"Created {directory} directory")


def convert_file(directory) -> None:
    """Converts PDF file to CSV"""
    tabula.convert_into_by_batch(
        Path(directory, "PDFs"), output_format="csv", pages="all")
    for file in Path(directory, "PDFs").glob("*.csv"):
        file.rename(Path(directory, "CSVs", file.name))
        print(f"Created {file.name} file")
