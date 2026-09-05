def calculate_enery(mass):
    """

    Einstein's mass-energy equivalence formula : E = mc²
    mass : mass in kilograms
    returns : energy in joules
    """ 
    c = 299792458
    energy = mass * (c ** 2)
    return energy

mass = 1
E = calculate_enery(mass)

print(f"Mass : {mass} kg")

print (f"Speed of light : {299792458} m/s")

print(f"Energy (E): {E:,} joules")

print(f"Energy (E): {E/1e15:.2f} petajoules")

