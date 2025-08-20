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
- **Docker**: Containerizes the entire solution for easy deployment

## Prerequisites

- Docker and Docker Compose
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
   - Default username: `admin`
   - Default password: `admin`

### Configuration

The project includes the following containers:
- `apache-airflow`: Runs Airflow webserver, scheduler, and other components in standalone mode
- `broker-1`: Kafka broker for message streaming
- `controller-1`: Kafka controller for cluster management

## Data Pipeline

The main data pipeline (`streaming_dag.py`) performs the following operations:
1. Runs every 5 minutes
2. Fetches random user data from [randomuser.me API](https://randomuser.me)
3. Produces the data to Kafka topic `user_created`
4. Reports success or failure

## Kafka Topics

- `user_created`: Contains user creation events with complete user information

## Development

### Adding New DAGs

Place your new DAG files in the `airflow/dags/` directory. They will be automatically picked up by Airflow.

### Adding Python Dependencies

1. Add new dependencies to `airflow/requirements.txt`
2. Rebuild the Airflow container:
   ```bash
   docker-compose build airflow
   docker-compose up -d
   ```

## Troubleshooting

### Common Issues

1. **Kafka Connection Issues**:
   - Check if Kafka containers are running: `docker ps`
   - Verify network connectivity between containers

2. **Airflow DAG Not Running**:
   - Check Airflow logs: `docker logs apache-airflow`
   - Verify DAG syntax and dependencies

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- Kevin Leo (@kevinleo01)
