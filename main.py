from pygame import Vector2
from planet import Planet

def main():

  sun_mass = 100
  sun_pos = Vector2(0,1.5)

  p = Planet()
  p.add_external_force(sun_pos, sun_mass)
  print(p.total_force)
  pass





if __name__ == "__main__":
  main()