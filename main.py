from fastapi import FastAPI

app = FastAPI()

@app.post("/items")
async def create_item(item: dict):
    print(item.job_id)
    print(item.predictions[0].results.predictions)