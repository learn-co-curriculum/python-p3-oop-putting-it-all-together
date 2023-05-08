#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size = 0):
        self.brand = brand
        self.size = size
        
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if type(size)  == int:
            self._size = size
        else:
            print("not an integer")
            
    size = property(get_size, set_size)