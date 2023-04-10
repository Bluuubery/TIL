package swea.ai로봇;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution
{
    private final static int CALL_JOB				= 100;
    private final static int RETURN_JOB				= 200;
    private final static int BROKEN					= 300;
    private final static int REPAIR 				= 400;
    private final static int CHECK					= 500;

    private static UserSolution usersolution = new UserSolution();

    private static int run (BufferedReader br, int score) throws Exception
    {
        int N, Q;
        int wIDCnt = 1;
        int cTime, mNum, rID, wID, mOpt;
        int res = -1, ans;

        N = Integer.parseInt(br.readLine());
        usersolution.init(N);

        Q = Integer.parseInt(br.readLine());

        while (Q-- > 0)
        {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int cmd = Integer.parseInt(st.nextToken());

            switch (cmd)
            {
                case CALL_JOB:
                    cTime = Integer.parseInt(st.nextToken());
                    mNum = Integer.parseInt(st.nextToken());
                    mOpt = Integer.parseInt(st.nextToken());
                    res = usersolution.callJob(cTime, wIDCnt, mNum, mOpt);
                    ans = Integer.parseInt(st.nextToken());
                    if (ans != res)
                        score = 0;
                    System.out.println("Q = " + Q + ", cmd = CALL_JOB"  + ", cTime = " + cTime + ", wId = " + wIDCnt + ", mNum = " + mNum + ", mOpt = " + mOpt + ", res = " + res + ", ans = " + ans);
                    wIDCnt++;
                    break;
                case RETURN_JOB:
                    cTime = Integer.parseInt(st.nextToken());
                    wID = Integer.parseInt(st.nextToken());
                    usersolution.returnJob(cTime, wID);
                    System.out.println("Q = " + Q + ", cmd = RETURN_JOB" + ", cTime = " + cTime + ", wId = " + wID);
                    break;
                case BROKEN:
                    cTime = Integer.parseInt(st.nextToken());
                    rID = Integer.parseInt(st.nextToken());
                    usersolution.broken(cTime, rID);
                    System.out.println("Q = " + Q + ", cmd = BROKEN" + ", cTime = " + cTime + ", rId = " + rID);

                    break;
                case REPAIR:
                    cTime = Integer.parseInt(st.nextToken());
                    rID = Integer.parseInt(st.nextToken());
                    usersolution.repair(cTime, rID);
                    System.out.println("Q = " + Q + ", cmd = REPAIR" + ", cTime = " + cTime + ", rid = " + rID);

                    break;
                case CHECK:
                    cTime = Integer.parseInt(st.nextToken());
                    rID = Integer.parseInt(st.nextToken());
                    res = usersolution.check(cTime, rID);
                    ans = Integer.parseInt(st.nextToken());
                    System.out.println("Q = " + Q + ", cmd = CHECK " + ", cTime = " + cTime + ", rId= " + rID + ", res = " + res + ", ans = " + ans);
                    if (ans != res)
                        score = 0;
                    break;
                default:
                    score = 0;
                    break;
            }
        }

        return score;
    }

    public static void main(String[] args) throws Exception
    {
        System.setIn(new java.io.FileInputStream("swea/ai로봇/sample_input25.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer line = new StringTokenizer(br.readLine(), " ");

        int TC = Integer.parseInt(line.nextToken());
        int Ans = Integer.parseInt(line.nextToken());

        for (int testcase = 1; testcase <= TC; ++testcase)
        {
            System.out.println("#" + testcase + " " + run(br, Ans));
        }

        br.close();
    }
}