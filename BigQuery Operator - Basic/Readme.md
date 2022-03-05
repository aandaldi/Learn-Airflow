This is tutorial how to use bigquery operator in airflow to accses bigquery

Steps:
- Generate keys from IAM
- export GOOGLE_APPLICATION_CREDENTIALS=<json-key-file>
- install google providers (pip install apache-airflow-providers-google)
- init db, create user, run webserver and scheduler


This directory will cover:
- how to create empty dataset
- how to get datail existing dataset
- hot to get tables of dataset
- how to create table in bigquery
- how to insert data in table *need to activate billing if use airflow.cloud)