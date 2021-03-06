# imports
import sys  # for args when running 'standalone'

from classes import *  # importing from ./classes/

def main():
    vars.datas.update({
        'items': tools.import_json(vars.urls['items'])['data']
    })
    vars.champions.update({
        'fiora': Champion("Fiora"),
        'twitch': Champion("Twitch")
    })

    if sys.argv[1] == 'get':
        vars.champions.update({
            sys.argv[2]: Champion(sys.argv[2])
        })
        print(vars.champions[sys.argv[2]].data)

    # Showing all CDRs for a champion
    # print(champions['fiora']._get_spell("E")['name'])
    # print(champions['fiora']._get_spell("E")['cooldownBurn'])
    # print(champions['fiora']._get_spell("R")['name'])
    # print(champions['fiora']._get_spell("R")['cooldownBurn'])
    # Showing values for specific spells, e.g. "QE", "QWER", "QWEP", ...
    # for spell in champions['fiora']._get_spell("QE"):
    #    print(spell['name'])

    # Adding items and calculating new stats
    vars.champions['twitch'].add_item(item.Item('1011'))  # adding Giant's Belt
    # print(Item('1011').data["name"]) # Item of id 1011 is Giant's Belt
    # Twitch's base HP at level 1 is 612:
    #print(champions['twitch'].get_raw_stat_on_level("hp", 1))
    # Giant's Belt gives 350 HP
    # print(Item('1011').get_stats()["FlatHPPoolMod"])
    # Calculating base Twitch's stats plus their items:
    #print(champions['twitch'].get_stat_on_level("hp", 1))
    # for item in datas['items']:
    #    items.append(datas['items'][item]["name"])
    # print(Item.get_id("Dagger"))


# main
if __name__ == '__main__':
    main()
