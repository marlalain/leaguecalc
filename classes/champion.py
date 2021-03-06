# importcs
from . import vars
from . import Tools as tools


class Champion:
    def __init__(self, name):
        self.name = name
        self.url = vars.urls['champion'].replace('XXX', self.name)
        self.data = tools.import_json(self.url)['data'][self.name]
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
        if value == "name" or value == "description":  # TODO add images, better the code
            values.append(self.data['passive'][value])
        return values
