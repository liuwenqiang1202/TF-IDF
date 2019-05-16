import jieba  
import jieba.analyse
from optparse import OptionParser
  
sentence = '冰，水为之，而寒于水'
tags = jieba.analyse.extract_tags(sentence, topK=3, withWeight=True, allowPOS=())

for item in tags:
    print(item[0],item[1])