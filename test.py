import sketchingpy


sketch = sketchingpy.Sketch2D(500, 500)
sketch.set_stroke('#33333350')

def draw(sketch):
  mouse = sketch.get_mouse()
  x = mouse.get_pointer_x()
  y = mouse.get_pointer_y()
  sketch.draw_line(x, y, 250, 250)

sketch.on_step(draw)

sketch.clear('#FFFFFF')
sketch.show()
