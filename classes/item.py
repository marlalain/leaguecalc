# imports
from . import tools
from . import vars


class Item:
    def __init__(self, id):
        self.id = str(id),
        self.data = vars.datas['items'][id]
        self.name = self.data["name"]

    def get(id, var):
        """Returns an Item variable based on an id

        Args:
            id (string): Item id
            var (string): Name of the variable (to be returned)

        Returns:
            Item variable based on an id
        """
        return tools.import_json(vars.urls['items'])['data'][id][var]

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
        for item in vars.datas['items']:
            if name == vars.datas['items'][item]["name"]:
                return item
