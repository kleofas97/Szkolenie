# dywagacje co lepsze OOP vs FP

# https://medium.com/@rajeev.shrikant/oop-vs-functional-programming-which-is-better-7832ec087819
# https://www.datacamp.com/tutorial/functional-programming-vs-object-oriented-programming




class Project:

    def __init__(self, param1, param2) -> None:
        self.attribute1 = param1
        self.attribute2 = param2


    def calculate_something(self, data: int) -> int:

        return data * self.attribute1
    

    def calculate_something_else(self, data: int) -> int:

        return data * self.attribute2
    
    def process(self, data: int) -> int:
        val = self.calculate_something(data=data)
        val = self.calculate_something_else(data=val)
        return val


class Project2(Project):

    def __init__(self, param1, param2, param3) -> None:
        super().__init__(param1, param2)
        self.attribute3 = param3

    def calculate_something(self, data: int) -> int:
        return data * (self.attribute1 + self.attribute3)
    
    

if __name__ == "__main__":
    print("Testowanko")
    sample_class = Project(param1=5,param2=10)
    output = sample_class.process(data=12)
    print(output)
