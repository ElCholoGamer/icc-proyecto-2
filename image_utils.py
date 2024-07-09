import math
from colorist.constants.ansi import RESET_ALL
from colorist import BgColorRGB
import cv2


def print_image(image: list[list[int]]):
    for row in image:
        for value in row:
            scaled_value = math.floor((255 / 16) * value)
            color_code = BgColorRGB(
                255 - scaled_value, 255, 255 - scaled_value)
            print(f'{color_code}  ', end='')

        print(RESET_ALL)


def flatten(matrix: list[list[int]]) -> list[int]:
    return [x for row in matrix for x in row]


def rescale_pixel(pixel: int) -> int:
    return round((16 / 255) * (255 - pixel))


def read_image_scaled(file_path: str) -> list[list[int]]:
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    img_small = cv2.resize(img, (8, 8))

    return [[rescale_pixel(pixel) for pixel in row] for row in img_small]


def target_average(data_zip: list[tuple[list[list[int]], list[int], int]], target: int) -> list[list[int]]:
    image_rows = len(data_zip[0][0])
    image_cols = len(data_zip[0][0][0])
    result = [[0] * image_cols for _ in range(0, image_rows)]

    count = 0

    for image, _, image_target in data_zip:
        if image_target != target:
            continue

        for i in range(0, image_rows):
            for j in range(0, image_cols):
                result[i][j] += image[i][j]

        count += 1

    return [[math.floor(pixel / count) for pixel in row] for row in result]
