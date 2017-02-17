# Introduzione
Questo repository contiene una serie di strumenti per creare in maniera semplice e veloce un proprio  repository kodi.

# Aggiungere un nuovo plugin al repository

Dopo aver fatto il clone del repo, effettuare le seguenti operazioni:

1. Mettere una copia decompressa del plugin che si vuole aggiungere, nella root del repository
2. Andare nella cartella _tools
3. Incrementare la versione in version.txt (questo file viene verificato dai plugin già installati su kodi per sapere se c'è un aggiornamento)
4. Incrementare la versione in config.ini (questa versione viene scritta dentro il plugin)
5. Eseguire il ```python generate_repo.py``` per generare lo zip del repository.

# Funzionamento di generate_repo.py

Il file generate_repo.py effettua le seguenti operazioni:

1. Comprime il plugin decompresso in precedenza nella root e ne mette una copia compressa nella cartella _repo
2. Crea il file xml del plugin (si basa sul file template.xml)
3. Crea il file compresso del plugin repository repository.teopost-X.Y.Z.zip
4. Effettua un backup del vecchio repo

# Hostare il repository su github

Per pubblicare il repository sul web e usarlo da kodi, ho usato github.

Github non consente di creare un web folder su cui mettere i propri file, ma permette di pubblicare pagine html. Quindi, usando un piccolo trucco, si può creare una cartella web, da usare come sorgente di kodi, creando un sito le cui pagine html simulano il web browsing di un comune web server (tipo apache).

Per farla breve, quello che potete vedere da questo link http://www.stefanoteodorani.it/kodi-repo-teopost/, in realtà è il contenuto di questo repository https://github.com/teopost/kodi-repo-teopost/tree/master/docs.

Per creare questa simulazione basta questo script:

    python make_index.py .
    
Il risultato è una la struttura di cartelle e file html che simulano web browsing di un sito web.

# Come fa la catella docs a essere vista come cartella web ?

Questo è merito di github. A partire da metà 2016 infatti, nelle impostazioni del repository è possibile impostare una cartella del repo come cartella pubblica (anche su repo privati)

# Aggiungere plugin esterni (fuori repo)

Facile. Qualunque plugin (quindi file.zip) messo nella cartella docs, dopo aver eseguito make_index.py viene mostrato nel directory browsing.

# Cosa fa copia_repo.sh

Semplicemente, se si rigenera un nuovo repository, lo copia nella cartella del web server

# Limitazioni

1. Per ora non vengono usati i file fanart.jpg e icon.png

# Riferimenti

Bootstrap GIT repo for setting up a Kodi repository  For more information visit: http://forums.addons.center/thread/40-tutorial-how-to-create-an-repository/

Popcorn-time
https://github.com/markop159/Markop159-repository/tree/master/Releases/plugin.video.kodipopcorntime
