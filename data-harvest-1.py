import requests

def search_internet(query):
    url = f"https://www.searchengine.com/search?q={query}"
    response = requests.get(url)
    return response.text

def harvest_data():
    query = input("Enter a topic to search: ")
    search_results = search_internet(query)
