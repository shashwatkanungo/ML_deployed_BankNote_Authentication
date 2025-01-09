
import uvicorn ##ASGI
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Hello, World'}


@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}



# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload



