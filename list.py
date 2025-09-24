fruits = ["apple","banana","orange","mango","guavor","mango steen","apple"]
animals= list(("dog","cat","cow","deer","buffelo","tiger"))

animals.insert(3,"lion")
animals.append("Python")
animals.append("crab")
animals.append("crocodile")

animals_with_cname = []
animals_with_cname = [a for a in animals if "c" in a]

print("==============Data Collection: List in Python===============")
print(fruits)
i=1
print(f"There are {len(animals)}: ")
for animal in animals:
  print(i, "- ", animal)
  i +=1

c = 0
while c < len(animals_with_cname):
  print((c+1),animals_with_cname[c])
  c +=1

