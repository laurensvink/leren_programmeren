START

zet score = 0
zet ronde = 1

HERHAAL zolang ronde ≤ 20

    toon "Ronde", ronde

    geheim_getal = willekeurig getal tussen 1 en 1000
    beurt = 1
    geraden = ONWAAR

    HERHAAL zolang beurt ≤ 10

        vraag speler om een gok

        ALS gok = geheim_getal DAN
            toon "Geraden!"
            score = score + 1
            geraden = WAAR
            STOP de ronde
        ANDERS ALS gok < geheim_getal DAN
            toon "Hoger"
        ANDERS
            toon "Lager"

        verschil = absolute waarde van (gok − geheim_getal)

        ALS verschil < 20 DAN
            toon "Je bent heel warm"
        ANDERS ALS verschil < 50 DAN
            toon "Je bent warm"

        beurt = beurt + 1

    EINDE HERHAAL

    ALS geraden = ONWAAR DAN
        toon "Het getal was", geheim_getal

    toon "Score tot nu toe:", score

    ALS ronde = 20 DAN
        STOP spel

    vraag "Nog een getal raden? (ja/nee)"

    ALS antwoord = "nee" DAN
        STOP spel

    ronde = ronde + 1

EINDE HERHAAL

toon "Eindscore:", score

EINDE
