# These classes are used to analyze commonalities between sentences and entire speeches.
# They will be implemented to return the commonalities of a particular speaker. 
# For example: the length of sentences in Obama's speeches, how many words he uses
# the most common words he uses, etc.
#

import re
from operator import itemgetter


class FileContextManager():
        def __init__(self, file_name):
            self._file_name = file_name
            self._file = None

        def __enter__(self):
            self._file = open(self._file_name)
            return self._file

        def __exit__(self, cls, value, tb):
            self._file.close()


class Sentence(object):
	def __init__(self, number, sentence):
		self.sentence = sentence
		self.number = number
		self.keyword_dict = {}
		self.getKeywords()
		
	def getKeywords(self):
		for words in self.sentence.split():
			word = words.strip('.').strip('!').strip('?').strip(',')
			try:
				self.keyword_dict[word]
			except:
				self.keyword_dict[word] = 1
			else:
				self.keyword_dict[word] += 1
				
	def Return_Sorted_Keywords(self,num):
		keyword_list = sorted(self.keyword_dict.items(), key=itemgetter(1), reverse=True)
		return keyword_list[0:num]


class Speech(object):
	def __init__(self, file_name):
		self.loc_and_sentence = {}
		self.length = 0
		self.keyword_dict = {}
		self.avg = 0
		self.compounds = 0
		self.syllables_per_word = 0
		self.syllables_per_sentence = 0
		self.Get_Sentences(file_name)
		self.Get_Keywords()
		self.Get_Compound_sentence_Count(file_name)
		self.Get_syllables()

	def Get_Sentences(self, speech_file_name):
		with FileContextManager(speech_file_name) as f:
			speech = f.read()
        	count = 1
        	for sent in speech.split('.'):
        		self.loc_and_sentence[count] = sent
        		count +=1
        	return
        	
	def Get_Keywords(self):
		avg_len = 0
		total_to_divide = 0
		for num in range(1,len(self.loc_and_sentence)):
			temp = Sentence(num,self.loc_and_sentence[num])
			for k,v in temp.keyword_dict.items():
				self.keyword_dict[k] = v
	
	def Return_Sorted_Keywords(self,num):
		keyword_list = sorted(self.keyword_dict.items(), key=itemgetter(1), reverse=True)
		return keyword_list[0:num]
	
	def Get_avg_Len(self):
		all_len = 0
		tot = 0
		for sent in self.loc_and_sentence.values():
			all_len += len(sent.split())
			tot += 1
		avg = all_len/tot
		self.avg = avg
		return avg
		
	def Get_Compound_sentence_Count(self, speech_file_name):
		with FileContextManager(speech_file_name) as f:
			speech = f.read()
        	count = 1
        	compounds = re.findall(r',.*?\.',speech, flags=re.DOTALL)
        	self.compounds = len(compounds)

	def Get_syllables(self):
		syls = 0
		count = 0
		syls2 = 0
		count2 = 0
		for sentence in self.loc_and_sentence.values():
			syls += Return_Syllable_Count(sentence)
			for word in sentence.split():
				syls2 += Return_Syllable_Count(word)
				count2 +=1
			count += 1
		syls_p_sent = syls/count
		syls_p_word
		self.syllables_per_sentence = syls_p_sent
		self.syllables_per_word = syls_p_word
		
		
def Return_Syllable_Count(text):
  # Place holder return.  Put new code here.
	return 10
	
		

speech1 = Speech('shorttest.txt')



class Speaker(object):
	def __init__(self,name):
		self.name = name
		self.keyword_totals = {}
		self.avg_len = 0
		
		
	def Load_Speeches(self, dir_name):
		pass
		#Implement code that opens and analyzes all speeches from a speaker folder
		#For example: user/.../Obama/bunch_of_txt_files_to_open
            	

	
