import matplotlib.pyplot as plt

# Data untuk sumbu X dan Y
x = [1.0, 5.5, 2.0, 3.0, 4.0]
y = [3.0, 6.0, 3.0, 1.0, 4.0]
combined = sorted(zip(x, y))
# x_sorted = [point[0] for point in combined]
# y_sorted = [point[1] for point in combined]
# Membuat plot garis dengan titik (marker)
plt.plot(*zip(*combined), marker='o', color='red')

# Menambahkan judul dan label pada sumbu
plt.title("Grafik Visualisasi Sederhana")
plt.xlabel("nilai")
plt.ylabel("frekuensi")
fig = plt.gcf()
# Pindahkan jendela ke koordinat X=800, Y=100 (area kanan layar)
fig.canvas.manager.window.wm_geometry("+980+100")
plt.show()