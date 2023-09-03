import yaml
import subprocess

# Load the YAML configuration file
with open('evilginx2_config.yaml', 'r') as config_file:
    config_data = yaml.load(config_file, Loader=yaml.FullLoader)

# Access the configuration data
phishing_targets = config_data['phishing_targets']
web_server = config_data['web_server']
phishing_domain = config_data['phishing_domain']

# Print the configuration data (you can remove this if not needed)
print("Phishing Targets:")
for target in phishing_targets:
    print(f"Domain: {target['domain']}, SSLStrip: {target['sslstrip']}")
print(f"Web Server Address: {web_server['address']}, Port: {web_server['port']}")
print(f"Phishing Domain: {phishing_domain}")

# Assuming you have Evilginx2 installed, you can run it here with the generated config
try:
    subprocess.run(["evilginx", "-c", "evilginx2_config.yaml"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running Evilginx2: {e}")