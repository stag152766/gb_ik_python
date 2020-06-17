import sys
import ctypes
import struct

a = 5
x=y=a
b = 125.54
c = 'Hello World!'

print(id(a)) # адрес памяти по которому лежим объект целого типа 5
print(sys.getsizeof(a))


print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack('LLLcc', ctypes.string_at(id(a), sys.getsizeof(a))))

print(id(int))
