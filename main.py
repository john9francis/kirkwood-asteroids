from pygame import Vector2
from planet import Planet
from matplotlib import pyplot as plt

def main():

  sun_mass = 100
  sun_pos = Vector2(0,1.5)

  p = Planet()
  p.add_external_force(sun_pos, sun_mass)
  print(p.total_force)


  # start off our loop with our lists
  dt = .1
  r_initial = Vector2(-100, 0)
  v_initial = Vector2(0, 10)
  t = [0]
  r = [r_initial]
  v = [v_initial]

  # start with a little euler's method to fill up the next part of the list
  v.append(v[-1] + p.get_total_force() * .5 * dt)
  r.append(r[-1] + r[-1] * .5 * dt)
  t.append(t[-1] + .5 * dt)

  # now we have 2 data points, we start leap frogging
  while t[-1] < 10:

    # reset the planet to get the new force in there
    p.set_pos(r[-1])
    p.reset_external_forces()
    p.add_external_force(sun_pos, sun_mass)

    # acceleration is the total force
    a = p.get_total_force()
    
    # leapfrog to find new v
    new_v = v[-2] + a * v[-1] * dt

    # leapfrog to find new r
    new_r = r[-2] + dt * new_v * r[-1]

    # add variables to the lists
    t.append(t[-1] + .5 * dt)
    v.append(new_v)
    r.append(new_r)
    pass
  


  # now plot
  for i in range(len(r)):
    plt.plot(r[i].x, r[i].y, '.')

  plt.show()





if __name__ == "__main__":
  main()