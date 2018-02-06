#/bin/bash
#$1 is the first parameter being passed when calling the script. 
#foldername=$1
find ./data_kaggle_ng_no_long -type f | xargs sed -i -e 's/[[:space:]]\S\{8,15\}\s/ subs8 /g;s/[[:space:]]\S\{16,25\}\s/ subs16 /g;s/[[:space:]]\S\{26,35\}\s/ subs26 /g;s/[[:space:]]\S\{36,\}/ sub36/g'