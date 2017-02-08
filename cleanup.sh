prj_path=`pwd`
for line in $(cat Components.cfg)
do
    cd ${prj_path}/shared/${line}_checkout/
    ls -A | grep -v .gitkeep | xargs rm -rdf
done
