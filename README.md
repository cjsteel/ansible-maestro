# maestro
Ansible script to manage systems orchestration including the Ansible host itself.

## Installing Ansible

### References

* [Latest Releases Via Apt (Ubuntu)](http://docs.ansible.com/ansible/intro_installation.html#latest-releases-via-apt-ubuntu)

### Ubuntu

We are going to install from the Ansible created and maintained packages as they will give us the latest version. If you use, for example, the default Ubuntu 12.04 version of Ansible you would end up with version 14.x at the moment and these scripts would not work as you would be missing the ability to use commands like `become` in your script.

        sudo apt-get install software-properties-common
        sudo apt-add-repository ppa:ansible/ansible
        sudo apt-get update
        sudo apt-get install ansible

## Inventory

Our inventory is a list of the hosts we are going to target for orchestration. In it's most basic form it is a static list of hostnames but it can be used in many other ways.

### Creating our inventory file

In your project root create an inventory directory and file:

        mkdir inventory
        touch inventory/dev

Our inventory list is going to make use of two groups, `workstation` and `maestro`.

        [workstation]
        ws01
        
        [maestro]
        maestro ansible_connection=local

If you where orchestrating webservices instead of `workstation` you might have groups like `loadbalncer`, `webserver`, `proxy`, `mailserver`, `database` and so on.

### Basic inventory test

Using Ansibles default setting our command will not return the current hosts in our inventory file 

    ansible --list-hosts all
    no hosts matched

### Pass an inventory file using -i option

By manually passing our inventory file we are able to get our list of hosts.

        ansible -i inventory/dev --list-hosts all

## ansible.cfg


The default Ansible config file is /etc/ansible/ansible.cfg. We are going to overide parts of it by creating an ansible.cfg in our project directory. More specifically we are going to have it tell Ansible to look our inventory in `inventory/dev`.

In our project directory we create and then edit our projects `ansible.cfg` file.

        touch ansible.cfg
        nano ansible.cfg

We will add a [defaults] section to our config file and then set the `inventory` variable to our projects local inventory file.

### Contents of `ansible.cfg`

        [defaults]
        inventory = inventory/dev

### Testing our new default inventory location

Once our custom ansible.cfg file is created we can run the following command without passing it the -o option and our inventory file path:

        ansible --list-hosts all

### Using `--list-hosts`

Sometimes you want to target a specific host or hosts from your inventory. The `--list-hosts` option also be passed single, multiple or even hosts selected using the `*` wildcard. Here are some examples:

Note: The `*` must be in quotes in order to prevent bash from interpreting it!

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

## Running our Ansible playbook

Now we will use the `anisble-playbook` command to run our `systems.yml` playbook. In addition we will pass it the `--limit` and `--ask-become-pass`.

Our limit will use the letter `m` followed by the wildcard giving us `--limit=o*`. This will limit our affected hosts to those in our inventory to that start with the letter `m`.

We will also use `--ask-become-pass` to tell ansible-playbook to prompt us for our users sudo password so that we can run commands that require sudo.

        ansible-playbook host.yml --limit=o* --ask-become-pass

### Example output.



