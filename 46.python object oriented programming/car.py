
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale 

    def drive(self):
        print("You drive the car")
    
    def stop(self):
        print("You stop the car")        # these methods are identical for each object

    # ------ let's insert the model of the car
    
    # ---- self is referring to the object we are currently working with

    def drive(self):
        print(f"You drive the {self.color} {self.model}")
    
    def stop(self):
        print(f"You stop the {self.color} {self.model}") 


    # for describe the car
    
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

