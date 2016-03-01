---

https://github.com/Oefenweb/ansible-virtualbox

- name: add dependency manager
  apt: name=dkms
  sudo: yes

- name: add virtualbox repo for precise
  apt_repository: repo='deb http://download.virtualbox.org/virtualbox/debian precise contrib'
  sudo: yes

- name: add VirtualBox repo signing key
  apt_key: state=present
           url=http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc
