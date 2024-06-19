str= input("enter the string: ")
def countcharacters(string):
 characters = {}
 for character in string:
  if character not in characters:
    characters[character] = 0
  characters[character] += 1
 return characters

charactercounts = countcharacters(str)
print(charactercounts)