#! /usr/bin/python
#!encoding: UTF-8

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

if a != 0:   
   x = -b/a
   print 'La solución es x = ', x
elif b == 0:
   print 'La ecuación tiene infinitas soluciones.'
else:
   print 'La ecuación no tiene solución.'
   
