def count_frequencies(nums: list[int]) -> dict[int, int]:
    result = {}

    for n in nums:
        if not n in result:
            result[n] = 1
        else:
            result[n] += 1

    return result


def most_frequent(nums: list[int]) -> int | None:
    if len(nums) == 0:
        return None

    if len(nums) == 1:
        return nums[0]

    target_frequencies = list(count_frequencies(nums).items())
    target_frequencies.sort(key=lambda x: x[1], reverse=True)

    if len(target_frequencies) > 1 and target_frequencies[0][1] == target_frequencies[1][1]:
        return None

    return target_frequencies[0][0]
