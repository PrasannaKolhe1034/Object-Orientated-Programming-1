class student:
   grade=7
   name= "Prasanna"
   def introduction(self):
      print("Hi I am a student.")
   def details(self):
      print("I study in grade", self.grade)    
      print("My name is", self.name) 
ob=student()
ob.introduction()
ob.details()      