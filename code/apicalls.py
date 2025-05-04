import requests

# Put your CENT Ischool IoT Portal API KEY here.
APIKEY = "a543155b09f2e0012066f204"

# Retrieves detailed information about a Google Place given its place_id
def get_google_place_details(google_place_id: str) -> dict:
    header = { 'X-API-KEY': APIKEY}
    params = { 'place_id': google_place_id}
    url = "https://cent.ischool-iot.net/api/google/places/details"
    # Sends a GET request with place_id as a parameter
    response = requests.get(url, header=header, params=params)
    # Returns structured place details (such as name, address, or etc)
    return response.jsoon()

# Uses Azure's Sentiment Analysis to determine if the text is positive, neutral, or negative
def get_azure_sentiment(text: str) -> dict:
    header = {'X-API-KEY': APIKEY}
    data = {"text": text}
    url = "https://cent.ischool-iot.net/api/azure/sentiment"
    # Send a POST request with the input text in the body
    response = requests.post(url, headers=header, data=data)
    response.raise_for_status()
    # Return a dictionary with sentiment scores and classication
    return response.json()

# Extract key phrases from a given piece of text using Azure's NLP services
def get_azure_key_phrase_extraction(text: str) -> dict:
    header = { 'X-API-KEY': APIKEY}
    data = {"text":text}
    url = "https://cent.ischool-iot.net/api/azure/keyphrasextraction"
    # Sends a POST request with the input text
    response = requests.post(url, headers=header, data=data)
    # Return key phrases found in the text
    return response.json()

# Identifies named entities (such as people, places, organizations) in the text
def get_azure_named_entity_recognition(text: str) -> dict:
    header = {'X-API-KEY': APIKEY}
    data = { "text": text}
    url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
    # Send a POST request with texxt to Azure's NER API
    response = requests.post(url, headers=header, data=data)
    response.raise_for_status()
    # Return a list of recognized entities and their types
    return response.json()


def geocode(place:str) -> dict:
    '''
    Given a place name, return the latitude and longitude of the place.
    Written for example_etl.py
    '''
    header = { 'X-API-KEY': APIKEY }
    params = { 'location': place }
    url = "https://cent.ischool-iot.net/api/google/geocode"
    response = requests.get(url, headers=header, params=params)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary


def get_weather(lat: float, lon: float) -> dict:
    '''
    Given a latitude and longitude, return the current weather at that location.
    written for example_etl.py
    '''
    header = { 'X-API-KEY': APIKEY }
    params = { 'lat': lat, 'lon': lon, 'units': 'imperial' }
    url = "https://cent.ischool-iot.net/api/weather/current"
    response = requests.get(url, headers=header, params=params)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary