from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Replace these with your own values
account_name = "pythonazurestorage78330"
account_key = "YourKey"
container_name = "blob-container-01"
blob_name = "sample-blob-4c2ee.txt"
download_file_path = r"C:\Users\ellio\OneDrive\Workspace\Data Engineer Training\Week_3\Day11\downloaded_file.txt"

# Create a BlobServiceClient
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

# Get a reference to the container
container_client = blob_service_client.get_container_client(container_name)

# Get a reference to the blob
blob_client = container_client.get_blob_client(blob_name)

# Download the blob to a local file
with open(download_file_path, "wb") as download_file:
	download_file.write(blob_client.download_blob().readall())
