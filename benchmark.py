import csv
from client import RestClient, GrpcClient

FLASK_PORT = 8001
FLASK_ORJSON_PORT = 8004
VANILLA_PYTHON_PORT = 8005
GRPC_PORT = 8003

def benchmark():
    flask_client = RestClient(FLASK_PORT, 'flask')
    vanilla_python_client = RestClient(VANILLA_PYTHON_PORT, 'vanilla_python') 
    grpc_client = GrpcClient(GRPC_PORT)
    flask_orjson_client = RestClient(FLASK_ORJSON_PORT, 'flask_orjson')
    with open('benchmarks.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        data = list(zip(
            flask_client.benchmark_simple_req(), 
            flask_client.benchmark_complex_req(),
            flask_orjson_client.benchmark_simple_req(),
            flask_orjson_client.benchmark_complex_req(),
            vanilla_python_client.benchmark_simple_req(),
            vanilla_python_client.benchmark_complex_req(),
            grpc_client.benchmark_simple_req(),
            grpc_client.benchmark_complex_req()))

        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    benchmark()
