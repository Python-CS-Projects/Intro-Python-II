# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return str(self.name)

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_current_room(self):
        return self.current_room

    def set_current_room(self, new_current_room):
        self.current_room = new_current_room

    def set_item(self, new_item):
        self.items.append(new_item)
        return self.items

    def remove_item(self, item):
        self.items.remove(item)
