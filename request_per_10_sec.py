from helper import is_valid_ip,sort_lines
from datetime import datetime

log_file = './NodeJsApp.log'

ip_dict = {}


with open(log_file,'r') as file:
    file_lines = file.readlines()
    sorted_lines = sort_lines(file_lines)

    for line in sorted_lines:
        line_array = line.strip().split(' ')
        temp_time = line_array[0]
        ip = line_array[1]
        if is_valid_ip(ip) and ip not in ip_dict:
            initial_time = datetime.strptime(temp_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            ip_dict[ip] = [1,initial_time]
        elif is_valid_ip(ip) and ip in ip_dict:
            new_time = datetime.strptime(temp_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            if (new_time - ip_dict[ip][1]).seconds < 10:
                ip_dict[ip][0] += 1


for key, value in ip_dict.items():
    print(f"IP {key} made {value[0]} requests in 10 secs")