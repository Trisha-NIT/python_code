class car:  
    def __init__(self, model, year, speed, colour):  
        self.vehicle_model = model
        self.vehicle_year = year
        self.max_speed = speed
        self.vehicle_colour = colour

    def speed(self):  
            print(self.max_speed)
    
    def colour(self):
            print(self.vehicle_colour)

    def year(self):
            print(self.vehicle_year)

    def model(self):
            print(self.vehicle_model)

def max_seat(seating):
        print(str(max_seat))

max_seat(5)        

       
car_1 = car("Toyota", 2016, 120, "blue")
car_2 = car("swift", 2012, 110, "white")




car_1.speed()
car_1.colour()
car_2.year()
car_2.model()