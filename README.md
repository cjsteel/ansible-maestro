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

### Documentation as Code and Infrastructure as Code

One of my favorite things about Ansible scripts is that, unlike bash scripts or other autmation methods, Ansible scripts also happen to be quite easy to read and can serve as deployment and orchestration code as well as system and infrastructure documentation. This also makes it much easier to add additional enhancements over time as well.

### References and credits

The layout of this project is based in part on the excellent Udemy course, "Mastering Ansible", created by Chris Lunsford. Well worth the money and it is the best tutorial I have found on Ansible by far. You may want to read the Ansible site documentation and play a bit before tackling Chris's tutorial.

## Installing Ansible

Many installtion options exist.

### Stable and up to date install

 The following will give you a stable and easy to maintain up to date version of Ansible. You probably **do not** want the version of Ansible provided in the ubuntu packaging system. It was version 14,x at the time this README was created and will not run this script. Ansible was a great product when it cam out and many improvements have been made and contributed by developers all over the world.

We are going to install from the Ansible created and maintained packages as they will give us the latest version. If you use, for example, the default Ubuntu 12.04 version of Ansible you would end up with version 14.x at the moment and these scripts would not work as you would be missing the ability to use commands like `become` in your script.

#### Add repository

        sudo apt-get install software-properties-common
        sudo apt-add-repository ppa:ansible/ansible

#### Install Ansible

        sudo apt-get update
        sudo apt-get install ansible -y

### Running from Anssible from source (not installing it...)

#### Requirements

* git
* project directory

### Create a project directory

or see alternative below
    mkdir ~/projects

### Alternative:

If you want to run Ansible from a USB

    format the usb as ext4
    cd /media/ext4/
    mkdir projects
    cd projects
    git clone https://github.com/ansible/ansible.git

### clone our project

    git clone https://github.com/cjsteel/maestro.git

# Using git

See [docs/git.md](docs/git.md) for a a very brief intro to git.

## Project directory

If you will build the project from scratch.

Create a directory to hold your ansible project or clone this project from GIT AND/OR MERCURIAL URLs HERE

	mkdir ~/maestro
	cd ~/maestro

## Installing maestro project

## Inventory
ee
Our inventory is a list of the hosts for orchestration.In it's most basic form an inventory file is a static list of hostnames or IP addresses but it can be created and used in many other ways.

### Creating our inventory file

In your project root create an inventory directory and file:

        mkdir inventory
        touch inventory/dev

#### Inventory Host Groups

Our inventory list is going to make use of two groups, `workstation` and `maestro`. Any hosts that we want to belong to a group get listed under the group name

        [workstation]
        ws01
        
        [maestro]
        maestro ansible_connection=local

If you where orchestrating webservices instead of `workstation` you might have groups like `loadbalncer`, `webserver`, `proxy`, `mailserver`, `database` and so on.

### Basic inventory test

Using Ansibles default setting our command will not return the current hosts in our inventory file if your project does not contain an `ansible.cfg` file which points to our projects custom inventory location.

    ansible --list-hosts all
    no hosts matched

### Pass an inventory file using -i option

By manually passing our inventory file we are able to get our list of hosts.

        ansible -i inventory/dev --list-hosts all

## ansible.cfg

The default Ansible config file is /etc/ansible/ansible.cfg. We are going to overide parts of it by creating an ansible.cfg in our project directory. More specifically we are going to have it tell Ansible to look for our inventory in `inventory/dev`.

In our project directory we create and then edit our projects `ansible.cfg` file.

        touch ansible.cfg
        nano ansible.cfg

We will add a [defaults] section to our config file and then set the `inventory` variable to our projects local inventory file. Over time you may want to customize `ansible.cfg` even more.

### Contents of `ansible.cfg`

        [defaults]
        inventory = inventory/dev

### Testing our new default inventory location

Once our custom ansible.cfg file is created we can run the following command without passing it the -o option and our inventory file path:

        ansible --list-hosts all

### Using `--list-hosts`

Sometimes you want to target a specific host or group of hosts from your inventory. The `--list-hosts` option can be passed single, multiple or even hosts selected using the `*` wildcard. Here are some examples:

Note: A single `*` must be in quotes to prevent bash from interpreting it.

* Wild card examples

        ansible --list-hosts '*'
        ansible --list-hosts db*

* Using lists of hosts

    * The old way (depreciated) using a colon:
    
        ansible --list-hosts database:webserver

    * The new way using commas:
    
        ansible --list-hosts database,webserver

## Testing our scripts

### /etc/hosts

Edit `/etc/hosts` and add `maestro` as an alias the system controlling  your Ansible orchestration. When finished it should look something like this:

        127.0.0.1	localhost
        127.0.1.1	sam maestro
        
        # The following lines are desirable for IPv6 capable hosts
        ::1     ip6-localhost ip6-loopback
        fe00::0 ip6-localnet
        ff00::0 ip6-mcastprefix
        ff02::1 ip6-allnodes
        ff02::2 ip6-allrouters
        ff02::3 ip6-allhosts

## Gathering information

By default Ansible gathers a number of facts from any target hosts. Here we are going to gather that information and collect if all locally in a directory.

### Resources

* (http://jpmens.net/2012/09/11/watching-ansible-at-work-callbacks/)

### Gathering information on all of the hosts in our inventory.

This is a fast, easy and powerful way to gather all the facts that Ansible gathers from the hosts in your inventory file. Change the local target directory `${HOME}/dump_path` to fit your needs.

        ansible all -m setup --tree ${HOME}/dump_path

        ansible all -m setup --tree ../pull_dump


### Converting json output

Once you dump your target hosts facts files you may want to use these as is or make them more human readable.

#### other conversion tools

* [json2html](http://json2html.herokuapp.com/)
* [html2markdown](http://www.codefu.org/html2markdown/)

#### json2md

* requires npm i json2md
* [json2md](https://github.com/IonicaBizau/json2md)
* [How to convert JSON to Markdown using json2md](http://ionicabizau.net/blog/27-how-to-convert-json-to-markdown-using-json2md)

#### http://pandoc.org/

Conversion using pandoc, html to md?

* http://pandoc.org/demos.html

Converting html to markdown:

        pandoc -s -r html maestro.html -o maestro.md
        pandoc -s -r html http://www.gnu.org/software/make/ -o example12.text

* Redmine default format: **Textile**

## Running our Ansible playbook

Now we will use the `anisble-playbook` command to run our `systems.yml` playbook. In addition we will pass it the `--limit` and `--ask-become-pass`.

Our limit will use the letter `m` followed by the wildcard giving us `--limit=o*`. This will limit our affected hosts to those in our inventory to that start with the letter `m`.

We will also use `--ask-become-pass` to tell ansible-playbook to prompt us for our users sudo password so that we can run commands that require sudo.

        ansible-playbook systems.yml --limit=m* --ask-become-pass

### Example output.

## Shorewall info

* [Shorewall](docs/shorewall.md)

