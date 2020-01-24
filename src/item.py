class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return "{}, {}".format(self.name, self.description)

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.name = new_description
