import logging

from fastapi import FastAPI
from app.worker.celery_worker import create_order, t_status



log = logging.getLogger(__name__)

from pydantic import BaseModel
# Pydantic BaseModel
# Order class model for request body
class Order(BaseModel):
    customer_name: str
    order_quantity: int

app = FastAPI()


def celery_on_message(body):
    log.warning(body)


def background_on_message(task):
    log.warning(task.get(on_message=celery_on_message, propagate=False))


@app.post('/order')
def add_order(order: Order):
    # use delay() method to call the celery task
    task = create_order.delay(order.customer_name, order.order_quantity)
    return {"message": "Order Received! Thank you for your patience.","uuid":task.id}

@app.get('/order')
def get_order_status(uuid:str):
    task = t_status(uuid)
    return {"state":task.state,"result":task.result}

