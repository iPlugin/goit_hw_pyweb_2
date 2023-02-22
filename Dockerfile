FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "app/__main__.py" ]