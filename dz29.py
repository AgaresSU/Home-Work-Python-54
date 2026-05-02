class Liquid:
    def __init__(self, name, density):
        self._name = name
        self._density = density

    def change_density(self, new_density):
        self._density = new_density

    def volume_from_mass(self, mass):
        return mass / self._density

    def mass_from_volume(self, volume):
        return self._density * volume

    def print_info(self):
        print(f"Жидкость '{self._name}' (плотность = {self._density} kg/m^3).")


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self._strength = strength

    def change_strength(self, new_strength):
        self._strength = new_strength

    def get_strength(self):
        return self._strength

wine = Alcohol("Wine", 1064.2, 14)

wine.print_info()

wine.change_density(1000)

wine.print_info()

mass = wine.mass_from_volume(0.5)
print(f"Вес 0.5 m^3 of Wine составляет {mass} kg.")

volume = wine.volume_from_mass(300)
print(f"Объем 300 kg Wine равен {volume} m^3.")

print(wine.get_strength())
wine.change_strength(20)
print(wine.get_strength())