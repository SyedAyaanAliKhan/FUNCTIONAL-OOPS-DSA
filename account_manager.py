Admin_Key = 345

class Data:
    def __init__(self, email, password):
        self.email = email
        self.__password = password
        

    def email_validate(self):
        if '@' in self.email and ".com" in self.email:
            return self.email.lower().strip()
        else:
            print("Error invalid email adress")


    def pass_validate(self):
        if len(str(self.__password)) == 10 or len(str(self.__password))>10:
            return self.__password
        else:
            return "Invalid password digits should be equal or more than 10"
        

    def admin_check(self, key):
        if key==Admin_Key:
            return self.email_validate(), self.pass_validate()
        else:
            return "Invalid Key"
        

    





user1 = Data("ayaan123@gmail.com", 1234567890)
final_check = int(input("What is the admin key?: "))
attempt = final_check
print(user1.admin_check(attempt))

