from pygame import Vector2

class Planet:
  '''extends stationary planet but adds movement'''

  # Constants
  G = 6.6743 * 10**(-11) # m^3 kg^-1 s^-2

  # member variables
  mass = 1
  pos = Vector2(0,0)

  # changeable variables
  total_force = Vector2(0,0)

  def __init__(self) -> None:
    pass


  def add_external_force(self, other_pos:Vector2, other_mass:float) -> None:
    '''
    Takes in another planet's position and mass,
    and calculates the force on this planet based on that.
    It adds this force vector to this planets total force
    '''

    # first, get the force as a scalar
    r = self.find_r(other_pos)
    r_mag = r.length()
    force = self.gravitational_force(other_mass, r_mag)

    # second, add the force to the total force variable
    direction = r.normalize()
    self.total_force += direction * force
    pass



  def reset_external_forces(self):
    self.total_force = Vector2(0,0)


  def gravitational_force(self, m_other:float, r_magnitude:float)->float:
    '''
    Calculates the gravitational force scalar 
    based on the equation:
    F = G*m1*m2/r**2, 
    returns F/m so can be used as acceleration.
    '''
    return self.G * m_other / (r_magnitude**2)
  
  
  def find_r(self, pos_other:Vector2) -> Vector2:
    '''
    Takes in a pos vector of the other object
    and returns a vector FROM this object TO the other
    '''
    return pos_other - self.pos

  pass