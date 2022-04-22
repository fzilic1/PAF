import ProjectileDrop as pd

p1=pd.ProjectileDrop()
p2=pd.ProjectileDrop()

p1.set_init(20, 40)
p2.set_init(70, 70)

p1.new_h(133)
p2.new_vx(20)

print (p1.y[0], p2.vx[0])