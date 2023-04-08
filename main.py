import math

num_int = int(input('Digite um número inteiro: '))

div_tres = num_int % 3
div_cinco = num_int % 5

print(div_cinco)
print(div_tres)
  
if div_tres == 0 and div_cinco == 0:
    print('FizzBuzz')

elif div_tres == 0:
    print("Fizz")

elif div_cinco == 0:
    print('Buzz')
  
else:
    print(num_int)
