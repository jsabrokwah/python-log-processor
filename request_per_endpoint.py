import re

log_file = 'NodeJsApp.log'

endpoints = {}

with open(log_file, 'r') as f:
    for line in f:
        if 'Server running' in line or not '"GET' in line:
            continue
            
        match = re.search(r'"([^"]+)"', line.strip())
        if match:
            endpoint = match.group(1)
            if endpoint in endpoints:
                endpoints[endpoint] += 1
            else:
                endpoints[endpoint] = 1

print("Request count per endpoint:")
for endpoint, count in endpoints.items():
    print(f"{endpoint}: {count}")