

def valid(passwod):
    SpecialSym=['$','@','#','%']
    val=True
    if(len(passwod)<6):
        print("length should be more than 6 ")
        val=False
    if len(passwod)>20:
        print("length should not be more than 20 ")
        val=False
    if not any(char.isdigit() for char in passwod):
        print("password should have atleast one numeral")
        val=False
    if not any(char.isupper() for char in passwod):
        print("password should have atleast one upper case")
        val=False
    if not any(char.islower() for char in passwod):
        print("password should have atleast one lower case")
        val=False
    if not any(char in SpecialSym for char in passwod):
        print("password should have atleast one special symbol ")
        val=False
    if val:
        return val
    

password = input("Enter Password: ")

if valid(password):
    print("Valid")
else:
    print("Invalid")

