# imports
import json, requests
# constants
VERSION = "11.5.1"
LANGUAGE = "en_US"
champions, datas, items = {}, {}, []
urls = {
    'champion': f"http://ddragon.leagueoflegends.com/cdn/{VERSION}/data/{LANGUAGE}/champion/XXX.json",
    'items': f"http://ddragon.leagueoflegends.com/cdn/{VERSION}/data/{LANGUAGE}/item.json"
}
# classes
class Champion:
    def __init__(self, name):
        self.name = name
        self.url = urls['champion'].replace('XXX', self.name)
        self.data = import_json(self.url)['data'][self.name]
        self.spells = self.data['spells']
        self.items = []
    def _get_stat_on_level(self, stat, level):
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
    def _get_raw_stat_on_level(self, stat, level):
        base_stat = self.data['stats'][stat]
        stat_per_level = self.data['stats'][f"{stat}perlevel"]
        return base_stat + (stat_per_level * (level - 1))
    def _add_item(self, item):
        self.items.append(item)
    def _get_spell(self, spell):
        """Get spell from self.spell

        Args:
            spell (string): Spells to be returned

        Returns:
            list or dict: Depending on the number of spells asked, will return the dict or a list of dicts
        """
        out = []
        spell = list(spell)
        for letter in spell:
            print('letter', letter)
            for s in self.spells:
                if s['id'].find(letter) != -1:
                    out.append(s)
        if spell == "P":
            out.append(self.data['passive'])
        if len(out) == 1:
            return out[0]
        else:
            return out
    def _get_spells_values(self, value):
        values = []
        # Adding Q/W/E/R spells
        for spell in self.spells:
            values.append(spell[value])
        # Adding passive
        if value == "name" or value == "description": # TODO add images, better the code
            values.append(self.data['passive'][value])
        return values
class Item:
    def __init__(self, id):
        self.id = str(id),
        #self.name = import_json(urls['items'])['data'][id]['name']
        #self.data = import_json(urls['items'])['data'][id]
        self.data = datas['items'][id]
        self.name = self.data["name"]
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
    def get_id(name):
        for item in datas['items']:
            if name == datas['items'][item]["name"]:
                return item

class Calculator:
    def _get_stat_on_level(base_stat, stat_per_level, level):
        return base_stat + (stat_per_level * (level - 1))

# defs
def import_json(url):
    return requests.get(url).json()
def main():    
    datas.update({
        'items': import_json(urls['items'])['data']
    })
    champions.update({
        'fiora': Champion("Fiora")
    })

    # Showing all CDRs for a champion
    #print(champions['fiora']._get_spell("E")['name'])
    #print(champions['fiora']._get_spell("E")['cooldownBurn'])
    #print(champions['fiora']._get_spell("R")['name'])
    #print(champions['fiora']._get_spell("R")['cooldownBurn'])
    # Showing values for specific spells, e.g. "QE", "QWER", "QWEP", ...
    for spell in champions['fiora']._get_spell("QE"):
        print(spell['name'])

    # Adding items and calculating new stats
    #champions['twitch'].add_item(Item('1011')) # adding Giant's Belt
    #print(Item('1011').data["name"]) # Item of id 1011 is Giant's Belt
    # Twitch's base HP at level 1 is 612:
    #print(champions['twitch'].get_raw_stat_on_level("hp", 1))
    # Giant's Belt gives 350 HP
    #print(Item('1011').get_stats()["FlatHPPoolMod"])
    # Calculating base Twitch's stats plus their items:
    #print(champions['twitch'].get_stat_on_level("hp", 1))
    #for item in datas['items']:
    #    items.append(datas['items'][item]["name"])
    #print(Item.get_id("Dagger"))
    
# main
if __name__ == '__main__':
    main()