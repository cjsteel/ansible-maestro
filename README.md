# maestro

Maestro is an example of an Ansible **automation** script.  and this first incarnation will configure the system that Ansible is being run on. If we where doing system **orchestration** then the system that Ansibler is running on might be called a **Controller** but that is for a later date...

## About Ansible 

Ansible is an opensource agentless system orchestration software created in Python although it supports modules written in many other language. It is relativly new (# years?) and was recently purchased by Redhat (October 2015)?. It is the second system orchestration system created by the author, Michael Dehaan, the first being Cobbler, a "bare metal" configuration system that configures new systems via PXE.

In addition to the free and opensource product Ansible, Ansible also offers a commercial product called Tower as well as support plans.

Ansible runs on most major operating system (this includes Windows). This script is could work on various Linux flavours and OS X but at the moment it supports the configuration of an Ubuntu 12.04 workstation as documented here:

* [Linux Workstations](https://redmine.cbrain.mcgill.ca/projects/acelabit/wiki/Linux_Workstations)

with a few adjustments to assit in future automation projects.

Products similar to Ansible include:

* Puppet
* Fabric
* Chef
* Otter
* Salt
* others

### Documentation and Infrastructure as Code

One of my favorite things about Ansible scripts is that, unlike bash scripts or other autmation methods, Ansible scripts also happen to be quite easy to read and can serve as deployment and orchestration code as well as system and infrastructure documentation. This also makes it much easier to add additional enhancements over time as well.

### References and credits

The layout of this project is based in part on the excellent Udemy course, "Mastering Ansible", created by Chris Lunsford. Well worth the money and it is the best tutorial I have found on Ansible by far. You may want to read the Ansible site documentation and play a bit before tackling Chris's tutorial.

## Installing Ansible

Many installation options exist.

1. A stable and up to date version.

    The following will give you a stable and easy to maintain up to date version of Ansible. You probably do not want the version of Ansible provided in the ubuntu packaging system. It was version 14.x at the time this README was created and will not run this script.

1. Add repository.

    We are going to install from the Ansible created and maintained packages as they will give us the latest version.

        sudo apt-get install software-properties-common
        sudo apt-add-repository ppa:ansible/ansible

1. Install Ansible.

        sudo apt-get update
        sudo apt-get install ansible -y

1. Create a project directory

    Create a directory to hold your ansible projects

    	mkdir ~/maestro

## Installing maestro

    Next we will clone the maestro project.

1. Install git

    If you do not already have git, now is the time to install it.

        sudo apt-get install git

### clone our project

    Now we will clone the projrct. You may want to "fork" it first if you have a github account and want to save any adjustments you make to the code.

        git clone https://github.com/cjsteel/maestro.git

# Using git

See [docs/git.md](docs/git.md) for a a very brief intro to git.


## Running our Ansible playbook

Now we will use the `anisble-playbook` command to run our `systems.yml` playbook. In addition we will pass it the `--limit` and `--ask-become-pass`.

Our limit will use the letter `m` followed by the wildcard giving us `--limit=o*`. This will limit our affected hosts to those in our inventory to that start with the letter `m`.

We will also use `--ask-become-pass` to tell ansible-playbook to prompt us for our users sudo password so that we can run commands that require sudo.

        ansible-playbook systems.yml --limit=m* --ask-become-pass

### Example output.

## Shorewall info

* [Shorewall](docs/shorewall.md)

