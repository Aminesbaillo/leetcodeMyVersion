import collections

class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        print(self.q)
        print(self.q[0])
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# Test case for RecentCounter
def test_recent_counter():
    # Create instance of RecentCounter
    recentCounter = RecentCounter()

    # Test case 1: Calling ping(1)
    print(f"ping(1): {recentCounter.ping(1)}")  # Expected: 1
    
    # Test case 2: Calling ping(100)
    print(f"ping(100): {recentCounter.ping(100)}")  # Expected: 2
    
    # Test case 3: Calling ping(3001)
    print(f"ping(3001): {recentCounter.ping(3001)}")  # Expected: 3
    
    # Test case 4: Calling ping(3002)
    print(f"ping(3002): {recentCounter.ping(3002)}")  # Expected: 3
    
    # Test case 5: Calling ping(5000)
    print(f"ping(5000): {recentCounter.ping(5000)}")  # Expected: 4
    
    # Test case 6: Calling ping(6000)
    print(f"ping(6000): {recentCounter.ping(6000)}")  # Expected: 4

# Run the test
test_recent_counter()
