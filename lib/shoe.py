#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'

    def get_size(self):
        return self._size

    def set_size(self, size):
        size_type = type(size)
        if size_type == int:
            self._size = size
        if size_type != int:
            print('size must be an integer')


    size = property(get_size, set_size)