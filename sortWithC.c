#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

typedef struct {
    double x;
    double y;
    double z;
} Point;

double distance(Point p) {
    return sqrt(p.x * p.x + p.y * p.y + p.z * p.z);
}

int compare(const void* a, const void* b) {
    Point pointA = *(Point*)a;
    Point pointB = *(Point*)b;
    double distanceA = distance(pointA);
    double distanceB = distance(pointB);
    return (distanceA > distanceB) - (distanceA < distanceB);
}

void read_points_from_file(char* filename, Point** points, int* size) {
    FILE* file = fopen(filename, "r");
    Point p;
    *points = NULL;
    *size = 0;
    while (fscanf(file, "%lf %lf %lf", &p.x, &p.y, &p.z) == 3) {
        *points = realloc(*points, (*size + 1) * sizeof(Point));
        (*points)[*size] = p;
        (*size)++;
    }
    fclose(file);
}

void write_points_to_file(Point* points, int size) {
    FILE* file = fopen("output.txt", "w");
    for (int i = 0; i < size; i++) {
        fprintf(file, "%f %f %f\n", points[i].x, points[i].y, points[i].z);
    }
    fclose(file);
}

int main(int argc, char** argv) {
    if (argc != 2) {
        printf("Usage: %s <input file>\n", argv[0]);
        return 1;
    }

    int size = 0;
    Point* points = NULL;

    clock_t start_time = clock();
    read_points_from_file(argv[1], &points, &size);
    qsort(points, size, sizeof(Point), compare);
    write_points_to_file(points, size);
    clock_t end_time = clock();

    FILE* f = fopen("timings.txt", "a");
    fprintf(f, "%f\n", (double)(end_time - start_time) / CLOCKS_PER_SEC);
    fclose(f);

    free(points);

    return 0;
}
