import pymunk

# crear space
space = pymunk.Space()

space.gravity = (0, -981)

# crear un cuerpo rigido o body
body = pymunk.Body()
body.position = (50,100)

poly = pymunk.Poly.create_box(body)
poly.mass = 10

space.add(body,poly)

print_options = pymunk.SpaceDebugDrawOptions()

for _ in range(100):
  space.step()