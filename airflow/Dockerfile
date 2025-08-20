FROM apache/airflow:slim-3.0.3-python3.12

COPY ./requirements.txt /opt/airflow/requirements.txt

WORKDIR /opt/airflow

RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt
