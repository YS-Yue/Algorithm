# Suppose you have n integers labeled 1 through n.
# A permutation of those n integers perm (1-indexed) is considered
# a beautiful arrangement if for every i (1 <= i <= n),
# either of the following is true:

#       perm[i] is divisible by i.
#       i is divisible by perm[i].
#
# Given an integer n, return the number of the beautiful arrangements
# that you can construct.


class SolutionLC526:

    def countArrangement(self, n: int) -> int:

        def backtracking(n, position, visited):
            # to the end, one possible permutation done.
            if position > n:
                self.count += 1
            else:
                for i in range(1, n+1):
                    if not visited[i] and (position % i == 0 or i % position == 0):
                        visited[i] = 1
                        backtracking(n, position+1, visited)
                        visited[i] = 0

        self.count = 0
        visited = [0] * (n+1)
        backtracking(n, 1, visited)

        return self.count


def main():

    solution = SolutionLC526()
    # some tests.
    if solution.countArrangement(15) != 24679:
        print("Algo failed!")
        return

    if solution.countArrangement(2) != 2:
        print("Algo failed!")
        return

    if solution.countArrangement(5) != 10:
        print("Algo failed!")
        return

    print("ALgo works :)")


main()
