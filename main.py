from fastapi import FastAPI

app = FastAPI()  # This is the 'app' instance Uvicorn is looking for.

@app.get("/")
def read_root():
    return {"message": "Hello World"}
