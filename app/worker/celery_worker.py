from time import sleep

from .celery_app import celery_app
from celery.utils.log import get_task_logger


celery_log = get_task_logger(__name__)

@celery_app.task(acks_late=True)
def create_order(name, quantity):
    
    # 5 seconds per 1 order
    complete_time_per_item = 5
    
    # Keep increasing depending on item quantity being ordered
    sleep(complete_time_per_item * quantity)
# Display log    
    celery_log.info(f"Order Complete!")
    return {"message": f"Hi {name}, Your order has completed!",
            "order_quantity": quantity}

def t_status(id):
    c = celery_app.AsyncResult(id)
    return c