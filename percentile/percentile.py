import numpy
import math

def main():
	
	  #Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
    #Example: Let's say we have an array of the ages of all the people that live in a street.
    #What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
    #The NumPy module has a method for finding the specified percentile:

	p = 75
	
	ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
	
	x = numpy.percentile(ages, p)
	
	print(x)
	
	n = len(ages)
	
	ages.sort()
	
	index = math.ceil(p/100*n)
	
	answer = ages[index-1]
	
	print(answer)
	
main()    
