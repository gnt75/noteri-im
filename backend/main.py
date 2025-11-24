from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Noteri-im API is working!"}
