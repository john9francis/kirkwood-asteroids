import numpy as np

class Planet:
  '''Moveable planet object'''

  # Constants
  G = 6.6743 * 10**(-11)  # m^3 kg^-1 s^-2

  # member variables
  mass = 2.4e23
  position_list = []
  velocity_list = []

  # changeable variables
  total_force = np.array([0, 0])
  v_half = 0.0


  def __init__(self) -> None:
    pass

  def add_to_position_list(self, new_pos):
    self.position_list.append(new_pos)

  def add_to_velocity_list(self, new_vel):
    self.velocity_list.append(new_vel)

  def get_position_list(self):
    return self.position_list
  
  def get_velocity_list(self):
    return self.velocity_list
  
  def get_previous_position(self):
    return self.position_list[-1]
  
  def get_previous_velocity(self):
    return self.velocity_list[-1]

  def set_mass(self, new_mass):
    self.mass = new_mass

  def get_total_force(self):
    return self.total_force
  
  def get_pos_mass_list(self):
    return [self.position_list[-1], self.mass]
  

  def update_force_from_planets(self, planet_pos_mass_list):
    '''
    note: planet_pos_mass_list is a list of lists of the form:
    [planet_position, planet_mass].
    '''
    self.reset_external_forces()
    for sub_list in planet_pos_mass_list:
      pos = sub_list[0]
      mass = sub_list[1]
      self.add_external_force(pos, mass)

    pass


  def store_v_half(self, v_half):
    self.v_half = v_half

  def get_v_half(self):
    return self.v_half


  def add_external_force(self, other_pos: np.ndarray, other_mass: float) -> None:
    '''
    Takes in another planet's position and mass,
    and calculates the force on this planet based on that.
    It adds this force vector to this planets total force
    '''

    # first, get the force as a scalar
    r = self.find_r(other_pos)
    r_mag = np.linalg.norm(r)
    #force = self.gravitational_force(other_mass, r_mag)
    force = self.AU_force(r_mag)

    # second, add the force to the total force variable
    direction = r / r_mag
    new_force = direction * force

    # have to reset total force this way because
    # np can't do the += thing for some reason
    new_total_force = new_force + self.total_force
    self.total_force = new_total_force


  def reset_external_forces(self):
    self.total_force = np.array([0, 0])



  def gravitational_force(self, m_other: float, r_magnitude: float) -> float:
    '''
    Calculates the gravitational force scalar 
    based on the equation:
    F = G*m1*m2/r**2, 
    returns F/m so can be used as acceleration.
    '''
    return self.G * m_other / (r_magnitude**2)


  def AU_force(self, r_magnitude):
    return 4 * np.pi**2 /(r_magnitude**2)


  def find_r(self, pos_other: np.ndarray) -> np.ndarray:
    '''
    Takes in a pos vector of the other object
    and returns a vector FROM this object TO the other
    '''
    return pos_other - self.position_list[-1]

