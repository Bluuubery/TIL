package swea.긴사다리게임;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {
    private final static int CMD_INIT				= 1;
    private final static int CMD_ADD				= 2;
    private final static int CMD_REMOVE				= 3;
    private final static int CMD_NUMBER_OF_CROSS	= 4;
    private final static int CMD_PARTICIPANT		= 5;

    private final static UserSolution usersolution = new UserSolution();

    private static boolean run(BufferedReader br) throws Exception
    {
        StringTokenizer st;

        int numQuery;

        int mX, mY, mID;

        int userAns, ans;

        boolean isCorrect = false;

        numQuery = Integer.parseInt(br.readLine());

        for (int q = 0; q < numQuery; ++q)
        {
            st = new StringTokenizer(br.readLine(), " ");

            int cmd;
            cmd = Integer.parseInt(st.nextToken());

            switch (cmd)
            {
                case CMD_INIT:
                    usersolution.init();
                    isCorrect = true;
                    break;
                case CMD_ADD:
                    mX = Integer.parseInt(st.nextToken());
                    mY = Integer.parseInt(st.nextToken());
                    usersolution.add(mX, mY);
                    break;
                case CMD_REMOVE:
                    mX = Integer.parseInt(st.nextToken());
                    mY = Integer.parseInt(st.nextToken());
                    usersolution.remove(mX, mY);
                    break;
                case CMD_NUMBER_OF_CROSS:
                    mID = Integer.parseInt(st.nextToken());
                    userAns = usersolution.numberOfCross(mID);
                    ans = Integer.parseInt(st.nextToken());
                    if (userAns != ans)
                    {
                        isCorrect = false;
                        System.out.println("q = " + q + " cmd = NUMBEROFCROSS "  + "userAns = " + userAns + " ans = " + ans);
                    }
                    break;
                case CMD_PARTICIPANT:
                    mX = Integer.parseInt(st.nextToken());
                    mY = Integer.parseInt(st.nextToken());
                    userAns = usersolution.participant(mX, mY);
                    ans = Integer.parseInt(st.nextToken());
                    if (userAns != ans)
                    {
                        isCorrect = false;
                        System.out.println("q = " + q + " cmd = PARTICIPANTS "  + "userAns = " + userAns + " ans = " + ans);
                    }
                    break;
                default:
                    isCorrect = false;
                    break;
            }
        }
        return isCorrect;
    }

    public static void main(String[] args) throws Exception
    {
        int TC, MARK;

        System.setIn(new java.io.FileInputStream("swea/긴사다리게임/sample_input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        TC = Integer.parseInt(st.nextToken());
        MARK = Integer.parseInt(st.nextToken());

        for (int testcase = 1; testcase <= TC; ++testcase)
        {
            int score = run(br) ? MARK : 0;
            System.out.println("#" + testcase + " " + score);
        }

        br.close();
    }
}
