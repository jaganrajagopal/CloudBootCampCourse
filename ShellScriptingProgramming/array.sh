#! bin/bash
NAME[0]="Ram"
NAME[1]="kiran"
NAME[2]="Sita"
NAME[3]="Hari"
NAME[4]="siva"
echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"
echo "Second Index: ${NAME[-1]}"
#Name=('ram' kiran site )

for mydata in "${NAME[@]}"; do 
    echo "name: $mydata "
done    

# for mydata in "${fruits[@]}"; do
# #     echo "$mydata"
# # done