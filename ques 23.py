def main():
  """Main function of the program."""
  starting_unit = input("Enter starting temperature unit (C/F): ").upper()
  temperature = float(input("Enter the temperature: "))

  if starting_unit == "C":
    converted_temp = celsius_to_fahrenheit(temperature)
    unit = "Fahrenheit"
  elif starting_unit == "F":
    converted_temp = fahrenheit_to_celsius(temperature)
    unit = "Celsius"
  else:
    print("Invalid unit entered. Please enter C or F.")
    return

  print(f"{temperature:.2f} degrees {starting_unit} is equivalent to {converted_temp:.2f} degrees {unit}.")

def celsius_to_fahrenheit(temp):
  """Converts Celsius to Fahrenheit."""
  return (temp * 9/5) + 32

def fahrenheit_to_celsius(temp):
  """Converts Fahrenheit to Celsius."""
  return (temp - 32) * 5/9

if __name__ == "__main__":
  main()