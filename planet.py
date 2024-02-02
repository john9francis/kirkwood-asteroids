class Planet:
  '''extends stationary planet but adds movement'''

  def __init__(self) -> None:
    print("Hello Planet World!")


  def add_force_vector(self, other_pos, other_mass) -> None:
    '''
    Takes in another planet's position and mass,
    and calculates the force on this planet based on that.
    It adds this force vector to the total force
    '''
    pass


  def gravitational_force(self, m_other, r_other):
    '''
    Calculates the gravitational force based on the equation
    F = G*m1*m2/r**2, returns F.
    '''
  pass