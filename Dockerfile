FROM python:3.8

WORKDIR /app/

ENV PYTHONPATH=/app/

COPY . /app/

# Install Poetry
RUN curl -sSL https://install.python-poetry.org/ | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# RUN pip install poetry
RUN poetry install

EXPOSE 8000

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000