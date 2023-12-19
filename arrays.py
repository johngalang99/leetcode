arr = [1, 2, 3]
print(arr)


arr.append(4)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr[1] = 8
print(arr)

n = 1
arr = [1] * n
print(arr)
print(len(arr))

arr = [1, 2, 3, 4, 5]
print(arr)
print(arr[-1])
print(arr[-2])

print(arr[1:3])

print(arr[1:4])

a, b, c = [1, 2, 3]
print(a, b, c)

nums = [1, 2, 3]

for i in range(len(nums)):
    print(nums[i])

for n in nums:
    print(n)

for i, n in enumerate(nums):
    print(i, n)


nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

nums.reverse()
print(nums)
