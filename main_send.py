from fastapi import FastAPI
import uvicorn
import json

app = FastAPI(debug=True)


# Data
with open("sample0.json", 'rb') as f:
    page = json.load(f)


# Route
@app.get('/page0')
async def get_page():
    return {"page": page}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8080")
