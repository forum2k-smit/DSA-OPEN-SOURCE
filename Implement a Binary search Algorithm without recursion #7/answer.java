/**
    IMPLEMENTATION OF A BINARY SEARCH WITHOUT USING RECURSION

    WE WILL USE ITERATIVE APPROACH.
 */

import java.util.*;

public class Answer {

    public static int binarySearch(int[] arrayOfNums, int elementToSearch) {
        int low = 0;
        int high = arrayOfNums.length-1;
        int mid = low + (high-low)/2;

        while ( low <= high ) {
            if ( elementToSearch > arrayOfNums[mid] )
                low = mid+1;
            
            else if ( elementToSearch == arrayOfNums[mid] ) 
                return mid;
            
            else
                high = mid-1;
            
            mid = high + (high-low)/2;
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in); // Creating Scanner Object to take input from User.
        
        System.out.println("Enter the size of the array: ");
        int arraySize = scn.nextInt(); //  Take input for the Size of the array.
        
        int [] arrayOfNums = new int[arraySize]; //Creating new Array "arrayOfNums" of size "arraySize".

        System.out.println("Enter elements: ");
        for ( int i = 0; i != arrayOfNums.length; i++ )  // Inserting Values into arrayOfNums.
            arrayOfNums[i] = scn.nextInt();              // Note: Values should be in either Ascending or Descending Order.

        System.out.println("Now enter element to search: "); 
        int elementToSearch = scn.nextInt();  

        int index = binarySearch(arrayOfNums, elementToSearch);

        if ( index == -1 )
            System.out.println(elementToSearch + " is not present in the given array!");
        else
            System.out.println(elementToSearch + " is found at index: " + index);
        
    }
}