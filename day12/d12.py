import numpy as np
from scipy.ndimage import label

with open("input.txt") as f:
    array = [list(line.strip()) for line in f]
array = np.array(array)
unique_chars = np.unique(array)


def check_fence(padded_mask, pixel):
    row, col = pixel
    pixel_fence = 0
    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for r, c in neighbors:
        if padded_mask[r, c] == 0:
            pixel_fence += 1

    return pixel_fence


def check_corner(padded_mask, pixel, num_region):
    row, col = pixel
    top_left = [(row - 1, col - 1), (row - 1, col), (row, col - 1)]
    top_right = [(row - 1, col + 1), (row - 1, col), (row, col + 1)]
    bottom_left = [(row + 1, col - 1), (row + 1, col), (row, col - 1)]
    bottom_right = [(row + 1, col + 1), (row + 1, col), (row, col + 1)]
    L_shapes = [top_left, top_right, bottom_left, bottom_right]
    corner_count = 0

    # outer corners
    for L_shape in L_shapes:
        L_count = 0
        for l in L_shape:
            if padded_mask[l] != num_region:
                L_count += 1
        if L_count == 3:
            corner_count += 1
    # inner corners
    for L_shape in L_shapes:
        if (
            padded_mask[L_shape[0]] != num_region
            and padded_mask[L_shape[1]] == num_region
            and padded_mask[L_shape[2]] == num_region
        ):
            corner_count += 1
        if (
            padded_mask[L_shape[0]] == num_region
            and padded_mask[L_shape[1]] != num_region
            and padded_mask[L_shape[2]] != num_region
        ):
            corner_count += 1
    return corner_count


def count_fences(padded_mask, num_region):
    label_pixels = np.where(padded_mask == num_region)
    region_fence = 0
    for pixel in zip(label_pixels[0], label_pixels[1]):
        # Task 1
        # pixel_fence = check_fence(padded_mask, pixel)
        # Task 2
        pixel_fence = check_corner(padded_mask, pixel, num_region)
        region_fence += pixel_fence
    return region_fence


total_price = 0

for char in unique_chars:
    binary_mask = array == char
    labeled_mask, num_regions = label(binary_mask)
    region_sizes = np.bincount(labeled_mask.ravel())[1:]

    padded_mask = np.pad(labeled_mask, pad_width=1, mode="constant", constant_values=0)

    for num_region, region_size in zip(range(1, num_regions + 1), region_sizes):
        region_fences = count_fences(padded_mask, num_region)
        total_price += region_fences * region_size

print(total_price)
# 853588
