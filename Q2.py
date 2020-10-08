# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323

def calc_weight_on_planet(earth_weight, gravity = 23.1):
    mass = earth_weight / 9.8
    return mass * gravity

print(calc_weight_on_planet(120))
