# __*__ coding:utf-8 __*__

data = []

grade=90
if grade<60 and grade>0:
	print '不及格'
elif grade<70 and grade>=60:
	print '差'
elif grade<80 and grade>=70:
	print '良好'
elif grade<90 and grade>=80:
	print '优秀'
elif grade<100 and grade>=90:
	print 'perfect'
elif grade==100 :
	print '满分'
else :
	print '零分'

class Word:
	def __init__(self, word):
		self.word = word
	def equals(self, word2):
		return word2.lower() == self.word.lower()

first = "dai"
second = Word("Dai")
print second.equals(first)


class Word:
	def __init__(self, word):
		self.word = word
	def __eq__(self, word2):
		return word2.lower() == self.word.lower()

print "dai" == Word("Dai")
print len("dai")

class Bill:
    def __init__(self, desc):
        self.desc = desc

class Bill:
    def __init__(self, desc):
        self.len = desc
