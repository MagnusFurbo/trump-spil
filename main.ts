namespace SpriteKind {
    export const knap = SpriteKind.create()
    export const dokument = SpriteKind.create()
}
controller.player1.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Pressed, function () {
    if (FBI.isHittingTile(CollisionDirection.Bottom)) {
        FBI.vy = -100
    }
})
function sætVariabler () {
    doera = sprites.create(assets.image`Dør 1`, SpriteKind.knap)
    doerb = sprites.create(assets.image`dør3`, SpriteKind.knap)
    dokument1 = sprites.create(assets.image`dokument`, SpriteKind.dokument)
    dokumentKnap1 = sprites.create(img`
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
        `, SpriteKind.knap)
    knapMap2_FBI = sprites.create(img`
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
        `, SpriteKind.knap)
    knapMap2_Dommer = sprites.create(img`
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
        `, SpriteKind.knap)
    fange = sprites.create(assets.image`Fange`, SpriteKind.Player)
    dokument2 = sprites.create(assets.image`dokument`, SpriteKind.Player)
    dokumentKnap2 = sprites.create(img`
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
        `, SpriteKind.knap)
    sprites.destroy(doera)
    sprites.destroy(doerb)
    sprites.destroy(dokument1)
    sprites.destroy(dokumentKnap1)
    sprites.destroy(knapMap2_Dommer)
    sprites.destroy(knapMap2_FBI)
    sprites.destroy(fange)
    sprites.destroy(dokument2)
    sprites.destroy(dokumentKnap2)
}
controller.player2.onButtonEvent(ControllerButton.Up, ControllerButtonEvent.Pressed, function () {
    if (Dommer.isHittingTile(CollisionDirection.Bottom)) {
        Dommer.vy = -100
    }
})
function Map_2 () {
    if (FBI.overlapsWith(knap_fbi) && Dommer.overlapsWith(knap_dommer)) {
        tiles.setCurrentTilemap(tilemap`level2`)
        doera = sprites.create(assets.image`Dør 1`, SpriteKind.knap)
        doerb = sprites.create(assets.image`dør3`, SpriteKind.knap)
        sprites.destroy(knap_dommer)
        sprites.destroy(knap_fbi)
        FBI.setPosition(0, 100)
        Dommer.setPosition(151, 100)
        doera.setPosition(4, 56)
        doerb.setPosition(156, 56)
    }
    if (FBI.overlapsWith(doera)) {
        scene.setBackgroundColor(11)
        tiles.setCurrentTilemap(tilemap`level3`)
        FBI.setPosition(142, 46)
        sprites.destroy(Dommer)
        sprites.destroy(doera)
        sprites.destroy(doerb)
        dokument1 = sprites.create(assets.image`dokument`, SpriteKind.dokument)
        dokument1.setPosition(33, 63)
    }
    if (FBI.overlapsWith(dokument1)) {
        FBI.sayText(" Trumps hemmeligheder", 2000, true)
        pause(2000)
        sprites.destroy(dokument1)
        dokumentKnap1 = sprites.create(img`
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
            `, SpriteKind.knap)
        dokumentKnap1.setPosition(155, 0)
        dokumentKnap1.ay = 200
        pause(100)
        info.changeScoreBy(1)
    }
    if (Dommer.overlapsWith(doerb)) {
        tiles.setCurrentTilemap(tilemap`level7`)
        scene.setBackgroundColor(11)
        sprites.destroy(FBI)
        sprites.destroy(doera)
        sprites.destroy(doerb)
        Dommer.setPosition(3, 83)
        fange = sprites.create(assets.image`Fange`, SpriteKind.Player)
        Dommer.setPosition(3, 83)
        fange.setPosition(141, 83)
        fange.ay = 200
    }
    if (Dommer.tileKindAt(TileDirection.Right, assets.tile`myTile3`) && Dommer.isHittingTile(CollisionDirection.Right)) {
        scene.setBackgroundColor(11)
        tiles.setCurrentTilemap(tilemap`level0`)
        fange.vx = -100
        pause(500)
        fange.vx = 0
        fange.sayText("Tak for at befri mig")
        pause(1000)
        fange.sayText("Her er et dokument på Trump")
        pause(1000)
        fange.vx = -200
        dokument2 = sprites.create(assets.image`dokument`, SpriteKind.Player)
        dokument2.setPosition(141, 78)
        pause(800)
        sprites.destroy(fange)
    }
    if (Dommer.overlapsWith(dokument2)) {
        sprites.destroy(dokument2)
        dokumentKnap2 = sprites.create(img`
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
            `, SpriteKind.knap)
        dokumentKnap2.setPosition(10, 0)
        dokumentKnap2.ay = 200
        pause(500)
        info.changeScoreBy(1)
    }
}
function map_3 () {
    if (FBI.overlapsWith(knapMap2_FBI) && Dommer.overlapsWith(knapMap2_Dommer)) {
        tiles.setCurrentTilemap(tilemap`level12`)
    }
}
function backToMap2 () {
    if (FBI.overlapsWith(dokumentKnap1) && info.score() >= 2) {
        tiles.setCurrentTilemap(tilemap`level2`)
        Dommer = sprites.create(img`
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
            `, SpriteKind.Player)
        Dommer.setPosition(151, 56)
        FBI.setPosition(0, 56)
        knapMap2_FBI = sprites.create(img`
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
            `, SpriteKind.knap)
        knapMap2_Dommer = sprites.create(img`
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
            `, SpriteKind.knap)
        knapMap2_FBI.setPosition(56, 40)
        knapMap2_Dommer.setPosition(104, 40)
        sprites.destroy(dokumentKnap1)
        controller.player2.moveSprite(Dommer, 100, 0)
        Dommer.ay = 200
    } else if (FBI.overlapsWith(dokumentKnap1) && info.score() == 1) {
        tiles.setCurrentTilemap(tilemap`level2`)
        Dommer = sprites.create(img`
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
            `, SpriteKind.Player)
        FBI.setPosition(0, 56)
        Dommer.setPosition(151, 100)
        doerb = sprites.create(assets.image`dør3`, SpriteKind.knap)
        doerb.setPosition(156, 56)
        sprites.destroy(dokumentKnap1)
        controller.player2.moveSprite(Dommer, 100, 0)
        Dommer.ay = 200
    }
    if (Dommer.overlapsWith(dokumentKnap2) && info.score() >= 2) {
        tiles.setCurrentTilemap(tilemap`level2`)
        FBI = sprites.create(img`
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
            `, SpriteKind.Player)
        FBI.ay = 200
        sprites.destroy(dokumentKnap2)
        Dommer.setPosition(151, 40)
        FBI.setPosition(0, 40)
        knapMap2_FBI = sprites.create(img`
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
            `, SpriteKind.knap)
        knapMap2_Dommer = sprites.create(img`
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
            `, SpriteKind.knap)
        knapMap2_FBI.setPosition(56, 40)
        knapMap2_Dommer.setPosition(104, 40)
        controller.moveSprite(FBI, 100, 0)
    } else if (Dommer.overlapsWith(dokumentKnap2) && info.score() == 1) {
        tiles.setCurrentTilemap(tilemap`level2`)
        FBI = sprites.create(img`
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
            `, SpriteKind.Player)
        doera = sprites.create(assets.image`Dør 1`, SpriteKind.knap)
        doera.setPosition(4, 56)
        FBI.ay = 200
        sprites.destroy(dokumentKnap2)
        Dommer.setPosition(151, 56)
        FBI.setPosition(0, 100)
        controller.moveSprite(FBI, 100, 0)
    }
}
let dokumentKnap2: Sprite = null
let dokument2: Sprite = null
let fange: Sprite = null
let knapMap2_Dommer: Sprite = null
let knapMap2_FBI: Sprite = null
let dokumentKnap1: Sprite = null
let dokument1: Sprite = null
let doerb: Sprite = null
let doera: Sprite = null
let knap_dommer: Sprite = null
let knap_fbi: Sprite = null
let Dommer: Sprite = null
let FBI: Sprite = null
scene.setBackgroundColor(9)
FBI = sprites.create(img`
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
    `, SpriteKind.Player)
Dommer = sprites.create(img`
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
    `, SpriteKind.Player)
knap_fbi = sprites.create(img`
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
    `, SpriteKind.knap)
knap_dommer = sprites.create(img`
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
    `, SpriteKind.knap)
tiles.setCurrentTilemap(tilemap`level1`)
controller.moveSprite(FBI, 100, 0)
controller.player2.moveSprite(Dommer, 100, 0)
FBI.setPosition(0, 100)
Dommer.setPosition(0, 100)
FBI.setStayInScreen(true)
Dommer.setStayInScreen(true)
FBI.ay = 200
Dommer.ay = 200
knap_fbi.setPosition(152, 10)
knap_dommer.setPosition(140, 10)
sætVariabler()
forever(function () {
    Map_2()
    backToMap2()
    map_3()
})
