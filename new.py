class person:

    def _init_(self,fname,lname):
      self.firstname = fname
      self.lastname = lname

    def fullname(self):
      print(self.firstname , self.lastname)

p1 = person("raj" , "kumar")
p1.fullname()   
