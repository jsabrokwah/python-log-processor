from ipaddress import ip_address
from datetime import datetime
def is_valid_ip(address):
    try:
        ip_address(address)
        return True
    except ValueError:
        return False

def sort_lines(file_lines):
    return sorted(file_lines, key=lambda line: datetime.strptime(line.split(' ')[0], "%Y-%m-%dT%H:%M:%S.%fZ"))