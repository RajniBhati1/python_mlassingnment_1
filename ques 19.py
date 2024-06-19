import string

def remove_punctuation(text):
  table = str.maketrans('', '', string.punctuation)
  return text.translate(table)

text = "This is a string with punctuation!"
print(remove_punctuation(text))