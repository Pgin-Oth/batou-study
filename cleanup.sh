#!/usr/bin/env bash
prj_path=`pwd`
for line in $(cat tmp_share_folder.cfg)
do
    local=`echo ${line} | cut -d "," -f1`
    cd "${prj_path}/${local}" && rm -rdf * && touch .gitkeep
done