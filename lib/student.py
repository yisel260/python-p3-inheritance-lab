#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self, last_name, first_name):
       
        super().__init__(last_name, first_name)
        self.knowledge = []
    
    def learn(self, string):
        self.knowledge.append(string)
        