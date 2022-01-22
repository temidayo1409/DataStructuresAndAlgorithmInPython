# Question 1: Alice has some cards with numbers written on them. She arranges the cards in
# decreasing order, and lays them out face down in a sequence on a table.
# She chalenges Bob to pick out the card containing a given number by turning over as
# few cards as possible. Write a function to help Bob locate the card.
# --This may seem like a simple problem, especially if you're familiar with
# --binary search, but the strategy and technique learned here will be widely applicable.

# inputs = cards, num_to_find
# output = num_index

# let's come up with useful test cases:
# 1. the num_to_find may just be the middle number
# 2. num_to_find may be the first number
# 3. num_to_find may be the last number
# 4. num_to_find may not be in the cards list
# 5. cards may contain just one number, which is the num_to_find
# 6. cards may contain repeating numbers
# 7. cards may contain repeating numbers and num_to_find is a repeating number
# 8. cards may be empty

# to write out these test cases:

tests = []
tests.append({'input':{'cards':[14,11,9,8,7,3,1], 'num_to_find':8}, 'output':{'num_index':3}})
tests.append({'input':{'cards':[14,11,9,8,7,3,1], 'num_to_find':14}, 'output':{'num_index':0}})
tests.append({'input':{'cards':[14,11,9,8,7,3,1], 'num_to_find':1}, 'output':{'num_index':6}})
tests.append({'input':{'cards':[14,11,9,8,7,3,1], 'num_to_find':5}, 'output':{'num_index':'NIL'}})
tests.append({'input':{'cards':[9], 'num_to_find':9}, 'output':{'num_index':0}})
tests.append({'input':{'cards':[14,14,14,11,11,9,8,7,3,3,3,3,1,1,1], 'num_to_find':8}, 'output':{'num_index':6}})
tests.append({'input':{'cards':[14,14,14,11,11,9,8,7,3,3,3,3,1,1,1], 'num_to_find':11}, 'output':{'num_index':3}})
tests.append({'input':{'cards':[], 'num_to_find':5}, 'output':{'num_index':'NIL'}})


def BinarySearch(cards, num_to_find):
    n = len(cards)
    low = 0
    high = n-1
    while(high >= low):
        mid = (low + high)//2
        if num_to_find == cards[mid]: 
            if(mid-1 >= 0 and cards[mid-1]==num_to_find):
                high = mid - 1
            else:
                return mid
        elif num_to_find > cards[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "NIL"

def LinearSearch(cards, num_to_find):
    for i in range(len(cards)):
        if cards[i] == num_to_find:
            return i
    return "NIL"

# checking our code against all the listed test cases:

for test in tests:
    print(LinearSearch(**test['input']) == test['output']['num_index'])

for test in tests:
    print(BinarySearch(**test['input']) == test['output']['num_index'])


# example to implement

solve = BinarySearch([15,13,13,13,12,9,8,7,5,5,4,1], 13)
print(solve)
solve2 = LinearSearch([15,13,13,13,12,9,8,7,5,5,4,1], 5)
print(solve2)


# now let's analyze time complexity

# For linear search, we access an element once in every iteration, for a list size of n
# i.e we access elements from the list up to n-times 
# So, in the worst case scenario, Bob may need to turn up to n cards.
# suppose a card can only be turned per minute and suppose we have 30 cards,
# this means for the worst case, it will take Bob up to 30minutes.
# is this the best we can do? Can we optimize our code?
# So, for linear search, the time complexity is O(n) and space complexity is O(1)

# For binary search, if we start out with an array of n elements,
# then the size reduces by half for each iteration i.e n/2
# next iteration = n/2/2 = n/4
# next = n/4/2 = n/8....and so on
# we know it stops when we only have one element i.e n is now totally reduced to 1
# i.e n/2^k == 1. This means the running time depends on the k value
# k = log(n) base 2 OR k = lg(n)
# So, time complexity for binary search in worst case is O(lg(n))


# Now, using binary search to solve another problem:


# Question2: Given an array of integers sorted in ascending order,
# find the starting and ending index of a given number.

def StartingPosition(numbers, num_to_find):
    low, high = 0, len(numbers) - 1
    while(low <= high):
        mid = (low + high)//2
        if(numbers[mid] == num_to_find):
            if(mid > 0 and numbers[mid-1] == num_to_find):
                high = mid -1
            else:
                return mid
        elif(numbers[mid] > num_to_find ):
            high = mid - 1
        else:
            low = mid + 1
    return "NIL"

def EndingPosition(numbers, num_to_find):
    low, high = 0, len(numbers) - 1
    while(low <= high):
        mid = (low + high)//2
        if(numbers[mid] == num_to_find):
            if(mid < (len(numbers) - 1) and numbers[mid+1] == num_to_find):
                low = mid + 1
            else:
                return mid
        elif(numbers[mid] > num_to_find ):
            high = mid - 1
        else:
            low = mid + 1
    return "NIL"

numbers = [1,4,5,5,7,8,9,12,13,13,13,15]
num_to_find = 12
result = (StartingPosition(numbers, num_to_find), EndingPosition(numbers, num_to_find))
print(result)


# Question 3:
# You are given a list of numbers obtained by rotating a sorted list an unknown number of times.
# Write a function to determine the minimum number of times the original sorted list was rotated
# to obtain the given list.
# Your function should have the worst case complexity of O(lg n), where n is the length of the list.
# You can assume that all the numbers in the list are unique.

# for this question,
# inputs = obtained_list, sorted_list
# output = min_rotation_times

# example:
# inputs = [12,13,21,45,3,8],[3,8,12,13,21,45]
# output = |new_index - old_index| = |0-2| = 2 (for number 12) OR
#            |5-3| = 2 (for number 45)

# let's come up with test/edge cases:
# 1. maybe the two inputs are the same i.e zero rotation
# 2. sorted in descending order
# 3. what if either of the list is empty


# implementation code
# binary search = O(lg n)
# key insight to solution: if a list of sorted numbers is rotated k times, then the smallest
# number in the list ends up at position k (counting from 0)
# further, it is the only number in the list which is smaller than the number before it.
# So, if the middle number is smaller than its predecessor, then it is the answer
# if the middle number is smaller than the last number in the list, then the answer lies to the left of it
# otherwise, the answer lies to the right of it

def Num_of_Rotation(obtained_list):
    #num_to_search = min(obtained_list)
    #return obtained_list.index(num_to_search)
    low = 0
    high = len(obtained_list) - 1
    while low <= high:
        mid = (low + high)//2
        if obtained_list[mid] < obtained_list[mid - 1]:
            return mid
        elif obtained_list[mid] < obtained_list[len(obtained_list) - 1]:
            high = mid - 1
        else:
           low = mid + 1
    return mid

solve3 = Num_of_Rotation([2,3,4,5,6,9,0])
print(solve3)
