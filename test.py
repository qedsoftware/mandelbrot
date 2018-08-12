from mandelbrot import Mandelbrot, MandelbrotScalar, MandelbrotVector
import time

x_min = -1.75
x_max = 0.75
x_len = 200
y_min = -1.25
y_max = 1.25
y_len = 200
num_iters = 100

m_s = MandelbrotScalar(x_min, x_max, x_len, y_min, y_max, y_len, num_iters)
m_v = MandelbrotVector(x_min, x_max, x_len, y_min, y_max, y_len, num_iters)

def render_and_time(m: Mandelbrot):
    start = time.time()
    m.generate()
    end = time.time()
    elapsed = end - start
    print (f"{m.__class__.__name__}: {elapsed}")

for m in [m_v]:
    render_and_time(m)
