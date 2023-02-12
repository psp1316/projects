sum=0
f=open("bill.txt","w")
f.write("              THANKYOU SO MUCH                        \n")
f.close() 
while(True):
    a=input("enter the prices\n")
    
    if(a!="q"):
     sum=sum+int(a)
     f=open("bill.txt","a")
     f.write(f"price is {a}\n")
     f.close() 
     
    else:
        f=open("bill.txt","a")
        f.write(f"total sum is {sum}")
        f.close()
        
        
        print("thanks for using our calculator\n your total sum is",sum)
       
   

  
    

     




    



