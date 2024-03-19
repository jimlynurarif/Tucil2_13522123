'''
Programmer = Jimly Nur Arif
NIM = 13519097
Objective: Divide and Conquer (DnC) for Quadratic Bezier Curve 
This is an assignment in the algorithmic strategy course

IF2211 Bandung Institute of Technology

Spesification = bit.ly/tucil2stima24
revision = bit.ly/qnastima24
group = bit.ly/kelompoktucil2stima24
'''

import matplotlib.pyplot as plt
import time

def divide_quadratic_bezier(p0, p1, p2, num_segments):
    if num_segments == 1:
        mid_point_1 = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
        mid_point_2 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        mid_point_3 = ((mid_point_1[0] + mid_point_2[0]) / 2, (mid_point_1[1] + mid_point_2[1]) / 2)
        return [p0, mid_point_3, p2]
    else:
        # midpoint yang baru
        mid_point_1 = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
        mid_point_2 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        mid_point_3 = ((mid_point_1[0] + mid_point_2[0]) / 2, (mid_point_1[1] + mid_point_2[1]) / 2)
        
        left_segments = divide_quadratic_bezier(p0, mid_point_1, mid_point_3, num_segments - 1)
        right_segments = divide_quadratic_bezier(mid_point_3, mid_point_2, p2, num_segments - 1)
        
        return left_segments + right_segments[1:]


def draw_bezier(p0, p1, p2, iterations):
    if iterations == 0:
        plt.plot(*p0, 'ro')
        plt.plot(*p1, 'ro')
        plt.plot(*p2, 'ro')
        return

    q0 = ((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    q1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

    r0 = ((q0[0] + q1[0]) / 2, (q0[1] + q1[1]) / 2)

    plt.plot(*p0, 'ro')

    plt.plot(*p1, 'ro')

    plt.plot(*p2, 'ro')

    plt.plot([p0[0], p1[0]], [p0[1], p1[1]], 'r--')
    plt.pause(0.12)
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r--')
    plt.pause(0.12)

    plt.plot(*q0, 'gs')
    plt.pause(0.12)
    plt.plot(*q1, 'gs')
    plt.pause(0.12)
    plt.plot([q0[0], q1[0]], [q0[1], q1[1]], 'g--')
    plt.pause(0.12)


    plt.plot(*r0, 'bs')
    plt.pause(0.12)
    plt.plot([p0[0], r0[0]], [p0[1], r0[1]], 'b--')
    plt.pause(0.12)
    plt.plot([r0[0], p2[0]], [r0[1], p2[1]], 'b--')
    plt.pause(0.12)

    draw_bezier(p0, q0, r0, iterations - 1)
    draw_bezier(r0, q1, p2, iterations - 1)

x0, y0 = map(int, input("Masukkan koordinat titik awal (pisahkan dengan spasi): ").split())
x1, y1 = map(int, input("Masukkan koordinat titik kontrol (pisahkan dengan spasi): ").split())
x2, y2 = map(int, input("Masukkan koordinat titik akhir (pisahkan dengan spasi): ").split())
iterations = int(input("Masukkan jumlah iterasi: "))


p0 = (x0, y0)
p1 = (x1, y1)
p2 = (x2, y2)

start_time = time.time()
curve_points = divide_quadratic_bezier(p0, p1, p2, iterations)
end_time = time.time()
runtime = end_time - start_time
print(f"Waktu eksekusi: {runtime} detik")

plt.figure(figsize=(8, 6))
for i in range(iterations + 1):
    # plt.clf()  # Clear the previous plot
    plt.title(f"Iterasi {i}")
    draw_bezier((x0, y0), (x1, y1), (x2, y2), i)
    plt.pause(0.4)  # Pause for 1 second
    if i < iterations:
        plt.draw()  # Redraw the plot


plt.show()
