def reverse(s):
    return s[::-1]

def identify_a_and_A(s):
    counter_a=0
    counter_A=0
    for i in s:
        if i=='a':
            counter_a+=1
        elif i=='A':
            counter_A+=1
        
    return " Existem ", counter_a, 'a e', counter_A, 'A' 

def vowels(s):
    vowels_list=['a','e','i','o','u','A','E','I','O','U']
    list=[vowel for vowel in s if vowel in vowels_list]
    return len(list)

def lower(s):
    return s.lower()

def upper(s):
    return s.upper()

def capicua(s):
    d=s.lower()
    if d[::-1]==d:
        i=True
    else:
        i=False
    return i

def balanco(s1,s2):
    i=True
    a1 = s1.replace(" ", "")
    a2 = s2.replace(" ", "")
    not_balanco1=[b for b in a2 if b not in a1]
    not_balanco2=[c for c in a1 if c not in a2]
    if len(not_balanco1)!=0:
        i=False 
        print('caracter(es): ', not_balanco1, 'não encontrado(s)')
    elif len(not_balanco2)!=0:
        i=False
        print('caracter(es): ', not_balanco2, 'não encontrado(s)')
    return i

def ocorrencias(s1,s2):
    counter=0
    for i in range(len(s2)-len(s1)+1):
        if s2[i:i+len(s1)]==s1:
            counter+=1
    return counter


def anagrama(s1, s2):
    a1=s1.lower()
    a2=s2.lower()
    return sorted(a1) == sorted(a2)




def classes_anagrama(dic):
    classes = {}
    
    for palavra in dic:
        chave = "".join(sorted(palavra))  
        if chave in classes:
            classes[chave].append(palavra)
        else:
            classes[chave] = [palavra]
    
    return classes


print(reverse('leonor'))
print(identify_a_and_A('Amoras e bananas'))
print(vowels('Amoras e bananas'))
print(lower('YOUR VOICE'))
print(upper('case'))
print(capicua('Ana'))
print(capicua('Jacinta'))
print(balanco('espana', 'spanaa'))
print(balanco('banana', 'ba nnnaaaaa nnnaaa'))
print(ocorrencias('na', 'banana'))
print(anagrama('amora', 'aroma'))
print(anagrama('tolo', 'lota'))
dic = ["pato", "topa", "pota", "gato", "toga", "otap"]
for chave, palavras in classes_anagrama(dic).items():
    print(f"Classe {chave}: {palavras}")