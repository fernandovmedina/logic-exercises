import re

# Limpia el texto: deja solo letras (incluida Ñ) y espacios
def cleanText(s: str) -> str:
  return re.sub(r"[^A-Za-zÑñ ]", "", s)

# Cuenta cada letra (ignora espacios y símbolos), ordenado de mayor a menor
def getLetterCount(s: str) -> dict:
  letters_dict: dict = {}
  for letter in s.upper():
    if not letter.isalpha():
      continue
    letters_dict[letter] = letters_dict.get(letter, 0) + 1
  return dict(sorted(letters_dict.items(), key=lambda item: item[1], reverse=True))

# Aplica una tabla de sustitución; las letras sin traducir quedan como '_'
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

  key = {
    "J": "E", "K": "A", "S": "O", "W": "I", "C": "R", "E": "S", "F": "N",
    "U": "D", "T": "L", "N": "T", "Y": "U", "D": "C", "V": "M", "Q": "P",
    "Ñ": "H", "Z": "Q", "M": "G", "H": "F", "I": "J", "O": "Y", "P": "B",
    "G": "V", "L": "Z", "X": "X",
  }
  print(decrypt(text, key).strip())

if __name__ == "__main__":
  main()