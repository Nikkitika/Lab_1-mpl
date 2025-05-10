import matplotlib.pyplot as plt


def read_points(filename):
    try:
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            points = []
            for _ in range(n):
                line = file.readline().strip()
                x, y = map(float, line.split())
                points.append((x, y))
            print(f"Успешно прочитано {len(points)} точек.")
            return points
    except Exception as e:
        print(f"Ошибка: {e}")
        return []


def plot_points(points, filename):
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    plt.figure(figsize=(10, 6))
    plt.scatter(x_coords, y_coords, s=50, color='red', edgecolors='black')
    plt.title(f"Точки из файла: {filename}\nВсего точек: {len(points)}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')

    # Сохранение и отображение
    plt.savefig(f"{filename}_plot.png")
    plt.show()


if __name__ == "__main__":
    filename = '005.dat'
    points = read_points(filename)
    if points:
        plot_points(points, filename)
    else:
        print("Нет данных для визуализации.")