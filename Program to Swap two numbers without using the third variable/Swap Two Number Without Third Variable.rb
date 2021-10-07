"""

   AUTHOR : GAUTAM CHANDRA SAHA
   DATE & TIME: Thursday, 7th Oct at 1:40 pm
"""

# global variable
$num1=10
$num2=20

# function ot print a number
def print(num,subs)
    puts "num#{subs} = #{num}"
end

# function to print numbers
def printNumbers()
    print($num1,1)
    print($num2,2)
end

# function main
def main()
    printNumbers # print numbers before swap
    puts "\nAfter Swap\n\n"
    $num1,$num2 =$num2,$num1 # swap numbers
    printNumbers # print numbers after swap
end

main #call main