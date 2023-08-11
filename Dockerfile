FROM python:3.11

WORKDIR /app

COPY ./requirements.txt .

RUN python3 -m pip install -r ./requirements.txt

RUN gdown 1-8PGv5ElSSdgiHbtTK4J1O5eKMh5MySD -O pytorch_model.bin

ENV PYTHONPATH=/app

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]