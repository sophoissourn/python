from tabulate import tabulate
class Person:
  def __init__(self, f_name, l_name, sex, age):
    self.f_name = f_name
    self.l_name = l_name
    self.sex = sex
    self.age = age
    
  def __str__(self):
    return(f"My name is {self.l_name} {self.f_name}; I am {self.sex} and {self.age} years old.")

  def show_info(self):
    print(f"My name is {self.l_name} {self.f_name}; I am {self.sex} and {self.age} years old.")
  
person1 = Person("Sourn", "Sophois", "Male", 45)
print()
person1.show_info()

person2 = Person("Sok", "Dara","Female", 25)
print(person2)
print()
print("*" * 10, "Inheritance Class", "*" * 10)

class Student(Person):
  num_of_students = 0
  school_fee_discount = 1.08
  def __init__(self, f_name, l_name, sex, age, subject, level):
    super().__init__(f_name, l_name, sex, age)
    self.subject = subject
    self.university_level = level
    
    Student.num_of_students += 1
    
  def display_subject(self):
    print(f"Student's degree is {self.university_level} with subject of {self.subject}")
  
  @classmethod
  def discount_amount(self):
    print(f"Every student is discounted for their school fee {(Student.school_fee_discount * 100) - 100:.2f}%")

print()
# student1 = Student("Soeun", "Panharith", "Male", 14, "Computer Science", "Master Degree")
# print(student1)
# student1.display_subject()
# print()
# student2 = Student("Soeun", "Panhachakriya", "Female", 15, "Doctor", "Doctor Degree")
# student2.show_info()
# student2.display_subject()
# print()
# student3 = Student("Soeun", "Panhalita","Female", 12, "Bussiness Management", "Master Degree")
# student3.show_info()
# student3.display_subject()

# print(f"The number of students created is : {Student.num_of_students}")

print("*" * 10, "Inheritance Employee Class from Person", "*" * 10)

class Employee(Person):
  def __init__(self, f_name, l_name, sex, age, position, department, salary):
    super().__init__(f_name, l_name, sex, age)
    self.position = position
    self.department = department
    self.salary = salary
  
    
employee1 = Employee("Sourn", "Sophois","M", 45, "IT", "Casino", 1000)
employee2 = Employee("Wong", "Hong Kong", "M", 50, "Casino Manager", "Casino", 50000)
employee3 = Employee("Liew", "Ah Pheng", "M", 48, "Casino Shift Manager", "Casino", 3000)
employee4 = Employee("San", "Hong Seng", "M", 44, "PIT Manager", "Casino", 1000)
employee5 = Employee("Chenda", "Sophea", "F", 48, "PIT Manager", "Casino", 1300)



employees = [employee1, employee2, employee3,employee5,employee4]
data = [ [e.f_name, e.l_name, e.sex, e.age, e.position, e.department, e.salary] for e in employees]

row_index_with_data = [[index] + row for index, row in enumerate(data, start = 1)]
headers = ["No","First Name", "Last Name", "Sex", "Age", "Position", "Department", "Salary"]

print(tabulate(row_index_with_data, headers= headers, tablefmt="grid"))
# print(row_index_with_data)
