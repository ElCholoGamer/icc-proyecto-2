from sklearn import datasets
import image_utils
import frequency_utils
import math


def distance(vec_a: list[int], vec_b: list[int]) -> float:
    square_sum = 0

    for a, b in zip(vec_a, vec_b):
        square_sum += (a - b) ** 2

    return math.sqrt(square_sum)


digits = datasets.load_digits()
digits_zip = list(zip(digits.images, digits.data, digits.target))

averages = [image_utils.target_average(digits_zip, i) for i in range(0, 10)]

for i, average in enumerate(averages):
    print(f'Promedio de {i}:')
    image_utils.print_image(average)
    print()

print('=' * 42)
print()

image_path = input('Ingrese la imagen a reconocer: ')
image = image_utils.read_image_scaled(image_path)

print('Imagen a reconocer:')
image_utils.print_image(image)
print()

image_flat = image_utils.flatten(image)

distance_results = [(distance(data, image_flat), target)
                    for _, data, target in digits_zip]

distance_results.sort()
nearest_targets = [e[1] for e in distance_results[:3]]

prediction = frequency_utils.most_frequent(nearest_targets)

if prediction == None:
    for t in range(3, 11):
        next_nearest_target = distance_results[t][1]

        if next_nearest_target in nearest_targets:
            prediction = next_nearest_target
            break

        nearest_targets.append(next_nearest_target)

print(
    'Soy la inteligencia artificial,',
    'y he detectado que el dígito ingresado',
    f'corresponde al número {prediction}.'
)

print()


distances_to_avgs = [
    distance(image_utils.flatten(avg), image_flat) for avg in averages
]

prediction_2 = distances_to_avgs.index(min(distances_to_avgs))

print(
    'Soy la inteligencia artificial versión 2,',
    'y he detectado que el dígito ingresado',
    f'corresponde al número {prediction_2}.'
)
