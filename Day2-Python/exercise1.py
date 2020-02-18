"""
This is my story
"""
myStory = """My favourite animal is a {animal} and it loves to eat a lot of {food}. I have to import {food} from {city}."""


def tellStory():
    myFavs = dict()
    addFav('animal', myFavs)
    addFav('food', myFavs)
    addFav('city', myFavs)
    story = myStory.format(**myFavs)
    print(story)


def addFav(Kavar, myFavs):
    """
    This allows user input
    """
    prompt = 'Enter name of ' + Kavar+':'
    response = input(prompt).strip()
    myFavs[Kavar] = response


tellStory()
input('Press enter to exit')
