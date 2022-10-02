if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()


import sys
import os
import os.path
from configparser import ConfigParser, BasicInterpolation


class EnvInterpolation(BasicInterpolation):
    def before_get(self, parser, section, option, value, defaults):
        value = super().before_get(parser, section, option, value, defaults)
        if not os.path.expandvars(value).startswith("$"):
            return os.path.expandvars(value)
        else:
            return


try:
    config = ConfigParser(interpolation=EnvInterpolation())
    config.read(f"conf/application.conf")

except:
    print("Error while loading the configuration")
    print("Exiting")
    sys.exit(1)


class Credentials:
    class AccessKey:
        akey = config.get("ACCESS_KEY",'akey')
        if not akey:
            print("Error, ENV variable ACCESS KEY not set")
            sys.exit(1)
    
    class SecretKey:
        skey = config.get("SECRET_KEY",'skey')
        if not skey:
            print("Error, ENV variable SECRET KEY not set")
            sys.exit(1)