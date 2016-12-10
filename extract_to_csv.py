import csv
import json
import re

def parse_json(filename='small.json'):
  with open(filename) as data_file:
    return json.load(data_file)

def main():
  timestamp = open('timestampMs.txt', 'r')
  latitude = open('latitudeE7.txt', 'r')
  longitude = open('longitudeE7.txt', 'r')

  csvfile = open('out.csv', 'wb')

  target = re.compile(r'(-?\d+)"?[,\n]$')

  limit = -1 # -1 means no limit
  i = 0
  while limit < 0 or i < limit:
    i += 1

    t_line = timestamp.readline()
    lat_line = latitude.readline()
    lon_line = longitude.readline()

    if '\n' not in t_line:
      exit(0)

    t_query = target.search(t_line)
    if t_query is None:
      print i, t_line, len(t_line)
    time = t_query.group(1)

    lat_query = target.search(lat_line)
    if lat_query is None:
      print i, lat_line, len(lat_line)
    lat = lat_query.group(1)

    lon_query = target.search(lon_line)
    if lon_query is None:
      print i, lon_line, len(lon_line)
    lon = lon_query.group(1)

    writeout = csv.writer(csvfile)
    writeout.writerow([time, lat, lon])

if __name__ == '__main__':
  main()
