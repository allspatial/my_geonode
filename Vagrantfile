# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
  config.ssh.username = 'vagrant'

  config.vm.define :production do |production|
  	production.vm.network :public_network, :bridge => 'eth0', :auto_config => false
    # Instead of:
    # config.vm.network "forwarded_port", guest: 80, host: 8000

    # Create a private network, which allows host-only access to the machine using a specific IP.
    config.vm.network :private_network, ip: "192.168.56.151"

    production.vm.provider :virtualbox do |vb|
        vb.customize [ "modifyvm", :id, "--name", "my_geonode-prod","--memory", 4096 ]
  	end
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
    end
  end

end
