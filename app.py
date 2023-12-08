from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Extract values from environment variables
longlived_access_key = os.environ.get('LONG_LIVED_ACCESS_KEY', '')
server_url = os.environ.get('SERVER_URL', '')

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
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
