from mandelbrot import Mandelbrot
import time

x_min = -1.75
x_max = 0.75
x_len = 200
y_min = -1.25
y_max = 1.25
y_len = 200
num_iters = 100

m = Mandelbrot(x_min, x_max, x_len, y_min, y_max, y_len, num_iters)

t0 = time.time()
m.generate_scalar()
t1 = time.time()
print(t1-t0)
