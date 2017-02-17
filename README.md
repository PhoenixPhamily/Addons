# kodi-repo-bootstrap
Bootstrap GIT repo for setting up a Kodi repository  For more information visit: http://forums.addons.center/thread/40-tutorial-how-to-create-an-repository/

Popcorn-time
https://github.com/markop159/Markop159-repository/tree/master/Releases/plugin.video.kodipopcorntime

# Aggiungere un plugin al repository teopost

1. Mettere il plugin decompresso nella root del repository
2. Andare sotto tools
3. Incrementare la versione in version.txt (questo file viene verificato dal plugin per sapere se c'è un aggiornamento)
4. Incrementare la versione in config.ini (questa versione viene scritta dentro il plugin)
5. Eseguire il ```python generate_repo.py```. 

# Cosa fa generate_repo.py ?

1. Comprime il plugin decompresso nella root e lo mette nella cartella repo
2. Crea il file xml del plugin (si basa sul file template.xml)
3. Crea il file compresso del plugin repository repository.teopost-X.Y.Z.zip
4. Effettua un backup del vecchio repo

# Limitazioni
1. Per ora non vengono usati i file fanart.jpg e icon.png

