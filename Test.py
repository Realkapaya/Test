
#Skapa en sträng med flera ord
words = "Hejsan svejsan mamma mia pappa pia tia"
words_string = words.split()
words_other = ""

#Skriv ut vartannat ord
for words in range(0,len(words_string),2):
    words_other += words_string[words] + " "
print(words_other)

words_other_back =""
#Skiv ut meningen ord för ord i omvänd ordning
for words in range(len(words_string)-1,-1,-1):
    words_other_back += words_string[words] + " "
print(words_other_back)



"""
my_string = "Här är några ord"
str_split = my_string.split()

index = 0

while index < len(str_split):
    print(str_split[index])
    index += 2
"""

"""
my_string = "Här är några ord yo"
str_split = my_string.split()

# Börja med sista ordet
index = len(str_split) - 1 #Måste börja på slutet. Kom ihåg att kod börjar på 0 och inte 1, så plats 4 är egentligen 3

# Skriv ut orden i omvänd ordning

while index >= 0:
    print(str_split[index])
    index -= 1
"""   

"""
import random

num_one = int(input("Skriv ett tal: "))
num_two = int(input("Skriv ett till tal: "))

if num_one > num_two:
    random_number = random.randint(num_two,num_one)      #Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
else:
    random_number = random.randint(num_one,num_two)
    
print("Slumpad siffra: ", random_number)
"""

#Slumpa fram ett nummer mellan 1-10
import random

num_rng = random.randint(1, 10)
print(num_rng)

# Be användaren skriva ett tal
num_user = int(input("Skriv in ett tal: "))
chances = 0

# Skriv ut om gissningen är rätt eller fel
while num_rng != num_user:
    print("Inkorrekt, försök igen!")
    chances += 1
    num_user = int(input("Skriv in ett tal: "))
# Låt använadren gissa tre gånger    
    if chances == 2 and num_rng != num_user:
        print("Tyvärr! Bättre lycka nästa gång!")
        break
    elif chances > 2:
        print("Tyvärr! Försök igen!")
        num_user = int(input("Skriv in ett tal: "))
    
if num_rng == num_user:
    print("Korrekt!")    





