 

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def upload_building(self):
            with open('building.txt', 'a') as file:
                file.write(self.name + "," + str(self.floors) + "\n")
    def download_building(self):
        f = open('building.txt', 'r')
        content = f.read()
        print(content)
        f.close()
        
testing = Building("Test", 5)
testing.upload_building()
testing.download_building()
        
                                      
    

  
   


# Expected Outcome: A complete Building class with 
# methods for saving to and loading details from a file.
# A script demonstrating saving multiple buildings to a file and
# then reading them back into the program.
