import os
class GlobalLabelParameters:
    POST = "POST"
    GET = "GET"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    GET_LOWER_CASE = "get "
    POST_LOWER_CASE = "post "
    PUT_LOWER_CASE = "put "
    DELETE_LOWER_CASE = "delete "
    PATCH_LOWER_CASE = "patch "
    HTTP_URL_PREFIX = "https://"
    HTTP = "HTTP_Signature"
    MERCHANT_ID = "v-c-merchant-id"
    AUTHORIZATION_BEARER = "Authorization"
    REQUEST_TARGET = "(request-target)"
    PUBLIC_KEY = "x5c"
    JWT = "JWT"
    DATE = "Date"
    HOST = "Host"
    SIGNATURE = "Signature"
    USER_AGENT = "User-Agent"
    USER_AGENT_VALUE = "Mozilla/5.0"
    CONTENT_TYPE = "Content-Type"
    APPLICATION_JSON = "application/json"
    V_C_CORRELATION_ID = "v-c-correlation-id"
    DIGEST = "Digest"
    REQUEST_TYPE = "Request Type"
    URL = "URL"
    DIGEST_PREFIX = "SHA-256="
    P12_PREFIX = ".p12"
    SIGNATURE_HEADER = ", signature=\""
    ALGORITHM = ", algorithm=\"HmacSHA256\""
    HEADERS_PARAM = ", headers=\""
    MASKING_VALUE = "XXXXX"
    JWT_TIME = "iat"
    JWT_ALGORITHM = "digestAlgorithm"
    JWT_DIGEST = "digest"
    CYBS_FILE_NAME = 'config_params'
    KEY_ID = "keyid=\""
    LOG_FILE_NAME_DEFAULT = "cybs"
    SANBOX_URL = "apitest.cybersource.com"
    PRODUCTION_URL = "api.cybersource.com"
    SANBOX_RUN_ENVIRONMENT = "CyberSource.Environment.SANDBOX"
    PRODUCTION_RUN_ENVIRONMENT = "CyberSource.Environment.PRODUCTION"
    BOA_SANDBOX_URL = "apitest.merchant-services.bankofamerica.com"
    BOA_PRODUCTION_URL = "api.merchant-services.bankofamerica.com"
    BOA_SANDBOX_RUN_ENVIRONMENT = "BankofAmerica.Environment.SANDBOX"
    BOA_PRODUCTION_RUN_ENVIRONMENT = "BankofAmerica.Environment.PRODUCTION"
    IDC_SANDBOX_URL = "apitest.cybersource.com"
    IDC_PRODUCTION_URL = "api.in.cybersource.com"
    IDC_SANDBOX_RUN_ENVIRONMENT = "CyberSource.in.Environment.SANDBOX"
    IDC_PRODUCTION_RUN_ENVIRONMENT = "CyberSource.in.Environment.PRODUCTION"
    HIDE_MERCHANT_CONFIG_PROPS = "merchantid,merchant_secretkey,merchant_keyid,key_alias,key_password"
    PROXY_PREFIX = "https"
    FILE_NOT_FOUND = "File not found. Check path/filename entered. Entered path/filename : "
    SYSTEM_ERROR = "System error encountered while accessing file : "
    AUTH_ERROR = "Check Authentication Type (HTTP_Signature/JWT) in cybs.json."
    KEY_ALIAS_NULL_EMPTY = "KeyAlias Empty/None. Assigining merchantID value"
    INVALID_KEY_ALIAS = "KeyAlias Invalid. Assigining merchantID value"
    REQUEST_JSON_ERROR = "Request Json File missing. File Path :: "
    KEY_FILE_EMPTY = "KeyFileName is empty, Assigining merchantID value"
    REFER_LOG = "Please refer Log for details"
    MERCHANTID_REQ = "MerchantID is mandatory"
    NOT_ENTERED = "The Following Parameter is Missing in Cybs.Json::"
    INCORRECT_KEY_PASSWORD = "The Entered key_password is Incorrect"
    AUTHENTICATION_REQ = "AuthenticationType is Mandatory"
    MERCHANT_KEY_ID_REQ = "MerchantKeyId is Mandatory"
    MERCHANT_SECRET_KEY_REQ = " MerchantSecretKey is Mandatory"
    PORTFOLIO_ID_REQ = " Portfolio ID is Mandatory"
    KEY_PASSWORD_EMPTY = "KeyPassword Empty/None. Assigining merchantID value"
    INVALID_KEY_PASSWORD = "KeyPassword Invalid. Assigining merchantID value"
    KEY_DIRECTORY_EMPTY = "KeysDirectory not provided. Using Default Path:"
    REQUEST_JSON_EMPTY = "RequestJsonPath not provided"
    INVALID_REQUEST_TYPE_METHOD = "Entered Request Type should be (GET/POST/PUT/PATCH)"
    RUN_ENVIRONMENT_EMPTY = "RunEnvironment Is Mandatory."
    DEFAULT_LOG_FILE_NAME = "Log File Name Empty/None.Using Default Value"
    DEFAULT_ENABLE_LOG = True
    DEFAULT_MAXIMUM_SIZE = 10487560
    DEFAULT_TIMEOUT = 1000
    DEFAULT_LOG_DIRECTORY =os.path.join(os.getcwd(),"Logs")
    DEFAULT_PROXY_ADDRESS = "userproxy.visa.com"
    DEFAULT_PROXY_PORT = 443
    DEFAULT_KEY_FILE_PATH = os.path.join(os.getcwd(),"resources")
    ENABLE_LOG_DEFAULT_MESSAGE = "Enable log value Empty/None.Using Default Value"
    LOG_MAXIMUM_SIZE_DEFAULT_MESSAGE = "Log Maximum Size Empty/None.Using Default Value"
    LOG_DIRECTORY_DEFAULT_MESSAGE = "Log Directory value Empty/None.Using Default Value"
    LOG_DIRECTORY_INCORRECT_MESSAGE = "Log Directory value Incorrect.Using Default Value"
    INVALID_CYBS_PATH = "The Cybs.Json Path Provided Is Incorrect"
