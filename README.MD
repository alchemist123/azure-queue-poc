# Azure Queue Service Example

This repository contains an example of how to use Azure Queue Storage service in a Python application. The example demonstrates how to create a queue, send a message to the queue, receive the message from the queue, and delete the queue.

## Prerequisites

- Python 3.6 or higher
- An Azure account
- Azure Storage account and access key
- `dotenv` package to manage environment variables

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your Azure Storage connection string and queue name:
    ```sh
    AZ_CONNECTION_URI="YourAzureConnectionString"
    QUEUE_NAME="YourQueueName"
    ```

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```

2. The script will perform the following actions:
    - Create a queue
    - Send a message to the queue
    - Receive the message from the queue
    - Delete the queue

## File Structure

- `main.py`: The main script that interacts with Azure Queue Storage.
- `.env`: Environment variables file containing Azure connection string and queue name.
- `.gitignore`: Git ignore file to exclude unnecessary files from the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Azure Storage Queue documentation](https://docs.microsoft.com/en-us/azure/storage/queues/storage-python-how-to-use-queue-storage)
- [dotenv package](https://pypi.org/project/python-dotenv/)
