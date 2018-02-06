#/bin/bash
#$1 is the first parameter being passed when calling the script. 
#foldername=$1
find ./data_kaggle -type f | xargs sed -i -e 's/[[:space:]]offset[[:space:]]/ /g'