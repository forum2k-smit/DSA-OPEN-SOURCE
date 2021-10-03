package javaprojects;

import java.util.Map;
import java.util.LinkedHashMap;

class PairsInArray {
    int[] nums = { 8, 7, 2, 5, 3, 1 };
    int target = 10;

    // O(n^2) approach
    /*
     * public void findPairOnSquare(int[] A, int target) {
     * 
     * for (int i = 0; i < nums.length - 1; i++) {
     * 
     * for (int j = i + 1; j < nums.length; j++) { if (nums[i] + nums[j] == target)
     * { System.out.println("Pair found (" + nums[i] + ", " + nums[j] + ")"); } } }
     * System.out.println("Pair not found"); }
     */

    // O(n) approach
    public void findPairOn() {

        int flag = 0;

        Map<Integer, Integer> map = new LinkedHashMap<>();
        int index = 0;
        for (int num : nums) {
            map.put(num, index++);
        }

        index = 0;
        for (int num : nums) {
            int pair = target - num;
            if (map.containsKey(pair) && (map.get(pair) != index)) {
                System.out.printf("Pair found ( %d , %d )\n", num, pair);
                map.remove(pair);
                map.remove(num);
                flag = 1;
            }
            index++;

        }

        if (flag == 0)
            System.out.println("Pair not found");
    }

    public static void main(String[] args) {

        new PairsInArray().findPairOn();
    }
}
