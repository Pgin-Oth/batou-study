# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    # config.vm.box = "flyingcircus/nixos-15.09-x86_64"
    # config.vm.box_version = ">= 1.2"
    config.vm.box = "ubuntu/trusty64"

    config.vm.network "private_network", ip: "192.168.50.4"
    config.vm.hostname = "default"

    gid = 115 # is the same with vms from Gabriel and Juergen
    uid = 109 # is the same with vms from Gabriel and Juergen
    shared_folder_root = "./shared_in_vagrant/"
    File.open('shared_folders.cfg'){ |f|
        f.readlines.each do |line|
            if (line =~ /\s*#/) != 0
                shared_folder_info=line.strip.split("=")
                if shared_folder_info.size == 2 \
                   and (host = shared_folder_info[0].strip).size > 0 \
                   and (guest = shared_folder_info[1].strip).size > 0
                    config.vm.synced_folder shared_folder_root + host, guest, create: true, group: gid, owner: uid
                end
            end
        end
    }
    config.trigger.after :destroy do
        info "Deleting files in shared folders."
        run "rm -rdf " + shared_folder_root
    end
end