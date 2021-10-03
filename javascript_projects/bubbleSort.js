/* 
        AUTHOR : GAUTAM CHANDRA SAHA
        DATE & TIME: MONDAY 4 OCT, 2021 AT 9:00 AM
*/

class BubbleSort {
  arr = [2, -3, 1, 4, 6, 86, 0]; //array to be sorted

  //function to swap two numbers
  swap(x, y) {
    //   using destructuring assignment to swap variables
    [this.arr[x], this.arr[y]] = [this.arr[y], this.arr[x]];
  }

  //funciton to sort the array using bubble sort
  bubbleSort() {
    const { length } = this.arr;
    //first loop for iteration
    for (let i = 0; i < length - 1; i++) {
      //second loop for comparison to sort the array
      for (let j = 0; j < length - i - 1; j++)
        if (this.arr[j] > this.arr[j + 1]) this.swap(j, j + 1); //call swap function
    }
  }
}
function main() {
  const sorter = new BubbleSort(); // instantiates the BubbleSort object
  sorter.bubbleSort(); //call the sort method
  console.log(sorter.arr); //log the sorted array
}

main(); // calls the main function
