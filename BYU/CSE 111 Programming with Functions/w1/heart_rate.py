#ingresar edad
edad = input ("What your age?")
age = int(edad)

#calculos
range = 220 - age
min_rate = range *0.65
MAX_rate = range * 0.85

#print resultado
print (f"For a person of {age:.0f}")
print (f"You should need to to keeo yuor heart rate between {min_rate:.0f} and {MAX_rate:.0f}")
print("Pleases BEE carrefuly ")

