# AIR QUALITY APP

This is an app for monitoring air quality from multiple stations. 

1. User guide 

An app requires few python libraries specified in requirement file.
To run the application you have to run web server using command: 
uvicorn main:app --reload
GUI is available at local host address eg. http://127.0.0.1:8000/
In first step user can choose the province. Then the list of available stations and sensors are showed. 
Finally graph and numerical data for last 2-3 days are presented for given monitoring station. 

2. Used tools and technologies

- GIOŚ API - an app is using free air quality API shared by GIOŚ at website: https://powietrze.gios.gov.pl/pjp/content/api
- JSON - aAPI responses are send as JSON 
- Matplotlib - data graph is generated using matplotlib library 
- freeapi - used to create web layer of this app
- jinja2 - provide html templates for GUI

3. Author 

justynaxtomaszewska@gmail.com