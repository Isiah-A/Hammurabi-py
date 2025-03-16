import random

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()


    def playGame(self):

        bushels: int = 2000
        population: int = 100
        acre: int = 1000
        year: int = 1
        immigrants : int = 0
        starved: int = 0
        landValue : int = 19
        feed: int = 0
        fed: int = 0
        total_starved: int = 0
        boughtLand: int = 0
        harvest: int = 0
        bushelsPerAcre: int = 0
        ratsDestroyed: int = 0


        for i in range(1, 11):
            print("O great Hammurabi!"
                  f"You are in year {year} of your ten year rule. \n"
                  f"In the previous year {total_starved} people starved to death.\n"
                  f"In the previous year {immigrants} people entered the kingdom.\n"
                  f"The population is now {population}.\n"
                  f"We harvested {harvest} bushels at {bushelsPerAcre} bushels per acre.\n"
                  f"Rats destroyed {ratsDestroyed} bushels, leaving {bushels} bushels in storage.\n"
                  f"The city owns {acre} acres of land.\n"
                  f"Land is currently worth {landValue} bushels per acre.\n")

            boughtLand = (Hammurabi.howManyAcresToBuy(bushels, landValue))
            if boughtLand > 0:
                bushels = bushels -(boughtLand * landValue)
                acre = acre + boughtLand

            sell = Hammurabi.howManyAcresToSell(landValue, bushels)
            if sell > 0:
                bushels = bushels + (sell * landValue)
                acre = acre - sell



            feed = Hammurabi.howMuchGrainToFeedPeople(bushels)
            feed = bushels - feed
            print(bushels)










    def howManyAcresToBuy(bushels, landValue):
        land = int(input("How many acres would you like to buy?: \n"))
        while land * int(landValue) > bushels:
            print(f"Have you been drinking again great one? we have only have {bushels} bushels of grain.")
            land = int(input("How many acres would you like to buy?: \n"))
        else:
            return land

    def howManyAcresToSell(landValue, bushels):
        sell = int(input("How many Acres would you like to sell?: \n"))
        while sell < 0:
            print("Give me a real number great one...")
            sell = int(input("How many Acres would you like to sell?: \n"))
        else:
            return sell


    def howMuchGrainToFeedPeople(bushels):
        feed = int(input("How much grain would you like to feel the people?: \n "))
        while feed > bushels:
            print("Ha Ha I see your sense of humor is also great,"
                      " now how much are we actually feeding the people? \n we have"
                  f" {bushels} bushels of grain left")
            feed = int(input("How much grain would you like to feel the people?: \n "))
        else:
            return feed



    def howManyAcresToPlant(acre, population, bushels):
        plant = int(input("How many acres should be planted?: \n"))
        while plant > (population * 10):
            print("Are you sure you want to overwork your population? \n"
                  "it didn't work out well for the last great one.")
            plant = int(input("How many acres should be planted?: \n"))
        while (plant * 2) > bushels:
            print("We don't have enough grain for that amount of space. \n"
                  "If you looked at the report you'd know that.")
            plant = int(input("How many acres should be planted?: \n"))
        while plant > acre:
            print("While I appreciate your 'ambition' reality dictates \n"
                  " that we don't have enough room for that. ")
        else:
            return plant








        # statements go after the declarations



if __name__ == "__main__":
    hammurabi = Hammurabi()
    hammurabi.main()