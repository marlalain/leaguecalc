# imports
import json, requests
# vars
version = "11.4.1"
champions = {}
urls = {
    'champion': f"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/XXX.json"
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
# main
if __name__ == '__main__':
    main()