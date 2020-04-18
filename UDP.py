
def processData(data):
    arr = ((data.decode()).split(" "))
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    return arr
