#/bin/bash
#$1 is the first parameter being passed when calling the script. 
#foldername=$1
find ./data_kaggle_ng_no_uppercased -type f | xargs sed -i -e 's/[[:space:]][[:upper:]]\{2,\}[[:lower:]]*/ UPP/g'