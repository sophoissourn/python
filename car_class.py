class Car:
  def __init__(self, model, color, year, car_type):
    self.model = model
    self.color = color
    self.year = year
    self.type = car_type
  
lexus = Car("Lexus", "White", 2007, "SUV")
print(f"Your car is {lexus.model}, {lexus.color} color, and {lexus.type}. It was made in {lexus.year}")
toyota = Car
toyota.model = "Camery"
toyota.color = "Black"
toyota.year = 2020
toyota.type = "SEDAN"
print(f"Your car is {toyota.model}, {toyota.color} color, and {toyota.type}. It was made in {toyota.year}")
    