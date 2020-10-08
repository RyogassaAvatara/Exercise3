# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323

def num_atoms(amount_grams, atomic_weight = 196.97):
    avogadro_constant = 6.022 * 10 ** 23
    return (amount_grams / atomic_weight) * avogadro_constant

print(num_atoms(10))