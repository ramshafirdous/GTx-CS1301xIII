#Write a function called "reader" that reads in a ".cs1301" 
#file described in the previous problem. The function should 
#return a list of tuples representing the lines in the file like so:
#
#[(line_1_number, line_1_assignment_name, line_1_grade, line_1_total, line_1_weight), 
#(line_2_number, line_2_assignment_name, line_2_grade, line_2_total, line_2_weight)]
#
#All items should be of type int except for the name (string) 
#and the weight (float). You can assume the file will be in the 
#proper format -- in a real program, you would use your code
#from the previous problem to check for formatting before
#trying to call the function below.
#
#Hint: Although you could use readlines() to read in all
#the lines at once, they would all be strings, not a list.
#You still need to go line-by-line and convert each string
#to a list.


#Write your function here!
def reader(filename):

    output_file = open(filename,"r")
    read_file = output_file.readlines()
    final_list = []

    for item in read_file:

        splititem= item.split()
        splititem0= int(splititem[0]) 
        splititem2= int(splititem[2])
        splititem3= int(splititem[3])
        splititem4= float(splititem[4])

        result01 = splititem0,splititem[1],splititem2,splititem3,splititem4
        final_list.append(result01)

    return final_list
    output_file.close()

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 
#[(1, 'assignment_1', 85, 100, 0.25), (2, 'test_1', 90, 100, 0.25), (3, 'exam_1', 95, 100, 0.5)]
print(reader("sample.cs1301"))






