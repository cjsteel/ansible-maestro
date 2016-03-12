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

