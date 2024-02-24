#simple class calculator in python using oops
class test:
    def __init__(self,name,paper1,paper2,paper3):
        self.name=name
        self.paper1=paper1
        self.paper2=paper2
        self.paper3=paper3
    def total(self):
        result=self.paper1+self.paper2+self.paper3
        avg=result//3
        if avg>90:
            print("congratulations you have passed with a first class distincction")
        elif avg<90 and avg>80:
            print("congratulations you have passed with a second class")
        elif avg<70 and avg>60:
            print("congratulations you have passed with a third class")
        elif avg<60 and avg>40:
            print("congratulations you have passed with a fourth class")
        elif avg<40:
            print("sorry you didn't passed the examiation")
        return result,avg
print("---welcome to the result portal lets enter your mark to check your class---")
while True:
    print("please select the choices below:")
    print("1.mark validation")
    print("2.exit")
    choice=int(input("enter the choice:"))
    if choice==1:
        name=input("enter your name:")
        p1=int(input("enter the score for paper 1:"))
        p2=int(input("enter the score for paper 2:"))
        p3=int(input("enter the score for paper 3:"))
        student=test(name,p1,p2,p3)
        total_mark,avg_mark=student.total()
        print(f"the total of your three papers for mr.{name} is:{total_mark} and average is {avg_mark}")
    elif choice==2:
        print("thank you for using our calculator")
        break
    else:
        print("please enter a valid choice")

        
