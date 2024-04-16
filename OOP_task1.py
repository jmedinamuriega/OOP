# 1. 
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    def update_owner(self,new_owner):
        self.owner=new_owner

vehicle1=Vehicle("LAB1441","FIAT SIENA", "JMEDINA")    
vehicle2=Vehicle("LAA3312","MITSUBISHI SPORTERO","RANDOM")

print(vehicle2.owner)
print(vehicle1.owner)

vehicle1.update_owner("New Owner1")
vehicle2.update_owner("New Owner2")

print(f"Here is the updates owners:{vehicle1.owner} and {vehicle2.owner}")



class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0

    def add_participant(self):
        self.participants += 1

    def get_participant_count(self):
        print(f"The number of assistants is {self.participants}")

event = Event("My Event", "2024-04-15")
event.get_participant_count()