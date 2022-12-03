import requests
import datetime
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


def search_stations_in_province(province, data):
    print(data[1]['city']['commune']['provinceName'])
    stations_in_province = []
    for station in data:
        if station['city']['commune']['provinceName'] == province.upper():
            stations_in_province.append(station)
    print(len(stations_in_province))
    return stations_in_province


def print_stations_names_from_list(station_list):
    station_index = 1
    for station in station_list:
        print(station_index, station['stationName'])
        station_index += 1


def choose_station_and_find_station_id(station_list):
    choose_station_by_user = 7
    station_id = station_list[choose_station_by_user - 1]['id']
    print(station_id)
    return station_id


def send_api_request_sensors(id):
    URL = "https://api.gios.gov.pl/pjp-api/rest/station/sensors/{}" #lista stanowisk pomiarowych
    URL = URL.format(id)
    print(URL)
    req = requests.get(url=URL)
    data = req.json()
    print(data)
    return data


def send_api_request_getData(id):
    URL = "https://api.gios.gov.pl/pjp-api/rest/data/getData/{}" #lista stanowisk pomiarowych
    URL = URL.format(id)
    print(URL)
    req = requests.get(url=URL)
    data = req.json()
    print(data)
    return data


def choose_sensor_and_find_sensor_id(sensor_list):
    choose_sensor_by_user = 1
    sensor_id = sensor_list[choose_sensor_by_user - 1]['id']
    print(sensor_id)
    return sensor_id


def print_sensor_names_from_list(sensor_list):
    sensor_index = 1
    for sensor in sensor_list:
        print(sensor_index, sensor['param']['paramName'])
        sensor_index += 1


def get_date_and_sensors_values_lists(data):
    date_list = []
    value_list = []
    temp = data['values']
    for measurement in temp:
        #print(measurement)
        date_list.append(measurement['date'])
        if measurement['value'] is None:
            value_list.append(0)
        else:
            value_list.append(measurement['value'])
    date_list.reverse()
    value_list.reverse()
    print(date_list)
    print(value_list)
    return date_list, value_list


def plot_graph(dates, values):
    plt.plot(dates, values)

    # naming the x axis
    plt.xlabel('x - axis')
    plt.tick_params(axis='x', rotation=85, labelsize=5)
    # naming the y axis
    plt.ylabel('y - axis')

    plt.grid(True, which='major')

    # giving a title to my graph
    plt.title('My first graph!')
    plt.margins(x=0, y=0)

    # function to show the plot
    plt.show()


def send_api_request():
    URL = "https://api.gios.gov.pl/pjp-api/rest/station/findAll" #lista stacji pomiarowych
    req = requests.get(url=URL)
    data = req.json()

    print(data)
    print(len(data))
    print(data[1])
    print(data[1]['city']['name'])

    stations = search_stations_in_province("opolskie", data)
    print_stations_names_from_list(stations)
    station_id = choose_station_and_find_station_id(stations)

    sensors = send_api_request_sensors(station_id)
    print_sensor_names_from_list(sensors)
    sensor_id = choose_sensor_and_find_sensor_id(sensors)
    sensor_data = send_api_request_getData(sensor_id)
    dates, values = get_date_and_sensors_values_lists(sensor_data)
    plot_graph(dates, values)



send_api_request()
