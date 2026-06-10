from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello():
    return ('Hellow world')

@app.get("/about")
def about():
    return ('This is me and me is this')