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
        """Returns a stat on a certain level

        Args:
            stat (string): Stat to be returned
            level (int): Level of the champion (stat)

        Returns:
            int: X stat on Y level
        """
        # calculate base and *perlevel stat
        base_stat = self.data['stats'][stat]
        stat_per_level = self.data['stats'][f"{stat}perlevel"]
        base = base_stat + (stat_per_level * (level - 1))
        # calculate items stats
        for item in self.items:
            for item_stat in item.get_stats():
                if item_stat.lower().find(stat.lower()) != -1:
                    items = item.get_stats()[item_stat]
        return base + items
    def get_raw_stat_on_level(self, stat, level):
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
    def get_stats(self):
        """Get all stats from an item

        Raises:
            ValueError: If there are no stats on item

        Returns:
            dict: Stats names and values
        """
        if len(self.data["stats"]) == 0:
            raise ValueError("Min. stat needed is 1, not 0.")
        else:
            return self.data["stats"]

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
    champions['twitch'].add_item(Item('1011')) # adding Giant's Belt
    print(Item('1011').data["name"]) # Item of id 1011 is Giant's Belt
    # Twitch's base HP at level 1 is 612:
    print(champions['twitch'].get_raw_stat_on_level("hp", 1))
    # Giant's Belt gives 350 HP
    print(Item('1011').get_stats()["FlatHPPoolMod"])
    # Calculating base Twitch's stats plus their items:
    print(champions['twitch'].get_stat_on_level("hp", 1))
# main
if __name__ == '__main__':
    main()