# Each name in a list is assigned a score based on 
# the sum of the letters in the name where each
# letter is worth it's position in the alphabet in
# points, i.e. 'COLIN' is assigned
# the score of 3 + 15 + 12 + 9 + 14 = 53
# Find the sum of scores for all names in the file names.txt


import pandas as pd
import string

f = open("names.txt", 'r')
names = sorted(f.read().replace('"','').split(','), key=str)
total_score = 0

alpha = string.ascii_lowercase.upper()
alpha_scores = dict(list(enumerate(alpha)))
alpha_scores = {k: j for j, k in alpha_scores.items()}

for i in alpha_scores:
    alpha_scores[i] += 1
    

def letter_score(name):
    
    scr = 0
    name_len = len(name)
    
    for i in range(name_len):
        scr += alpha_scores[name[i]]
        
    return scr
  
def name_score(name, index):
    
    return index * letter_score(name)
  


for i, j in enumerate(names):
    
    total_score += name_score(j, i+1)

print(total_score)
