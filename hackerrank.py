from itertools import product, permutations, combinations, combinations_with_replacement, groupby
from collections import Counter

print('-' * 4, "COUNTER", '-' * 4)
number_of_shoes = int(input())
shoe_size = Counter(map(int, input().split()))
number_of_custumers = int(input())
total = 0
for custumers in range(number_of_custumers):
    size, price = map(int, input().split())
    if shoe_size[size] > 0:
        shoe_size[size] -= 1
        total += price
print(total)
# itertools.product()
print('-' * 4, "PRODUCT", '-' * 4)
A = map(int, input().split())
B = map(int, input().split())
print(*product(A, B))
# itertools.combinations()
print('-' * 4, "COMBINATIONS", '-' * 4)
string, integer = input().split()
integer = int(integer)
for i in range(integer + 1):
    for c in combinations(sorted(string), i):
        print(''.join(c)) 

# itertools.permutaions()
print('-' * 4, "PERMUTATIONS", '-' * 4 )
string, integer = input().split()
integer = int(integer)
permutation = permutations(sorted(string), integer)
for x in permutation:
    print(''.join(x))
# combinations_with_replacement
# print('-' * 4 ,"combinations_with_replacement", '-' * 4)
# string, integer = input().split()
# integer = int(integer)
# replacement = combinations_with_replacement(sorted(string), integer)
# for x in replacement:
#     print(''.join(x)) 

# # itetools.groupby()
# print('-' * 4, "STRING VALIDATORS", '-' * 4)
# N = input()
# for key, group in groupby(N):
#     print(((len(list(group)), int(key))), end=" ")

# #nested list
# print('-' * 4, 'NESTED LIST' , '-' * 4)
# student_marks = []
# N = int(input())
# for i in range (N):
#     name = input()
#     score = int(input())
#     student_marks.append([name, score])
# ordered_score = sorted(set(score[1] for score in student_marks))
# second_lowest_score = ordered_score[1]
# for name, ordered_score in sorted(student_marks):
#     if ordered_score == second_lowest_score:
#         print(name)
        
# # finding the percentage
# print('-' * 4, "FINDING THE PERCENTAGE", '-' * 4)
# N = int(input())
# student_score = {}
# for i in range(N):
#     line = input().split()
#     name = line[0]
#     score = line[1:]
#     student_score[name] = list(map(float, line[1:]))
# query_name = input()
# query_score = student_score[query_name]
# average = sum(query_score) / len(query_score)
# print(f"{average:.2f}")

# # twoSum
# print('-' * 4, "TWOSUM", '-' * 4)
# def twoSum(nums, target):
#     seen = []
#     for num in nums:
#         complement = target - num
#         if complement in seen:
#             return [complement, num] 
#         seen.append(num)
        
# nums = list(map(int, input().split()))
# target = int(input())
# results = twoSum(nums, target)
# print(results)






















# def twoSum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i
# nums = list(map(int, input().split()))
# target = int(input())
# results = twoSum(nums, target)
# print(results)
