import csv
from client import RestClient, GrpcClient

FLASK_PORT = 8000

def benchmark():
    flask_client = RestClient(8000, 'flask')
    grpc_client = GrpcClient(8003)

    with open('benchmarks.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        data = list(zip(
            flask_client.benchmark_simple_req(), 
            flask_client.benchmark_complex_req(),
            grpc_client.benchmark_simple_req(),
            grpc_client.benchmark_complex_req()))

        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    benchmark()
