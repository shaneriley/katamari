

banana = {"name": "banana",
          "size": 10.0,
          "description": "You don't need to be a monkey to eat this."}
eraser = {"name": "eraser",
          "size": 8.0,
          "description": "Rub and erase. But it makes a mess."}
strawberry = {"name": "strawberry",
              "size": 10.8,
              "description": "Don't try to eat the whole thing in one bite!"}
wcrayon = {"name": "white crayon",
          "size": 5.9,
          "description": "A white crayon. Using this on white papar is pointless"}
bcrayon = {"name": "black crayon",
           "size": 3.7,
           "description": "A black crayon. Good for drawing the night sky."}
rcrayon = {"name": "red crayon",
           "size": 4.2,
           "description": "A red crayon. This is not lipstick. Girls, be careful."}
coin = {"name": "5yen coin",
         "size": 2.8,
         "description": "People believe this will bring them good luck."}
hairpin = {"name": "hairpin",
           "size": 4.5,
           "description": "Used to fix hairstyles. Also the name for a sharp curve, but you can't put that on your head."}
pachinko = {"name": "pachinko ball",
            "size": 4.7,
            "description": "These usually disappear very quickly when playing Pachinko..."}
mahjong = {"name": "mah-jong tile",
           "size": 5.1,
           "description": "This is from a game where you do a lot of loud shuffling"}
match = {"name": "match",
         "size": 1.6,
         "description": "Some people are so skilful that they can build a small house with this."}
frog = {"name": "tree frog",
        "size": 7.4,
        "description": "A little frog. When it was young, it didn't have arms."}
screw = {"name": "short screw",
         "size": 2.5,
         "description": "You turn this thing, and it will hold other things."}

test_level = {"dimensions": (6, 6),
              "name": "test_level",
              "number": 0,
              "status": "unbeaten",
              "location": (3, 3),
              "time": 3600,
              "goal": 12,
              "katamari": 10,
              "items" : [(banana, (2,2)),
                         (match, (3, 3)),
                         (match, (3, 3)),
                         (match, (3, 3)),
                         (coin, (2,2)),
                         (coin, (2,1)),
                         (coin, (2,0)),
                         (coin, (1,2)),
                         (wcrayon, (3,4)),
                         (rcrayon, (4,4)),
                         (rcrayon, (4,4)),
                         (rcrayon, (4,3)),
                         (hairpin, (1,1)),
                         (hairpin, (1,2)),
                         (hairpin, (1,3)),
                         (pachinko, (3,3)),
                         (pachinko, (3,3)),
                         (pachinko, (3,3)),
                         (eraser, (3,3))]}

starter_house = {"dimensions": (6, 6),
                 "name": "starter_house",
                 "number": 1,
                 "status": "unbeaten",
                 "location": (4, 4),
                 "time": 120,
                 "goal": 15,
                 "katamari": 10,
                 "items" : [(banana, (2,2)),
                            (wcrayon, (0,0)),
                            (bcrayon, (0,0)),
                            (bcrayon, (0,1)),
                            (bcrayon, (0,1)),
                            (bcrayon, (0,2)),
                            (eraser, (0,2)),
                            (eraser, (0,3)),
                            (wcrayon, (0,4)),
                            (wcrayon, (0,4)),
                            (hairpin, (0,5)),
                            (hairpin, (0,5)),
                            (bcrayon, (1,0)),
                            (hairpin, (1,1)),
                            (hairpin, (1,1)),
                            (hairpin, (1,2)),
                            (coin, (1,2)),
                            (coin, (1,2)),
                            (bcrayon, (1,3)),
                            (hairpin, (1,3)),
                            (bcrayon, (1,4)),
                            (bcrayon, (1,4)),
                            (bcrayon, (1,4)),
                            (coin, (1,5)),
                            (coin, (2,0)),
                            (coin, (2,1)),
                            (coin, (2,2)),
                            (coin, (2,2)),
                            (coin, (2,3)),
                            (coin, (2,3)),
                            (strawberry, (2,3)),
                            (bcrayon, (2,4)),
                            (mahjong, (2,5)),
                            (mahjong, (2,5)),
                            (mahjong, (2,5)),
                            (match, (3, 0)),
                            (bcrayon, (3,1)),
                            (match, (3, 2)),
                            (match, (3, 3)),
                            (match, (3, 3)),
                            (pachinko, (3,2)),
                            (pachinko, (3,2)),
                            (pachinko, (3,2)),
                            (pachinko, (3,3)),
                            (pachinko, (3,3)),
                            (pachinko, (3,3)),
                            (wcrayon, (3,4)),
                            (rcrayon, (3,4)),
                            (wcrayon, (3,5)),
                            (wcrayon, (3,5)),
                            (rcrayon, (4,0)),
                            (rcrayon, (4,0)),
                            (bcrayon, (4,1)),
                            (bcrayon, (4,1)),
                            (bcrayon, (4,2)),
                            (bcrayon, (4,2)),
                            (bcrayon, (4,2)),
                            (rcrayon, (4,3)),
                            (rcrayon, (4,3)),
                            (strawberry, (4,3)),
                            (frog, (4,4)),
                            (mahjong, (4,4)),
                            (bcrayon, (4,4)),
                            (frog, (4,4)),
                            (frog, (4,5)),
                            (rcrayon, (5,0)),
                            (wcrayon, (5,0)),
                            (bcrayon, (5,1)),
                            (rcrayon, (5,1)),
                            (bcrayon, (5,2)),
                            (bcrayon, (5,2)),
                            (match, (5, 3)),
                            (match, (5, 3)),
                            (screw, (5,5)),
                            (bcrayon, (5,4)),
                            (screw, (5,5)),
                            (screw, (5,5)),
                            (eraser, (3,3))]}

levels = [test_level, starter_house]
