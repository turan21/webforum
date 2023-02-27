import os

AWS_ACCESS_KEY_ID = "DO00L8QR27VETUWXB3PL"
AWS_SECRET_ACCESS_KEY = "Z9rt1bylhsaLW+uC4HhuYLfNaH+DD2zFn8wn8SOk5mw"
AWS_STORAGE_BUCKET_NAME = "aliaka"
AWS_S3_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400"
}
AWS_LOCATION = "https://aliaka.fra1.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "project.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "project.cdn.backends.StaticRootS3Boto3Storage"
