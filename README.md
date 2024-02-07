# Overview

Giordano problem 4.17: Simulate the motion of asteroids near the one of the Kirkwood gaps. The 2/1 and 7/3 gaps are good choices. 

# Methods

Leapfrog method (to conserve energy)

# Process
- [ ] Model a simple orbit using leapfrog method
- [ ] Add a trajectory calculator class for leapfrog method, set it up like the pendulum class. 
- [ ] Move things to np arrays instead of pygame vector2s...


# NOTE:
There are issues with my code. I assumed that the velocity of jupiter at it's max distance was 5.2 AU. This is not the case as jupiter does not have a perfectly circular orbit and also the orbit is closer to the sun at some points and further at other points. So to fix my issue, I need to calculate the radius and velocity at max distance from the sun, and use those as my initial conditions. For the max distance, the $r$ and $v$ are as follows. 

$$r = a(e+1)$$
$$v = \sqrt{\frac{4\pi^2(1-e)}{a(e+1)}}$$