FROM python:3.7-alpine

WORKDIR /src/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD waitress-serve --port=5000 find_me:app.app
