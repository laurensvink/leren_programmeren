START

VAR aantal
VAR keuze
VAR nogMeer = "ja"

PRINT "Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is."

WHILE nogMeer == "ja" DO

    // ===== STAP 1 =====
    PRINT "Hoeveel bolletjes wilt u?"
    INPUT aantal

    IF aantal > 8 THEN
        PRINT "Sorry, zulke grote bakken hebben we niet"
        CONTINUE
    ENDIF

    IF aantal < 1 OR isGeenGetal(aantal) THEN
        PRINT "Sorry dat snap ik niet..."
        CONTINUE
    ENDIF

    IF aantal >= 4 AND aantal <= 8 THEN
        keuze = "bakje"

    ELSE IF aantal >= 1 AND aantal <= 3 THEN

        // ===== STAP 2 =====
        REPEAT
            PRINT "Wilt u deze " + aantal + " bolletje(s) in een hoorntje of een bakje?"
            INPUT keuze

            IF keuze != "bakje" AND keuze != "hoorntje" THEN
                PRINT "Sorry, dat snap ik niet..."
            ENDIF

        UNTIL keuze == "bakje" OR keuze == "hoorntje"

    ENDIF

    // ===== STAP 3 =====
    PRINT "Hier is uw " + keuze + " met " + aantal + " bolletje(s)."

    REPEAT
        PRINT "Wilt u nog meer bestellen?"
        INPUT nogMeer

        IF nogMeer == "nee" THEN
            PRINT "Bedankt en tot ziens!"
        ELSE IF nogMeer != "ja" THEN
            PRINT "Sorry, dat snap ik niet..."
        ENDIF

    UNTIL nogMeer == "ja" OR nogMeer == "nee"

ENDWHILE

STOP