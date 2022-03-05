import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryGetDatasetTablesOperator

with DAG('get_table_list',
        description='this is dag for get list of table',
        schedule_interval='0 12 * * *',
        start_date=datetime.datetime(2022, 1, 20), catchup=False) as dag:

    start_task = DummyOperator(task_id='start_task')
    finish_task = DummyOperator(task_id='finish_task')

    get_table_list = BigQueryGetDatasetTablesOperator(task_id="get-list", dataset_id='empty_dataset_2022_03_05')

    start_task >> get_table_list >> finish_task


