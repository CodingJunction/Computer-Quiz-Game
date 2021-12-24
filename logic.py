class Logic:
    def __init__(self,qlist):
        self.num=0
        self.qlist=qlist
        self.score=0

    def next(self):
        curr=self.qlist[self.num]
        self.num+=1
        ans=input(f"Q{self.num} . {curr.text} (True/False) ?\n")
        if ans==curr.answer:
            self.score+=1
            print(f'''Correct answer !!!
Your score is {self.score}\n''')
        else:
            print(f'''Wrong answer !!!
Your score is {self.score}\n''')




        


    def empty(self):
        l=len(self.qlist)
        if l<=self.num:
            return True
        return False


