package swea.ai로봇;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;

class UserSolution
{
    private static int MAX_ROBOT;
    private static int MAX_WORK = 50000;

//    로봇, 작업
    private static Robot[] robots;
    private static ArrayList<Integer>[] works;

//    우선순위큐(아이큐 높은 / 낮은 순)
    private static PriorityQueue<Robot> maxPq;
    private static PriorityQueue<Robot> minPq;




//    로봇 객체
    private static class Robot {
        int rId; // 로봇 아이디
        boolean isBroken; // 망가졌나
        int iq; // 지능
        int wId; // 작업 번호 (0이면 작업 없음)
        int lastCheck; // 마지막 접근 시점

        public Robot (int rId, boolean isBroken, int iq, int wId, int lastCheck) {
            this.rId = rId;
            this.isBroken = isBroken;
            this.iq = iq;
            this.wId = wId;
            this.lastCheck = lastCheck;
        }
    }


    public void init(int N)
    {
//        자료구조 초기화
        MAX_ROBOT = N;
        robots = new Robot[MAX_ROBOT + 1];
        works = new ArrayList[MAX_WORK + 1];

//        아이큐 높은 순 / 아이큐 낮은 순
//        우선순위는 아이큐 - 마지막 확인 시간
        maxPq = new PriorityQueue<>((o1, o2) -> (o1.iq - o1.lastCheck) != (o2.iq - o2.lastCheck) ? (o2.iq - o2.lastCheck) - (o1.iq - o1.lastCheck) : o1.rId - o2.rId);
        minPq = new PriorityQueue<>((o1, o2) -> (o1.iq - o1.lastCheck) != (o2.iq - o2.lastCheck) ? (o1.iq - o1.lastCheck) - (o2.iq - o2.lastCheck) : o1.rId - o2.rId);

//        로봇 생성 후 pq에 추가
        for (int i = 1; i <= N; i++) {
            Robot robot = new Robot(i, false, 0, 0, 0);
            robots[i] = robot;

            maxPq.add(robot);
            minPq.add(robot);
        }

    }

    public int callJob(int cTime, int wID, int mNum, int mOpt)
    {
//        ans: id 더한 값 / cnt: 로봇 개수
        int ans = 0;
        int cnt = 0;
        works[wID] = new ArrayList<>();

        if (mOpt == 0) {
//            필요 로봇 채울 떄까지
            while (mNum > cnt) {
                Robot robot = maxPq.remove(); // 로봇을 뺀다
                minPq.remove(robot); // 다른 pq에서도 빼주기

                // 고장나거나 이미 일하는 로봇이면 건너 뛰기
                if (robot.isBroken || robot.wId > 0)
                    continue;

//                작업 할당
                works[wID].add(robot.rId);

//                로봇 정보 갱신
                robot.wId = wID;
                robot.iq += cTime - robot.lastCheck;
                robot.lastCheck = cTime;

                cnt++; // 세주기
                ans += robot.rId;
            }
        } else {
            while (mNum > cnt) {
                Robot robot = minPq.remove(); // 로봇을 뺀다
                maxPq.remove(robot);
                // 고장나거나 이미 일하는 로봇이면 건너 뛰기
                if (robot.isBroken || robot.wId > 0)
                    continue;

//                작업 할당
                works[wID].add(robot.rId);

//                로봇 정보 갱신
                robot.wId = wID;
                robot.iq += cTime - robot.lastCheck;
                robot.lastCheck = cTime;


                cnt++; // 세주기
                ans += robot.rId;
            }
        }

        return ans;
    }

    public void returnJob(int cTime, int wID)
    {

//        work 배열에서 아이디로 조회해서 복귀
        for (Integer rId : works[wID]) {
            Robot robot = robots[rId];

            if (robot.isBroken)
                continue;

//            작업 복귀 및 시간 갱신
            robot.wId = 0;
            robot.lastCheck = cTime;

//            다시 큐에 넣어주기
            maxPq.add(robot);
            minPq.add(robot);
        }


        works[wID].clear(); // 비워주기

    }

    public void broken(int cTime, int rID)
    {
        Robot robot = robots[rID];

//        이미 고장나거나 센터에 있는 경우 건너뛰기
        if (robot.isBroken || robot.wId == 0)
            return;

        works[robot.wId].remove(Integer.valueOf(rID));

//        고장 체크, 시간 갱신, 작업 복귀
        robot.isBroken = true;
        robot.lastCheck = cTime;
        robot.wId = 0;
    }

    public void repair(int cTime, int rID)
    {
        Robot robot = robots[rID];

//        안 고장난 경우 건너뛰기
        if (!robot.isBroken)
            return;

//        수리, 아이큐, 시간 갱신
        robot.isBroken = false;
        robot.iq = 0;
        robot.lastCheck = cTime;
//        robot.priority = robot.iq - cTime;

//        다시 큐에 넣어주기
        maxPq.add(robot);
        minPq.add(robot);

    }

    public int check(int cTime, int rID)
    {
        Robot robot = robots[rID];

        if (robot.isBroken)
            return 0;
        else if (robot.wId > 0)
            return -1 * robot.wId;
        else
            return cTime - robot.lastCheck + robot.iq;
    }
}
