class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        single_list = sorted([item for row in matrix for item in row])
        return single_list[k-1]