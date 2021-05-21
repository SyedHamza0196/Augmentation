import os 

# Function to rename multiple files 
def main(): 
    for count, filename in enumerate(os.listdir("./gf_food/")): 
        dst ='000_' + str(count) + ".jpg"
        src = filename 
        # dst ='xyz' + dst 

        # rename() function will 
        # rename all the files 
        os.rename(src, './gf_food/'+dst) 

# Driver Code 
if __name__ == '__main__': 
    # Calling main() function 
    main() 