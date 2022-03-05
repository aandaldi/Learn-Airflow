This repository for note steps-steps how to use Airflow;

Basic step for using Airflow:
- install apache-airflow
- run 'db init'
- create user with 

    airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org

- run airflow webserver --port 8080

- run airflow scheduler
