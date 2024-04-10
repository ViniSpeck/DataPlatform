from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from docker.types import Mount
default_args = {
'owner'                 : 'airflow',
'description'           : 'sample-pipeline', #Alterar nome da dag
'depend_on_past'        : False,
'start_date'            : datetime(2022, 1, 1),
'email_on_failure'      : False,
'email_on_retry'        : False,
'retries'               : 1,
'retry_delay'           : timedelta(minutes=5)
}

with DAG('sample-pipeline', default_args=default_args, schedule_interval=None, catchup=False, is_paused_upon_creation=False) as dag:
    start_dag = DummyOperator( #Pode remover, opcional
        task_id='start_dag'
        )
    end_dag = DummyOperator( #Pode remover, opcional
        task_id='end_dag'
        )
    hop = DockerOperator(
        task_id='sample-pipeline', #Alterar o nome da task (processo dentro da DAG)
        image='apache/hop',
        api_version='auto',
        auto_remove=True,
        environment= {
            'HOP_RUN_PARAMETERS': 'INPUT_DIR=',
            'HOP_LOG_LEVEL': 'Basic',
            'HOP_FILE_PATH': '/project/pipelines/teste.hpl', #Caminho do pipeline ou workflow
            'HOP_PROJECT_DIRECTORY': '/project',
            'HOP_PROJECT_NAME': 'dw',
            'HOP_ENVIRONMENT_NAME': 'dev-env-config.json',
            'HOP_ENVIRONMENT_CONFIG_FILE_NAME_PATHS': '/project-config/dev-env-config.json',
            'HOP_RUN_CONFIG': 'local'
        },
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        #Alterar o nome do usuário no caminho (nesse exemplo é ubuntu)
        mounts=[Mount(source='/home/ubuntu/hop/projects/dw', target='/project', type='bind'), Mount(source='/home/ubuntu/hop/config', target='/project-config', type='bind')],
        force_pull=False
        )
    start_dag >> hop >> end_dag