#Write a function code to find total count of word little in the given string: 

text = 'Mary had a little lamb Little lamb, little lamb Mary had a little lamb. Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go.'

def wordCount(str):
    words = str.split()
    freq = {}
    
    for key in words:
        freq[key] = words.count(key)

    print(f"The frequency of each words are {freq}.")

    for k, v in freq.items():
        if k == 'little':
            return(f"Frequency of word {k} is {v}")
        
x = wordCount(text)
print(x)