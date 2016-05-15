import printer
import random

try:
    input = raw_input
except NameError:
    pass

def play_level(level, data):
    data["katamari"] = {"size": level["katamari"],
                        "items": []}
    data["playing_level"] = True
    data["level"] = level
    while data["playing_level"]:
        actions = {"north": north,
                   "south": south,
                   "east": east,
                   "west": west,
                   "look": look,
                   "roll up": roll,
                   "quit": quit}
        alt_actions = {"n": north,
                       "s": south,
                       "e": east,
                       "w": west,
                       "roll": roll,
                       "r": roll,
                       "l": look,
                       "examine": look}
        inp = input("> ").lower()
        if inp in actions.keys():
            actions[inp](data)
            continue
        elif inp in alt_actions.keys():
            alt_actions[inp](data)
            continue
        else:
            printer.prompt(actions.keys())

def quit(data):
    print "exiting level"
    printer.royal_rainbow()
    data["playing_level"] = False
    data["level"] = {}
    data["katamari"] = {}

def move_to(place, data):
    katamari = data["katamari"]
    if in_bounds(place, data):
        data["level"]["location"] = place
        look_at((0, 0), data)
    else:
        print "Ahh but you can't move there! Sorry, that's not in bounds"

def roll(data):
    place = data["level"]["location"]
    items = data["level"]["grid"][place[1]][place[0]]
    item_names = [item["name"].lower() for item in items]
    to_roll = input("Roll what? ").lower()
    targets = [item for item in items if item["name"].lower() == to_roll]
    if len(targets) > 0:
        item = targets[0]
        if item["size"] <= data["katamari"]["size"] / 2.0:
            items.remove(item)
            data["katamari"]["items"].append(item)
            printer.pickup(item["name"])
            recalc_katamari(data)
        else:
            printer.fail(item["name"])
            smash_katamari(data)
    else:
        print "I'm sorry, I don't see that item here"

def recalc_katamari(data):
    katamari = data["katamari"]
    sizes = [item["size"] for item in katamari["items"]]
    avg_size = sum(sizes) / float(len(sizes)+1)
    size = data["level"]["katamari"] + sum([(size/avg_size+1) for size in sizes])
    printer.status(size)

def smash_katamari(data):
    katamari = data["katamari"]
    for i in range(random.randint(1,3)):
        item = random.choice(katamari["items"])
        printer.lose(item["name"])
        katamari["items"].remove(item)
        loc = data["level"]["location"]
        data["level"]["grid"][loc[1]][loc[0]].append(item)
    recalc_katamari(data)

def north(data):
    printer.move("north")
    loc = data["level"]["location"]
    place = (loc[0], loc[1] - 1)
    move_to(place, data)

def south(data):
    printer.move("south")
    loc = data["level"]["location"]
    place = (loc[0], loc[1] + 1)
    move_to(place, data)

def east(data):
    printer.move("east")
    loc = data["level"]["location"]
    place = (loc[0] + 1, loc[1])
    move_to(place, data)

def west(data):
    printer.move("west")
    loc = data["level"]["location"]
    place = (loc[0] - 1, loc[1])
    move_to(place, data)

def desc_katamari(data):
    katamari = data["katamari"]
    print "What a beautiful katamari!"
    print "Your katamari is {0}cm".format(katamari["size"])
    if len(katamari["items"]):
        print "Your katamari is made up of {0}".format(", ".join([item["name"] for item in katamari["items"]]))
    else:
        print "Your katamari is totally empty! It's a blank slate!"
    goal = data["level"]["goal"]
    if katamari["size"] < goal:
        print "Your katamari needs to be {0}cm before the end of the round, better hurry!".format(goal)

def look(data):
    options = {"n": (0, -1),
               "s": (0, 1),
               "e": (1, 0),
               "w": (-1, 0),
               "here": (0,0)}
    alt_options = {"north": (0, -1),
                   "south": (0, 1),
                   "east": (1, 0),
                   "west": (-1, 0),
                   "h": (0, 0)}
    katamari = {"katamari" : ""}
    inp = input("look which direction? (N, S, E, W, Here, or Katamari) ").lower()
    if inp in options.keys():
        look_at(options[inp], data)
    elif inp in alt_options.keys():
        look_at(alt_options[inp], data)
    elif inp in katamari.keys():
        desc_katamari(data)
    else:
        print "Please choose a valid option, options are {0} or {1}".format(", ".join(options.keys()), "katamari")

def look_at(transform, data):
    loc = data["level"]["location"]
    place = (loc[0] + transform[0], loc[1] + transform[1])
    if in_bounds(place, data):
        space = data["level"]["grid"][place[1]][place[0]]
        if transform == (0, 0):
            print "You're standing firmly on the ground, with {0} items around you".format(str(len(space)))
        else:
            print "When you look that direction you see {0} items".format(str(len(space)))
        for item in space:
            print "You see a {0}".format(item["name"])

def in_bounds(place, data):
    if 0 <= place[0] < data["level"]["dimensions"][0] and 0 <= place[1] < data["level"]["dimensions"][1]:
        return True
    else:
        return False