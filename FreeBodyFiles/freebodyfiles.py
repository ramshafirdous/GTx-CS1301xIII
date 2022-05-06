#Recall Coding Problem 4.3.9 (Advanced), the free body
#diagram problem. If you were unable to solve that, we've
#included the sample answer in the dropdown in the top left
#-- feel free to use that to write your answer to this
#problem.
#
#Revise your code from that problem to use a file instead of
#a list as its parameter. Name this new function
#find_net_force_from_file. The function should take one
#parameter, the name of a file. The function should return
#the net magnitude and direction, just as it did in the other
#problem.
#
#Each line of the file will have two numbers, both integers:
#the first number will be the magnitude, and the second
#number will be the angle (in degrees, from -180 to 180).
#There will be a space between them.
#
#HINT: You may have multiple functions in your code if you
#want!
#
#HINT 2: Try to write this such that you can reuse as much
#of your earlier code as possible. Remember, when loading
#from a file, any text you load is initially a string. You'll
#almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt

#Add your function here!
def find_net_force_from_file(filename):
    output_file= open(filename,"r")
    result=[]
    for item in output_file:
        item = item.rstrip('\n')
        item = item.split()
        
        item0 = int(item[0])
        item1 = int(item[1])
        finalitem = item0,item1

        tupleitem = tuple(finalitem)
        result.append(tupleitem)
        
    HC = 0
    VC = 0
    for s in result:
        s0 = radians(s[0])
        s1 = radians(s[1])

        HC +=s0*cos(s1)
        VC +=s0*sin(s1)
    
    ResultMagnitude = sqrt(HC**2 + VC**2)
    DeMagnitude = degrees(ResultMagnitude)

    ResultAngle = atan2(VC,HC)
    deAngle = degrees(ResultAngle)
    
    return round(DeMagnitude,1),round(deAngle,1)

    output_file.close()


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))




