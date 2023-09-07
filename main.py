from datetime import datetime
from typing import Union

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/api")
def hng_info(slack_name: str = "deprecate", track: str = "backend"):
    return {
        "slack_name": slack_name, 
        "current_day": datetime.today().strftime("%A"), 
        "utc_time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), 
        "track": track, 
        "github_file_url": "https://github.com/utukJ/hngx-stage-1/blob/main/main.py", 
        "github_repo_url": "https://github.com/utukJ/hngx-stage-1", 
        "status_code": 200
        }