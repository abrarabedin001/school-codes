import random
lengthOfArr = 10
Array = [""]*lengthOfArr

def hash(id):
    total = 0
    for r in range(len(id)):
        total = ord(id[r])*r + total
    return total % lengthOfArr

def id_generator():
    a = chr(random.randint(65,90))
    b = chr(random.randint(65,90))
    c = str(random.randint(0,9))
    d = str(random.randint(0,9))
    e = str(random.randint(0,9))
    f = str(random.randint(0,9))
    total = (a+b+c+d+e+f)
    return total

def hashTable(data,Array):
    index = hash(data)
    sentence =str(data)+" has an index :"+str(index)
    print(sentence)
    if Array[index]=="":
        Array[index] = data
    else:
        while Array[index] != "":
            if index == lengthOfArr-1:
                index = 0
            else:
                index += 1
        Array[index] = data
    print(Array)

for r in range (lengthOfArr):
    data = id_generator()
    if r == 0:
        global SampleData
        SampleData = data
        hashTable(data, Array)
    else:
        hashTable(data, Array)


def find_hash(dataForHash,Array):
    index = hash(dataForHash)
    start = index
    found = False
    if Array[index] != dataForHash:
        while Array[index] != dataForHash and index != start and found == False:
            if index == lengthOfArr-1:
                index = 0
            else:
                index += 1
            if Array[index] == dataForHash:
                Found = True
                print( dataForHash + "can be found in index position: %t"%(index))
                return
        print("Data not in Array")
        Array[index] = data
    else:
        print( dataForHash + " can be found in index position: "+ str(index))

find_hash(SampleData,Array)
