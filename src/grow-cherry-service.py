from fastapi import FastAPI


app = FastAPI()


@app.post("/auth_shopper")
async def auth_shopper(username:str, password:str):
    pass


@app.post("/auth_courier")
async def auth_courier(username:str, password:str):
    pass


@app.post("/get_products")
async def get_products():
    pass


