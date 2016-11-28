color= ['Blue' , 'Red', 'Black', 'Pink','Brown', 'Yellow']
print ("Trang's color list\n", color)

print("color_list at index 3: ",color[3])

##number = int(input("Enter a numberfrom 0-5: "))
##print("Your color: ", color[number])

##print(color)
##for i in range(6):
##    print(color[i])

guest_color= str(input("What is your favorite color?(enter red for red color and so on!"))
lowercase_of_colorlist = []
for i in range(6):
    lowercase_of_colorlist.append(color[i].lower())
for i in range(6): 
     if guest_color == lowercase_of_colorlist[i] or guest_color == color[i]:
          print(i)
          break
     elif i >= 5:
          print("Sorry! We don't find your color in the list.")
   
            

           
    
       

     
