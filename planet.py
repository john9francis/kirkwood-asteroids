from stationary_planet import StationaryPlanet

class Planet(StationaryPlanet):
  '''extends stationary planet but adds movement'''

  def __init__(self) -> None:
    super().__init__()
    print("From a moveable planet!")
  pass