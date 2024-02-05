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
  t = 0
  jupiter.add_to_position_list(r_initial)
  jupiter.add_to_velocity_list(v_initial)


  # start leap frogging
  while t < 15:

    # ===================================================
    # FIRST HALF
    # ===================================================
    # reset the planet to get the new force in there
    jupiter.update_force_from_planets([[sun_pos, sun_mass]])

    # acceleration is the total force
    a = jupiter.get_total_force()

    v_half = jupiter.get_previous_velocity() + a * .5 * dt
    new_r = jupiter.get_previous_position() + v_half * dt

    # store v_half
    jupiter.store_v_half(v_half)

    # add to pos list
    jupiter.add_to_position_list(new_r)


    # ===================================================
    # SECOND HALF
    # ===================================================

    # reset the planet to get the new force in there
    jupiter.update_force_from_planets([[sun_pos, sun_mass]])

    # acceleration is the total force
    a = jupiter.get_total_force()

    new_v = jupiter.get_v_half() + a * .5 * dt

    # add variables to the lists
    jupiter.add_to_velocity_list(new_v)


    # add to time
    t += dt

  # now plot
  jupiter_positions = jupiter.get_position_list()
  for i in range(len(jupiter_positions)):
    plt.plot(jupiter_positions[i][0], jupiter_positions[i][1], '.')

  plt.show()

if __name__ == "__main__":
  main()
