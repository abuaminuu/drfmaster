import multiprocessing

bind = "0.0.0.0:10000"
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 5
