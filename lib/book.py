#!/usr/bin/env python3

class Book:
        
    def __init__(self, title, page_count):
        
       self.title = title 
       self.page_count = page_count
       
       
    def get_page_count(self):
        print("getting page count")
        return self._page_count
    
    def set_page_count(self, page_count):
        if type(page_count) == int:
            print("setting page_count")
            self._page_count = page_count
        else:
            print("page_count must be an integer")
       
    page_count = property(get_page_count, set_page_count)
    
          
  
    # def int_page_count(page_count):
    #     if(isinstance(page_count, int)) :
    #         return page_count
    #     else :
    #         print("page_count must be an integer")
    
    
    # def __init__(self, title, page_count=0):
    #     self.title = title
    #     self.page_count = page_count

    # def turn_page(self):
    #     print("Flipping the page...wow, you read fast!")

    # def get_page_count(self):
    #     print("running get_page")
    #     return self._page_count

    # def set_page_count(self, value):
    #     print("running set_page")
    #     if type(value) == int:
    #         self._page_count = value

    #     print("page_count must be an integer")
    # print("about to hit property")
    # page_count = property(get_page_count, set_page_count)