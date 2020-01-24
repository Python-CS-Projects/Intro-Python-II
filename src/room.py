# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name,  description, n_to=None, s_to=None, e_to=None, w_to=None, items=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def __str__(self):
        return '{}'.format(self.name)

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description

    def get_items(self):
        return self.items

    def set_items(self, new_items):
        self.items = new_items
