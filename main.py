import numpy as np
from planet import Planet
from matplotlib import pyplot as plt

def main():

  # variables for the sun
  sun_mass = 2e30
  sun_pos = np.array([0, 0])

  # initialize planet object
  p = Planet()

  # Initial conditions
  dt = 0.1
  r_initial = np.array([-10000000000, 0])
  v_initial = np.array([0, 10000000000])
  t = [0]
  r = [r_initial]
  v = [v_initial]

  # set the planet's force values
  p.set_pos(r[-1])
  p.reset_external_forces()
  p.add_external_force(sun_pos, sun_mass)

  # start with a little euler's method to fill the h + .5 value
  v.append(v[-1] + p.get_total_force() * .5 * dt)
  r.append(r[-1] + r[-1] * 0.5 * dt)
  t.append(t[-1] + 0.5 * dt)

  # now we have 2 data points, we start leap frogging
  while t[-1] < 100:

    # reset the planet to get the new force in there
    p.set_pos(r[-1])
    p.reset_external_forces()
    p.add_external_force(sun_pos, sun_mass)

    # acceleration is the total force
    a = p.get_total_force()

    # leapfrog to find new v
    new_v = v[-2] + a * v[-1] * dt

    # leapfrog to find new r
    new_r = r[-2] + dt * new_v * r[-1]

    # add variables to the lists
    t.append(t[-1] + 0.5 * dt)
    v.append(new_v)
    r.append(new_r)

  # now plot
  for i in range(len(r)):
    plt.plot(r[i][0], r[i][1], '.')

  plt.show()

if __name__ == "__main__":
  main()
