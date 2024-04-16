class Bus:
    def __init__(self,passengers,route):
        self.city = "Chicago"
        self.company = "CT Travels"
        self.passengers=passengers
        self.route=route
    def routes(self):
        print(f"This bus from {self.company} in {self.city} will go from {self.route} with {self.passengers} passengers")

bus1 = Bus(50, "CH-IL")
bus2 = Bus(20, "MVD-COL")
bus1.routes()        
bus2.routes()      