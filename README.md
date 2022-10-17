# flask_grpc_benchmarks

need to install `flask` and `orjson` 

open 4 terminals, run one of the following commands in each 

```
python3 grpc_server.py 
python3 server_no_flask.py 
gunicorn -b :8000 'flask_server:create_app()
gunicorn -b :8004 'flask_server:create_app(True)'
```
and then `python3 benchmark.py` 

this will generate a `benchmarks.csv` file
