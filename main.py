import numpy as np
from planet import Planet
from matplotlib import pyplot as plt

def main():

  # variables for the sun
  sun_mass = 2e30
  sun_pos = np.array([0, 0])

  # initialize jupiter
  jupiter = Planet()
  mass = 1.9e27
  radius = 5.2 # AU
  tangential_velocity = 2.755
  jupiter.set_mass(mass)


  # Initial conditions
  dt = 0.02
  r_initial = np.array([radius, 0])
  v_initial = np.array([0, tangential_velocity])
  t = [0]
  r = [r_initial]
  v = [v_initial]


  # start leap frogging
  while t[-1] < 15:

    # reset the planet to get the new force in there
    jupiter.set_pos(r[-1])
    jupiter.reset_external_forces()
    jupiter.add_external_force(sun_pos, sun_mass)

    # acceleration is the total force
    a = jupiter.get_total_force()

    v_half = v[-1] + a * .5 * dt

    new_r = r[-1] + v_half * dt

    # reset the planet to get the new force in there
    jupiter.set_pos(r[-1])
    jupiter.reset_external_forces()
    jupiter.add_external_force(sun_pos, sun_mass)

    # acceleration is the total force
    a = jupiter.get_total_force()

    new_v = v_half + a * .5 * dt

    # add variables to the lists
    t.append(t[-1] + dt)
    v.append(new_v)
    r.append(new_r)

  # now plot
  for i in range(len(r)):
    plt.plot(r[i][0], r[i][1], '.')

  plt.show()

if __name__ == "__main__":
  main()
