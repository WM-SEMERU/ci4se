def create_queue_service(self):
    try:
        from azure.storage.queue.queueservice import QueueService
        return QueueService(self.account_name, self.account_key, sas_token=
            self.sas_token, is_emulated=self.is_emulated)
    except ImportError:
        raise Exception('The package azure-storage-queue is required. ' +
            'Please install it using "pip install azure-storage-queue"')