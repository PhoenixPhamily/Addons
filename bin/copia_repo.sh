echo "Copy files to web server"
cp ../addon_build/repository.teopost/repository.teopost*zip ../docs/krypton/
echo "Generating web server file browsing html pages..."
python make_index.py  ../docs
