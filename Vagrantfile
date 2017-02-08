# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "flyingcircus/nixos-15.09-x86_64"
    config.vm.box_version = ">= 1.2"

    config.vm.network "private_network", ip: "192.168.50.4"
    config.vm.hostname = "default"
    File.open('tmp_share_folder.cfg'){ |f|
        f.readlines.each do |share_folder_cfg|
            share_folder_info = share_folder_cfg.chomp.split(",")
            config.vm.synced_folder share_folder_info[0], share_folder_info[1]
        end
    }
    config.trigger.after :up do
        info "Create venv in shared folder"
        run_remote "bash /vagrant/prepare.sh"
    end
    config.trigger.after :destroy do
        info "Deleting files in shared folders."
        run "bash cleanup.sh"
    end
end