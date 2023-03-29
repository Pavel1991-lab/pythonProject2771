

from abc import abstractmethod

class Abstractstorage:
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Abstractstorage):
    def __init__(self, items: dict, capacity=100):
        self.items = items
        self.capacity = capacity

    def add(self, name, count):
        if self.get_unique_items_count() > 100:
            raise ValueError("Not enough space in the store")
        if self.get_free_space() < count:
            raise ValueError("Not enough space in the store")
        self.items[name.capitalize()] = self.items.get(name.capitalize(), 0) + count
        if self.items[name.capitalize()] > self.capacity:
            self.items[name.capitalize()] = self.capacity

    def remove(self, name, count):
        if name.capitalize() not in self.items:
            raise ValueError("Item not found")
        if self.items[name.capitalize()] < count:
            raise ValueError("Not enough items in the store")
        self.items[name.capitalize()] -= count
        if self.items[name.capitalize()] == 0:
            del self.items[name.capitalize()]

    def get_free_space(self):
        used_space = sum(self.items.values())
        return self.capacity - used_space

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)


class Shop(Abstractstorage):
    def __init__(self, items: dict, capacity=20):
        self.items = items
        self.capacity = capacity
    def add(self, name, count):
        if self.get_unique_items_count() > 4:
            raise ValueError("Not enough space in the shope")
        if self.get_free_space() < count:
            raise ValueError("Not enough space in the shope")
        self.items[name.capitalize()] = self.items.get(name.capitalize(), 0) + count
        if self.items[name.capitalize()] > self.capacity:
            self.items[name.capitalize()] = self.capacity

    def remove(self, name, count):
        if name.capitalize() not in self.items:
            raise ValueError("Item not found")
        if self.items[name.capitalize()] < count:
            raise ValueError("Not enough items in the store")
        self.items[name.capitalize()] -= count
        if self.items[name.capitalize()] == 0:
            del self.items[name.capitalize()]

    def get_free_space(self):
        used_space = sum(self.items.values())
        return self.capacity - used_space

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)


class Request:
    def __init__(self, request:str):
        parsed_request = request.lower().split(' ')
        if len(parsed_request) != 7:
            raise ValueError("eror")
        self.amount = int(parsed_request[1])
        self.product = parsed_request[2]
        self.depature = parsed_request[4]
        self.destination = parsed_request[6]
    def request(self):
         return f'Доставить {self.amount} {self.product} из {self.depature } в {self.destination}'


