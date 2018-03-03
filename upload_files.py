import timeit
import boto3
import requests

def upload_files():
    # measure execution time
    start_time = timeit.default_timer()

    # aws auth
    session = boto3.Session(
        aws_access_key_id='your access key'
        aws_secret_access_key='your secret key',
        region_name='your bucket region',
    )
    s3 = session.resource('s3')
    bucket = 'your s3 bucket'

    # download image file
    url = 'download.url/{}'.format('download_file_name.jpg')
    response = requests.get(url, stream=True)
    response_data = response.raw
    upload_data = response_data.read()

    # upload image file to s3 bucket
    # default path is bucket name - ex) '/my_bucket/'
    # if specify a detailed path, add path before {}
    # for example, '/my_bucket/photos/save_file' -> Key='photos/{}'.format('filename.extension')
    s3.Bucket(bucket).put_object(Key='{}'.format('filename'), Body=upload_data)

    end_time = timeit.default_timer()
    print('### total run-time - {}sec'.format(end_time - start_time))
