REMOVE_SDKROOT_FROM_ENV = True

FILE_NAME_CONANFILE_TXT = "conanfile.txt"
FILE_NAME_CONANFILE_PY = "conanfile.py"
FILE_NAME_DIST_PACKED = "dist.tar.gz"

AWS_KEY_ID_ENV = "NATIVIUM_AWS_KEY_ID"
AWS_SECRET_KEY_ENV = "NATIVIUM_AWS_SECRET_KEY"

AWS_S3_BUCKET_NAME = "nativium"
AWS_S3_DOCS_BUCKET_NAME = "nativium"
AWS_S3_BUCKET_PATH = "dist"
AWS_S3_URL = "https://{0}.s3.amazonaws.com/{1}".format(
    AWS_S3_BUCKET_NAME, AWS_S3_BUCKET_PATH
)

TARGET_VERBS_INTERNAL = ["config"]

PROFILE_BUILD_WINDOWS = "default"
PROFILE_BUILD_MACOS = "default"
PROFILE_BUILD_LINUX = "default"
PROFILE_BUILD_DEFAULT = "default"

DOCS_DEFAULT_NAME = "main"

APPLE_OS_LIST = ["iOS", "tvOS", "watchOS", "Macos"]
APPLE_MOBILE_OS_LIST = ["iOS", "tvOS", "watchOS"]

HTTP_SERVER_HOST = "127.0.0.1"
HTTP_SERVER_PORT = "8000"
