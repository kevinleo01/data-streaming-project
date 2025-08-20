# Data Streaming Project

A containerized data streaming architecture using Apache Airflow and Apache Kafka for real-time data ingestion and processing.

## Project Overview

This project demonstrates a real-time data streaming pipeline that:
1. Fetches random user data from an external API
2. Processes the data using Apache Airflow
3. Produces messages to Apache Kafka topics
4. Enables real-time data streaming for downstream applications

## Architecture

The project uses the following components:

- **Apache Airflow**: Orchestrates the data pipeline
- **Apache Kafka**: Handles real-time data streaming
- **Docker/Podman**: Containerizes the entire solution for easy deployment

## Prerequisites

- Docker/Podman and Docker/Podman Compose
- Git
- Internet connection (for API access)

## Directory Structure

```
data-streaming-project/
├── docker-compose.yml          # Docker Compose configuration
├── airflow/                    # Airflow related files
│   ├── Dockerfile              # Airflow container definition
│   ├── requirements.txt        # Python dependencies
│   └── dags/                   # Airflow DAG definitions
│       └── streaming_dag.py    # Main data streaming DAG
```

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kevinleo01/data-streaming-project.git
   cd data-streaming-project
   ```

2. Start the containers:
   ```bash
   docker-compose up -d
   ```

3. Access Airflow web interface:
   Open your browser and navigate to [http://localhost:8080](http://localhost:8080)

### Configuration

The project includes the following containers:
- `apache-airflow`: Runs Airflow webserver, scheduler, and other components in standalone mode
- `broker-1`: Kafka broker for message streaming
- `controller-1`: Kafka controller for cluster management

## Data Pipeline

The main data pipeline (`streaming_dag.py`) performs the following operations:
1. Runs every 5 seconds
2. Fetches random user data from [randomuser.me API](https://randomuser.me)
3. Produces the data to Kafka topic `user_created`
4. Reports success or failure

## Kafka Topics

- Create the user_created Kafka topic in broker-1

```bash
docker exec -ti --workdir=/opt/kafka/bin broker-1 sh kafka-topics.sh --bootstrap-server broker-1:19092 --create --topic user_created --partitions 1 --replication-factor 1 --config max.message.bytes=64000 --config flush.messages=1
```

- `user_created`: Contains user creation events with complete user information

- Create a console consumer for the `user_created` topic
```bash
docker exec -ti --workdir=/opt/kafka/bin broker-1 sh kafka-console-consumer.sh --bootstrap-server broker-1:19092 --topic user_created --from-beginning --partition 0
```

## Troubleshooting

### Common Issues

1. **Kafka Connection Issues**:
   - Check if Kafka containers are running: `docker ps`
   - Verify network connectivity between containers

2. **Airflow DAG Not Running**:
   - Check Airflow logs: `docker logs apache-airflow`
   - Verify DAG syntax and dependencies

## Author

- Kevin Leo (@kevinleo01)
