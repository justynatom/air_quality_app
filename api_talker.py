import requests

class API_talker:
    def send_api_request_sensors(self, id):
        URL = "https://api.gios.gov.pl/pjp-api/rest/station/sensors/{}"  # lista stanowisk pomiarowych
        URL = URL.format(id)
        print(URL)
        req = requests.get(url=URL)
        data = req.json()
        print(data)
        return data


    def send_api_request_getData(self, id):
        URL = "https://api.gios.gov.pl/pjp-api/rest/data/getData/{}"  # lista stanowisk pomiarowych
        URL = URL.format(id)
        print(URL)
        req = requests.get(url=URL)
        data = req.json()
        print(data)
        return data


    def send_api_request_findAll(self):
        URL = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"  # lista stacji pomiarowych
        req = requests.get(url=URL)
        data = req.json()
        return data
