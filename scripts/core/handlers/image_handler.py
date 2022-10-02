from scripts.utils import access_key, secret_key
from scripts.utils.s3_image_util import S3
import random
import string


class ImageHandler:
    def __init__(self) -> None:
        self.s3 = S3(access_key=access_key, secret_key=secret_key)

    def upload_image(self, img, img_name):
        key = ''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=20)) + '.' + img_name.split('.')[-1]
        return self.s3.upload_file(img, key=key)

    def delete_image(self, key):
        return self.s3.delete_file(key)
