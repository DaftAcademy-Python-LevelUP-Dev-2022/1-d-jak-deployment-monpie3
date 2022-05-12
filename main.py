class HerokuApp:
    app_url = ""  # Fill your heroku app url here


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
