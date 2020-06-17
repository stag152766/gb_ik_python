a = 42
print(bin(a)) # 2
print(oct(a)) # 8
print(hex(a)) # 16

b = 0b101010
print(b)

c = int('2cd50', base=24)
print(c)

z = int('z', base=36)
print(z)

# python сам выбирает какая кодировка необходима
print(ord('d'))
print(ord('л'))

