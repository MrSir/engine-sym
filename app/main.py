import matplotlib.pyplot as plt

import engine_plots
from units import torque
from parts.crankshaft import Crankshaft

# KTM Duke 690 Data
rpm = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
torques = [20, 37, 40, 45, 48, 50, 45, 40]
hps = [torque.to_hp(torques[index], rpm) for index, rpm in enumerate(rpm)]
newton_meters = [torque.to_N_m(pound_feet) for pound_feet in torques]
kilo_watts = [torque.to_kW(newton_meters[index], rpm) for index, rpm in enumerate(rpm)]

fig, axis = plt.subplots(2, 2)

fig.set_size_inches(7, 9)

engine_plots.plot(
    axis[0, 0], 'Torque/HP', rpm, {'lbs.ft': torques, 'hp': hps}, {'xlabel': 'RPM', 'ylim': (0, 80)}
)

engine_plots.plot(
    axis[1, 0], 'Newton Meter/Kilo Watts', rpm, {'N.m': newton_meters, 'kW': kilo_watts}, {'xlabel': 'RPM', 'ylim': (0, 80)}
)

crankshaft = Crankshaft(0.05)
force_on_crank = [crankshaft.rev_calc_force(newton_meter) for newton_meter in newton_meters]


engine_plots.plot(
    axis[0, 1], 'Crank Force', rpm, {'N': force_on_crank}, {'xlabel': 'RPM'}
)

plt.show()