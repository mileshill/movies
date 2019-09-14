# Load Testing

Steps:
1. Launch the local/remote application
2. Launch locust

```shell
# shell 1
python /path/to/app.py
```

```shell
# shell 2
locust --host=HOST_URI -f locustfile.py --no-web -c 100 -r 10 --run-time 1h10m
```