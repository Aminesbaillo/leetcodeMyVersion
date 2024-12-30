class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        queue = [0]
        visited = set()
        visited.add(0)
        while queue :
            current_room = queue.pop()
            for key in rooms[current_room] :
                if key not in visited :
                    visited.add(key)
                    queue.append(key)
        return len(visited) == n
    

            