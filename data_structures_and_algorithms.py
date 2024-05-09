import re

#file path
input_path = r"C:\Users\Admin\Downloads\sample_01.txt"

try:
    #opens the file for reading
    with open(input_path, 'r') as file:
        content = file.read()

        #Extracts all numbers from the content
        integers = [int(num) for num in content.split() if num.isdigit()]

        #removes duplicates by converting into a set
        unique_integers = set(integers)

        #writes the unique number to an output file
        output_path = "sample_01_output.txt"
        with open(output_path, 'w') as output_file:
            for num in sorted(unique_integers):
                output_file.write(f"{num}\n")
        
        print(f"Unique integeres written to {output_path}")
except FileNotFoundError:
    print(f"File not found: {input_path}")
except Exception as e:
    print(f"Error reading file: {e}")        