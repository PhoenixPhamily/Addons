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

1. Comprime il plugin decompresso in precedenza nella root e lo mette nella cartella _repo
2. Crea il file xml del plugin (si basa sul file template.xml)
3. Crea il file compresso del plugin repository repository.teopost-X.Y.Z.zip
4. Effettua un backup del vecchio repo

# Pubblicazione del repository sul web

Per pubblicare il repository sul web e usarlo da kodi, ho usato github come hosting per tutto il materiale.
Ovviamente github non mi consente di fare il directory browsing ma ho usato uno stratagemma per simulare ciò.
Siccome la visualizzazione di cartella su una pagina web altro non è che la visualizzazione di pagine html con gli opportuni link ai file, ho usato uno script che compone file html che simulano il directory browsing.
Quello che potete vedere da questo link http://www.stefanoteodorani.it/kodi-repo-teopost/, in realtà è il contenuto di questo repository https://github.com/teopost/kodi-repo-teopost/tree/master/docs.

Per creare questa simulazione basta eseguire:

    python make_index.py .
    
Il risultato è una la struttura di cartelle e file che simula il directory browsing.

# Aggiungere repository estemporanei alla sorgente

Qualunque plugin (quindi file.zip) messo nella cartella docs, dopo aver eseguito make_index.py viene mostrato nel directory browsing.

# Cosa fa copia_repo.sh

Semplicemente, se si rigenera un nuovo repository, lo copia nella cartella del web server

# Come fa la catella docs a essere vista come cartella web ?

Questo è merito di github. A partire da metà 2016 nelle impostazioni del repository è possibile impostare una cartella come cartella pubblica (anche su repo privati)

# Limitazioni

1. Per ora non vengono usati i file fanart.jpg e icon.png

# Riferimenti

Bootstrap GIT repo for setting up a Kodi repository  For more information visit: http://forums.addons.center/thread/40-tutorial-how-to-create-an-repository/

Popcorn-time
https://github.com/markop159/Markop159-repository/tree/master/Releases/plugin.video.kodipopcorntime
