class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:
            # If the asteroid is moving right, just add it to the stack
            if asteroid > 0:
                stack.append(asteroid)
            else:
                # If the asteroid is moving left, check for collisions
                while stack and stack[-1] > 0:
                    # There is a potential collision between a right-moving and left-moving asteroid
                    if abs(asteroid) > abs(stack[-1]):
                        stack.pop()  # The right-moving asteroid explodes
                    elif abs(asteroid) == abs(stack[-1]):
                        stack.pop()  # Both asteroids explode
                        break  # No more collision, stop checking
                    else:
                        break  # The left-moving asteroid explodes, stop checking

                else:
                    # If no collision or the stack is empty (no right-moving asteroid to collide with)
                    stack.append(asteroid)
                    
        return stack

# Test the function

asteroids = [10,2,-5]
solution = Solution()
print(solution.asteroidCollision(asteroids)) # Output: [5, 10]

asteroids = [8, -8]
