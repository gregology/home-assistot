from flask import Flask, render_template
import requests
import yaml

app = Flask(__name__)

# Function to read configuration from the YAML file
def read_config():
    with open('configuration.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config.get('home-assistant', {})

# Extract values at startup
config_data = read_config()
longlived_access_key = config_data.get('longlived-access-key', '')
server_url = config_data.get('server', '')

# Home Assistant API endpoint for script execution
api_endpoint = f"{server_url}/api/services/script/turn_on"

# Headers for Home Assistant API authentication
headers = {
    'Authorization': f'Bearer {longlived_access_key}',
    'Content-Type': 'application/json',
}

# Define routes
@app.route('/')
def home():
    return render_template('index.html', longlived_access_key=longlived_access_key, server_url=server_url)

# Trigger scripts on section click
@app.route('/trigger_script/<color>')
def trigger_script(color):
    script_name = color.lower()
    script_data = {
        "entity_id": f"script.{script_name}"
    }
    response = requests.post(api_endpoint, headers=headers, json=script_data)
    return f"Script triggered: {script_name}. Response: {response.status_code}"

if __name__ == '__main__':
    app.run(debug=True)
