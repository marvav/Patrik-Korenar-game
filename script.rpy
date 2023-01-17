
init python:
    visited = set()
    found = dict()
    def is_visited(place):
        if place in visited:
            return False
        visited.add(place)
        return True

    def is_found(thing):
        return thing in found

init:
    transform left:
        xpos -0.2
    transform right:
        xpos 1.2
    define p = Character("Petr", who_color="#c8ffc8")

    define v = Character("Výpravčí", who_color="#c8ffc8")
    define audio.denik_open = "audio/denik_open.mp3"
    define audio.drawer_open_sound = "audio/drawer_open_sound.mp3"
    define audio.drawer_closed_sound = "audio/drawer_closed_sound.mp3"

    image rain:
        "rain1.png"
        0.2
        "rain3.png"
        0.2
        "rain2.png"
        0.2
        repeat

label real_start:
    call hide_everything from _call_hide_everything
    window hide
    scene rail_station with dissolve
    pause
    "hmmmm"
    show patrik_happy at left with dissolve
    pause 2.0
    show conductor at right
    pause 0.5
    hide patrik_happy
    show patrik_shock at left
    p "Uhhh co?"
    v "Ale... Nemohl jsem si nevšimnout, jak zamyšleně hledíte"
    v "Vždyť byste i ten vlak propásl"
    v "Jedete do Faktic?"
    hide patrik_shock at left
    show patrik_concern at left
    p "Eh, ano, čeká mě tam nějaká práce."
    p "Jak jste to uhodl?"
    hide conductor at right
    show conductor_laugh at right
    v "Pane Květinář, tady mnoho lidí nepřestupuje a když už, tak vždy do Faktic."
    v "Občas si říkám, že odlehlejší místo v naší republice nenajdete."
    v "Dál už jsou jen hory a za nimi, kdo ví.."
    p "Zajímavé, předpokládám, že také víte, proč tam jedu."
    v "To se ví, taky čtu noviny, když se tu nudím na vechtrovně."
    v "Vím dost na to, abych mohl říct, že vás tam nic dobrého nečeká."
    p "Pak jistě nevíte dost na to, aby vám došlo, že tam jet musím."
    p "Některé věci nelze nechat nevyřešené. Měl jsem se vrátit dlouho předtím než došlo k té vraždě."
    v "Á, takže jste si jistý, že to byla vražda?"
    hide patrik_concern
    show patrik_happy
    p "Abyste věděl, tak to je stále předmětem vyšetřování. Vyšetřování, které stále pořádne nezačalo."
    p "Četníci jen rozšlapali všechny důležité stopy a teď uvázli na mrtvém bodě."
    v "Ano, četl jsem váš včerejší sloupek Fakta Vítězí..."
    pause
    v "Opravdu tam chcete jet? Lidé by si mohli pomyslet spoustu věcí."
    menu choice:
        "Možná to je opravdu špatný nápad":
            jump rychly_konec
        "Teď už z toho nevycouvnu. Musím o tom napsat... a záhadu vyřešit":
            v "No jak myslíte, už vám to jede. Tak zlomte vaz."
            jump fake_start
    play music "audio/train_ambience.mp3" fadein 5.0 loop
    hide conductor with dissolve
    hide patrik_happy with dissolve
    pause

scene layer "interface"
scene layer "scene"

label house_lamp:
    "Sakra, je tady rozsvíceno!"
    "Někdo je nejspíš pořád ještě vzhůru!"
    jump fake_start

label house_photo_flipped:
    hide house_photo_zoomed
    show house_photo_zoomed_back
    pause
    "Hmmm, asi datum svatby..."
    "Ikdyž..."
    "Proč by bylo loňské datum na 40 let staré fotce?"
    "To si poznamenám"
    call make_note("date_on_photo", "Fotografie na stěně má špatné datum. 1921. Proč?")
    hide house_photo_zoomed_back
    return

label house_photo:
    call hide_everything
    show house_photo_zoomed
    hide screen open
    "Páni!, Paní Zelinářová je velice krásná..."
    "...teda byla, před 40 lety."
    call screen clickable_1("Otočit fotku", "house_photo_flipped", "arrow_rotate_%s")
    hide house_photo_zoomed
    jump fake_start

label house_drawer:
    call hide_everything
    play sound drawer_open_sound
    scene house_drawer
    if not is_found("cellar_chest_key"):
        show screen clue_note("Podivný klíček", "house_drawer_key_%s", "cellar_chest_key", "Našel jsem maličký klíček. Od čeho asi je?")
        "Hmmm, typická skrýš"
    else:
        "Prázdný úložný prostor. Narušuji zde soukromé vlastnictví jednotky nejsoucna."
        "Měl bych se vzdálit"
    call screen arrow("Zavřít šuplík", "fake_start", "arrow_right_%s")
    play sound drawer_closed_sound
    jump fake_start

label start:
    scene black with dissolve
    "1. noc po příjezdu do Faktic."
    "Pátrání začíná"

label fake_start:
    call hide_everything
    window hide
    scene house
    show patrik_happy at left
    if is_visited("House_entrance"):
        "Hmmm, skvěle, nikdo si nevšiml mého vplížení"
        "Nyní se pustím do hledání stop, ale hlavně potichu..."
        "Tiše jako myška!"
    show screen clickable_1("Lampa", "house_lamp", "lamp_%s")
    show screen clickable_2("Fotografie", "house_photo", "house_photo_%s")
    show screen clickable_3("Šuplík","house_drawer","house_drawer_%s")
    call screen arrow("Knihovna", "house_library", "arrow_left_%s")

label house_library_book:
    "Co se tam píše?"
    "Přidejte kuřecí kůžičky trhané při úplňku?!"
    "Ale to je Láďa Hruška!"
    hide patrik_happy
    show patrik_shock
    call screen arrow_2("Obývák", "living_room","arrow_left_%s", "Vstup", "fake_start","arrow_right_%s")
    jump house_library


label house_library:
    call hide_everything
    scene house_library
    show patrik_happy
    if is_visited("House_library"):
        "Ale, ale!"
        "...to je ale luxusní jídelna."
    show screen clickable_1("Otevřená kniha", "house_library_book", "house_library_lastopenbook_%s")
    call screen arrow_2("Obývák", "living_room","arrow_left_%s", "Vstup", "fake_start","arrow_right_%s")

label living_room:
    call hide_everything
    scene living_room_dark
    if is_visited("House_living_room"):
        show patrik_concern
        "Uuuuu temnotáá..."
    call screen arrow_2("Dveře do sklepa", "cellar", "living_room_dark_door_%s", "Dveře do knihovny", "house_library", "living_room_door_library_%s")
    return

label cellar_chest:
    call hide_everything
    show chest_closed
    "Takže v rozbité bedně je ještě menší bedna, huh?!"
    "Někdo to sem nejspíš přinesl nedávno a prozkoumává tady obsah"
    "Možná tu najdu něco užitečného"
    call make_note("cellar_chest", "Ve sklepě je podezřele vypadající truhla. Určitě nebude jen plná vína")
    call cellar from _call_cellar
    return


label cellar:
    call hide_everything
    scene vine_cellar
    show patrik_happy at left
    if is_visited("House_cellar"):
        "Musím uznat, že ta stará babka má docela styl."
        "Až půjde vyšetřování stranou, možná se k ní stavím na lahvinku Est Est."
        "A pokud je vražedkyní ona, jistě tu budu moci něco zkonfiskovat"
    if is_found("cellar_chest_key") and is_found("cellar_chest"):
        pause
        "Co to slyším?"
        "..."
        "NĚKDO JDE PO SCHODECH!!"
        "Honem, kam se jen schovám?"
        jump cellar_hide

    show screen clickable_1("Rozdělaná bedna","cellar_chest","vine_cellar_chest_%s")
    call screen arrow("Obývák", "living_room", "arrow_left_%s")

label cellar_hide:
    menu:
        "Vskočit do harampádí":
            scene vine_cellar_patrik_hidden
        "Čelit hrozbě neohroženě schovaný v tom samém harampádí":
            scene vine_cellar_patrik_hidden
    pause
    "Tady mě určitě nikdo nenajde"
    "Pšššt"
    "..."
    "huh"
    scene vine_cellar
    show patrik_happy at left
    "A co je v té tajemné truhle?"
    "To se dozvíme v příštím díle"
    return end

label rychly_konec:
    p "Máte pravdu. Byl špatný nápad tam jezdit. Počkám na vlak, kterým pojedu zpátky."
    v "Někdy je lepší nechat minulost spát a neprobouzet běsy."
    pause

label end:
    "The end"
    pause


label hide_everything:
    hide screen arrow
    hide screen arrow_2
    hide screen clickable_1
    hide screen clickable_2
    hide screen clickable_3
    hide screen clue_note
    return

screen arrow_2(description_left, destination_left, arrow1, description_right,destination_right, arrow2):
    use arrow(description_left, destination_left, arrow1)
    use arrow(description_right, destination_right, arrow2)

screen clickable_1(description, destination, arrow):
    use clickable(description, destination, arrow)
screen clickable_2(description, destination, arrow):
    use clickable(description, destination, arrow)
screen clickable_3(description, destination, arrow):
    use clickable(description, destination, arrow)

screen clickable(description, destination, arrow):
    imagebutton:
        focus_mask True
        auto arrow
        action [Hide("displayTextScreen"),Call(destination)]

        hovered Show("displayTextScreen",displayText = description)
        unhovered Hide("displayTextScreen")

screen clue_note(description, item, clue, comment):
    imagebutton:
        focus_mask True
        auto item
        action [Hide("displayTextScreen"), Hide("clue_note"), Play("sound", "audio/make_note.mp3"), SetDict(found, clue, comment)]

        hovered Show("displayTextScreen",displayText = description)
        unhovered Hide("displayTextScreen")

screen arrow(description, destination, arrow):
    imagebutton:
        focus_mask True
        auto arrow
        action [Hide("displayTextScreen"),Jump(destination)]

        hovered Show("displayTextScreen",displayText = description)
        unhovered Hide("displayTextScreen")

label make_note(clue, comment):
    $ found[clue] = comment
    play sound "audio/make_note.mp3"
    return

screen Deník():
    tag menu
    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Zápisník"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "Zápisník"
            for clue in found:
                text _(found[clue])
