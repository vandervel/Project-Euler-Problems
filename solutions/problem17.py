# Number of letters in the words of the numbers one through one thousand.


total = 0

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
                  'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
thousand = 'one thousand'


for t in tens:
    
    words.append(t)
    for i in range(0, 9):
        
        words.append(str(t + words[i]))   

for j in range(0, 9):
    
    words.append(str(words[j] + 'hundred'))
    for k in range(0, 99):
        words.append(str(words[j] + 'hundredand' + words[k]))
        


words.append('onethousand')

for i in words:
    total += len(i)
    
print(total)
