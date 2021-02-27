# imports
import json, requests
# vars
version = "11.4.1"
language = "en_US"
champions = {}
urls = {
    'champion': f"http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/champion/XXX.json",
    'items': f"http://ddragon.leagueoflegends.com/cdn/{version}/data/{language}/item.json"
}
# classes
class Champion:
    def __init__(self, name):
        self.name = name
        self.url = urls['champion'].replace('XXX', self.name)
        self.data = import_json(self.url)['data'][self.name]
        self.items = []
    def get_stat_on_level(self, stat, level):
        base_stat = self.data['stats'][stat]
        stat_per_level = self.data['stats'][f"{stat}perlevel"]
        return base_stat + (stat_per_level * (level - 1))
    def add_item(self, item):
        self.items.append(item)
class Item:
    def __init__(self, id):
        self.id = str(id),
        self.data = import_json(urls['items'])['data'][id]
    def get(id, var):
        """Returns an Item variable based on an id

        Args:
            id (string): Item id
            var (string): Name of the variable (to be returned)
        
        Returns:
            Item variable based on an id
        """
        return import_json(urls['items'])['data'][id][var]
class Calculator:
    def get_stat_on_level(base_stat, stat_per_level, level):
        return base_stat + (stat_per_level * (level - 1))

# defs
def import_json(url):
    return requests.get(url).json()
def main():
    champions.update({
        'twitch': Champion("Twitch")
    })
    print("L1:", champions['twitch'].get_stat_on_level('hp', 1))
    print("L18:", champions['twitch'].get_stat_on_level('hp', 18))
    champions['twitch'].add_item(Item('1001'))
    print(Item.get("1011", "name"))
    champions['twitch'].add_item(Item('1011'))
    for item in champions['twitch'].items:
        print(item.data["name"])
# main
if __name__ == '__main__':
    main()