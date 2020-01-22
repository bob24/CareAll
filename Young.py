
f=open("Post_File_After_ElderClass_Firsttime", "r")
contents =f.readlines()



class Young:
 
    def __init__(self, name,age):
        
        self.name = name # Create an instance variable 
        self.age = age
 
    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        
        return 'person{} with age {}'.format(self.name,self.age)
 

 
    def select(self,select_row):
        
        self.select_row = select_row
        if self.select_row == 1:
            x = contents[0].split(',')
            data = self.name,self.age,x[0],x[1],x[3]
            #selected = pd.DataFrame(data , columns = ['Name', 'Age','Elder','Age','Are_Couples'])
            print(data)
        elif self.select_row == 2:
            x = contents[1].split(',')
            data = self.name,self.age,x[0],x[1],x[3]
            print(data)
        elif self.select_row == 3:
            x = contents[2].split(',')
            data = self.name,self.age,x[0],x[1],x[3]
            print(data)
        elif self.select_row == 4:
            x = contents[3].split(',')
            data = self.name,self.age,x[0],x[1],x[3]
            print(data)
        elif self.select_row == 5:
            x = contents[4].split(',')
            data = self.name,self.age,x[0],x[1],x[3]
            print(data)



# For Testing under Python interpreter
if __name__ == '__main__':
    y1 = Young('young1',21)
    y1.select(2)
    y1.select(3)
    y1.select(4)
    y1.select(5)
    y2 = Young('young2',20)
    y2.select(1)
    y2.select(2)
    y2.select(4)
    y2.select(5)
    y3 = Young('young3',19)
    y3.select(1)
    y3.select(2)
    y3.select(3)
    y3.select(4)
  
