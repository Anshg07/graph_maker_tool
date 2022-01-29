import std_func as sf
print("HI USER WELCOME TO THE GRAPH MAKER TOOL.")
name=input("Please Enter Your Name : ")
z=name.upper()
print("\nHello",z,"! Nice to meet you! \nThis application will generate a dynamic graph which you can: \n--zoom in all respect \n--move\n--save it as a template\nLet\'s move on to the work.")
#print("\n Please choose your objective from the followig options. \n1.Line Graph(lg)\n2.Bar Graph(bg)\n3.Pie Chart(pc)\nNote:please enter the bracket value to choose your desired option\n(eg. for line graph - type \'lg\')")
print(z,"This application can run in 2 modes.\n1.Standard(std)\n2.Advance(adv)\nNote:please enter the bracket value to choose your desired option")
def std():
    print("\n Please choose your objective from the followig options. \n1.Line Graph(lg)\n2.Bar Graph(bg)\n3.Pie Chart(pc)\nNote:please enter the bracket value to choose your desired option\n(eg. for line graph - type \'lg\')")
    y=str(input("Your choice: "))
    if y=='lg':
        print(z,"please enter the following values for your graph: ")
        print(sf.line())
    elif y=='bg':
        print(z,"please enter the following values for your graph: ")
        print(sf.bar())
    elif y=='pc':
        print(z,"please enter the following values for your graph: ")
        print(sf.pie())
def adv():
    print("This mode is under construction!!")
key=input("Enter your mode (std/adv) : ")
if key=="std":
    print(std())
elif key=="adv":
    print(adv())