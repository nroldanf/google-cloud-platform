from google.cloud import vision
from google.cloud import storage

storage_client = storage.Client(project="formal-purpose-331117")

# Make an authenticated API request
buckets = list(storage_client.list_buckets())
print(buckets)

# client = vision.ImageAnnotatorClient()
# response = client.annotate_image({
#   'image': {'source': {'image_uri': 'gs://gcp-nicolas-bucket/demo-img.jpeg'}},
#   'features': [{'type_': vision.Feature.Type.FACE_DETECTION}]
# })