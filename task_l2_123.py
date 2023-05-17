variable1= 1,2,3
variable2= 1,2,3
variable3= 1,2,3
variable4= list[33,34,35]
variable5= list[33,34,35]
print (id ( variable1),id(variable2), id(variable3),id(variable4), id(variable5))
print (id ( list(variable1)),id(list(variable2)), id(list(variable3)),id(str(variable4)), id(str(variable5)))