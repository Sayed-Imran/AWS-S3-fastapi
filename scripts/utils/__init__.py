from scripts.constants.app_configuration import Credentials
from scripts.utils.s3_image_util import S3Credentials

access_key, secret_key = S3Credentials(akey=Credentials.AccessKey.akey,skey=Credentials.SecretKey.skey)()