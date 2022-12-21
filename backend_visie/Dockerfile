FROM python:3.7


ENV LANG=C.UTF-8 \
  # python:
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \
  # poetry:
  POETRY_VERSION=1.1.15 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_HOME="/opt/poetry" \
  POETRY_CACHE_DIR='/var/cache/pypoetry'


RUN apt-get -y update && \
    apt-get install -y --no-install-recommends make wget gcc python3-dev libzbar0 && \
    apt install -y openssl && apt-get install -y libmariadb-dev && \
    rm -rf /var/lib/apt/lists/* && apt-get install -y libmariadb3 libmariadb-dev && \
    pip install "poetry==$POETRY_VERSION" && poetry --version


RUN python3 -m pip install --upgrade pip


WORKDIR /src

COPY ./src /src

RUN poetry config virtualenvs.create false
RUN pip install --upgrade setuptools
RUN poetry install --no-dev --no-interaction --no-ansi

RUN rm -rf "$POETRY_CACHE_DIR"

EXPOSE 8082

CMD [ "python", "app.py" ]
