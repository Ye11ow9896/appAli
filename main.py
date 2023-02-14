import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"work?": "YES"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.1.1", port=8001)
