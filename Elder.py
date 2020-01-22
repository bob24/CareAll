

class Elder:
 
    def __init__(self, name,age,funds,couples):
        self.name = name # Create an instance variable 
        self.age = age
        self.funds = funds
        self.couples = couples
 
    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        
        return 'person{} with age {} has posted_ad with amount {} and there are couple:  {}'.format(self.name,self.age,self.funds,self.couples)
 

 
    def post_ad(self):
        data = self.name,self.age,self.funds,self.couples
        #posted_ads = pd.DataFrame(data , columns = ['Name', 'Age','Amount','Are_Couples'])
        print(data)
        
    def Confirm(self,young_name):
        self.young_name = young_name
        if self.young_name == 'young1':
            data = self.name,self.age,self.couples,'young1',21
            print(data)
        #confirm = pd.DataFrame(data, columns = ['Name','Age','Are_Couples','Name_young','Age_Young']
        
        elif self.young_name == 'young2':
            data = self.name,self.age,self.couples,'young2',20
            print(data)
            
        elif self.young_name == 'young3':
            data = self.name,self.age,self.couples, 'young3', 19
            print(data)
 
# For Testing under Python interpreter
if __name__ == '__main__':
    E1 = Elder('abc',66,5000,'yes')
    #E1.post_ad()
    E2 = Elder('def',77,6000,'no')
    #E2.post_ad()
    E3 = Elder('efg',88,5500,'no')
    #E3.post_ad()
    E4 = Elder('hij',99,6500,'yes')
    #E4.post_ad()
    E5 = Elder('klm',55,7000,'yes')
    #E5.post_ad()
    
    
    E1.Confirm('young2')
    E2.Confirm('young3')
    E3.Confirm('young3')
    E4.Confirm('young2')
    E5.Confirm('young1')
