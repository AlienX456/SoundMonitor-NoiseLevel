import os
import boto3
import logging

class AwsS3Resource:

    def __init__(self):
        session = boto3.Session(region_name='us-east-1')
        self.bucket = session.resource('s3').Bucket(os.environ['BUCKET_NAME'])

    def download_object(self, file_name):
        try:
            logging.info('Trying to download %s', file_name)
            self.bucket.download_file(file_name, file_name)
            s3_object = self.bucket.Object(file_name)
            return s3_object.metadata
        except Exception as e:
            logging.error('Error: while downloading the file %s exception %s', file_name, str(e))
            raise
