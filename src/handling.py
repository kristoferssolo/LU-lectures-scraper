"""CSV file processing module"""

from pathlib import Path
import pandas


def read_file(directory, file_name) -> pandas.DataFrame:
    return pandas.read_csv(Path(directory, "CSVs", f"{file_name}.csv"), on_bad_lines="skip")


def write_xlsx(file, file_name, directory) -> None:
    file.to_excel(
        Path(directory, "XLSXs", f"{file_name}.xlsx"), index=False, header=True)
    print(f"Created {file_name}.xlsx file")
