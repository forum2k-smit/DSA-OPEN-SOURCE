// Not using node.js, so, it is not possible for viewing output in terminal. Please view the output in the browser console.

// We create an array of numbers
const arrayToBeSearched = [3, 4, 7, 5, 11, 6, 13];
//we are not looping and taking in inputs from the user as we are not using node, because of which input from terminal can't be taken.

// We create a function for the Linear Search Algorithm
const linearSearch = (array, num) => {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === num) {
      return i;
    }
  }
  return -1;
};

linearSearch(numbers, 7); //we call the function with the array and the number we want to search (7 in this case). It will return the index, ie, 2.
linearSearch(numbers, 20); //we call the function with the array and the number we want to search (20 in this case). Since this number isn't present, we return -1.
