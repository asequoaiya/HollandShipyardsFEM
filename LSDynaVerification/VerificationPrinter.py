# ----- Import Functions -----
from ResultIntegration import verification_difference

# ----- Function calling -----
verification_difference(r"PlateImpactValidation\V4",
                        0.01, 300_000_000, 2, 0.5, 0.05,
                        energy=True, force=True)
verification_difference(r"PlateImpactValidation\V4.1",
                        0.01, 300_000_000, 2, 0.5, 0.05,
                        energy=True, force=True)
verification_difference(r"PlateImpactValidation\MAT123",
                        0.01, 300_000_000, 2, 0.5, 0.05,
                        energy=True, force=True)