package javaprojects;

/* 
        AUTHOR: GAUTAM CHANDRA SAHA
        DATE & TIME: SUNDAY 3 OCT, 2021, AT 6:40 PM
*/

// imports from java collections
import java.util.Map;
import java.util.LinkedHashMap;

//main class
class PairsInArray {
    int[] nums = { 8, 7, 2, 5, 3, 1 };
    int target = 10;

    public void findPairOn() {

        int flag = 0; // flag to avoid unnecessary output

        Map<Integer, Integer> map = new LinkedHashMap<>();
        // map to store the numbers in the array as keys

        int index = 0;
        for (int num : nums) { // loop to put the numbers in the map from the array
            map.put(num, index++);
        }

        index = 0;
        for (int num : nums) {
            int pair = target - num; // e.g., pair = 10 - 8 = 2 is the pair
            if (map.containsKey(pair) && map.get(pair) != index) {
                // if the pair is in the map as a key
                // and if the value for the key is not the current index then,

                /*
                  e.g., for value 5 in array index = 3 for index 3 
                  the map will look like 
                  map = {5=3}, as we are removing the pair upon each iteration
                  where 5 is the number and 3 is its index 
                  pair = target(10) - num(5) = 5 
                  so the condition map.containsKey() is true and 
                  the condition map.get(pair) != index is false
                  hence, this pair is not a valid pair
                 */
                // print the output as below
                // pair found(8,2)
                System.out.printf("Pair found ( %d , %d )\n", num, pair);

                // remove the pair and the current number
                // from the map to avoid the same output with places shifted
                // e.g., if pair found(8,2) then to avoid pair found(2,8)
                map.remove(pair);
                map.remove(num);

                flag = 1; // to prevent unnecessary output
            }
            index++; // increment the index

        }

        if (flag == 0) //print if pair not found
            System.out.println("Pair not found");
    }

    //main function
    public static void main(String[] args) {

        // instantiate the object of PairsInArray
        // and call the faindPairOn method
        new PairsInArray().findPairOn();
        
    }
}
