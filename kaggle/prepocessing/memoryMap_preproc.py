import pandas as pd
from os import listdir
from os.path import isfile, join, splitext
from sklearn.model_selection import train_test_split
from shutil import copyfile
from sklearn.feature_extraction.text import CountVectorizer
import time
import csv
import os
import contextlib
import mmap

# Build regular expression for ngrams "redaction"
def getRegExStr():
    # Path to file containg most popular ngrams. File below is just for the demo.
    pathDict = "./ngram_dict.txt"

    df_dict = pd.read_csv(pathDict, names = ["n", "ngrams"])
    df_dict = df_dict.drop('n', 1)
    x = pd.core.strings.str_strip(df_dict["ngrams"])
    ngrams_dict = dict((x[i],x[i]) for i in range(0, len(x)))
    for i in range(len(x)):
        print(i, x[i])
        print(bytes(x[i], encoding='utf-8'))
    ngrams_dict_result = dict((x[i], bytes(x[i], encoding='utf-8')) for i in range(0, len(x)))

    reg = r'\w*(' + '|'.join(ngrams_dict.keys()) + r')\w*'
    return reg, ngrams_dict_result

def replace_with_MMAP(pathFile, pathResFile):
    regstr, ngrams_dict =  getRegExStr()
    pattern = re.compile(bytes(regstr, encoding='utf-8'), re.IGNORECASE)
    offset = max(0, os.stat(pathFile).st_size - 15000)
    print("offset: ", offset)
    start_time = time.time()
    with open(pathFile, 'r') as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)) as txt:
            result = pattern.sub(lambda x: ngrams_dict[bytes.decode(x.group(1)).lower()], txt)
            print("Done parsing, wriring now to {0}..... Elapsed secs: {1} ".format(pathResFile, time.time() - start_time))
            with open(pathResFile, 'w') as f:
                f.write(bytes.decode(result))


#Note: change file paths below appropiately
pathFile = "./data_kaggle/Malware_class1.txt"
pathResFile =  "./data_kaggle/Malware_class1_ng.txt"
replace_with_MMAP(pathFile, pathResFile)

pathFile = "./data_kaggle/Malware_class2.txt"
pathResFile =  "./data_kaggle/Malware_class2_ng.txt"
replace_with_MMAP(pathFile, pathResFile)


