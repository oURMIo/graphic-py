import matplotlib.pyplot as plt


def sierpinski_carpet(order):
    def draw_square(x, y, size):
        plt.gca().add_patch(plt.Rectangle((x, y), size, size, color="k"))

    def carpet(x, y, size, order):
        if order == 0:
            draw_square(x, y, size)
        else:
            new_size = size / 3
            for dx in range(3):
                for dy in range(3):
                    if dx != 1 or dy != 1:
                        carpet(
                            x + dx * new_size, y + dy * new_size, new_size, order - 1
                        )

    plt.figure(figsize=(6, 6))
    carpet(0, 0, 1, order)
    plt.gca().set_aspect("equal")
    plt.gca().axis("off")
    plt.show()


sierpinski_carpet(4)
