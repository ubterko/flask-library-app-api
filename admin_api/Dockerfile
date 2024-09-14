FROM python:3.12-slim-buster 

WORKDIR /admin_api 

COPY . /admin_api/app/
COPY ../start_frontend_api.py /frontend_api

RUN pip install -r ../requirements.txt 

CMD ["python", "start_admin_api.py"]
