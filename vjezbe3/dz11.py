import particle as par

p=par.Particle()
p.set_initial_conditions(8, 60, 2, 11, 0.01)
print (p.total_time())
p.reset()

p.set_initial_conditions(8, 60, 2, 11, 0.01)
print (p.max_speed())
p.reset()

print (p.velocity_to_hit_target(45, 2, 7, 5, 0.01))
p.reset

print (p.angle_to_hit_target(9.7, 2, 7, 5, 0.01))
p.reset