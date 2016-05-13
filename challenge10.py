#! /usr/bin/env python
from curses.ascii import islower

def score(input_arr):
  freq = dict()
  freq['a']=834
  freq['b']=154
  freq['c']=273
  freq['d']=414
  freq['e']=1260
  freq['f']=203
  freq['g']=192
  freq['h']=611
  freq['i']=671
  freq['j']=23
  freq['k']=87
  freq['l']=424
  freq['m']=253
  freq['n']=680
  freq['o']=770
  freq['p']=166
  freq['q']=9
  freq['r']=568
  freq['s']=611
  freq['t']=937
  freq['u']=285
  freq['v']=106
  freq['w']=234
  freq['x']=20
  freq['y']=204
  freq['z']=6
  freq[' ']=2320

  score_arr = []
  for cand in input_arr:
    ret = 0
    for c in cand[1].lower():
      if c in freq:
	ret += freq[c]
	
    score_arr.append([cand,ret])    
    
  return score_arr

#Find the best ranked candidates
def find_best_cands( column_cands ):
  
  #start on first column
  best_cands = []
  if(len(column_cands) < 4):
    return None
  
  first_col = column_cands[0]
  second_col = column_cands[1]
  third_col = column_cands[2]
  fourth_col = column_cands[3]
  fifth_col = column_cands[4]
  six_col = column_cands[5]
  
  rows1 = len(first_col)
  rows2 = len(second_col)
  rows3 = len(third_col)
  rows4 = len(fourth_col)
  rows5 = len(fifth_col)
  rows6 = len(six_col)
  
  ret = []
  for row in range(rows1):
    cand = first_col[row]
    letters1 = cand[0][1]
    
    for row2 in range(rows2):
      cand2 = second_col[row2]
      letters2 = cand2[0][1]
      
      for row3 in range(rows3):
	cand3 = third_col[row3]
	letters3 = cand3[0][1]
	
	for row4 in range(rows4):
	  cand4 = fourth_col[row4]
	  letters4 = cand4[0][1]
	  
	  for row5 in range(rows5):
	    cand5 = fifth_col[row5]
	    letters5 = cand5[0][1]
	    
	    for row6 in range(rows6):
	      cand6 = six_col[row6]
	      letters6 = cand6[0][1]
	      
	      chunks = []
              for i in range(0,2):
		chunks.append("%c%c%c%c%c%c" % ( letters1[i],letters2[i],letters3[i], letters4[i], letters5[i],letters6[i] ))
		chunks.append("%c%c%c%c%c"% ( letters1[2],letters2[2],letters3[2], letters4[2], letters5[2] ))
		key =  "Key: %c%c%c%c%c%c" % ( cand[0][0],cand2[0][0],cand3[0][0], cand4[0][0], cand5[0][0],cand6[0][0] )
		rank = cand[1] + cand2[1] + cand3[1] + cand4[1] + cand5[1] + cand6[1] 
		ret.append([rank, key, chunks])
      
  return ret

#Create pools
def create_pool( column ):
  
  ret = []
  for j in range(256):
    cand = ''
    for i in column:
      val = chr((ord(i)^j) & 0xff)
      c = filter(islower,val)
      if c:
	cand += c
      else:
	break
    
    #Make sure all characters have been added
    if len(cand) == len(column):
      ret.append([chr(j),cand])
      
  #print "Total candidates: ", len(ret)
  #print ret
  return ret
    

tolerance = 10

data = ""
filename = 'input'
data = open(filename, 'rb').read()

KEYSIZE = 16
print "[#] KEYSIZE = " + str(KEYSIZE)

split_data = [data[i::KEYSIZE] for i in range(KEYSIZE)]
print "Split into %d chunks." % len(split_data)

column_cands = []

pool = create_pool(split_data[0])
scores = score(pool)
sorted_scores = sorted(scores, key=lambda entry: entry[1])
keepers = sorted_scores[-8:]
column_cands.append(keepers)
#print keepers

pool = create_pool(split_data[1])
scores = score(pool)
sorted_scores = sorted(scores, key=lambda entry: entry[1])
keepers = sorted_scores[-8:]
column_cands.append(keepers)
#print keepers

pool = create_pool(split_data[2])
scores = score(pool)
sorted_scores = sorted(scores, key=lambda entry: entry[1])
keepers = sorted_scores[-8:]
column_cands.append(keepers)
#print keepers

pool = create_pool(split_data[3])
scores = score(pool)
sorted_scores = sorted(scores, key=lambda entry: entry[1])
keepers = sorted_scores[-8:]
column_cands.append(keepers)
#print keepers

pool = create_pool(split_data[4])
scores = score(pool)
sorted_scores = sorted(scores, key=lambda entry: entry[1])
keepers = sorted_scores[-8:]
column_cands.append(keepers)

pool = create_pool(split_data[5])
scores = score(pool)
sorted_scores = sorted(scores, key=lambda entry: entry[1])
keepers = sorted_scores[-8:]
column_cands.append(keepers)

#print all combinations
#print column_cands
cands = find_best_cands(column_cands)
sorted_cands = sorted(cands, key=lambda entry: entry[0])
#keepers = sorted_cands[-20:]

#print sorted_cands
for i in sorted_cands:
  print i
  
