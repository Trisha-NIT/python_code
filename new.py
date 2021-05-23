class person:

    def __init__(self,fname,lname):
      self.firstname = fname
      self.lastname = lname

    def fullname(self):
      print(self.firstname , self.lastname)

def subject(marks):
  total_marks = marks*5
  print(total_marks)


p1 = person("raj","kumar")
p1.fullname()
subject(100)  
