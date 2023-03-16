package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj_16571 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    private static int[][] board = new int[3][3];
    private static int cnt1, cnt2, start;

    private static boolean check (int turn) {

//        가로
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == turn && board[i][1] == turn && board[i][2] == turn) return true;
        }

//        세로
        for (int i = 0; i < 3; i++) {
            if (board[0][i] == turn && board[1][i] == turn && board[2][i] == turn) return true;
        }

//        대각1
        if (board[0][0] == turn && board[1][1] == turn && board[2][2] == turn) return true;

//        대각2
        if (board[0][2] == turn && board[1][1] == turn && board[2][0] == turn) return true;

        return false;
    }

    private static int backtracking (int turn) {

//        이긴 경우 (턴 넘어가고 체크하니까 반대로)
        if (check(3 - turn))
            return -1;


        int res = 2;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == 0) {
                    board[i][j] = turn;
//                    최선의 수는 이긴 경우 (-1)
                    res = Math.min(res, backtracking(3 - turn));
                    board[i][j] = 0;
                }
            }
        }

//        무승부 / 내가 이기면 1 / 상대가 이기면 -1
        return (res == 2 || res == 0) ? 0 : -res;
    }


    public static void main (String[] args) throws IOException {


        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1) cnt1 ++;
                else if (board[i][j] == 2) cnt2 ++;
            }
        }

        start = (cnt1 <= cnt2) ? 1:2;

        int ans = backtracking(start);

        if (ans == 1) System.out.println("W");
        else if (ans == 0) System.out.println("D");
        else System.out.println("L");

    }
}
