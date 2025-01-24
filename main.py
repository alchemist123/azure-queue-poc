from azure_services import AzureQueueServices
import os
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv("AZ_CONNECTION_URI")
QUEUE_NAME = os.getenv("QUEUE_NAME")

def main():
    queue_service = AzureQueueServices(CONNECTION_STRING, QUEUE_NAME)
    
    queue_service.createQueue()
    queue_service.sendPayload("Hello, I am from a Queue")
    queue_service.receivePayload()
    queue_service.deleteQueue()

if __name__ == "__main__":
    main()
