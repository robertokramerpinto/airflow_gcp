import datetime

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

##############################################################################################
# DAG definition
##############################################################################################

# Passed to all tasks
default_args = {
    'owner': 'roberto_kramer',
    'depends_on_past': False,
    'start_date': datetime.datetime(2019, 6, 1, 0),
    # 'end_date': datetime.datetime(2019, 6, 1, 6),
    'retries': 0,
    'retry_delay': datetime.timedelta(minutes=1),
}

DAG_ID = 'dag_initial_example'

dag = DAG(
    DAG_ID,
    default_args=default_args, catchup=False,
    max_active_runs=1, schedule_interval=None)


def print_name():
    print("Roberto Kramer")

##############################################################################################
# DAG Initiation
##############################################################################################

with dag:

    bash_task = BashOperator(task_id='bash_first_command',
                             bash_command='echo "Hello World"')

    python_task = PythonOperator(task_id='python_function',
                                 python_callable=print_name)


    bash_task >> python_task