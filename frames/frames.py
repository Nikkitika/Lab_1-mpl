import os
import matplotlib.pyplot as plt


def read_frames(filename):
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]

        if len(lines) % 2 != 0:
            raise ValueError("Некорректный файл: нечетное количество строк")

        return [
            (
                list(map(float, lines[i].split())),
                list(map(float, lines[i + 1].split()))
            )
            for i in range(0, len(lines), 2)
        ]
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return []


def calculate_global_limits(frames):
    all_x = [x for frame in frames for x in frame[0]]
    all_y = [y for frame in frames for y in frame[1]]
    return (
        (min(all_x) - 0.5, max(all_x) + 0.5),
        (min(all_y) - 0.5, max(all_y) + 0.5)
    )


def save_frames(frames, source_filename):
    base_name = os.path.splitext(os.path.basename(source_filename))[0]
    output_dir = f"frames_{base_name}"

    os.makedirs(output_dir, exist_ok=True)
    x_lim, y_lim = calculate_global_limits(frames)

    for i, (x, y) in enumerate(frames):
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'bo-', markersize=5, linewidth=1.5)
        plt.xlim(x_lim)
        plt.ylim(y_lim)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.title(f"Кадр {i + 1} из {len(frames)}", fontsize=12)

        filename = os.path.join(output_dir, f"frame_{i + 1:03d}.png")
        plt.savefig(filename, dpi=100, bbox_inches='tight')
        plt.close()

    print(f"Сохранено {len(frames)} кадров в папку '{output_dir}'")


if __name__ == "__main__":
    input_file = "2.dat"  # Укажите ваш файл
    frames = read_frames(input_file)

    if frames:
        save_frames(frames, input_file)
    else:
        print("Нет данных для визуализации")