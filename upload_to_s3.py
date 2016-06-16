import boto3
import os

BUCKET_NAME = 'crystal-dash-docset'
XML_FILENAME = 'Crystal.xml'
TARBALL_FILENAME = 'crystal.tgz'

path_to_this = os.path.dirname(os.path.realpath(__file__))

xml_path = os.path.join(path_to_this, XML_FILENAME)
tarball_path = os.path.join(path_to_this, TARBALL_FILENAME)

s3 = boto3.resource('s3')

s3.Object(BUCKET_NAME, XML_FILENAME).put(Body=open(xml_path, 'rb'))
s3.Object(BUCKET_NAME, TARBALL_FILENAME).put(Body=open(tarball_path, 'rb'))
