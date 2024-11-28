


import time
import random

# #original code : 
# class SolutionOriginal(object):
#     def uniqueCocurrence(self, arr):
#         """
#         :type arr: list[int]
#         :rtype: bool
#         """
#         record = {}

#         for i in range(len(arr)): 
#             if arr[i] in record:
#                 record[arr[i]] += 1
#             else:
#                 record[arr[i]] = 1   
#         frequency = list(record.values())
#         return len(frequency) == len(set(frequency))


# Optimized Solution
class SolutionOptimized(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: list[int]
        :rtype: bool
        """
        record = {}
        freq_set = set()

        # Count occurrences and check if any frequency repeats
        for num in arr:
            record[num] = record.get(num, 0) + 1

        # Check if any frequency is repeated directly
        for count in record.values():
            if count in freq_set:
                return False
            freq_set.add(count)

        return True



# Record execution time for the optimized solution
arr = [1,2,2,1,1,3]
solution_optimized = SolutionOptimized()
result_optimized = solution_optimized.uniqueOccurrences(arr)
print(f"Optimized Solution Result: {result_optimized}")













# # Generate a large test case (size 10^6)
# arr = [random.randint(1, 1000) for _ in range(10**6)]  # Array of 1 million elements

# # Record execution time for the original solution
# start_time = time.time()
# solution_original = SolutionOriginal()
# result_original = solution_original.uniqueCocurrence(arr)
# end_time = time.time()
# execution_time_original = end_time - start_time

# # Record execution time for the optimized solution
# start_time = time.time()
# solution_optimized = SolutionOptimized()
# result_optimized = solution_optimized.uniqueOccurrences(arr)
# end_time = time.time()
# execution_time_optimized = end_time - start_time

# # Print results
# print(f"Original Solution Result: {result_original}")
# print(f"Optimized Solution Result: {result_optimized}")
# print(f"Original Solution Execution Time: {execution_time_original:.10f} seconds")
# print(f"Optimized Solution Execution Time: {execution_time_optimized:.10f} seconds")
