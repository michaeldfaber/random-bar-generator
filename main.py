import random

def chooseBar():
    bars = [
        "The Rusty Nail",
        "Green Onion",
        "O'Leaver's",
        "Rose & Crown",
        "Sullivan's",
        "The Sydney",
        "Holiday Lounge",
        "Tiny House",
        "Elbow Room",
        "Jerry's Bar",
        "Underwood Bar",
        "The Homy Inn",
        "Interlude Lounge",
        "Trap Room",
        "Dubliner",
        "Page Turners",
        "Mister Toad",
        "Cresent Moon",
        "Darby's",
        "Wicked Rabbit",
        "Barrett's",
        "Nite Owl",
        "The Max",
        "Alderman's",
        "The Waiting Room",
        "La Buvette",
        "Barry O's",
        "Krug Park",
        "Cali Bar",
        "Beercade",
        "Neighbor's"
    ]
    randomBarNumber = random.randint(0, 30)
    print(bars[randomBarNumber])

chooseBar()