/*
Algorithm 
STEP 1: START
STEP 2: ENTER A, B
STEP 3: PRINT A, B
STEP 4: A = A + B
STEP 5: B= A - B
STEP 6: A =A - B
STEP 7: PRINT A, B
STEP 8: END 

Code Ide Platform:- https://replit.com/@devbot1/ReflectingLastRecursion#main.dart
*/
import 'dart:io';
void main()
{
  //Decleartion
  int  firstvar=0;
  int  secondvar=0;
  //First Num Input
  print("Enter the first number : ");
  firstvar = int.parse(stdin.readLineSync());
  //Second Num Input
  print("Enter the Second number : ");
  secondvar = int.parse(stdin.readLineSync());
  //Logic Part
  firstvar=firstvar+secondvar;
  secondvar=firstvar-secondvar;
  firstvar=firstvar-secondvar;
  //Screen Output
  print("First Number After Swap :$firstvar");
  print("Second Number After Swap :$secondvar");
  
}