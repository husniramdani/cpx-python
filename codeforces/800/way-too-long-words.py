for i in range(int(input())): #langsung ambil input dan jadikan range
    word=input() #input string
    panjang=len(word) #panjang kata
    print(word if panjang <= 10 else word[0] + str(panjang-2) + word[panjang-1])