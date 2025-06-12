from helper import is_valid_ip,sort_lines  # Import helper functions for IP validation and log sorting
from datetime import datetime  # Import for date/time operations

# Path to the log file to be processed
log_file = './NodeJsApp.log'

# Dictionary to store IP addresses and their request counts within 10-second windows
ip_dict = {}

try:
    with open(log_file,'r') as file:
        file_lines = file.readlines()  # Read all lines from the log file
        sorted_lines = sort_lines(file_lines)  # Sort lines by timestamp

        # Process each line in the sorted log file
        for line in sorted_lines:
            line_array = line.strip().split(' ')  # Split the line into components
            temp_time = line_array[0]  # Extract timestamp
            ip = line_array[1]  # Extract IP address
            
            # If this is a valid IP and we haven't seen it before
            if is_valid_ip(ip) and ip not in ip_dict:
                initial_time = datetime.strptime(temp_time, "%Y-%m-%dT%H:%M:%S.%fZ")  # Parse timestamp
                ip_dict[ip] = [1,initial_time]  # Store count (1) and initial timestamp
            
            # If this is a valid IP and we've seen it before
            elif is_valid_ip(ip) and ip in ip_dict:
                new_time = datetime.strptime(temp_time, "%Y-%m-%dT%H:%M:%S.%fZ")  # Parse timestamp
                # Check if this request is within 10 seconds of the first request from this IP
                if (new_time - ip_dict[ip][1]).seconds < 10:
                    ip_dict[ip][0] += 1  # Increment the request count for this IP

except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)


# Print results - number of requests per IP within a 10-second window
for key, value in ip_dict.items():
    print(f"IP {key} made {value[0]} requests in 10 secs")