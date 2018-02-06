####################################################################
#   Name:Kritwish Mondal                                           #
#   Roll No.: 16MF3IM08                                            #
#   Department: Mechanical Engineering                             #
####################################################################

import operator
import math
from math import exp,log

def loadDataset(filename,trainingSample=[]):
	with open("eda-18-ass1-data.txt","r") as infile :	#reading the input file
		for line in infile :
			words=line.split()
			x1=[float(temp) for temp in words[1:]]		#seperating and storing the trainingSample in trainingSample
			trainingSample.append(x1)

def getNeighbors(trainingSample, testSample, k ):
	distances = []										#for storing the distances
	length = len(testSample)-1
	for x in range(len(trainingSample)):
		dist = euclideanDistance(testSample, trainingSample[x], length)		#calculating the euclideanDistance and storing it into distances
		distances.append((trainingSample[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = [];										#for storing the neighbors
	for x in range(k):
	  neighbors.append(distances[x][0])					#appending the neighbors into the list neighbors
	return neighbors

def euclideanDistance(instance1, instance2, length):	#function to calculate the distances between the trainingSample and the testSample
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)							#using the euclidean distance formula and returining the distance value

def getResponse(neighbors):
	classVotes = {}										#for storing the classVotes of each target value of the neighboring samples
	for x in range(len(neighbors)):						#calculating the class votes for each neighboring target value
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1

	sortedVotes = sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)  #sorting the classVotes as per the items of the dictionary in descending order
	return sortedVotes[0][0]

def main():
	trainingSample=[]		                                    #for storing the input data trainingSample
	loadDataset("eda-18-ass1-data.txt",trainingSample)          #load the dataset
	print("Enter the features of the test sample(seperate the values using a space):")
	testSample = [float(x) for x in input().split()]  	        #input of sample from the user
	k=25                                                        #value of k
	neighbor=getNeighbors(trainingSample,testSample,k)          #find out the neighbouring samples
	result=getResponse(neighbor)                                #getting the result for the testSample
	print("The predicted target value for the given test sample is {}".format(result))   #print the target_value(result) of the testSample

if __name__ == "__main__":
    main()
