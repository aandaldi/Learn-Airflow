import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyTableOperator

with DAG('create_intenal_table',
         description="This is create table in internal",
         schedule_interval='0 12 * * *',
         start_date=datetime.datetime(2022, 1, 20), catchup=False) as dag:

    start_task = DummyOperator(task_id='start_task')
    finish_task = DummyOperator(task_id='finish_task')

    create_table = BigQueryCreateEmptyTableOperator(
    task_id="create_table",
    dataset_id='empty_dataset_2022_03_05',
    table_id=f'students_{datetime.date.today()}'.replace('-','_'),
    schema_fields=[
        {"name": "emp_name", "type": "STRING", "mode": "REQUIRED"},
        {"name": "grade", "type": "INTEGER", "mode": "NULLABLE"},
    ],
    )

    start_task >> create_table >> finish_task

