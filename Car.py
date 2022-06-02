Class Car: 
    Brand = "BMW"
    Model ="KV200
    Year = "2021"

    def __init__(self, brand_name, model, manu_year):
        Self.brand = brand_name
        Self.model = model
        Self.manu_year = year

    def details(self):
        print("car brand is", self.brand)
        print("car model is", self.model)
        print ("car manufacturer year is", self.year)

Brand = input("Car Brand: ")
Model = input("Car Model: ")
Manu_year = input("Car year: ")

car1 = Car(brand, model, manu_year)
car.details()

     
