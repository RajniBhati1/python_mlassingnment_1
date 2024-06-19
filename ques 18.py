def is_anagram(str1, str2):
  str1 = str1.lower()
  str2 = str2.lower()
  if len(str1) != len(str2):
    return False

  char_counts = {}
  for char in str1:
    if char not in char_counts:
      char_counts[char] = 0
      char_counts[char] += 1
  for char in str2:
    if char not in char_counts or char_counts[char] == 0:
      return False
    char_counts[char] -= 1

  # If we reach till here, the strings are anagrams.
  return True
str1 = "listen"
str2 = "silent"

if is_anagram(str1, str2):
  print("The strings are anagrams.")
else:
  print("The strings are not anagrams.")