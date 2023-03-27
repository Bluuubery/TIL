package swea.긴사다리게임;

import java.util.TreeSet;

class UserSolution
{

    private class Ladder implements Comparable<Ladder>{
        int y;
        int direction; // 1: 우, -1: 좌

        public Ladder(int y, int direction) {
            this.y = y;
            this.direction = direction;
        }

        @Override
        public int compareTo(Ladder o) {
            return this.y - o.y;
        }
    }

    private static TreeSet<Ladder>[] ladderList;


    public void init()
    {
         ladderList = new TreeSet[101];
        for (int i = 0; i < 101; i++) {
            ladderList[i] = new TreeSet<>();
        }
    }

    public void add(int mX, int mY)
    {
        ladderList[mX].add(new Ladder(mY, 1));
        ladderList[mX + 1].add(new Ladder(mY, -1));
    }

    public void remove(int mX, int mY)
    {
        Ladder ladder1 = ladderList[mX].lower(new Ladder(mY + 1, 1));
        ladderList[mX].remove(ladder1);

        Ladder ladder2 = ladderList[mX + 1].lower(new Ladder(mY + 1, 1));
        ladderList[mX + 1].remove(ladder2);
    }

    public int numberOfCross(int mID)
    {
        int currentX = mID;
        int currentY = 0;
        int ans = 0;

        while (true) {
            Ladder next = ladderList[currentX].higher(new Ladder(currentY, 1));

            if (next == null)
                break;

            currentX += next.direction;
            currentY = next.y;
            ans ++;
        }

        return ans;
    }

    public int participant(int mX, int mY)
    {
        int currentX = mX;
        int currentY = mY;

        while (true) {
            Ladder next = ladderList[currentX].lower(new Ladder(currentY, 1));

            if (next == null)
                break;

            currentX += next.direction;
            currentY = next.y;
        }

        return currentX;
    }
}
