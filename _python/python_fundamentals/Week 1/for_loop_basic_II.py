#1 Biggie Size

def biggie_size(nums):
    for i in range(0, len(nums)):
        if nums[i]>0:
            nums[i]="big"
    return nums
print(biggie_size([-1,4,5,6,7,-3,-9,0]))

#2 Count Positives

def count_positives(nums):
    num_positives = 0
    for i in nums:
        print nums[i]
        if i > 0:
            num_positives += 1
    nums.pop()
    nums.append(num_positives)
print(count_positives([7,8,9,2,4,-9,0,-1]))