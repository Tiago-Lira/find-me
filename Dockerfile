FROM python:3.7-alpine

WORKDIR /src/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PORT 5000

CMD waitress-serve --port=$PORT find_me:app.app
