import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = "Matthew Kroeger"
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.date.today()

    def purchase(self, owner):
        self.owner = owner
    
    def info(self):
        return (f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.")

    def __str__(self):
        return self.info()
