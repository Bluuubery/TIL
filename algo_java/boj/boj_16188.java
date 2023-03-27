package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class boj_16188 {

//    입출력
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

//    변수
    private static int V, E, cnt;
    private static int[] indegree;
    private static boolean[] visited;
    private static ArrayList<Integer>[] graph;

//    dfs
    private static void dfs(int node) {

        visited[node] = true;

        for (int next : graph[node]) {
            if (!visited[next]) dfs(next);
        }
    }

//    그래프 분리되어있는지 판별
    private static boolean check(){
        dfs(1);
        visited[0] = true;

        for (boolean bool : visited) {
            if(!bool) return false;
        }

        return true;
    }

    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());
        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        indegree = new int[V + 1];
        visited = new boolean[V + 1];

        graph = new ArrayList[V + 1];
        for (int i = 0; i < V + 1; i++) {
            graph[i] = new ArrayList<>();
        }

//        그래프 및 진입차수 입력
        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            indegree[node1] ++;
            indegree[node2] ++;
            graph[node1].add(node2);
            graph[node2].add(node1);
        }

//       진입차수 홀수인 정점
        cnt = 0;
        for (int i = 1; i < V + 1; i++) {
            if (indegree[i] % 2 != 0)
                cnt++;
        }

//        오일러 경로 판별
        if ((check() && cnt == 0) || (check() && cnt == 2))
            sb.append("YES");
        else
            sb.append("NO");

        System.out.println(sb);
    }



}
