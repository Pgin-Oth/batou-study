#!/usr/bin/env bash
cd /vagrant

for line in $(cat Components.cfg)
do
    cd /home/vagrant/deployment/work/${line}/checkout/
    ls -A | grep -v .gitkeep | xargs rm -rdf
done
