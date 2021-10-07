/* 

        AUTHOR : GAUTAM CHANDRA SAHA
        DATE & TIME: Thursday, 7th Oct at 12:05 pm
*/

// initialize the numbers
var number1 = 10;
var number2 = 20;

//function to print a number
function print(num: number, subs: number) {
  console.log(`num${subs}: ${num}`);
}

// function to print the numbers
function printNumbersAgain() {
  print(number1, 1);
  print(number2, 2);
}

printNumbersAgain(); //print original values of the numbers
console.log("\nAfter Swap\n");
[number1, number2] = [number2, number1]; //swap using destructuring assigment
printNumbersAgain(); //print the swapped values of numbers
