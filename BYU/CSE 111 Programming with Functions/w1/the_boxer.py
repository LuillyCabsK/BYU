import math

#ingresar cantidades
date1 = int(input (f"Enter the number of items:"))
date2 = int(input (f"Enter the number of items per box:"))

#calculos
elem_box = math.ceil(date1 / date2)

#presentar resultados
print (f"For {date1} items, packing {date2} in each box, you will need {elem_box} boxes")