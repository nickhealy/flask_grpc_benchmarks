# flask_grpc_benchmarks

need to install `flask`, `orjson`, `grpc`, and `grpc-tools`

generate protobufs
`python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./grpc_benchmark.proto`

open 4 terminals, run one of the following commands in each 

```
python3 grpc_server.py 
gunicorn -b :8005 'server_no_flask:application'
gunicorn -b :8000 'flask_server:create_app()
gunicorn -b :8004 'flask_server:create_app(True)'
```
and then `python3 benchmark.py` 

this will generate a `benchmarks.csv` file
