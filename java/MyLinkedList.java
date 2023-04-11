public class MyLinkedList {

    static int NODE_SIZE;

    static class Node {
        int data;
        Node next;

        public Node (int data) {
            this.data = data;
            this.next = null;
        }
    }

    static class LinkedList{

        Node head;
        Node tail;
        Node[] nodeArr;
        int nodeCnt;

        public LinkedList() {
            head = null;
            nodeArr = new Node[NODE_SIZE];
            nodeCnt = 0;
        }

//        새로운 노드 생성하고, 생성된 노드 반환
        Node getNewNode(int data) {
            nodeArr[nodeCnt] = new Node(data);
            return nodeArr[nodeCnt++];
        }

//        앞에서 idx 개 이후에 nums 추가하기
        void insert(int idx, int[] nums){
            int start = 0;

//            맨 앞에 붙이는 경우(head 변경) -> 한 개 추가 후 head 재조정
            if (idx == 0){
                if (head != null) {
                    Node newNode = getNewNode(nums[0]);
                    newNode.next = head;
                    head = newNode;
                } else {
                    head = getNewNode(nums[0]);
                }
                idx = 1;
                start = 1;
            }


            Node current = head;
//            idx만큼 이동
            for (int i = 1; i < idx; i++) {
                current = current.next;
            }
//            nums 추가
            for (int i = start; i < nums.length; i++) {
                Node newNode = getNewNode(nums[i]);
                newNode.next = current.next;
                current.next = newNode;
                current = newNode;
            }
            if (current.next == null) {
                tail = current;
            }
        }

//        idx 번 인덱스부터 cnt개만큼 삭제
        void delete(int idx, int cnt) {
            Node current = head;

//            맨 앞이 삭제 되는 경우 (head 재조정)
            if (idx == 0) {
                for (int i = 0; i < cnt; i++) {
                    current = current.next;
                }
                head = current;
                return;
            }

//            idx 개만큼 이동
            for (int i = 1; i < idx; i++) {
                current = current.next;
            }

//            삭제되기 직전 위치 기억
            Node last = current;
            for (int i = 0; i < cnt; i++) {
                current = current.next;
            }
            last.next = current.next;

            if (last.next == null) {
                tail = last;
            }
        }

//        제일 뒤에 데이터 추가
        void add(int data) {
            Node current = tail;
            Node newNode = getNewNode(data);
            current.next = newNode;
            tail = newNode;
        }



    }



}
