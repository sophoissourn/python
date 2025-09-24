def show_message():
  print("Welcome to Python function!")

def check_is_number(size1, size2):
  if size1.isdigit() or size2.isdigit(): 
    return True
  else:
    print("Accept ONLY NUMBER!")
    
def user_input():
  shape_types = ["rectangle", "triangle", "circle", "square", "eclipse"]
  
  area_type = input("Please enter a kind of area to calculate (rectangle, triangle, circle, square, eclipse): ")
  
  if area_type in shape_types:
    
    area_size1 = input(f"Please enter the first length of {area_type}: ")
    area_size2 = input(f"Please endter the second length of {area_type}: ")
    
    if check_is_number(area_size1, area_size2):
      area_size1 = float(area_size1)
      area_size2 = float(area_size2)
      square_meters = 0
      match area_type:
        case "eclipse":
          square_meters = 3.14 * (area_size1 * area_size2)
        case "rectangle" | "square" | "circle":
          square_meters = area_size1 * area_size2
        case "triangle":
          square_meters = (area_size1 * area_size2) / 2
          
      print(f"The square meter of {area_type} with length: {area_size1} and width: {area_size2} is {square_meters:,.2f}")
  else:
    print(f"Please enter the area shape correctly {shape_types}")

def main():
  while True:
    show_message()
    user_input()
    confirm = input("To exit types x !")
    if confirm.lower() == "x": break
  
  

main()  