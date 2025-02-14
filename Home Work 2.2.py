a = int(input('Please your number')) #12345
print(type(a))
x = a%1000
five =x%10
four = x%11
three = x//100

y = a//1000
two = y%10
one = y%11

print(f"{five}{four}{three}{two}{one}")














