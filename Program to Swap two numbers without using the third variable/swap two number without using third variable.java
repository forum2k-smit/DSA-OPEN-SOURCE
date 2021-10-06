import java.util.*; 
// Creating a class for swapping two number without using third variable
class Swap   
{  
    public static void main(String a[])   
    {   
        System.out.println("Enter the value of first number and second number ");  
        Scanner sc = new Scanner(System.in);  
        //Take 2 numbers as user input  
        int firstnum = sc.nextInt();  
        int secondnum = sc.nextInt(); 
        //printing numbers before swapping 
        System.out.println("before swapping numbers: "+firstnum +" "+ secondnum);  
       //Swapping logic  
        firstnum = firstnum + secondnum;   
        secondnum = firstnum - secondnum;   
        firstnum = firstnum - secondnum;  
        //printing numbers after swapping 
        System.out.println("After swapping: "+firstnum +"  " + secondnum);   
    }   
}  