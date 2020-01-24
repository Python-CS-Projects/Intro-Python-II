# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


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
        room = 'Current Room: {} \nRoom Items:'.format(self.name)
        for i in self.items:
            room += '\n {}'.format(i)
        return room

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description

    def get_items(self):
        list_of_items = ""
        for i in self.items:
            list_of_items = '\nItems: {}'.format(i)
        return list_of_items

    def set_items(self, new_items):
        self.items.append(new_items)

    def on_take(self, take_item):
        self.items.remove(take_item)
        print("You have picked up {}".format(take_item))

    def on_drop(self, take_item):
        self.items.append(take_item)
        print("You have dropped {}".format(take_item))
