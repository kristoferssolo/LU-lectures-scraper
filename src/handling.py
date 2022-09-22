"""CSV file processing module"""

from pathlib import Path
import pandas


def read_file(directory, file_name) -> pandas.DataFrame:
    """Read csv file"""
    dataframe = pandas.read_csv(
        Path(directory, "CSVs", f"{file_name}.csv"), on_bad_lines="skip")
    dataframe = dataframe[dataframe["Unnamed: 0"].notna()]
    dataframe.columns = ["Nr. p. k.", "Vārds", "Uzvārds",
                         "Plūsma", "Lekciju laiki", "Izlīdzinošais kurss matemātikā"]
    return dataframe


def write_xlsx(dataframe, file_name, directory) -> None:
    """Write dataframe to xlsx file"""
    dataframe.to_excel(
        Path(directory, "XLSXs", f"{file_name}.xlsx"), index=False, header=True)
    print(f"Created {file_name}.xlsx file")
