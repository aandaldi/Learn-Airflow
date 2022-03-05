import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator

with DAG('create_empty_dataset',
         description="This is create empty dataset",
         schedule_interval='0 12 * * *',
         start_date=datetime.datetime(2022, 1, 20), catchup=False) as dag:

    start_task = DummyOperator(task_id='start_task')
    finish_task = DummyOperator(task_id='finish_task')

    create_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id = "create_dataset",
        dataset_id = f'empty_dataset_{datetime.date.today()}'.replace('-','_')
    )

    start_task >> create_dataset >> finish_task

