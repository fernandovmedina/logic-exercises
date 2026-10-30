# program to understand all the text formats like:
# -> ascii
# -> unicode
# -> utf-8

# import the library to read flags throug i/o
import argparse
import math

# function to get the ascii number of a char
def ascii(char: str) -> str:
  return ord(char)

# function to convert decimal number to binary, using own logic, no internal/external libraries
def decimalToBinary(decimal: str) -> str:
  # variable to save the binary string
  binary: str = ""
  # convert the string to number
  n: int = int(decimal)
  # array to save the digits of the convertion
  digits: list[int] = []
  for i in range(7, -1, -1):
    if math.exp2(i) > n:
      digits.append(0)
      continue
    else:
      if math.exp2(i) == n:
        n -= math.exp2(i)
        digits.append(1)
      else:
        n -= math.exp2(i)
        digits.append(1)
  # convert the array to string
  binary = "".join(map(str, digits))
  # return the binary string
  return binary

# function to convert the text to unicode or utf-8

# get the "text" flag, so we can convert the text to all the formats
def main():
  parser = argparse.ArgumentParser()
  # declare the only flag that we are going to use while running the code
  parser.add_argument("-t", "--text", type=str, default="A", help="text to convert through all the text formats")
  # parse all the flags
  args = parser.parse_args()
  # get the value of the [-t,--text] flag
  text = args.text
  # print the text to the different formats
  print(f"TEXT: {text}\n") # €
  print(f"ASCII: {ascii(text)}\n") # 8364
  print(f"BINARY: {decimalToBinary(ascii(text))}") # 10000010101100
  print(f"UNICODE: \n") # U+20AC
  print(f"UTF-8: \n") # 11100010 10000010 10101100

if __name__ == "__main__":
  main()
