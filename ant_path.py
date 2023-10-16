import numpy as np
from PIL import Image

# Размер поля
size = 1024
field = np.zeros((size, size), dtype=np.uint8)
x, y = size // 2, size // 2
direction = 0

while 0 <= x < size and 0 <= y < size:

    if field[y, x] == 0:
        direction = (direction + 1) % 4
        field[y, x] = 1
    else:
        direction = (direction - 1) % 4
        field[y, x] = 0


    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    else:
        x -= 1

img = Image.fromarray(field * 255)
img.save('ant_path.png')
num_black_cells = np.sum(field)

print(f'count: {num_black_cells}')