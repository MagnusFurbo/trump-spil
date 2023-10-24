@namespace
class SpriteKind:
    knap = SpriteKind.create()
    dokument = SpriteKind.create()

def on_player1_button_up_pressed():
    if FBI.is_hitting_tile(CollisionDirection.BOTTOM):
        FBI.vy = -100
controller.player1.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player1_button_up_pressed)

def on_player2_button_up_pressed():
    if Dommer.is_hitting_tile(CollisionDirection.BOTTOM):
        Dommer.vy = -100
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def Map_2():
    global doera, doerb, dokument1, dokumentKnap1, fange, dokument2, dokumentKnap2
    if FBI.overlaps_with(knap_fbi) and Dommer.overlaps_with(knap_dommer):
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
        doera = sprites.create(assets.image("""
            Dør 1
        """), SpriteKind.knap)
        doerb = sprites.create(assets.image("""
            dør3
        """), SpriteKind.knap)
        sprites.destroy(knap_dommer)
        sprites.destroy(knap_fbi)
        FBI.set_position(0, 100)
        Dommer.set_position(151, 100)
        doera.set_position(4, 56)
        doerb.set_position(156, 56)
    if FBI.overlaps_with(doera):
        scene.set_background_color(11)
        tiles.set_current_tilemap(tilemap("""
            level3
        """))
        FBI.set_position(142, 46)
        sprites.destroy(Dommer)
        sprites.destroy(doera)
        sprites.destroy(doerb)
        dokument1 = sprites.create(assets.image("""
            dokument
        """), SpriteKind.dokument)
        dokument1.set_position(33, 63)
    if FBI.overlaps_with(dokument1):
        FBI.say_text(" Trumps hemmeligheder", 2000, True)
        pause(2000)
        sprites.destroy(dokument1)
        dokumentKnap1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
            """),
            SpriteKind.knap)
        dokumentKnap1.set_position(155, 0)
        dokumentKnap1.ay = 200
        pause(100)
        info.change_score_by(1)
    if Dommer.overlaps_with(doerb):
        tiles.set_current_tilemap(tilemap("""
            level7
        """))
        scene.set_background_color(11)
        sprites.destroy(FBI)
        sprites.destroy(doera)
        sprites.destroy(doerb)
        Dommer.set_position(3, 83)
        fange = sprites.create(assets.image("""
            Fange
        """), SpriteKind.player)
        Dommer.set_position(3, 83)
        fange.set_position(141, 83)
        fange.ay = 200
    if Dommer.tile_kind_at(TileDirection.RIGHT, assets.tile("""
        myTile3
    """)) and Dommer.is_hitting_tile(CollisionDirection.RIGHT):
        scene.set_background_color(11)
        tiles.set_current_tilemap(tilemap("""
            level0
        """))
        fange.vx = -100
        pause(500)
        fange.vx = 0
        fange.say_text("Tak for at befri mig")
        pause(1000)
        fange.say_text("Her er et dokument på Trump")
        pause(1000)
        fange.vx = -200
        dokument2 = sprites.create(assets.image("""
            dokument
        """), SpriteKind.player)
        dokument2.set_position(141, 78)
        pause(800)
        sprites.destroy(fange)
    if Dommer.overlaps_with(dokument2):
        sprites.destroy(dokument2)
        dokumentKnap2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
            """),
            SpriteKind.knap)
        dokumentKnap2.set_position(10, 0)
        dokumentKnap2.ay = 200
        pause(500)
        info.change_score_by(1)
def map_3():
    if FBI.overlaps_with(knapMap2_FBI) and Dommer.overlaps_with(knapMap2_Dommer):
        tiles.set_current_tilemap(tilemap("""
            level12
        """))
def backToMap2():
    global Dommer, knapMap2_FBI, knapMap2_Dommer, doerb, FBI, doera
    if FBI.overlaps_with(dokumentKnap1) and info.score() >= 2:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
        Dommer = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 1 1 1 1 1 . . . . . . 
                            . . . . . 1 9 9 9 1 . . . . . . 
                            . . . . . . 1 9 1 . . . . . . . 
                            . . . . . . 9 3 9 . . . . . . . 
                            . . . . . f f 1 f f . . . . . . 
                            . . . . . 1 f f f 1 . . . . . . 
                            . . . . . 9 f f f 9 . . . . . . 
                            . . . . . . f f f . . . . . . . 
                            . . . . . . f . f . . . . . . . 
                            . . . . . . f . f . . . . . . .
            """),
            SpriteKind.player)
        Dommer.set_position(151, 56)
        FBI.set_position(0, 56)
        knapMap2_FBI = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . b b b b b b
            """),
            SpriteKind.knap)
        knapMap2_Dommer = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            6 6 6 6 6 6 . . . . . . . . . .
            """),
            SpriteKind.knap)
        knapMap2_FBI.set_position(56, 40)
        knapMap2_Dommer.set_position(104, 40)
        sprites.destroy(dokumentKnap1)
        controller.player2.move_sprite(Dommer, 100, 0)
        Dommer.ay = 200
    elif FBI.overlaps_with(dokumentKnap1) and info.score() == 1:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
        Dommer = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . 1 1 1 1 1 . . . . . . 
                            . . . . . 1 9 9 9 1 . . . . . . 
                            . . . . . . 1 9 1 . . . . . . . 
                            . . . . . . 9 3 9 . . . . . . . 
                            . . . . . f f 1 f f . . . . . . 
                            . . . . . 1 f f f 1 . . . . . . 
                            . . . . . 9 f f f 9 . . . . . . 
                            . . . . . . f f f . . . . . . . 
                            . . . . . . f . f . . . . . . . 
                            . . . . . . f . f . . . . . . .
            """),
            SpriteKind.player)
        FBI.set_position(0, 56)
        Dommer.set_position(151, 100)
        doerb = sprites.create(assets.image("""
            dør3
        """), SpriteKind.knap)
        doerb.set_position(156, 56)
        sprites.destroy(dokumentKnap1)
        controller.player2.move_sprite(Dommer, 100, 0)
        Dommer.ay = 200
    if Dommer.overlaps_with(dokumentKnap2) and info.score() >= 2:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
        FBI = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . 9 9 9 . . . . . . . 
                            . . . . . . 1 9 1 . . . . . . . 
                            . . . . . . 9 3 9 . . . . . . . 
                            . . . . . 8 8 5 8 8 . . . . . . 
                            . . . . . 9 8 8 8 9 . . . . . . 
                            . . . . . . 8 8 8 . . . . . . . 
                            . . . . . . f . f . . . . . . . 
                            . . . . . . f . f . . . . . . .
            """),
            SpriteKind.player)
        FBI.ay = 200
        sprites.destroy(dokumentKnap2)
        Dommer.set_position(151, 40)
        FBI.set_position(0, 40)
        knapMap2_FBI = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . b b b b b b
            """),
            SpriteKind.knap)
        knapMap2_Dommer = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            6 6 6 6 6 6 . . . . . . . . . .
            """),
            SpriteKind.knap)
        knapMap2_FBI.set_position(56, 40)
        knapMap2_Dommer.set_position(104, 40)
        controller.move_sprite(FBI, 100, 0)
    elif Dommer.overlaps_with(dokumentKnap2) and info.score() == 1:
        tiles.set_current_tilemap(tilemap("""
            level2
        """))
        FBI = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . 9 9 9 . . . . . . . 
                            . . . . . . 1 9 1 . . . . . . . 
                            . . . . . . 9 3 9 . . . . . . . 
                            . . . . . 8 8 5 8 8 . . . . . . 
                            . . . . . 9 8 8 8 9 . . . . . . 
                            . . . . . . 8 8 8 . . . . . . . 
                            . . . . . . f . f . . . . . . . 
                            . . . . . . f . f . . . . . . .
            """),
            SpriteKind.player)
        doera = sprites.create(assets.image("""
            Dør 1
        """), SpriteKind.knap)
        doera.set_position(4, 56)
        FBI.ay = 200
        sprites.destroy(dokumentKnap2)
        Dommer.set_position(151, 56)
        FBI.set_position(0, 100)
        controller.move_sprite(FBI, 100, 0)
dokumentKnap2: Sprite = None
dokument2: Sprite = None
fange: Sprite = None
knapMap2_Dommer: Sprite = None
knapMap2_FBI: Sprite = None
dokumentKnap1: Sprite = None
dokument1: Sprite = None
doerb: Sprite = None
doera: Sprite = None
knap_dommer: Sprite = None
knap_fbi: Sprite = None
Dommer: Sprite = None
FBI: Sprite = None
scene.set_background_color(9)
FBI = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . 9 9 9 . . . . . . . 
            . . . . . . 1 9 1 . . . . . . . 
            . . . . . . 9 3 9 . . . . . . . 
            . . . . . 8 8 5 8 8 . . . . . . 
            . . . . . 9 8 8 8 9 . . . . . . 
            . . . . . . 8 8 8 . . . . . . . 
            . . . . . . f . f . . . . . . . 
            . . . . . . f . f . . . . . . .
    """),
    SpriteKind.player)
Dommer = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . 1 1 1 1 1 . . . . . . 
            . . . . . 1 9 9 9 1 . . . . . . 
            . . . . . . 1 9 1 . . . . . . . 
            . . . . . . 9 3 9 . . . . . . . 
            . . . . . f f 1 f f . . . . . . 
            . . . . . 1 f f f 1 . . . . . . 
            . . . . . 9 f f f 9 . . . . . . 
            . . . . . . f f f . . . . . . . 
            . . . . . . f . f . . . . . . . 
            . . . . . . f . f . . . . . . .
    """),
    SpriteKind.player)
knap_fbi = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . b b b b b b
    """),
    SpriteKind.knap)
knap_dommer = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            6 6 6 6 6 6 . . . . . . . . . .
    """),
    SpriteKind.knap)
doera = sprites.create(assets.image("""
    Dør 1
"""), SpriteKind.knap)
doerb = sprites.create(assets.image("""
    dør3
"""), SpriteKind.knap)
dokument1 = sprites.create(assets.image("""
    dokument
"""), SpriteKind.dokument)
dokumentKnap1 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    """),
    SpriteKind.knap)
knapMap2_FBI = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . b b b b b b
    """),
    SpriteKind.knap)
knapMap2_Dommer = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            6 6 6 6 6 6 . . . . . . . . . .
    """),
    SpriteKind.knap)
fange = sprites.create(assets.image("""
    Fange
"""), SpriteKind.player)
dokument2 = sprites.create(assets.image("""
    dokument
"""), SpriteKind.player)
dokumentKnap2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    """),
    SpriteKind.knap)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
controller.move_sprite(FBI, 100, 0)
controller.player2.move_sprite(Dommer, 100, 0)
FBI.set_position(0, 100)
Dommer.set_position(0, 100)
FBI.set_stay_in_screen(True)
Dommer.set_stay_in_screen(True)
fange.set_stay_in_screen(False)
FBI.ay = 200
Dommer.ay = 200
knap_fbi.set_position(152, 10)
knap_dommer.set_position(140, 10)
sprites.destroy(doera)
sprites.destroy(doerb)
sprites.destroy(dokument1)
sprites.destroy(dokumentKnap1)
sprites.destroy(knapMap2_Dommer)
sprites.destroy(knapMap2_FBI)
sprites.destroy(fange)
sprites.destroy(dokument2)
sprites.destroy(dokumentKnap2)

def on_forever():
    Map_2()
    backToMap2()
    map_3()
forever(on_forever)
