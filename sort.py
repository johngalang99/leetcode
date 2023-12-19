arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

arr.sort(reverse=True)
print(arr)

arr = ["bob", "alice", "charlie", "david"]
arr.sort()
print(arr)

arr.sort(key=lambda x: len(x))
print(arr)

arr = [i+i for i in range(5)]
print(arr)


arr = [[0] * 4 for i in range(4)]
print(arr)
