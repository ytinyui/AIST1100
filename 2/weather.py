import datetime
import html
import json
import urllib.request


def dt_format(dt):
    return datetime.datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S%z').strftime("%Y-%m-%d %H:%M:%S")


with urllib.request.urlopen('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en') as f:
    response = json.loads(f.read())
print('1. Rainfall\n2. Temperature')
x = int(input('Which type of weather info? ')) - 1

type = ['rainfall', 'temperature']
value = ['max', 'value']
data = response[type[x]]['data']
place = [html.unescape(data[i]['place']) for i in range(len(data))]
result = [data[i][value[x]] for i in range(len(data))]
for i in range(len(place)):
    print(i + 1, '. ', place[i], sep='')

y = int(input('Which place? ')) - 1
print(
    f"The {type[x]} is {result[y]} {data[y]['unit']} in {place[y]} ", end='')
print(f"from {dt_format(response[type[x]]['startTime'])} to {dt_format(response[type[x]]['endTime'])}." if x ==
      0 else f"at {dt_format(response[type[x]]['recordTime'])}.")
