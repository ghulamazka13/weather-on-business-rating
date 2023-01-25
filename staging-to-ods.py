from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

# Default arguments for the DAG
default_args = {
    'owner': 'ghulam',
    'start_date': days_ago(1),
    #'depends_on_past': False,
    #'retries': 1,
}

# Create the DAG
dag = DAG(
    'migrate_data_between_mysql',
    default_args=default_args,
    schedule_interval='0 2 * * *',
)

# initiate task
start_task  = DummyOperator(task_id="start_task", dag=dag)
end_task    = DummyOperator(task_id="end_task", dag=dag)


migrate_data = MySqlOperator(
    task_id='migrate_data',
    mysql_conn_id='src_conn', # already set up the source connection on the airflow UI
    sql='INSERT INTO dest_table SELECT * FROM src_table',
    dag=dag,
)

# Set the order of the tasks
start_task >> migrate_data >> end_task