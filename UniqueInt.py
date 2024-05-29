import time
import tracemalloc
import os

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def is_unique(integer, unique_list):
    for num in unique_list:
        if num == integer:
            return False
    return True

def process_file(inputFilePath, outputFilePath):
    try:
        # Start measuring time and memory usage
        start_time = time.time()
        tracemalloc.start()

        unique_integers = []

        # Read the input file
        with open(inputFilePath, 'r') as input_file:
            for line in input_file:
                # Manually remove whitespace and newline characters
                line = ''.join(c for c in line if c.isdigit() or c == '-' or c.isspace()).strip()
                
                try:
                    # Attempt to convert each line to an integer
                    integer = int(line)
                    
                    # Check if the integer is unique before adding
                    if is_unique(integer, unique_integers):
                        unique_integers.append(integer)
                except ValueError:
                    # If conversion fails, skip the line
                    continue

        # Sort unique integers using custom bubble sort
        sorted_unique_integers = bubble_sort(unique_integers)

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(outputFilePath), exist_ok=True)

        # Write the sorted unique integers to the output file
        with open(outputFilePath, 'w') as output_file:
            for num in sorted_unique_integers:
                output_file.write(f"{num}\n")

        print(f"Unique integers written to {outputFilePath}")

        # Stop measuring time and memory usage
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        # Print the runtime and peak memory usage
        print(f"Runtime: {end_time - start_time:.6f} seconds")
        print(f"Memory usage: {peak / 10**6:.6f} MB")

    except FileNotFoundError:
        print(f"File not found: {inputFilePath}")
    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    input_files = [
        "/mnt/c/Users/Admin/Downloads/sample_01.txt",
        "/mnt/c/Users/Admin/Downloads/sample_02.txt",
        "/mnt/c/Users/Admin/Downloads/sample_03.txt",
        "/mnt/c/Users/Admin/Downloads/sample_04.txt",
    ]
    output_directory = "/mnt/c/Users/Admin/Downloads/Results/"

    for input_file in input_files:
        output_filename = os.path.join(output_directory, os.path.basename(input_file) + "_results.txt")
        process_file(input_file, output_filename)

if __name__ == "__main__":
    main()

