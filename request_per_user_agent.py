import re  # Import regular expression module for pattern matching

# Path to the log file to be processed
log_file = './NodeJsApp.log'

# Dictionary to store count of requests per user agent
agent_dict = {}

# Open and read the log file
with open(log_file, 'r') as file:
    lines = file.readlines()
    
    # Process each line in the log file
    for line in lines:
        # Extract user agent string using regex - looking for the last quoted string in the line
        agent_data = re.search(r'"([^"]+)"$', line)
        # Get the matched group or None if no match
        agent = agent_data.group(1) if agent_data else None
        if agent:
            # Categorize user agents based on OS and browser
            # if 'Linux' in agent and 'Chrome' in agent:
            #     the_agent = 'Chrome(Linux)'
            # elif 'Mac' in agent and 'Chrome' in agent  and 'Safari' not in agent:
            #     the_agent = 'Chrome(Mac)'
            # elif 'Mac' in agent and 'Chrome' not in agent  and 'Safari' in agent:
            #     the_agent = 'Safari(Mac)'
            # elif 'Windows' in agent and 'Chrome' in agent:
            #     the_agent = 'Chrome(Windows)'
             # Categorize user agent by browser/platform
            if "Chrome" in agent and "Safari" in agent:
                if "Macintosh" in agent:
                    the_agent = "Chrome (Mac)"
                elif "Windows" in agent:
                    the_agent = "Chrome (Windows)"
                elif "Linux" in agent:
                    the_agent = "Chrome (Linux)"
                else:
                    the_agent = "Chrome (Other)"
            elif "Safari" in agent and "Macintosh" in agent and "Chrome" not in agent:
                the_agent = "Safari (Mac)"
            elif "Firefox" in agent:
                the_agent = "Firefox"
            elif "MSIE" in agent or "Trident" in agent:
                the_agent = "Internet Explorer"
            elif "Edge" in agent:
                the_agent = "Edge"
            else:
                the_agent = "Other"
                    
            # Increment the count for this agent category or initialize to 1 if first occurrence
            if agent_dict.get(the_agent):
                    agent_dict[the_agent] += 1
            else:
                agent_dict[the_agent] = 1

# Print the results - number of requests per user agent category
for key, value in agent_dict.items():
    print(f'{value} request came from {key}')
