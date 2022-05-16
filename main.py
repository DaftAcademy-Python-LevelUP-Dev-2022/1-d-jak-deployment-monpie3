class HerokuApp:
    app_url = "http://127.0.0.1:8000/"  # Fill your heroku app url here


from fastapi import FastAPI, Response, status, Request
from pydantic import BaseModel
import datetime


app = FastAPI()
# to see what funny will come
app.counter = 0



@app.get("/")
def root():
    return {"start": "1970-01-01"}


# generic route -> https://github.com/tiangolo/fastapi/issues/819
@app.get('/method', status_code=200)
def method_get():
    return {"method": "GET"}

@app.put('/method', status_code=200)
def method_delete():
    return {"method": "PUT"}

@app.post('/method', status_code=201)
def method_post():
    return {"method": "POST"}

@app.options('/method', status_code=200)
def method_options():
    return {"method": "OPTIONS"}

@app.delete('/method', status_code=200)
def method_delete():
    return {"method": "DELETE"}


# status -> https://www.django-rest-framework.org/api-guide/status-codes/
@app.get("/day/")
def get_day(name: str, number: int, response: Response):
    day_dict = {1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday", 7: "sunday"}
    if day_dict[number] == name:
        response.status_code = status.HTTP_200_OK
        return name
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return f"jesteś Janiną"


list_of_events = []
    
@app.get('/events')
def counter():
    app.counter += 1
    return app.counter
    
class Event_Details(BaseModel):
    date: str
    event: str
    
  
@app.put("/events", status_code=200)
def add_event(item : Event_Details):
    id = counter()
    new_json =  {
        "date" : item.date,
        "name" : item.event, 
        "date_added": datetime.date.today(),
        "id": id
    }
    list_of_events.append(new_json)
    return new_json



@app.get("/events/{my_date}", status_code=200)
def show_event(my_date : str, response: Response):  
    try:
        datetime.datetime.strptime(my_date, "%Y-%m-%d")
    except ValueError:  
        response.status_code = status.HTTP_400_BAD_REQUEST
        return "Not a valid date"
        
    if len(list_of_events) == 0:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return "List of events is empty"
    
    event_in_this_day = []
    
    for my_event in list_of_events:
        if my_event["date"] == my_date:
            event_in_this_day.append(my_event)
            
    if len(event_in_this_day):    
        return event_in_this_day  
    else: 
        response.status_code = status.HTTP_404_NOT_FOUND
        return "You have plans, but for other days"
