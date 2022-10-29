import matplotlib.pyplot as plt
import utils
from parts.crankshaft import Crankshaft

rpm = [2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]
torques = [20, 37, 40, 45, 48, 50, 45, 40]
hps = [utils.torque_to_horsepower(torques[index], rpm) for index, rpm in enumerate(rpm)]

plt.plot(rpm, torques, color='green', label='Torque')
plt.plot(rpm, hps, color='red', label='HP')

crankshaft = Crankshaft(0.05)
force_on_crank = [crankshaft.rev_calc_force(torque) for torque in torques]
print(force_on_crank)
plt.plot(rpm, force_on_crank, color='blue', label='Force On Crank')


plt.title('Dyno Chart')
plt.xlabel('RPM')
# plt.ylim((0, 80))
plt.legend()
plt.show()

