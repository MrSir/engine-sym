def to_N_m(pound_feet: float) -> float:
    return pound_feet * 1.356


def to_lbs_ft(newton_meter: float) -> float:
    return newton_meter / 1.356


def to_hp(pound_feet: float, rpm: float) -> float:
    return pound_feet * rpm / 5252


def to_kW(newton_meter: float, rpm: float) -> float:
    return newton_meter * rpm * 0.105 / 1000
