#!/bin/bash

# While loop example
count=5
while [ $count -gt 0 ]; do
    echo "Countdown: $count"
    ((count--))
done

# ! bin/bash
# count=1
# while [ $count -gt 0 ]; do
#     echo "Countdown: $count"
#     ((count++))
# done     