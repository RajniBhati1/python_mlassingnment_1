def copy_file(source_file, destination_file):

  with open(source_file, "r") as f:
    source_data = f.read()

  with open(destination_file, "w") as f:
    f.write(source_data)


if __name__ == "__main__":
  source_file = "source.txt"
  destination_file = "destination.txt"

  copy_file(source_file, destination_file)