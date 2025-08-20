import os
import json
import requests
from airflow import DAG
from datetime import datetime
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.apache.kafka.operators.produce import ProduceToTopicOperator

def generate_messages():

    response = requests.request(method='GET', url='https://randomuser.me/api/')

    data = response.json()

    results = data['results'][0]

    payload = json.dumps(results, indent=2, ensure_ascii=False)

    yield None, payload


default_args = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": 60,
    "email_on_failure": False,
    "email_on_retry": False,
}

with DAG(
    dag_id="{}".format(os.path.basename(__file__).replace('.py', '')),
    start_date=datetime(2025, 7, 2),
    default_args=default_args,
    schedule="*/5 * * * *",
    catchup=True,
    tags=[
        "data_ingestion",
        "container"
    ],
    max_active_runs=1,
):

    start = EmptyOperator(
        task_id="start",
    )

    produce = ProduceToTopicOperator(
        task_id='produce',
        kafka_config_id='kafka',
        topic='user_created',
        producer_function=generate_messages,
        poll_timeout=5
    )

    success = EmptyOperator(
        task_id="success",
        trigger_rule="all_success",
    )

    failure = EmptyOperator(
        task_id="failure",
        trigger_rule="one_failed",
    )

start >> produce >> [success, failure]
