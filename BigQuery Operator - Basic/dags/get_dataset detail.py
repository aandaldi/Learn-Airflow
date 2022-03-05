import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryGetDatasetOperator

with DAG('get_dataset_detail',
        description='this is dag for get detail of dataset',
        schedule_interval='0 12 * * *',
        start_date=datetime.datetime(2022, 1, 20), catchup=False) as dag:

    start_task = DummyOperator(task_id='start_task')
    finish_task = DummyOperator(task_id='finish_task')

    get_detail = BigQueryGetDatasetOperator(task_id="get-dataset", dataset_id='empty_dataset_2022_03_05')

    start_task >> get_detail >> finish_task


