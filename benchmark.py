import csv
from client import RestClient

FLASK_PORT = 8000

def benchmark():
    rest_client = RestClient(8000)

    with open('benchmarks.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        iters_row = ['iters']
        for i in range(1000):
            iters_row.append(i)

        data = list(zip(
            iters_row, 
            rest_client.benchmark_simple_req(), 
            rest_client.benchmark_complex_req()))

        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    benchmark()
