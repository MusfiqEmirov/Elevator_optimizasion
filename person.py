import random

person_text_in = "daxil oldu"
person_text_out = "cixdi getdi"

class Person:
    def __init__(self):
        self.p_current_floor = random.randint(1, 10)      
        self.p_target_floor = random.randint(1, 10) 
        self.person_name = random.choice(["leyla", "nigar"])  

    def person_enter(self):
        print(f"{self.person_name} {person_text_in}")

    def person_exit(self):
        print(f"{self.person_name} {person_text_out}")