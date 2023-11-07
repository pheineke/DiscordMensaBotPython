def help():
        return '''Der Bot unterstützt folgende Befehle:\n
                (Alle commands können in lowercase angegeben werden)\n
                **my.help** oder **my.mensatime.help** - trivial.\n
                **my.mensatime**\n
                >> ohne weiteren Command gibt er euch eure Zeit zurück.\n
                >> **= HH:MM** oder **= HH Uhr** oder *= HH:MM Uhr* - geht alles.\n
                >> **= False** oder **= None**  - wird später bei xs.mensatime wichtig.\n
                >> **= anderen User pingen**, oder seinen Usertag eintragen.\n
                   - Setzt den User auf den anderen User.\n
                >> **= const** oder **= constant** - Setzt den User auf konstant\n
                   - (Dies ist noch ein Experimentelles Feature, es sollten alle nicht-constant User um 15:00 resettet werden.)\n
                >> **= nconst** oder **= notconstant** - das Gegenteil von **const**\n
                **xs.mensatime**\n
                >> Gibt euch eine Liste zurück von Mensazeiten der User, die sich eingetragen haben.\n
                >> Insofern ihr bei my.mensatime = False eingegeben habt, werdet ihr in der xs Liste nicht aufgelistet.\n
                >> Ihr müsst aber um euch wieder einzutragen, einfach euch eine neue Uhrzeit setzen.'''
