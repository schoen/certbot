"""Some useful constants to use throughout certbot-ci integration tests"""
DEFAULT_HTTP_01_PORT = 5002
TLS_ALPN_01_PORT = 5001
CHALLTESTSRV_PORT = 8055
BOULDER_V2_CHALLTESTSRV_URL = f'http://10.77.77.77:{CHALLTESTSRV_PORT}'
BOULDER_V2_DIRECTORY_URL = 'http://localhost:4001/directory'
PEBBLE_DIRECTORY_URL = 'https://localhost:14000/dir'
PEBBLE_MANAGEMENT_URL = 'https://localhost:15000'
PEBBLE_CHALLTESTSRV_URL = f'http://localhost:{CHALLTESTSRV_PORT}'
MOCK_OCSP_SERVER_PORT = 4002
PEBBLE_ALTERNATE_ROOTS = 2
MAX_SUBPROCESS_WAIT = 120
