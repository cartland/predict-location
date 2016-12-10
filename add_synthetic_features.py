import csv
import datetime
import json
import re

def main():
  input = open('out.csv', 'r')

  csvfile = open('out_synthetic.csv', 'wb')
  writeout = csv.writer(csvfile)

  limit = -1 # -1 means no limit
  i = 0
  while limit < 0 or i < limit:
    i += 1

    input_line = input.readline()

    if '\n' not in input_line:
      exit(0)

    timestampMs, latitudeE7, longitudeE7 = map(int, input_line.split(','))

    dt = datetime.datetime.fromtimestamp(timestampMs/1000.0)
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour
    minute = dt.minute

    row = [
            timestampMs,
            latitudeE7,
            longitudeE7,
            year,
            month,
            day,
            hour,
            minute
    ]
    writeout.writerow(row)

if __name__ == '__main__':
  main()
