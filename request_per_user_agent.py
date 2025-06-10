import re
# from helper import is_valid_ip

log_file = './NodeJsApp.log'

agent_dict = {}

with open(log_file, 'r') as file:
    lines = file.readlines()
    
    for line in lines:
        agent_data = re.search(r'"([^"]+)"$', line)
        agent = agent_data.group(1) if agent_data else None
        if agent:
            if 'Linux' in agent and 'Chrome' in agent:
                the_agent = 'Chrome(Linux)'
            elif 'Mac' in agent and 'Chrome' in agent  and 'Safari' not in agent:
                the_agent = 'Chrome(Mac)'
            elif 'Mac' in agent and 'Chrome' not in agent  and 'Safari' in agent:
                the_agent = 'Safari(Mac)'
            elif 'Windows' in agent and 'Chrome' in agent:
                the_agent = 'Chrome(Windows)'
                    
            if agent_dict.get(the_agent):
                    agent_dict[the_agent] += 1
            else:
                agent_dict[the_agent] = 1

for key, value in agent_dict.items():
    print(f'{value} request came from {key}')
