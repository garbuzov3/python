class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, mass_per_sq_m, thickness_cm):
        area_sq_m = self._length * self._width
        thickness_m = thickness_cm / 100
        asphalt_mass_tons = area_sq_m * mass_per_sq_m * thickness_m / 1000
        return asphalt_mass_tons


road = Road(20, 5000)
asphalt_mass_tons = road.asphalt_mass(25, 5)
print(f"Масса асфальта, необходимого для покрытия всей дороги: {asphalt_mass_tons} т.")
