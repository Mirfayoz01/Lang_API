from fastapi import FastAPI
from dataapi import translate_text, translate_text2

app = FastAPI()

@app.get("/")
async def home_page():
    return {"message": "en / uz"}

@app.get("/uz_en/{name}")
async def uz_en(name: str):
    data = translate_text(name)
    return {
        "EN": data
    }

@app.get("/en_uz/{name}")
async def en_uz(name: str):
    data = translate_text2(name)
    return {
        "UZ": data
    }