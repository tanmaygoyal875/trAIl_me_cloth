from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Myntra API endpoint
MYNTRA_API_URL = "https://fake-myntra-api.com/products"

# Amazon API endpoint
AMAZON_API_URL = "https://fake-amazon-api.com/products"

@app.route('/recommend', methods=['POST'])
def recommend_clothing():
    data = request.json
    preferences = data.get('preferences', {})
    body_type = data.get('body_type', '')

    # Fetch clothing data from Myntra API
    myntra_data = fetch_clothing_data(MYNTRA_API_URL, preferences, body_type)

    # Fetch clothing data from Amazon API
    amazon_data = fetch_clothing_data(AMAZON_API_URL, preferences, body_type)

    # Combine data from both APIs
    all_data = myntra_data + amazon_data

    # Use fuzzy logic model for recommendation
    recommended_items = fuzzy_logic_recommendation(all_data)

    return jsonify(recommended_items)

def fetch_clothing_data(api_url, preferences, body_type):
    # Make request to API
    response = requests.get(api_url)
    data = response.json()

    # Filter data based on preferences and body type (dummy filtering)
    filtered_data = [item for item in data if item['category'] in preferences.get('categories', [])]

    return filtered_data

def fuzzy_logic_recommendation(data):
    # Dummy fuzzy logic recommendation (random selection)
    recommended_items = data[:5]
    return recommended_items

if __name__ == '__main__':
    app.run(debug=True)
