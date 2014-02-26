#! /usr/bin/python
#!encoding: UTF-8

from math import sqrt

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))

if a == 0 and b == 0 and c == 0:
   print 'La ecuación tiene infinitas soluciones.'
elif a == 0 and b == 0:
   print 'La ecuación no tiene solución.'
elif a == 0:
   x = -c/b
   print 'La solución de la ecuación es: x%4.3f.' %x
elif (b**2 < 4*a*c):
   print 'Las soluciones de la ecuación son números complejos.'
else:
   x1 = (-b + sqrt(b**2 -4*a*c)) / (2 * a)
   x2 = (-b - sqrt(b**2 -4*a*c)) / (2 * a)
   print 'Las soluciones de la ecuación son: x1=%4.3f y x2=%4.3f.' %(x1, x2)
