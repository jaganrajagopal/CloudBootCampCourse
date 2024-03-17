# #!bin/bash

# fruits=('apple' 'organe' 'pineapple')
# #olors=('red' 'green' 'blue')
# echo $fruits[0]
# echo $fruits[2]
# for mydata in "${fruits[@]}"; do
#     echo "$mydata"
# done

# Working with associative arrays
declare -A fruits
fruits[apple]='red'
fruits[banana]='yellow'
fruits[grape]='purple'

# Add a new key-value pair
fruits[orange]='orange'

# Access an element
echo "Apple is ${fruits[apple]}"

# # Iterate over keys
# for fruit in "${!fruits[@]}"; do
#     echo "$fruit is ${fruits[$fruit]}"
# done