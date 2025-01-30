"""
PRIMM: Python Data Processing
In this PRIMM Activity, you'll learn how to process a 
CSV file and complete some basic extraction techniques.

name - date
"""

import csv
from typing import Union

def get_records(data_filename: str) -> list[dict[str, Union[str, int]]]:
  """
  Gets records from a csv data file.
  Parameters:
    data_filename(str): The location and name of the csv file that contains the data
  Returns:
    list[dict[str, Union[int, str]]]: a list of records where each 
        record is a dictionary where the keys are strings 
        and the values can be int or str
  """
  records: list[dict[str,Union[str, int]]] = []
  with open(data_filename, "r", encoding='utf-8-sig') as data_file:
    reader: csv.DictReader = csv.DictReader(data_file)
    for record in reader:      
      records.append(record)

  return records

def main() -> None:
  data_filename: str = "resources/stolen_bikes.csv"
  records: list[dict[str, Union[str, int]]] = get_records(data_filename)

  print(f"{len(records)} records read in.")
  print(records[0])
  print(records[0]["District"])


if __name__ == "__main__":
  main()