package swea.끝말잇기2;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.PriorityQueue;

class UserSolution {
    private static PriorityQueue<String>[] words;
    private static HashSet<String> usedGlobal;
    private static ArrayList<String> used;
    private static int MAX_USERS;
    private static boolean[] lose;

    public void init(int N, int M, char[][] mWords)
    {
        MAX_USERS = N;
        words = new PriorityQueue[26];
        usedGlobal = new HashSet<>();
        lose = new boolean[MAX_USERS + 1];


        for (int i = 0; i < 26; i++) {
            words[i] = new PriorityQueue<>();
        }

        for (int i = 0; i < M; i++) {
            char[] word = mWords[i];
            char c = word[0];
            String s = new String(word).trim();

            words[c - 'a'].add(s);
        }

    }

    public int playRound(int mID, char mCh)
    {
        int currentPlayer = mID;
        char startChar = mCh;
        boolean end = false;
        String currentWord = "";
        used = new ArrayList<>();

        while (true) {

//            다음 단어
            while (true) {

//                탈락
                if (words[startChar - 'a'].isEmpty()) {
                    lose[currentPlayer] = true;
                    end = true;
                    break;
                }

                currentWord = words[startChar - 'a'].remove();
//                이미 쓰인 단어
                if (!usedGlobal.contains(currentWord))
                    break;
            }

//            라운드 끝
            if (end) break;



            usedGlobal.add(currentWord);
            used.add(currentWord);

//            변수 갱신
            startChar = currentWord.charAt(currentWord.length() - 1);

            do {
                currentPlayer++;
                if (currentPlayer > MAX_USERS)
                    currentPlayer = 1;
            } while (lose[currentPlayer]);
        }

//        다시 넣기
        for (String usedWord : used) {
            char[] reverse = new char[usedWord.length()];
            for (int i = 0; i < usedWord.length(); i++) {
                reverse[i] = usedWord.charAt(usedWord.length() - 1 - i);
            }
            String reverseWord = new String(reverse);

            if (!usedGlobal.contains(reverseWord)) {
                words[reverseWord.charAt(0) - 'a'].add(reverseWord);
            }
        }


        return currentPlayer;
    }
}
