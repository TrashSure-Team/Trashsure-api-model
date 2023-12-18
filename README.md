# TrashSure Api Model

## Python and Pip Versions

- Python version: 3.6.1
- Pip version: 21.3.1

## Libraries


To ensure that pip is up-to-date, run the following command:
````bash
python -m pip install --upgrade pip
````
After that, install the project dependencies:
You can install the required libraries using the following command:

````bash
pip install fastapi[all] uvicorn python-multipart pillow tensorflow
````
or

````bash
pip install -r requirements.txt
````


## Run the Application
To run the application, use the following command:

````bash
uvicorn main:app --reload
````
This will start the server, and you can access your FastAPI application at http://127.0.0.1:8000.
