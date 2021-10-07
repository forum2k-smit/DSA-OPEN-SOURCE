/* 

        AUTHOR : GAUTAM CHANDRA SAHA
        DATE & TIME: Thursday, 7th Oct at 11:29 am
*/

// initialize the numbers
var number1 = 10;
var number2 = 20;

//function to print a number
const print = (num, subs) => console.log(`num${subs}: ${num}`);

// function to print the numbers
const printNumbers = () => {
  print(number1, 1);
  print(number2, 2);
};

printNumbers(); //print original values of the numbers
console.log("\nAfter Swap\n");
[number1, number2] = [number2, number1]; //swap using destructuring assigment
printNumbers(); //print the swapped values of numbers
