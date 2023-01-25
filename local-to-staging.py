from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta


# Function to import the JSON file
def import_json():
    # Connect to the MySQL database
    import pandas as pd 
    from sqlalchemy import create_engine

    # Connect to the MySQL database
    my_conn=create_engine("mysql+pymysql://root:ghulam@localhost:3306/dana")
    print("connect Successfully")

    # Read JSON Data
    df = pd.read_parquet(r'D:\Dana\business.parquet')
    print("read Successfully")

    # convert nested data
    df["attributes"] = df["attributes"].to_json(orient='records')
    df["hours"] = df["hours"].to_json(orient='records')

    # upload data
    df.to_sql(con=my_conn,name='yelp_business',if_exists='append',index=False)
    print("File Loaded Successfully")
    return 'File Load Successfully'

# Default arguments for the DAG
default_args = {
    'owner': 'ghulam',
    'start_date': days_ago(1),
    #'depends_on_past': False,
    #'retries': 1,
}

# Create the DAG
dag = DAG(
    'local-to-staging',
    default_args=default_args,
    schedule_interval='0 2 * * *',
)

# initiate task
start_task  = DummyOperator(task_id="start_task", dag=dag)
end_task    = DummyOperator(task_id="end_task", dag=dag)


    
# Create the PythonOperator to run the import_json function
import_task = PythonOperator(
    task_id='import_json',
    python_callable=import_json,
    dag=dag
)


# Set the order of the tasks
start_task >> import_task >> end_task