text = 'Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.'

for i in text:
            if i in '.?!,':
                formattedtext = text.replace(i, '').lower()
print(formattedtext)                