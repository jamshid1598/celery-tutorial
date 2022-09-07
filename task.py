from celery import Celery
import time

app = Celery('tasks', backend="rpc://", broker='pyamqp://guest@localhost//')

# changing task_serializer
app.conf.task_serializer = 'json'

# configuring many settings at once
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Asia/Tashkent',
    enable_utc=True,
)

# load changed configurations from manually created module
# app.config_from_object('celeryconfig')


@app.task
def add(x,y):
    y *= 1000
    while not x > y:
        x += 1
        time.sleep(0.001)
    return x + y
