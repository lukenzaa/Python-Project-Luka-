n = int(input())

# dictionary to store word counts
word_counts = {}

for i in range(n):
    word = input().strip()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(len(word_counts))
for word in word_counts:
    print(word_counts[word], end=' ')
print()








    
    
    

    
    
   






        
        
    
        

        
        
    
        
    
   







