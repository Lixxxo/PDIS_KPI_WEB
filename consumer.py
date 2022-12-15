from RabbitMQ.rabbit import Rabbit
from app import app
import sys

if __name__ == "__main__":
    with app.app_context():
        # exchange_list = ["createProject", "useOfMaterials", "HHRR"]
        rabbit = Rabbit()
        rabbit.consume(sys.argv[1:][0])
