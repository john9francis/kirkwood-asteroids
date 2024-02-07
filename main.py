import numpy as np
from planet import Planet
from matplotlib import pyplot as plt

def main():

  # variables for the sun
  sun_mass = 2e30
  sun_pos = np.array([0, 0])

  jupiter_mass = 1.9e27
  jupiter_pos = np.array([0, 5.2])

  # initialize jupiter
  jupiter = Planet()
  jupiter.set_mass(1.9e27)
  jupiter.add_to_position_list(np.array([5.2, 0]))
  jupiter.add_to_velocity_list(np.array([0, 2.755]))
  jupiter.set_name("Jupiter")

  # initialize our 2/1 gap asteriod
  asteriod1 = Planet()
  asteriod1.set_mass(1e10)
  asteriod1.add_to_position_list(np.array([3.0, 0]))
  asteriod1.add_to_velocity_list(np.array([0, 3.628]))
  asteriod1.set_name("Asteriod 1")



  # put all our planets in a list to update later
  planet_list = [asteriod1]


  # Initial conditions
  t = 0
  dt = 0.02
  simulation_time = 5
  
  # this list holds the all the planets'
  # positions and masses, which we will use
  # to update each planet's force later. 
  planet_pos_mass_list = [
    [sun_pos, sun_mass],
    [jupiter_pos, jupiter_mass]
  ]

  # FUNCTIONS

  def reset_planet_pos_mass_list():
    '''
    Updates the planet pos mass list with all the new
    positions and masses of planets. 
    '''
    planet_pos_mass_list.clear()
    planet_pos_mass_list.append([sun_pos, sun_mass])
    for p in planet_list:
      planet_pos_mass_list.append(p.get_pos_mass_list())

  
  def first_half_leapfrog(planet: Planet):
    '''
    Completes the first half of the leapfrog method with a certain
    planet. this is the part where r get's updated using v half. 
    '''
    # reset the planet to get the new force in there
    planet.update_force_from_planets(planet_pos_mass_list)

    # acceleration is the total force
    a = planet.get_total_force()

    # leapfrog method
    v_half = planet.get_previous_velocity() + a * .5 * dt
    new_r = planet.get_previous_position() + v_half * dt

    # store v_half
    planet.store_v_half(v_half)

    # add to pos list
    planet.add_to_position_list(new_r)
    pass


  def second_half_leapfrog(planet: Planet):
    '''
    performs the second half of the leapfrog method, 
    namely using v half to update the v.
    '''
    # reset the planet to get the new force in there
    planet.update_force_from_planets(planet_pos_mass_list)

    # acceleration is the total force
    a = planet.get_total_force()

    new_v = planet.get_v_half() + a * .5 * dt

    # add variables to the lists
    planet.add_to_velocity_list(new_v)
    pass

  # loop until we reach the desired time
  while t < simulation_time:

    # loop through all the planets and leapfrog with them
    for p in planet_list:
      # debug print
      #print(f"{p.get_name()}, position: {p.get_previous_position()}")

      # perform leap frog method with this planet
      first_half_leapfrog(p)
      second_half_leapfrog(p)



    # add to time
    t += dt

  # now plot
  # for each planet we plot their position x's v.s their position y's. 
  for p in planet_list:
    planet_positions = p.get_position_list()
    for i in range(len(planet_positions)):
      plt.plot(planet_positions[i][0], planet_positions[i][1], '.')

  plt.show()




if __name__ == "__main__":
  main()
