# inspect_cert.py

import ssl
import socket

hostname = "pypi.org"

context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(
        sock,
        server_hostname=hostname
    ) as ssock:

        print(ssock.getpeercert())