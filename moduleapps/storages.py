from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = "c1018102dcbs"
    account_key = "XszL6Xjgd2qxisTx3itwPxolsCYhuDlZhgntZwdyLc+qMjslUGb5dHgNnhfN/EZ7y3JlMUEv/fpV+AStYqNUtg=="
    azure_container = "media"
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = "c1018102dcbs"
    account_key = "XszL6Xjgd2qxisTx3itwPxolsCYhuDlZhgntZwdyLc+qMjslUGb5dHgNnhfN/EZ7y3JlMUEv/fpV+AStYqNUtg=="
    azure_container = "static"
    expiration_secs = None