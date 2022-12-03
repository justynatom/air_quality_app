class Data_parser:
    def search_stations_in_province(self, province, data):
        print(data[1]['city']['commune']['provinceName'])
        stations_in_province = []
        for station in data:
            if station['city']['commune']['provinceName'] == province.upper():
                stations_in_province.append(station)
        print(len(stations_in_province))
        return stations_in_province

    def print_stations_names_from_list(self, station_list):
        station_index = 1
        for station in station_list:
            print(station_index, station['stationName'])
            station_index += 1

    def choose_station_and_find_station_id(self, station_list):
        choose_station_by_user = 7
        station_id = station_list[choose_station_by_user - 1]['id']
        print(station_id)
        return station_id

    def choose_sensor_and_find_sensor_id(self, sensor_list):
        choose_sensor_by_user = 1
        sensor_id = sensor_list[choose_sensor_by_user - 1]['id']
        print(sensor_id)
        return sensor_id

    def print_sensor_names_from_list(self, sensor_list):
        sensor_index = 1
        for sensor in sensor_list:
            print(sensor_index, sensor['param']['paramName'])
            sensor_index += 1

    def get_date_and_sensors_values_lists(self, data):
        date_list = []
        value_list = []
        temp = data['values']
        for measurement in temp:
            # print(measurement)
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