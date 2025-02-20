"""
PRIMM: Python Data Processing
In this PRIMM Activity, you'll learn how to process a 
CSV file and complete some basic extraction techniques.

name - date
"""

import csv
from typing import Union

record = dict[str, Union[str, int, float]]

def get_records(data_filename: str) -> list[record]:
  """
  Gets records from a csv data file.
  Parameters:
    data_filename(str): The location and name of the csv file that contains the data
  Returns:
    list[dict[str, Union[int, str]]]: a list of records where each 
        record is a dictionary where the keys are strings 
        and the values can be int or str
  """
  records: list[record] = []
  with open(data_filename, "r", encoding='utf-8-sig') as data_file:
    reader: csv.DictReader = csv.DictReader(data_file)
    for record in reader:      
      records.append(record)

  return records


def convert_fields(records: list[record]) -> None:
  for record in records:
    record["SHIFT"] = record["SHIFT"]
  for record in records:
    record["OFFENSE"] = record["OFFENSE"]


def calculate_average(records, k: str) -> float:
  total: int = 0
  for record in records:
    total += record[k]
  
  return total / len(records)



def summarize_by_shift(records: list[record]) -> dict[str, int]:
  summary: dict[str, int] = {} # Setup empty dictonary
  
  for r in records:
    shift: str = r["SHIFT"]
    if shift in summary:
      summary[shift] += 1
    else:
      summary[shift] = 1

  return summary


def summarize_by_time(records: list[record]) -> dict[str, int]:
  summary: dict[str, int] = {}

  for r in records:
    time: str = r["REPORT_DAT"][11:15]
    hour, _ = time.split(":")
    
    if hour in summary:
      summary[hour] += 1
    else:
      summary[hour] = 1
  
  return summary
    

def summarize_by_crime(records: list[record]) -> dict[str, int]:
  summary: dict[str, int] = {} # Setup empty dictonary
  
  for r in records:
    crime: str = r["OFFENSE"]
    if crime in summary:
      summary[crime] += 1
    else:
      summary[crime] = 1

  return summary



def main() -> None:
  data_filename: str = "resources/Crimes.csv"
  records: list[record] = get_records(data_filename)
  convert_fields(records)


  shift: dict[str, int] = summarize_by_shift(records)
  time: dict[str, int] = summarize_by_time(records)
  crime: dict[str, int] = summarize_by_crime(records)


  for daytime in shift.keys():
    print(f"{daytime}: {shift[daytime]}")

  for hour in time.keys():
    print(f"{hour}: {time[hour]}")
  
  for count in crime.keys():
    print(f"{count}:{crime[count]}")

  print(f"{len(records)} records read in...")




if __name__ == "__main__":
  main()