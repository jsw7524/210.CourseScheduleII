class Solution(object):
    def HasCycle(self, v):
        if 0 == self.vertices[v]:
            for e in self.courseGraph[v]:
                self.vertices[v] = 1
                if self.HasCycle(e):
                    return True
                self.vertices[v] = 0
        else:
            return True
        return False

    def canFinish(self, numCourses, prerequisites):
        self.vertices = [0] * numCourses
        self.courseGraph = {n: [] for n in range(numCourses)}
        for p in prerequisites:
            self.courseGraph[p[1]].append(p[0])
        for v in range(numCourses):
            if self.HasCycle(v):
                return False
        return True

    def TopologicalSort(self, v):
        if 0 == self.vertices[v]:
            self.vertices[v] = 1
            for e in self.courseGraph[v]:
                self.TopologicalSort(e)
            self.postOrder.append(v)
        return

    def findOrder(self, numCourses, prerequisites):
        if not self.canFinish(numCourses, prerequisites):
            return []
        self.postOrder = []
        self.vertices = [0] * numCourses
        self.courseGraph = {n: [] for n in range(numCourses)}
        for p in prerequisites:
            self.courseGraph[p[1]].append(p[0])
        for v in range(numCourses):
            self.TopologicalSort(v)
        return self.postOrder[::-1]

sln=Solution()
assert [0,1]==sln.findOrder(numCourses = 2, prerequisites = [[1,0]])
assert [0,2,1,3]==sln.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
assert []==sln.findOrder(numCourses = 2, prerequisites = [[0,1],[1,0]])
