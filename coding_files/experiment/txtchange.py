text = 'Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.'

formattedtext = text.lower()
for letter in formattedtext:
    if letter in '.?,!':
        formattedtext = formattedtext.replace(letter, ' ')
print(formattedtext)   
  