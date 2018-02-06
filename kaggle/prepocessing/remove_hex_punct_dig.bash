#/bin/bash
#$1 is the first parameter being passed when calling the script. 
#foldername=$1
find ./train_3025_12_hex_punct_dig -type f | xargs sed -i -e 's/\bd[dwb]\b/ datDecl /gi' -e 's/\be[abcd]x\b/ regEX /gi' -e 's/\b[[:xdigit:]]*\b/ /g'  -e 's/_[[:xdigit:]]*\b/ /g'  -e 's/[+*\/-]/ op /g' -e 's/[[:punct:]]//g' -e 's/[[:digit:]]h*//g'