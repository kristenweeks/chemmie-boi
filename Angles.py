#!/usr/bin/env python3
#https://github.com/kristenweeks/chemmie-boi
import math

a=float(input("Enter first side: "))
b=float(input("Enter second side: "))
c=float(input("Enter third side: "))

#calculate angle C using cos theorem
C = (math.acos(((a**2)+(b**2)-(c**2))/2*a*b))

#calculate angle B using C and sin theorem
B = (math.asin((b(math.sin(C)))/c))

#calculate angle A from B and C
A=180-(B+C)

Print("Angle A is", A)
Print("Angle B is", B)
Print("Angle C is", C)
