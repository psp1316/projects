def details():
    a=input("enter patient name: ")
    b=input("enter patient mobile number: ")
    c=input("enter unique code")
    d=(b+a+c)
    with open("patient.txt","w") as f:
            f.write(d )

def codecheck():
    
    with open('patient.txt') as file:
          contents = file.read()
    search_word = input("enter a word you want to search in file: ")
    if search_word in contents:
        print ('word found')
    else:
        print ('word not found')

d=input('''select any one!!
1)Patient details entry
2)promo code checker
''')
if(d=="1"):
    details()
else:
    codecheck()








