def test1(*args):
    #tokno in not number for no in len(tokkyo)
   print "hairetusu = ",len(tokkyo)
   for tokno in range(len(tokkyo)):
         for housiki in args:
             if housiki == tokkyo[1]:
                  #print "same"
                 #print str(tokkyo[0]) +" "+ str(tokkyo[1])
                  print tokkyo[tokno]
             #print ""
kahiki = []
kahiki.append('MC1')
kahiki.append('MC2')
kahiki.append('MC3')

tokkyo = []

tokkyo = [9876543, 'MC1','MC2','MC3']


test1(*kahiki)

kahiki = []
kahiki.append('QCM')

tokkyo =[1234567,'QCM']
test1(*kahiki)
