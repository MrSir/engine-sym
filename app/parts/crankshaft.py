import utils


class Crankshaft:
    def __init__(self, trow: float):
        self.trow: float = trow
        self.counter_weight = None

    def rev_calc_force(self, torque: float):
        """
        Force = Torque / Lever Arm Length
        N = Nm / m
        """
        torque_nm = utils.ftlbs_to_nm(torque)

        return torque_nm / self.trow

