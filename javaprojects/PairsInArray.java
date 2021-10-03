package javaprojects;

/* 
        AUTHOR: GAUTAM CHANDRA SAHA
        DATE & TIME: SUNDAY 3 OCT, 2021, AT 6:40 PM
*/

import java.util.Map;
import java.util.LinkedHashMap;

class PairsInArray {
    int[] nums = { 8, 7, 2, 5, 3, 1 };
    int target = 10;

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
