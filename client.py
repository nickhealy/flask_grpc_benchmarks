import grpc
import requests
import time

from grpc_benchmark_pb2_grpc import ServiceStub
from grpc_benchmark_pb2 import SimpleRequestInput, SimpleRequestOutput, ComplexRequestInput, ComplexRequestOutput

WARMUPS = 10
ITERATIONS = 10000

def get_latencies_after_x_iterations(name, cb, iterations):
    latencies = [name]

    for _ in range(WARMUPS):
        cb()

    for _ in range(iterations):
        start = time.perf_counter()
        cb()
        end = time.perf_counter()
        latencies.append((end - start) * 1000) # convert to ms

    return latencies

class RestClient:
    def __init__(self, port, base_name):
        self.port = port
        self.base_name = base_name

    def get_benchmarks(self, name, url, iterations):
        session = requests.Session()
        def req():
            session.get(f"http://localhost:{self.port}{url}")
        return get_latencies_after_x_iterations(name, req, iterations)

    def benchmark_simple_req(self, iters = ITERATIONS):
        return self.get_benchmarks(f"{self.base_name}_simple", "/simple/", iters)
    
    def benchmark_complex_req(self, iters = ITERATIONS):
        return self.get_benchmarks(f"{self.base_name}_complex", "/complex/", iters)

class GrpcClient():
    def __init__(self, port):
        channel = grpc.insecure_channel(f"localhost:{port}")
        self.client = ServiceStub(channel)

    def get_benchmarks(self, name, req_obj, req_cb, iterations):
        def req():
            req_cb(req_obj)
        return get_latencies_after_x_iterations(name, req, iterations)
    
    def benchmark_simple_req(self, iters = ITERATIONS):
        return self.get_benchmarks("grpc_simple", SimpleRequestInput(), self.client.SimpleRequest, iters)

    def benchmark_complex_req(self, iters = ITERATIONS):
        return self.get_benchmarks("grpc_complex", ComplexRequestInput(), self.client.ComplexRequest, iters)
