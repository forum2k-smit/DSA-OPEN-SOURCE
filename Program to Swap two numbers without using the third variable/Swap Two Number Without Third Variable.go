package main

/*

   AUTHOR : GAUTAM CHANDRA SAHA
   DATE & TIME: Thursday, 7th Oct at 1:30 pm
*/
import "fmt" //import fmt

//global vars
var num1 = 10
var num2 = 20

//function to print a number
func print(num int, subs int) {
	str := fmt.Sprintf("num%d %d", subs, num)
	fmt.Println(str)
}

//function to print the numbers
func printNumbers() {
	print(num1, 1)
	print(num2, 2)
}

//function main
func main() {
	printNumbers()          //print numbers before swap
	num1, num2 = num2, num1 //swap numbers
	fmt.Print("\nAfter Swap\n\n")
	printNumbers() //print numbers after swap
}
