import multiprocessing
import os

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = os.environ.get("LOG_FILE", "flask.log")
errorlog = os.environ.get("LOG_FILE", "flask.log")
capture_output = True
reload = True