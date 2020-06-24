# -*- coding: utf-8 -*-
a = [1, 2, 3, 4, 5, 6, 7]
print(a[5])
print(a[3])

a[5] = a[3]

print(a[5])
print(a[3])

# Al principio a[5] valia 6, sin embargo al igualarlo con a[3] ha cambiado el valor a 4.


print("\n")

b = [1, 2, 3, 4, 5, 6, 7]
print(b[5])
print(b[3])

b[3] =b[5]
print(b[5])
print(b[3])

# En este caso b[3] se iguala a b[5], copiandose asi el resultado de b[5] en b[3], que es 6.
 
