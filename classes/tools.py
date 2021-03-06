# imports
import requests

class Tools:
    def import_json(url):
       return requests.get(url).json()