FROM python:3.11

WORKDIR /app

COPY ./requirements.txt .

RUN python3 -m pip install -r ./requirements.txt

RUN gdown 1-8PGv5ElSSdgiHbtTK4J1O5eKMh5MySD -O pytorch_model.bin

ENV PYTHONPATH=/app

RUN mkdir -p /app/dataset
ENV HF_DATASETS_CACHE=/app/dataset
ENV TRANSFORMERS_CACHE=/app/dataset

COPY . .
RUN python3 base_models.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# uvicorn main:app --host 0.0.0.0 --port 80