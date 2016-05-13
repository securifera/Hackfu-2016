#theleastsignificantisthemostsignificant
#0x436 - next
data = open("image.bmp","rb").read()
c = data[0x436:]
newfile = ""
for i in range(len(c)/2):
  first  = ord(c[2*i])   & 0x3;
  second = ord(c[2*i+1]) & 0x3;
  result = (first << 4) + (second)
  newfile += chr(result)


f = open("layer2.img","wb")
f.write(data[:0x436])
f.write(newfile)
