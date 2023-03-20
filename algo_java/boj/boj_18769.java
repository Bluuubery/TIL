package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class boj_18769 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    private static int T, R, C, node;
    private static ArrayList<int[]> graph;
    private static int[] parent;


    private static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    private static void merge(int x, int y) {
        x = find(x);
        y = find(y);

        if (x < y) {
            parent[y] = x;
        } else {
            parent[x] = y;
        }
    }

    public static void main (String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {

            st = new StringTokenizer(br.readLine());
            R = Integer.parseInt(st.nextToken());
            C = Integer.parseInt(st.nextToken());

            parent = new int[R * C + 1];
            graph = new ArrayList<>();
            for (int i = 0; i < R * C + 1 ; i++) {
                parent[i] = i;
            }

            for (int i = 0; i < R; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 1; j < C; j++) {
                    graph.add(new int[]{Integer.parseInt(st.nextToken()), (C * i) + j, (C * i) + j + 1});
                    }
                }


            for (int i = 0; i < R - 1; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 1; j <= C; j++) {
                    graph.add(new int[]{Integer.parseInt(st.nextToken()), (C * i) + j, (C * (i + 1)) + j});
                }
            }

            graph.sort(Comparator.comparingInt(edge -> edge[0]));

            int totalCost = 0;

            for (int i = 0; i < graph.size(); i++) {
                int cost = graph.get(i)[0];
                int node1 = graph.get(i)[1];
                int node2 = graph.get(i)[2];

                if (find(node1) != find(node2)) {
                    merge(node1, node2);
                    totalCost += cost;
                }
            }
            sb.append(totalCost).append("\n");
        }

        System.out.println(sb);
        }
    }




