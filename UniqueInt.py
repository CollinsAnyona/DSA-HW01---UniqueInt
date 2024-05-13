import re

def process_file(input_path, output_path):
    try:
        #opens the file for reading
        with open(input_path, 'r') as file:
            content = file.read()

            #extracts all numbers from the content
            integers = []
            start_index = 0
            for i, char in enumerate(content):
                if not char.isdigit():
                    if start_index < i:
                        num = int(content[start_index:i])
                        integers.append(num)
                    start_index = i + 1
            
            #initializes a boolean array to keep track of encountered number within range
            encountered = [False] * 2047

            #loops through integers and adds them to unique_integers if not already present
            for num in integers:
                if -1023 <= num <= 1023:
                    index = num + 1023
                    encountered[index] = True

            #writes the unique numbers to an output file
            with open(output_path, 'w') as output_file:
                for i, is_encountered in enumerate(encountered):
                    if is_encountered:
                        num = i -1023
                        output_file.write(f"{num}\n")

            print(f"Unique integers written to {output_path}")
    except FileNotFoundError:
        print(f"File not found: {input_path}")
    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    input_files = [
        r"/mnt/c/Users/Admin/Downloads/sample_01.txt",
        r"/mnt/c/Users/Admin/Downloads/sample_02.txt",
        r"/mnt/c/Users/Admin/Downloads/sample_03.txt",
        r"/mnt/c/Users/Admin/Downloads/sample_04.txt",
    ]
    for input_file in input_files:
        output_file = f"{input_file}_results.txt"
        process_file(input_file, output_file)

if __name__ == "__main__":
    main()
