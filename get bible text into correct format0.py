#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-info">
# This notebook can be used to transform the given bible text at https://raw.githubusercontent.com/christos-c/bible-corpus/master/bibles/English.xml into single chapters
# <div>

# In[11]:


f=open("bible_text.txt", "r")
bible_content = f.read()
#print(bible_content)
print(len(bible_content))
import re
#1. Split everywhere where the hint to a chapter section can be found:
split = re.split('type="chapter">', bible_content)

i =1
for s in split[1:3]:
    print('THIS IS ENTRY nr. '+ str(i))
    #see what the result of splitting looks like:
    #print(s)
    #print('\n \n')
    i+=1

#splitting as in step 1. is not enough;
#2. all xml-tags should be removed:
single_chapters = []
for s in split:
    clean_chapter_text = re.sub('<[^<]+?>','',s)
#3. remove all the extra lines \n:
#               and tab stops  \t:
    rem_n = re.sub('\n','',clean_chapter_text)
    rem_t = re.sub('\t','',rem_n)
    rem_div = re.sub('<.*$','', rem_t)
    single_chapters.append([rem_div])

print(len(single_chapters))
k=0

#print the first 10 chapters to see if it looks plausible
for chapter in single_chapters[0:10]:
    print('CHAPTER nr. '+str(k))
    print(chapter)
    print('\n \n')
    k+=1
#4. write the result into a new txt-file:
with open('bible.txt', 'w') as f:
    for chapter in single_chapters:
        f.write("%s\n" % chapter)
f.close()


# In[ ]:
