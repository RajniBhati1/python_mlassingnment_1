def read_file(filename):
  with open(filename, "r") as f:
    return f.read()


def main():
#function to print the content of a text file to the console.
  filename = input("Enter the name of the text file to read: ")
  content = read_file(filename)
  print(content)


if __name__ == "__main__":
  main()