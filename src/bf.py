import numpy as np
import matplotlib.pyplot as plt
import time

def calculateBezierPoint(control_points, t):
    n = len(control_points) - 1
    x = 0
    y = 0
    for i, point in enumerate(control_points):
        coeff = np.math.comb(n, i) * (1 - t)**(n - i) * t**i
        x += coeff * point[0]
        y += coeff * point[1]
    return x, y

def bruteForceBezier(control_points, num_iterations):
    curve_points = []
    for i in range(num_iterations + 1):
        t = i / num_iterations
        curve_points.append(calculateBezierPoint(control_points, t))
    return curve_points

def plotBezierCurve(control_points, curve_points):
    control_x = [point[0] for point in control_points]
    control_y = [point[1] for point in control_points]

    curve_x = [point[0] for point in curve_points]
    curve_y = [point[1] for point in curve_points]

    plt.plot(curve_x, curve_y, label="Bezier Curve", color="blue")
    plt.scatter(control_x, control_y, color="red", label="Control Points")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Bezier Curve (Brute Force)")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    p0_x, p0_y = map(float, input("Masukkan koordinat titik awal (pisahkan dengan spasi): ").split())
    p1_x, p1_y = map(float, input("Masukkan koordinat titik kontrol (pisahkan dengan spasi): ").split())
    p2_x, p2_y = map(float, input("Masukkan koordinat titik akhir (pisahkan dengan spasi): ").split())
    num_iterations = int(input("Masukkan jumlah iterasi: "))

    start_time = time.time()
    control_points = [(p0_x, p0_y), (p1_x, p1_y), (p2_x, p2_y)]  

    curve_points = bruteForceBezier(control_points, num_iterations)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Waktu eksekusi: {runtime} detik")
    plotBezierCurve(control_points, curve_points)

if __name__ == "__main__":
    main()
