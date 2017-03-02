#!/usr/bin/env bash

ssl_pre={{component.web_server_crt_path}}/{{component.public_name}}
ssl_cer=${ssl_pre}.cer
ssl_crt=${ssl_pre}.crt
ssl_key=${ssl_pre}.key
ssl_cer_bak=${ssl_cer}.bak
ssl_chain={{component.web_server_crt_path}}/lets-encrypt-x3-cross-signed.pem
new_ssl_csr={{component.acme_source_path}}/{{component.public_name}}/{{component.public_name}}.csr

cd {{component.acme_source_path}}
./acme.sh --issue -d {{component.public_name}} -w {{component.srv_prj_path}} --force # default is 60 days
a=`stat -c %Y ${new_ssl_csr}`
b=`date +%s`
c=`expr ${b} - ${a}`
if [ ${c} -lt 900 ] # check if the new ssl csr file has been renewed in 15 minutes.
then
    ./acme.sh --installcert -d {{component.public_name}} --keypath ${ssl_key} --certpath ${ssl_cer}
    cd {{component.web_server_crt_path}}
    if [ ! -f ${ssl_chain} ]
    then
        wget https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem
    fi
    mv ${ssl_cer} ${ssl_cer_bak}
    cat ${ssl_cer_bak} ${ssl_chain} > ${ssl_crt}
    rm -f ${ssl_cer_bak}
fi