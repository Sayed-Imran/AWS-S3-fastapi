import boto3


class S3Credentials():
    def __init__(self, akey, skey) -> None:
        try:
            self.access_key = akey
            self.secret_key = skey
        except Exception as e:
            print(e.args)

    def __call__(self, *args, **kwds):
        return self.access_key, self.secret_key


class S3:
    def __init__(self, access_key: str, secret_key: str) -> None:
        self.s3_client = boto3.client(
            's3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    def upload_file(self, img, key):
        try:
            self.s3_client.put_object(
                Body=img.file.read(), Bucket='social-media-bucket-images', Key=key)
            url = "https://social-media-bucket-images.s3.ap-south-1.amazonaws.com/" + key
            return url
        except Exception as e:
            print(e.args)


    def delete_file(self, key):
        try:
            response = self.s3_client.delete_object(
                Bucket='social-media-bucket-images', Key=key)
            return response
        except Exception as e:
            print(e.args)
