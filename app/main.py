# main.py
from fastapi import FastAPI, status
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"title": "QC resource API server"}


@app.get("/resource", status_code=status.HTTP_200_OK)
async def get_resource():
    with open("./resource.json", "r") as file:
        return json.load(file)
