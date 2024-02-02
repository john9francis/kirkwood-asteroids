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
    print("Hello Planet World!")


  def add_force_vector(self, other_pos, other_mass) -> None:
    '''
    Takes in another planet's position and mass,
    and calculates the force on this planet based on that.
    It adds this force vector to the total force
    '''
    pass


  def gravitational_force(self, m_other, r_magnitude):
    '''
    Calculates the gravitational force scalar 
    based on the equation:
    F = G*m1*m2/r**2, 
    returns F.
    '''
    return self.G * self.mass * m_other / (r_magnitude**2)

  pass