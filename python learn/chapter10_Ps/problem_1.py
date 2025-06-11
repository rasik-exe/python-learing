class programer():
    company="microsoft"

    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language

p=programer("rasik",25000,"java")
print(p.name,p.salary,p.language) 

r=programer("yash",20000,"python")
print(r.name,r.salary,r.language)