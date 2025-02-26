"""
PRIMM: Python Data Processing
In this PRIMM Activity, you'll learn how to process a 
CSV file and complete some basic extraction techniques.

Seth Hays - February
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


def calculate_duration(crimes) -> float:
  hour_difference: int = 0
  minute_difference: int = 0
  average: float = 0.0
  empty: str = ""
  crime: str = ""

  for i in range(len(crimes)):
    empty = crimes[i]
    empty = empty[6:8]

    if empty != "":
        crime = crimes[i]

        start_hour: int = int(crime[0:2])
        start_minute: int = int(crime[3:5])
        end_hour: int = int(crime[6:8])
        end_minute: int = int(crime[9:11])

        hour_difference = end_hour - start_hour

        if end_minute > start_minute:
          minute_difference = end_minute - start_minute
        elif end_minute < start_minute:
          minute_difference = start_minute - end_minute
        else:
          minute_difference = 0
        
        average += (hour_difference * 60) + minute_difference
    
    average = average / len(crimes)
    return average


def summarize_by_duration(records: list[record]) -> float:  
  theft_auto: list[str] = []
  theft_other: list[str] = []
  homicide: list[str] = []
  motor_theft: list[str] = []
  robbery: list[str] = []
  assault: list[str] = []
  arson: list[str] = []
  burglary: list[str] = []
  sa: list[str] = []
  crime_count: dict[str, float] = {'THEFT F/AUTO' : 0.0, 'THEFT/OTHER' : 0.0, 'HOMICIDE' : 0.0, 'MOTOR VEHICLE THEFT' : 0.0, 'ROBBERY' : 0.0, 'ASSAULT W/DANGEROUS WEAPON' : 0.0, 'ARSON' : 0.0, 'BURGLARY' : 0.0, 'SA' : 0.0}
  crime: str = ""

  for r in records:
    crime = r['OFFENSE']

    # Adding all the start and end times to a list
    if crime == "THEFT F/AUTO":
      theft_auto.append(f"{r["START_DATE"][11:13]} {r["START_DATE"][14:16]} {r["END_DATE"][11:13]} {r["END_DATE"][14:16]}")

    elif crime == "THEFT/OTHER":
      theft_other.append(f"{r["START_DATE"][11:13]} {r["START_DATE"][14:16]} {r["END_DATE"][11:13]} {r["END_DATE"][14:16]}")
    
    elif crime == "HOMICIDE":
      homicide.append(f"{r["START_DATE"][11:13]} {r["START_DATE"][14:16]} {r["END_DATE"][11:13]} {r["END_DATE"][14:16]}")

    elif crime == "MOTOR VEHICLE THEFT":
      motor_theft.append(f"{r["START_DATE"][11:13]} {r["START_DATE"][14:16]} {r["END_DATE"][11:13]} {r["END_DATE"][14:16]}")

    elif crime == "ROBBERY":
      robbery.append(f"{r["START_DATE"][11:13]} {r["START_DATE"][14:16]} {r["END_DATE"][11:13]} {r["END_DATE"][14:16]}")

    elif crime == "ASSAULT W/DANGEROUS WEAPON":
      assault.append(f"{r["START_DATE"][11:13]} {r["START_DATE"][14:16]} {r["END_DATE"][11:13]} {r["END_DATE"][14:16]}")  

    elif crime == "ARSON":
      arson.append(f"{r["START_DATE"][11:13]} {r["START_DATE"][14:16]} {r["END_DATE"][11:13]} {r["END_DATE"][14:16]}")

    elif crime == "BURGLARY":
      burglary.append(f"{r["START_DATE"][11:13]} {r["START_DATE"][14:16]} {r["END_DATE"][11:13]} {r["END_DATE"][14:16]}")
      
    else:
      sa.append(f"{r["START_DATE"][11:13]} {r["START_DATE"][14:16]} {r["END_DATE"][11:13]} {r["END_DATE"][14:16]}")
    
    crime_count['THEFT F/AUTO'] = (calculate_duration(theft_auto))
    crime_count['THEFT/OTHER'] = (calculate_duration(theft_other))
    crime_count['HOMICIDE'] = (calculate_duration(homicide))
    crime_count['MOTOR VEHICLE THEFT'] = (calculate_duration(motor_theft))
    crime_count['ROBBERY'] =(calculate_duration(robbery))
    crime_count['ASSAULT W/DANGEROUS WEAPON'] = (calculate_duration(assault))
    crime_count['ARSON'] = (calculate_duration(arson))
    crime_count['BURGLARY'] = (calculate_duration(burglary))
    crime_count['SA'] = (calculate_duration(sa))

    return crime_count

    
def main() -> None:
  data_filename: str = "resources/Crimes.csv"
  records: list[record] = get_records(data_filename)
  convert_fields(records)


  shift: dict[str, int] = summarize_by_shift(records)
  time: dict[str, int] = summarize_by_time(records)
  crime: dict[str, int] = summarize_by_crime(records)
  duration: dict[str, float] = summarize_by_duration(records)


  for daytime in shift.keys():
    print(f"{daytime}: {shift[daytime]}")

  print("")

  for hour in time.keys():
    print(f"{hour}: {time[hour]}")
  
  print("")


  for count in crime.keys():
    print(f"{count}:{crime[count]}")
  
  print("")

  for length in duration.keys():
    print(f"{length}:{duration[length]} minutes")

  print(f"{len(records)} records read in...")




if __name__ == "__main__":
  main()