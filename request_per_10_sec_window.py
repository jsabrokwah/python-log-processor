
from datetime import datetime
from helper import is_valid_ip

log_file = './NodeJsApp.log'
window_dict = {}
ip_dict = {}
temp_time = None
initial_time = None
window = 1

with open(log_file,'r') as f:
    for line in f:
        line_array = line.strip().split(' ')
        temp_time = line_array[0]
        ip = line_array[1]
        
        if is_valid_ip(ip):
            if not ip_dict.get(ip):
                ip_dict[ip] = 1
            elif ip_dict.get(ip): 
                ip_dict[ip] +=1
            
            if not initial_time:
                    initial_time = datetime.strptime(temp_time, "%Y-%m-%dT%H:%M:%S.%fZ")
        
            new_time = datetime.strptime(temp_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            if(new_time - initial_time).seconds >= 10:
                initial_time = datetime.strptime(temp_time, "%Y-%m-%dT%H:%M:%S.%fZ")
                window_dict[f"10_min_window_{window}"] = ip_dict
                window += 1
                ip_dict = {}
            
        
for win_key, win_value in window_dict.items():
    for key, value in win_value.items():
        prefix = win_key.replace('_',' ')
        print(f"In {prefix}, IP {key} made {value} requests")
    print('\n------------------------------\n')

