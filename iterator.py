class Sentence:
  def __init__(self, sentence):
    self.sentence = sentence
    self.index = 0
  def __iter__(self):
    return self
  def __next__(self):
    # words = [word for word in self.sentence.split(" ")]
    words = self.sentence.split(" ")
    if self.index >= len(words):
      raise StopIteration
    else: 
      current = words[self.index]
      self.index +=1
    return current
    
        

my_sentence = Sentence('This is a man')
for word in my_sentence:
  print(word)
 