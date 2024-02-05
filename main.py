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
  jupiter.set_name("Jupiter")

  # initialize our 2/1 gap asteriods
  asteriod1 = Planet()
  asteriod1.set_mass(1e10)
  asteriod1.add_to_position_list(np.array([3.0, 0]))
  asteriod1.add_to_velocity_list(np.array([0, 3.628]))
  asteriod1.set_name("Asteriod 1")



  # put all our planets in a list to update later
  planet_list = [jupiter, asteriod1]


  # Initial conditions
  t = 0
  dt = 0.02
  simulation_time = 2
  
  planet_pos_mass_list = []

  # FUNCTIONS

  def reset_planet_pos_mass_list():
    planet_pos_mass_list.clear()
    planet_pos_mass_list.append([sun_pos, sun_mass])
    for p in planet_list:
      planet_pos_mass_list.append(p.get_pos_mass_list())

  
  def first_half_leapfrog(planet: Planet):
    # reset the planet to get the new force in there
    planet.update_force_from_planets(planet_pos_mass_list)

    # acceleration is the total force
    a = planet.get_total_force()

    v_half = planet.get_previous_velocity() + a * .5 * dt
    new_r = planet.get_previous_position() + v_half * dt

    # store v_half
    planet.store_v_half(v_half)

    # add to pos list
    planet.add_to_position_list(new_r)
    pass


  def second_half_leapfrog(planet: Planet):
    # reset the planet to get the new force in there
    planet.update_force_from_planets(planet_pos_mass_list)

    # acceleration is the total force
    a = planet.get_total_force()

    new_v = planet.get_v_half() + a * .5 * dt

    # add variables to the lists
    planet.add_to_velocity_list(new_v)
    pass

  # start leap frogging
  while t < simulation_time:

    for p in planet_list:
      print(f"{p.get_name()}, position: {p.get_previous_position()}")

      first_half_leapfrog(p)
      reset_planet_pos_mass_list()
      second_half_leapfrog(p)
      reset_planet_pos_mass_list()



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
