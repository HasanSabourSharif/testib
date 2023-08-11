FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/

RUN python3 -m pip install -r ./requirements.txt

RUN gdown 1-8PGv5ElSSdgiHbtTK4J1O5eKMh5MySD -O pytorch_model.bin

COPY . /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]