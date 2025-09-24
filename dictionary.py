students = {
  "dara" : 58.0,
  "sok" : 69.5,
  "vina" : 45.6,
  "mina" : 67.9,
  "bopha" : 90.5
  
}
print("*" * 10,"Data Type Dictionary in Python", "*" * 10) 
# print(type(students))
for key in students:
    print(key, "=", students[key])

cars = {
  "Lexus": {
    "Model" : "RX350",
    "Year" : 2007,
    "Color" : "White",
    "Engine" : 6
  },
  "Toyota" : {
    "Model" : "Camery",
    "Year" : 2024,
    "Color" : "Pearl",
    "Engine" : 4
  },
  "Ford" : {
    "Model" : "Rapter",
    "Year" : 2025,
    "Color" : "Blue",
    "Engine" : 6
  }
}    
print("=" * 10, "Second Exercise on Dictionary Type in Python", "=" * 10)
"""
for m in cars:
  print(m, " :")
  for s in cars[m]:
    print("       " , cars[m][s])
  print("*" * 20)
"""
for (m , obj) in cars.items():
  print(m , " :")
  for s in obj:
    print("       " , s , " :", obj[s])
  print("*" * 20 )
  # for s in m:
  #   print(cars[s])
  
  

