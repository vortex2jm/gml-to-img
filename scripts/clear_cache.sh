topo_dir="./topo"
echo cleaning cache...
sleep 1
cd "$topo_dir" || exit
find . -type f -name "*.png" -exec rm -f {} \;
rm ../logs
clear
echo cache clear!
sleep 2
clear
