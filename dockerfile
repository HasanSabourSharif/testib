FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/
COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN gdown 1-8PGv5ElSSdgiHbtTK4J1O5eKMh5MySD -O pytorch_model.bin

EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]