FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/
COPY main.py /app/

RUN pip install --no-cache-dir -r requirements.txt
RUN python model.py
EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
