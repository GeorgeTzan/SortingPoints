import math
import argparse
import time


def quicksort(points):
    if len(points) < 1:
        return points
    pivot = points[len(points) // 2]
    left = [x for x in points if distance(x) < distance(pivot)]
    middle = [x for x in points if distance(x) == distance(pivot)]
    right = [x for x in points if distance(x) > distance(pivot)]
    return quicksort(left) + middle + quicksort(right)


def distance(points):
    x, y, z = points
    return math.sqrt((x**2 + y**2 + z**2))


def read_points_from_file(filename):
    points = []
    with open(filename, "r") as file:
        for line in file:
            x, y, z = map(float, line.split())
            points.append((x, y, z))
    return points


def write_points_to_file(points):
    output_filename = "output.txt"
    with open(output_filename, "w") as file:
        for point in points:
            file.write(f"{point[0]} {point[1]} {point[2]}\n")


def main(file_path):
    start_time = time.process_time()
    points = read_points_from_file(file_path)
    sorted_points = quicksort(points)
    write_points_to_file(sorted_points)
    end_time = time.process_time()
    with open("timings.txt", "a") as f:
        f.write(str(end_time - start_time) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a input file.")
    parser.add_argument(
        "-i", "--input", type=str, help="The path to the input file", required=True
    )
    args = parser.parse_args()

    main(args.input)
