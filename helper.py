from ipaddress import ip_address
def is_valid_ip(address):
    try:
        ip_address(address)
        return True
    except ValueError:
        return False