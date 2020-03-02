#! /usr/bin/python3
#author: Michele Fischer, 27.02.2020
#This program compute the most likely outcomes for the sum of two dice rolls.
#Each die has 4 <= N,M <= 20 numbered faces, starting with 1 and each face has equal roll probability.

#import the string with the number of faces of the two dice 
import sys

#split the string in half and convert each string to an integer
for line in sys.stdin:
    NM = line.split()
    N = int(NM[0])
    M = int(NM[1])

#in case we have a symmetric matrix, the main diagonal has the most likely possibilities
    if N == M:
        print(N+1)

#as we have more than one main diagonal with the same amount of entries, the sums with the most likely
#possibilities will be listed from lowest to highest value
    elif N < M:
        for i in range(N,M+1):
            #prints every result in seperate lines
            print(i+1)

    elif M < N:
        for i in range(M,N+1):
            print(i+1)
