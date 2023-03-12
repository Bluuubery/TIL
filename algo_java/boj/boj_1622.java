package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1622 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    private static int[] Count(String s) {
        int[] countS = new int[26];
        for (int i = 0; i < s.length(); i++) {
            countS[s.charAt(i) - 'a'] ++;
        }
        return countS;
    }

    public static void main (String[] args) throws IOException {
        while (true) {
            String a = br.readLine();
            if (a == null) break;
            String b = br.readLine();

            int[] countA = Count(a);
            int[] countB = Count(b);

            for (int i = 0; i < 26; i++) {
                int cnt = Math.min(countA[i], countB[i]);
                sb.append(String.valueOf((char) (i + 'a')).repeat(Math.max(0, cnt)));
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
