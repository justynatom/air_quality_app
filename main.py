import air_quality_app
from fastapi import FastAPI, Query, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import starlette.status as status
import time

obj = air_quality_app.Air_quality_app()
#app.main()
app = FastAPI()
app.counter = 0
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
class HelloResp(BaseModel):
    msg: str

@app.get("/",  response_class=HTMLResponse)
async def root(request: Request):
    #provinces = ["Dolnośląskie", "Mazowieckie", "Wielkopolskie"]
    return templates.TemplateResponse("index.html", {"request": request, 'choices': obj.get_provinces_list()})

@app.post("/")
async def get_province(province: str = Form()):
    print(province)
    return RedirectResponse(url="/stations/" + str(province.title()), status_code=status.HTTP_302_FOUND)


@app.get("/hello/{name}", response_model=HelloResp)
async def hello(name: str):
    return HelloResp(msg = f"Hello {name}!")

@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)


class Product(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    code: str

@app.post("/product/")
async def create_item(product: Product):
    return product


@app.get('/test')
async def get_something(
        choice: str = Query('eu', enum =['eu','us'])
):
    return {'selected': choice}




@app.get("/test2/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.get("/stations/{province}", response_class=HTMLResponse)
async def read_item(request: Request, province: str):
    item = obj.get_stations_in_province(province)
    return templates.TemplateResponse("item2.html", {"request": request, 'items': item, 'province': province, 'min_value': 1, "max_value": len(item)})


@app.get("/sensors/{station_id}", response_class=HTMLResponse)
async def print_sensors(request: Request, station_id: str):
    item = obj.get_sensors_in_station(int(station_id))
    return templates.TemplateResponse("item3.html", {"request": request, 'items': item, 'station': obj.station_name, 'min_value': 1, "max_value": len(item)})

@app.post("/stations/{province}")
async def get_id(id: str = Form()):
    print(id)
    return RedirectResponse(url="/sensors/" + str(id), status_code=status.HTTP_302_FOUND)

@app.get("/measurement/{measure}")
async def show_measurement(request: Request, measure: str):
    data = obj.get_measurements_and_show_graph(int(measure))
    return templates.TemplateResponse("item4.html", {"request": request, 'data': data})

@app.post("/sensors/{sensor_id}")
async def get_sensor(id2: str = Form()):
    print(id2)
    return RedirectResponse(url="/measurement/" + str(id2), status_code=status.HTTP_302_FOUND)



