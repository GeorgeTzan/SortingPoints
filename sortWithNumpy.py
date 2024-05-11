import numpy as np
import argparse
import time


def distance(points):
    return np.sqrt(np.sum(points**2, axis=1))


def read_points_from_file(filename):
    return np.loadtxt(filename)


def write_points_to_file(points):
    output_filename = "output.txt"
    np.savetxt(output_filename, points)


def main(file_path):
    start_time = time.process_time()
    points = read_points_from_file(file_path)
    sorted_indices = np.argsort(distance(points))
    sorted_points = points[sorted_indices]
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
