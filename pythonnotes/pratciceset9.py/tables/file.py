for i in range(2,21):
     with open(f"tables/Multiplication tables of {i}",'w') as f:
         for j in range (1,11):
            f.write(f"{i} x {j} = {i*j}\n")
            if j!=10:
                print("\n")
         break # if we dont add the break statement all the table from 2-20 will be created in the tables folder
        
         