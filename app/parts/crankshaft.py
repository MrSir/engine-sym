class Crankshaft:
    def __init__(self, trow: float):
        self.trow: float = trow
        self.counter_weight = None

    def rev_calc_force(self, newton_meter: float) -> float:
        """
        Force = Torque / Lever Arm Length
        N = Nm / m
        """

        return newton_meter / self.trow

    def force_per_rpm(self, newton_meters: float, rpm: int) -> float:
        return newton_meters / rpm


    """
    Notes:
        Force on crank needs to go up in order for the RPM to go up.
            - at some point the force on the piston is not able to accelerate the crank anymore due to
              reaching it's max velocity based on friction and inertial momentum.
    """