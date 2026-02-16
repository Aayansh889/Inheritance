class Vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage
class bus(Vehicle):
    pass
buss=bus("School Volvo",180,12)
print(f"Vehicle Name:{buss.name}, Max Speed:{buss.maxspeed}, Mileage:{buss.mileage}")