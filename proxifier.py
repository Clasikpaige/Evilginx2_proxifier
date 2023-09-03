import yaml

# Load the YAML configuration file
with open('evilginx2_config.yaml', 'r') as config_file:
    config_data = yaml.load(config_file, Loader=yaml.FullLoader)

# Access the configuration data
phishing_targets = config_data['phishing_targets']
web_server = config_data['web_server']
phishing_domain = config_data['phishing_domain']

# Now you can use the configuration data as needed
print("Phishing Targets:")
for target in phishing_targets:
    print(f"Domain: {target['domain']}, SSLStrip: {target['sslstrip']}")
print(f"Web Server Address: {web_server['address']}, Port: {web_server['port']}")
print(f"Phishing Domain: {phishing_domain}")
