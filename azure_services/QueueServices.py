from azure.storage.queue import QueueServiceClient

class AzureQueueServices:
    def __init__(self, connection_string: str, queue_name: str):
        self.queue_name = queue_name
        self.queue_service_client = QueueServiceClient.from_connection_string(connection_string)
        self.queue_client = self.queue_service_client.get_queue_client(queue_name)
    
    def createQueue(self):
        try:
            self.queue_client.create_queue()
            print(f"Queue '{self.queue_name}' created successfully.")
        except Exception as e:
            print(f"Error creating queue: {e}")

    def sendPayload(self,payload:str):
        try:
            self.queue_client.send_message(payload)
            print(f"Payload sent: {payload}")
        except Exception as e:
            print(f"Error sending payload: {e}")
    
    def receivePayload(self):
        try:
            payload = self.queue_client.receive_messages()
            for msg in payload:
                print(f"Received payload message: {msg.content}")
                self.queue_client.delete_message(msg)
                print("Message deleted successfully.")
        except Exception as e:
            print(f"Error receiving message: {e}")
    
    def deleteQueue(self):
        try:
            self.queue_client.delete_queue()
            print(f"Queue '{self.queue_name}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting queue: {e}")