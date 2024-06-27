from sklearn.datasets import load_digits
from colorist.constants.ansi import RESET_ALL
from colorist import BgColorRGB
import math
import cv2


def most_frequent(nums: list[int]) -> int | None:
    return max(nums, key=lambda n: nums.count(n))


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


distance_info = []

for data_index in range(0, len(digits.data)):
    distance = 0

    for i in range(0, len(digits.data[data_index])):
        distance += (digits.data[data_index][i] - img_flat[i]) ** 2

    distance = math.sqrt(distance)

    distance_info.append((distance, digits.target[data_index]))

distance_info.sort()

targets_ordered = [distance[1] for distance in distance_info]

print(most_frequent(targets_ordered[:3]))
