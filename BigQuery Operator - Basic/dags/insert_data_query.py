import datetime
from airflow import DAG
from airflow.models import Variable
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.bigquery_operator import BigQueryOperator

sql = """
        INSERT empty_dataset_2022_03_05.students_2022_03_05 VALUES ('me', 7), ('you', 8)
    """


with DAG('insert_query',
        description='this is dag for insert data ',
        schedule_interval='0 12 * * *',
        start_date=datetime.datetime(2022, 1, 20), catchup=False) as dag:

    start_task = DummyOperator(task_id='start_task')
    finish_task = DummyOperator(task_id='finish_task')

    insert_query_job = BigQueryOperator(
        dag=dag,
        task_id='insert_data_from_staging_to_core',
        # provide_context=True,
        bigquery_conn_id=Variable.get('GOOGLE_APPLICATION_CREDENTIALS'),
        sql=sql,
        write_disposition='WRITE_APPEND',
        location='EU',
        use_legacy_sql=False
    )

    start_task >> insert_query_job >> finish_task


