# function to clean an string, only let letters and blanck spaces
def cleanText(s: str) -> str:
  clean: str = ""
  for char in s:
    if "a" <= char <= "z" or "A" <= char <= "Z" or char in "Ññ":
      clean += char
  return clean

# function to build the frequencies table
def buildKey(text: str, frequencies: dict) -> dict:
  cipher_letters = list(getLetterCount(text).keys())

  # spanish letters ordered from most to least frequent
  spanish_letters = [
    letter.upper() for letter, _ in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
  ]

  # matches position by position: 1st most frequent with 1st most frequent
  key: dict = {}
  for i in range(len(cipher_letters)):
    if i < len(spanish_letters):
      key[cipher_letters[i]] = spanish_letters[i]

  return key

# function to get all the letter, and count of each letter in a string, ignore symbols, only letters
def getLetterCount(s: str) -> dict:
  # clean the text, but first make it all to uppercase
  s: str = cleanText(s.upper())
  letters_dict: dict = {}
  # walt through all the string
  for letter in s:
    if letter in letters_dict:
      letters_dict[letter] += 1
    else:
      letters_dict[letter] = 1
  # return the dictionary sorted in descendent order
  return dict(sorted(letters_dict.items(), key=lambda item: item[1], reverse=True))

# walk through all the string in upper case, if it is letter it translates to the frequency, if it is not letter, it ignores it
def decrypt(text: str, key: dict) -> str:
  return "".join(key.get(c, "_") if c.isalpha() else c for c in text.upper())

def main():
  text = """
    VSÑKVJU KT HKOJU ÑK SHCJDWUS TK EYVK UJ GJWFNJ VWTTSFJE UJ USTKCJE K TK QJCESFK ZYJ QYJUK UJVSENCKC ZYJ EY ÑWIS USUW O TK QCWFDJEK UWKFK VYCWJCSF DSVS CJEYTNKUS UJ YFK DSFEQWCKDWUF NJCCSCWENK. 
    JT VWTTSFKCWS JMWQDWS ÑWLS TK SHJCNK UJEQYJE UJ ZYJ JT JX KMJFNJ UJT EJCGWDWS EJDCJNS WFMTJE, CWDÑKCU NÑSVTWFESF, TJ UWIJCK K YF IYJL JF QKCWE ZYJ ÑJFCO QKYT, JT DÑSHJC PSCCKDÑS VYJCNS JF JT KDDWUJFNJ, JCK YF KMJFNJ EJDCJNS PCWNKFWDS. JT MSPWJCFS WFMTJE ÑK UJDTKCKUS ZYJ JEK ÑWENSCWK JCK "QYCJ HKFNKEWK"
  """

  frequencies = {
    "e": 13.68, "a": 12.53, "o": 8.68, "s": 7.98, "r": 6.87, "n": 6.71,
    "i": 6.25, "d": 5.86, "l": 4.97, "c": 4.68, "t": 4.63, "u": 3.93,
    "m": 3.15, "p": 2.51, "b": 1.42, "g": 1.01, "v": 0.90, "y": 0.90,
    "q": 0.88, "h": 0.70, "f": 0.69, "z": 0.52, "j": 0.44, "ñ": 0.31,
    "x": 0.22, "k": 0.02, "w": 0.01,
  }

  key = buildKey(text, frequencies)

  print(decrypt(text, key).strip())

if __name__ == "__main__":
  main()
