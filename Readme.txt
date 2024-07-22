1. Install dependencies
    pip install sqlalchemy
    pip install "uvicorn[standard]" gunicorn

2. Run the app
    uvicorn main:app --reload

3. Open the browser and test the api
    http://127.0.0.1:8000/docs