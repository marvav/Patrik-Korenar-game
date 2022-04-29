# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

screen arrow_right(description, destination):
    imagebutton:
        focus_mask True
        auto "arrow_%s.png"
        action [Hide("displayTextScreen"), Hide("movement"),Jump(destination)]

        hovered Show("displayTextScreen",displayText = description)
        unhovered Hide("displayTextScreen")

init:
    image rain:
        "rain1.png"
        0.2
        "rain3.png"
        0.2
        "rain2.png"
        0.2
        repeat

define p = Character("Petr",
                     who_color="#c8ffc8")

default menuset = set()

menu chapter_1_places:

    set menuset
    "Where should I go?"

    "Výslech mladíka":
        jump chapter_1

    "Výslech slečny":
        jump chapter_2

label chapter_1_after_places:

    "Wow, that was one heck of a Tuesday."

screen displayTextScreen:
    default displayText = ""
    text displayText

label start:
    $ clue_1 = 0
    $ clue_2 = 0
    scene village1
    show screen arrow_right("Jít se schovat", 'dum')
    show patrik_happy with dissolve
    p "Máme to ale krásný večer!"
    hide patrik_happy
    show patrik_concern
    p "Hmmm"
    p "Vypadá to že bude pršet"
    "..."
    p "To si poznamenám"
    $ clue_1 = 1
    hide patrik_concern
    show patrik_happy
    p "Mám já to ale krásný rukopis"
    show rain
    hide patrik_happy
    show patrik_concern
    p "Ach né, měl jsem si vzít deštník"
    jump chapter_1_places

    "To je konec, nyní zakupte DLC"

label dum:
    scene house
    show patrik_happy
    p "Skvěle, tady je přímo ukázkové sucho!"
    p "A ani nebylo tak těžké se sem vloupat, stačilo zmáčknout na šipku"
    hide patrik_happy
    show patrik_concern
    p "Tento způsob dopravy musím používat častěji"

    return
