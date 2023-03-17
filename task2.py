def biggerIsGreater(w):
    n = len(w)
    pivot = n - 2
    while pivot >= 0 and w[pivot] >= w[pivot + 1]:
        pivot -= 1
    if pivot < 0:
        return "no answer"
    successor = n - 1
    while successor > pivot and w[successor] <= w[pivot]:
        successor -= 1
    w = list(w)
    w[pivot], w[successor] = w[successor], w[pivot]
    w[pivot + 1:] = sorted(w[pivot + 1:])
    return ''.join(w)
T = int(input())
words = []

for I in range (T):
  word = input().strip()
  words.append(word)
for word in words:
  print(biggerIsGreater(word))









    
    
    

    
    
   






        
        
    
        

        
        
    
        
    
   







