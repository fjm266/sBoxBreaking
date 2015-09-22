import codecs

f = open('simple.file', 'a')

cp = codecs.encode("print 'we good'", 'punycode')
print cp
f.write(cp)
