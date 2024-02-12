# ----- Import functions -----
from DeflectionCalc import plate_deflection_energy
from PlateStripMethod import plate_strip_energy
from DeckCrushingMethod import deck_plate_crushing_energy
from PlateCuttingMethod import plate_cutting_energy


# ----- Output calling -----
print(plate_deflection_energy(1.5, 1.5, 0.358, 0.472, 300_000_000,
                              0.025, 0.6, 90, 0.075))

print(plate_strip_energy(0.01, 300_000_000, 1, 0.1896,
                         0.6, 0.4, 0.4))

print(deck_plate_crushing_energy(0.025, 300_000_000, 1, 0.1896,
                                 0.8, 0.3, 0.3))

print(plate_cutting_energy(300_000_000, 0.1, 0.6, 0.01, 0.485, 45))
