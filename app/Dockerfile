FROM python:3.9

COPY requirements.txt /app/

RUN pip install -r /app/requirements.txt

COPY . app/

WORKDIR /app

RUN ls -la .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
