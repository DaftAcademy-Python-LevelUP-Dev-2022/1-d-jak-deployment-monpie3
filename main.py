class HerokuApp:
    app_url = "https://daft-academy.herokuapp.com/"  # Fill your heroku app url here


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"start": "1970-01-01"}
