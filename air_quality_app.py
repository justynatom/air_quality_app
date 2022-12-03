import api_talker
import data_parser
import matplotlib.pyplot as plt

class Air_quality_app:
    def __init__(self):
        self.api_talker = api_talker.API_talker()
        self.data_parser = data_parser.Data_parser()
        self.full_station_list = self.api_talker.send_api_request_findAll()

    def plot_graph(self, dates, values):
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

    def main(self):
        stations = self.data_parser.search_stations_in_province("opolskie", self.full_station_list)
        self.data_parser.print_stations_names_from_list(stations)
        station_id = self.data_parser.choose_station_and_find_station_id(stations)

        sensors = self.api_talker.send_api_request_sensors(station_id)
        self.data_parser.print_sensor_names_from_list(sensors)
        sensor_id = self.data_parser.choose_sensor_and_find_sensor_id(sensors)
        sensor_data = self.api_talker.send_api_request_getData(sensor_id)
        dates, values = self.data_parser.get_date_and_sensors_values_lists(sensor_data)
        self.plot_graph(dates, values)

