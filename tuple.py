scores = (56.4,67.6,39.0,47.3, 70.8, 85.8,90, 95.4,45.9,52.8,48.5)
students= tuple(("Sok","Dara","Vanna","Bopha","Kim", "Dara"))

print("==============Collection Data Type with Tuple in Python=============")
# print(type(scores))
# print(len(students))
for name in students:
  print(name)

print("========Student Scores=========")
print(scores[0])
print(scores[-1])
i=0
while i < len(scores):
  print((i+1), scores[i])
  i +=1
print("==============Number of students passing the exame:=========")
i =0
while i<len(scores):
  if scores[i] >= 50:
    print((i+1), scores[i])
  else:
    print(scores[i])
  i +=1
print("==============Number of students failing the exam:==========")
n=0
for s in scores:
  if s < 50:
    print((n+1),s)
    n +=1

colors = ("Red","Blue")
list_colors = list(colors)
list_colors[1] = "Pink"
list_colors[0]="Purple"
list_colors.append("Orange")
list_colors.append("Blue")
list_colors.insert(1,"White")
colors = tuple(list_colors)
print(colors)