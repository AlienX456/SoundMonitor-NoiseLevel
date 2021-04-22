import os
import boto3
import logging

class AwsS3Resource:

    def __init__(self):
        session = boto3.Session(aws_access_key_id=os.environ['AWS_KEY'],
                                aws_secret_access_key=os.environ['AWS_SECRET'])
        s3 = session.resource('s3')
        self.bucket = s3.Bucket(os.environ['BUCKET_NAME'])

    def download_object(self, file_name):
        try:
            self.bucket.download_file(file_name, '%s.jpg'.format(file_name))
        except Exception as e:
            logging.error('Error: while downloading the file %s exception %e', file_name, str(e))
            raise

    def remove_file(self, file_name):
        file = self.bucket.Object(file_name)
        file.delete()
