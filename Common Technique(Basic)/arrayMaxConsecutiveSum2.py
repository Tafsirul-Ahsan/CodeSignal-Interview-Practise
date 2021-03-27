def arrayMaxConsecutiveSum2(inputArray):
    maxSum = 0
    maxSoFar = 0
    maximum = max(inputArray)
    for i in (inputArray):
        
        if maximum < 0:
            return maximum
        else:
            maxSum = maxSum + i
            maxSum = max(maxSum, 0)
            maxSoFar = max(maxSoFar, maxSum)
    return maxSoFar


if __name__ == '__main__':

    inputArray = [-2, 2, 5, -11, 6]

    print(arrayMaxConsecutiveSum2(inputArray))
