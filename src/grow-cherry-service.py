from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Everybody freeze, this is a robbery"}