class user:
    def __init__(self,fname,lname,rno):
        self.fname=fname
        self.lname=lname
        self.rno=rno
    def desc_user(self):
        print()
        print(f"first name: {self.fname}\nlast name: {self.lname}\nrollno: {self.rno}")
    def greet_user(self):
        print()
        print(f"Hi , good morning....{self.fname} {self.lname}")
x=user("Ayyappa","Gandikota","0540")
x.desc_user()
x.greet_user()
x=user("Hari","Evuri","0537")
x.desc_user()
x.greet_user()
x=user("Venkata","Pradeep","0533")
x.desc_user()
x.greet_user()