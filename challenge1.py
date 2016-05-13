#!/usr/bin/python
from os import listdir
from os.path import isfile, join

book_path = "./Books"
onlyfiles = [f for f in listdir(book_path) if isfile(join(book_path, f))]

tuples = [ (85,8),
(124,11),
(1984,8),
(3,5),
(901,1),
(3,13),
(8546,12),
(5,2),
(3,4),
(85,10),
(3437,7) ]

for file_name in onlyfiles:
   f = open( book_path + "/" + file_name, "r")
   data = f.readlines()
   try:
      if len(data) > 8548 :
	 out_str = ''
	 for loc in tuples:
	    start = loc[0]
	    str_len = loc[1]
	    #print "Start: " + str(start)
	    #print "Len: " + str(str_len)
	    line = data[start-1]
	    #print "Current line: " + line
	    words = line.split(" ")
	    word = words[str_len-1].strip()
	    #print "Word: " + word
	    #print clip
	    out_str += word
	    
	 print "Opening: " + file_name
	 print "Phrase: " + out_str + "\n"
   except:
      pass
   
   f.close()
   