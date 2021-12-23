FROM python:latest

RUN pip install poetry

RUN mkdir /app
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry export > /app/requirements.txt
RUN pip install -r requirements.txt
COPY . .

CMD [ "python", "datadog_sender/main.py" ]
