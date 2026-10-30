teclado = {
  2: "abc",
  3: "def",
  4: "ghi",
  5: "jkl",
  6: "mno",
  7: "pqrs",
  8: "tuv",
  9: "wxyz",
}
 #2,3
digitos="234"
nums=[int(x) for x in digitos]
result = []
for i in range(len(nums)-1):
    valor = teclado[(nums[i])]
    for j in range(len(valor)): #A, B,  C
        valorb = teclado[nums[i + 1]]#d,e,f
        for k in range(len(valorb)):
                result.append(f"{valor[j]}{valorb[k]}")

print(result)
