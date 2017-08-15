#Coded By The M4d Sc13nT15t
#Can You Hear Those Voices?
#Look Into My Eyes Can You See The Pain
#The Chaos I Bring, Youll Never Forget My Name
#The Troubles, The Pain, The Panic, The Fear
#Im Not Santa, But Ill Be Around All Year

import requests
myheaders={'user-agent' : 'Iphone 6'}
r = requests.get('http://www.skriptkiddie.com/headers', headers=myheaders)

print r.url

print 'Status code:'

print '\t[-]' + str(r.status_code) + '\n'

print 'Server headers'

print '#######################################'

for x in r.headers:

 print '\t' + x  + r.headers[x]

 print '#######################################\n'


 print "Content:\n"
print r.text
