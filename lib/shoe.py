#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand
        

    def cobble(self):
        self.condition = "New"
        print('Your shoe is as good as new!')