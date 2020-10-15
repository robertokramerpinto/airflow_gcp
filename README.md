# GCP - Airflow project


## Docker

**Build Container**

```docker build --rm --build-arg AIRFLOW_DEPS="gcp,statsd,sentry" --build-arg PYTHON_DEPS="pyspark==2.4.5" --build-arg AIRFLOW_VERSION=1.10.10 -t airflow-gcp .```

**Run Container**

```docker run -d -p 8080:8080 airflow-gcp webserver```

> Check running containers 

```docker container ls```

Access: localhost:8080 to check if airflow is running and accessible through this port

**Access Docker Instance**

```docker exec -it <container name> /bin/bash```

> Stop and Start Container

```docker stop <container name>```

```docker start <container name>```

Delete all containers : ```docker rm $(docker ps -a -q)```