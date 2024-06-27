from sklearn.datasets import load_digits
from colorist.constants.ansi import RESET_ALL
from colorist import BgColorRGB
import math
import cv2


def print_image(image: list[list[int]]):
    for row in img_small:
        for value in row:
            scaled_value = math.floor((255 / 16) * value)
            color_code = BgColorRGB(
                255 - scaled_value, 255, 255 - scaled_value)
            print(f'{color_code}  ', end='')

        print(RESET_ALL)


img = cv2.imread('datasets/five.jpeg', cv2.IMREAD_GRAYSCALE)
img_small = cv2.resize(img, (8, 8))

img_small = [[math.floor((16 / 255) * (255 - pixel))
              for pixel in row] for row in img_small]

img_flat = [x for row in img_small for x in row]

print_image(img_small)

digits = load_digits()

print(digits.data)


distances = []

for data_index in range(0, len(digits.data)):
    distance = 0

    for i in range(0, len(digits.data[data_index])):
        distance += (digits.data[data_index][i] - img_flat[i]) ** 2

    distance = math.sqrt(distance)
    distances.append((distance, digits.target[data_index]))

distances.sort()
print(distances[:3])
