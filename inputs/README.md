Download sample data for this assignment from this location.
Organize the code and the sample input into the following locations:
/dsa/hw01/code/src/
/dsa/hw01/sample_inputs/
/dsa/hw01/sample_results
However, you can choose to organize your code and data in your own way but be share to
organize things properly so that It be easy to understand your work.
2) Read a file that has one integer on each line. The integer can be positive or negative.
5
14
5
-9
62
-1
-9
-9
3) For each input file in the sample folder, you need to output a result file which contains a
list of the unique integers in this file. For example, for input file “sample_input_02.txt”,
your result should be in sample_results/sample_input_02.txt_results.txt
4) The integers in result file must be sorted in increasing order.
5) There must be one line in result file for each unique integer.
6) For example, if the input is as shown in number “2” above, the result must be:
-9
-1
5
14
62
Note that the digits 5 and -9 appeared multiple times in the input but have been printed
only once.
7) Few sample input files and result files are given in the UniqueInt Sample data file for test
purpose.
8) Your code must also handle following variations in the input file:
a) Integers in each line can have a white space before or after them. A whitespace is
limited to one or more tab, and space characters.
b) If there are any lines with no inputs or white spaces, those lines must be skipped.
See example input files.
c) If there are any lines with two integers separated by white space, those lines must
be skipped.
d) If there are any lines that contain a non-integer input, those lines must be skipped.
See example input file
• Non-integer input includes alphabets, punctuation marks, non-numeric values,
floating point numbers.

