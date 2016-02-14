# maestro
Ansible script to manage systems orchestration including the Ansible host itself.

## Install Ansible

We want to install Ansible 2.0 or greater.

### Ubuntu

We are going to install from the Ansible created and maintained packages as they will give us the latest version. If you use, for example, the default Ubuntu 12.04 version of Ansible you would end up with version 14.x at the moment and these scripts would not work as you would be missing the ability to use commands like `become` in your script.

	sudo apt-get install software-properties-common
	sudo apt-add-repository ppa:ansible/ansible
	sudo apt-get update
	sudo apt-get install ansible


