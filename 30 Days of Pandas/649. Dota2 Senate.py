from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        # Initialize two queues to store the indices of senators from each party
        q_R = deque()
        q_D = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                q_R.append(i)
            else:
                q_D.append(i)
        while q_R and q_D :
            r = q_R.popleft()
            d = q_D.popleft()

            if r < d :
                q_R.append(r + len(senate))
            else :
                q_D.append(d + len(senate))
        return 'Radiant' if q_R else 'Drive'
# Example usage
solution = Solution()
print(solution.predictPartyVictory("RDD"))  # Output: "Dire"
