import numpy as np
from planet import Planet
from matplotlib import pyplot as plt

def main():

  # variables for the sun
  sun_mass = 2e30
  sun_pos = np.array([0, 0])

  # initialize jupiter
  jupiter = Planet()
  jupiter.set_mass(1.9e27)
  jupiter.add_to_position_list(np.array([5.2, 0]))
  jupiter.add_to_velocity_list(np.array([0, 2.755]))

  # initialize our 2/1 gap asteriods
  asteriod1 = Planet()
  asteriod1.set_mass(1e10)
  asteriod1.add_to_position_list(np.array([3.0, 0]))
  asteriod1.add_to_velocity_list(np.array([0, 3.628]))



  # put all our planets in a list to update later
  planet_list = [jupiter]


  # Initial conditions
  t = 0
  dt = 0.02
  simulation_time = 15
  
  planet_pos_mass_list = []

  def reset_planet_pos_mass_list():
    planet_pos_mass_list.clear()
    planet_pos_mass_list.append([sun_pos, sun_mass])
    for p in planet_list:
      planet_pos_mass_list.append(p.get_pos_mass_list())

  # start leap frogging
  while t < simulation_time:

    reset_planet_pos_mass_list()

    # ===================================================
    # FIRST HALF
    # ===================================================
    for p in planet_list:
      # reset the planet to get the new force in there
      p.update_force_from_planets(planet_pos_mass_list)

      # acceleration is the total force
      a = p.get_total_force()

      v_half = p.get_previous_velocity() + a * .5 * dt
      new_r = p.get_previous_position() + v_half * dt

      # store v_half
      p.store_v_half(v_half)

      # add to pos list
      p.add_to_position_list(new_r)



    # reset pos mass list
    reset_planet_pos_mass_list()
    
    # ===================================================
    # SECOND HALF
    # ===================================================

    for p in planet_list:
      # reset the planet to get the new force in there
      p.update_force_from_planets(planet_pos_mass_list)

      # acceleration is the total force
      a = p.get_total_force()

      new_v = p.get_v_half() + a * .5 * dt

      # add variables to the lists
      p.add_to_velocity_list(new_v)


    # add to time
    t += dt

  # now plot
  for p in planet_list:
    planet_positions = p.get_position_list()
    for i in range(len(planet_positions)):
      plt.plot(planet_positions[i][0], planet_positions[i][1], '.')

  plt.show()

if __name__ == "__main__":
  main()
