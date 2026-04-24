'''
Let's consider a real-life scenario where you are analyzing customer feedback for a product. You have a large data set of customer reviews in the form of strings, and you want to extract useful information from them using the three identified tasks:
Task 1. String in lowercase: You want to pre-process the customer feedback by converting all the text to lowercase. This step helps standardize the text. Lower casing the text allows you to focus on the content rather than the specific letter casing.

Task 2. Frequency of all words in a given string: After converting the text to lowercase, you want to determine the frequency of each word in the customer feedback. This information will help you identify which words are used more frequently, indicating the key aspects 
or topics that customers are mentioning in their reviews. By analyzing the word frequencies, you can gain insights into the most common issues raised by customers.

Task 3. Frequency of a specific word: In addition to analyzing the overall word frequencies, you want to specifically track the frequency of a particular word that is relevant to your analysis. For example, you might be interested in monitoring how often the word 
"reliable" appears in customer reviews to gauge customer sentiment about the product's reliability. By focusing on the frequency of a specific word, you can gain a deeper understanding of customer opinions or preferences related to that particular aspect.
By performing these tasks on the customer feedback dataset, you can gain valuable insights into customer sentiment
'''

txt = 'Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.'
class textAnalyser():
    def __init__(self, text):
        self.fmtdtext = text
        print(self.fmtdtext)
    def lowerWord(self, text):
        formattedtext = text.lower()
        for letter in formattedtext:
            if letter in '.?,!':
                formattedtext = formattedtext.replace(letter, ' ')
        return formattedtext
    def wordFreq(self, t):
        freq = {}
        for word in t.split():
            freq[word] = t.count(word)
        return(freq)
    def sentimentFreq(self, word):
        fre = self.wordFreq(self.lowerWord(txt))
        if word in fre.keys():
            return('Relevant feedback.')
        else:
            return('Wrong feedback.')
        
x = textAnalyser(txt)
print(x)
y = x.lowerWord(txt)
print(y)
print(x.wordFreq(y))
print(x.sentimentFreq('lorem'))
#x.wordFreq()
#print(x.sentFreq('lorem'))
