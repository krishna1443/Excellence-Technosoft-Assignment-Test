def getMaxConsecutiveOne(inputList, n):
    count = 0
    result = 0

    for i in range(0, n):
        if (inputList[i] == 0):
            count = 0
        else:
            count = count + 1
            result = max(result, count)

    return result


inputList = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]
n = len(inputList)

print(getMaxConsecutiveOne(inputList, n))