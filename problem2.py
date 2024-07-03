'''
Course Schedule (https://leetcode.com/problems/course-schedule/)

Time Complexity: O(V + E)
Space Complexity: O(V + E)

where:
V: No of Vertics (courses)
E: No of Edges (prerequisite relations)

'''
from collections import deque

class Solution:
  def canFinish(self, numCourses: int, prerequisites):
    # indegree array and adjacency list hashmap
    indegrees = [ 0 for n in range(numCourses) ]
    adjList = { n : [] for n in range(numCourses) }
    for link in prerequisites:
      head, tail = link
      indegrees[head] += 1
      adjList[tail].append(head)

    # find socurces with 0 indegrees
    sources = []
    for course, indegree in enumerate(indegrees):
      if indegree == 0:
        sources.append(course)

    # if no such 0 indegree source means we can't start from any course
    if len(sources) == 0:
      return False

    # initialize bfs queue with sources and perform bfs
    bfsQueue = deque(sources)
    while len(bfsQueue) > 0:
      course = bfsQueue.popleft()
      for adj in adjList[course]:
        indegrees[adj] -= 1 # on every course completion, decrease the indegrees of its dependents
        if indegrees[adj] == 0:
          bfsQueue.append(adj)

    # check if all course were completed by checking if all indegrees are now 0
    for indegree in indegrees:
      if indegree > 0:
        return False

    return True

s = Solution()
numCourses1 = 2
prerequisites1 = [[1,0],[0,1]]
print(s.canFinish(numCourses1, prerequisites1))

numCourses2 = 5
prerequisites2 = [[1,0],[2,0],[2,1],[2,4],[3,2],[4,3]]
print(s.canFinish(numCourses2, prerequisites2))

numCourses3 = 6
prerequisites3 = [[1,0],[2,1],[3,2],[4,3],[5,0],[5,1],[5,2],[5,3],[5,4]]
print(s.canFinish(numCourses3, prerequisites3))
