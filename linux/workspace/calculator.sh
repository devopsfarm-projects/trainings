#!/bin/bash

# I need to create add substract multiply and divide operations
read_numbers(){
    read -p "Number1 : " num1
    read -p "Number2 : " num2
}

add(){
    result=0
    for num in $@; do
        result=$(expr $result + $num)
    done

    echo $result
}

mul(){
    result=1
    for num in $@; do
        result=$(( result * num ))
    done

    echo $result
}

add 1 2 3 4 5 6 7 8 9
mul 1 2 3 4 5 6 7 8 9


echo "What do you want me to do ?(one of 'add' 'sub' 'mul' and 'div')."
read OP

if  [ "$OP" == "add" ]; then
    echo "Adding numbers"
    read_numbers
    echo Sum is `add $num1 $num2`
elif [ "$OP" == "sub" ]; then
echo "Subtracing numbers"
    read_numbers
    echo Substraction is `expr $num1 - $num2`
elif [ "$OP" == "mul" ]; then
echo "Multiplying numbers"
    read_numbers
    echo Multiplication is `expr $num1 * $num2`
elif [ "$OP" == "div" ]; then
echo "Dividing numbers"
    read_numbers
    echo Division is `expr $num1 / $num2`
else
    echo "Wrong operation selection"
fi

 