import json
import grpc
from concurrent import futures 
import grpc_benchmark_pb2_grpc
from grpc_benchmark_pb2 import SimpleRequestOutput, ComplexRequestOutput

PORT = 8003

json_data = open('complex_response.json')
complex_res_json = json.load(json_data)

simple_reply = SimpleRequestOutput()
complex_reply = ComplexRequestOutput(**complex_res_json)

class GrpcTestService(grpc_benchmark_pb2_grpc.ServiceServicer):
    def SimpleRequest(self, request, context):
        return simple_reply
    def ComplexRequest(self, request, context):
        return complex_reply

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    grpc_benchmark_pb2_grpc.add_ServiceServicer_to_server(GrpcTestService(), server)
    server.add_insecure_port(f"[::]:{PORT}")
    server.start()
    print(f"Server start on port {PORT}")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

