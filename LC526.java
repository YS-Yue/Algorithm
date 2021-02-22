class Solution {
    public static int countArrangement(int n) {
        boolean[] visited = new boolean[n + 1];
        return backtracking(visited, 1, n);

    }

    private static int backtracking(boolean[] visited, int position, int n) {
        if (position > n) {
            return 1;
        } else {
            int count = 0;
            for (int i = 1; i < n + 1; i++) {
                if (!visited[i] && (position % i == 0 || i % position == 0)) {
                    visited[i] = true;
                    count += backtracking(visited, position + 1, n);
                    visited[i] = false;
                }
            }
            return count;
        }
    }

    public static void main(String[] args) {
        if (countArrangement(15) == 24679) {
            System.out.println("Works!");
        } else {
            System.out.println("Failed!");
        }
    }
}