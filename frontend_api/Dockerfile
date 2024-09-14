FROM python:3.12-slim-buster 

WORKDIR /frontend_api 

COPY . /frontend_api/app/
COPY ../start_frontend_api.py /frontend_api

RUN pip install -r ../requirements.txt 

CMD ["python", "start_frontend_api.py"]
