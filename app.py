number = 14
 
values = [1000, 900, 500, 400, 100,90, 50, 40, 10, 9, 5, 4, 1]
numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
result = ""
 
for i in range(0,len(values)):
    while(number >= values[i]):
        number = number - values[i]
        result = result + numerals[i]

print(result)

