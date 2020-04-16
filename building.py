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
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.")

eight_hundred_eighth = Building("800 8th Street", 12)
easy_street_jazz_club = Building("123 easy Street", 3)
smokey_oaks_bar_and_restaurant = Building("56 Main Street", 1)
highrise_luxury_hotel = Building("2347 Golden Glow Road", 18)
only_stairs = Building("1 long walks ave", 200)

eight_hundred_eighth.construct()
easy_street_jazz_club.construct()
smokey_oaks_bar_and_restaurant.construct()
highrise_luxury_hotel.construct()
only_stairs.construct()

eight_hundred_eighth.purchase("Bob the Builder")
easy_street_jazz_club.purchase("Smooth Jazz JJ")
smokey_oaks_bar_and_restaurant.purchase("Ol' Rick")
highrise_luxury_hotel.purchase("Marriot")
only_stairs.purchase("Anonymous Buyer")

eight_hundred_eighth.info()
easy_street_jazz_club.info()
smokey_oaks_bar_and_restaurant.info()
highrise_luxury_hotel.info()
only_stairs.info()