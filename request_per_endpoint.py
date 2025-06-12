import re  # Import regular expression module for pattern matching

# Path to the log file to be processed
log_file = 'NodeJsApp.log'

# Dictionary to store count of requests per endpoint
endpoints = {}

# Open and read the log file
try:
    with open(log_file, 'r') as f:
        for line in f:
            # Skip server startup messages and non-GET requests
            if 'Server running' in line or not '"GET' in line:
                continue
                
            # Extract the HTTP request (endpoint) using regex - first quoted string in the line
            match = re.search(r'"([^"]+)"', line.strip())
            if match:
                endpoint = match.group(1)  # Get the matched endpoint
                # Increment the count for this endpoint or initialize to 1 if first occurrence
                if endpoint in endpoints:
                    endpoints[endpoint] += 1
                else:
                    endpoints[endpoint] = 1

except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)

# Print the results header
print("Request count per endpoint:")
# Print each endpoint and its request count
for endpoint, count in endpoints.items():
    print(f"{endpoint}: {count} requests")