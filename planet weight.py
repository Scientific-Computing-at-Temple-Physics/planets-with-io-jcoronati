import math as ma

data = open("planet_data.txt", 'r')
obj = str(input("Enter the name of a planet: "))
mass = int(input("Enter your mass value in kilograms: "))
alt = int(input("Enter your elevation on the planet m: "))
name_list = []
radi_list = []
dens_list = []
G = 0.0000000000667408

for line in data:
    if line[0] == 'ï': #the char '#' was not showing up first in my shell
        continue
    var = line.split(';')
    name_list.append(var[0])
    radi_list.append(var[1])
    dens_list.append(var[2])
for i in name_list:
    i = 0
    while obj != name_list[i]:
        if i <= 13:
            i = i+1
        else:
            break
for j in radi_list:
    j = 0
    while i != j:
        if j <= 13:
            j = j+1
        else:
            break
    x = radi_list[j]
    x = float(x.strip().strip('km'))
    x = (x*1000)+alt
for k in dens_list:
    k = 0
    while j != k:
        if k <= 13:
            k = k+1
        else:
            break
    y = dens_list[k]
    y = float(y.strip().strip('g/cm^3'))
    y = y*1000

obj_mass = y*(4*ma.pi*(x**3)/3)
obj_grav = (G*obj_mass)/(x**2)
weight = float(mass*obj_grav)
lbs = weight*0.22481
gravg = float(obj_grav/9.80665)

print ("Your weight on ", name_list[i], "is ", lbs, "pounds.")
print ("The gravitational force in units of g is ", gravg)
