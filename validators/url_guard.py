import socket
import ipaddress
from urllib.parse import urlparse

# ranges we never want the renderer to reach from inside the VPC
BLOCKED_NETS = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("169.254.0.0/16"),
    ipaddress.ip_network("127.0.0.0/8"),
]


def _is_public(ip):
    addr = ipaddress.ip_address(ip)
    return not any(addr in net for net in BLOCKED_NETS)


def validate_asset_url(url):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError("unsupported scheme")
    host = parsed.hostname
    if not host:
        raise ValueError("missing host")
    resolved = socket.gethostbyname(host)
    if not _is_public(resolved):
        raise ValueError("asset points to a private address")
    return url
