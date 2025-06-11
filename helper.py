from ipaddress import ip_address  # Import for IP address validation
from datetime import datetime  # Import for date/time parsing and manipulation

def is_valid_ip(address):
    """
    Validates if a string is a valid IP address.
    
    Args:
        address: String to validate as IP address
        
    Returns:
        True if valid IP address, False otherwise
    """
    try:
        ip_address(address)  # Attempt to create an IP address object
        return True  # Return True if successful
    except ValueError:
        return False  # Return False if the string is not a valid IP address

def sort_lines(file_lines):
    """
    Sorts log lines by their timestamp.
    
    Args:
        file_lines: List of log lines to sort
        
    Returns:
        Sorted list of log lines by timestamp
    """
    # Sort lines based on the timestamp at the beginning of each line
    # Format: YYYY-MM-DDTHH:MM:SS.sssZ
    return sorted(file_lines, key=lambda line: datetime.strptime(line.split(' ')[0], "%Y-%m-%dT%H:%M:%S.%fZ"))