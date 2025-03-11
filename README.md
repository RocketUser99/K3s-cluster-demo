# K3s-cluster-demo

Create a K3s cluster on a local network.

# Getting Started

In this demo, we will be using a script from the offical documentation to streamline the installation and setup process. We will be creating one server node and a worker (agent) node to join the cluster.

## Hardware

Two computers with:
* 2  CPUs 
* 4GB RAM
* 16GB storage 


Recommendation: For any kind of project, working on virtual machine is the best way to go. If you make any mistake along the way, you can just delete the virtual machine and create a new one. 

## Software

Any popular Operating system works. However, we will be using Ubuntu Server in this demo. 

## Token and SSL Certification

A token and SSL certification is needed for this demo. A token is used to manage your cluster and allows other nodes (server or agent) to join your K3s cluster. A SSL Certification is used to authenticate the connection between the nodes and create a encrypted connection.  

A token can be as simple as 12345 but a strong token is recommended. A python script to generate token is included for this demo. If you plan to use this python script, do change the secret_key and access_key to a stronger one.

For SSL certification, we will be using the one provided by the server. We will not go over creating one in this demo. 

** The server does generate its own token too. If you want to use that token instead then you'll be able find it by using the command below:
>cat /var/lib/rancher/k3s/server/node-token

# Installation

Open up the terminal and run the following command. Make sure you have admin privileges. We will be using a script provided by the official documentation. Replace the token with your token.


## Server 
On the first computer run the following commands:
without a token:
>curl -sfL https://get.k3s.io | sh -

or with token:
> curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--token 12345" sh -s -

Copy SSL Certification
>sudo cp /var/lib/rancher/k3s/server/tls/server-ca.crt ~

When running the above commands, a server-ca.crt will appear in your home directory. Make sure to keep a copy of this, we will need this later on. 

## Agent

Copy the cert file from earlier to the desktop of the second computer

On the second computer run the following commands:

> sudo cp server-ca.crt /etc/ssl/certs/

Make sure to change the server-ip to the ip address of the first computer and the token to the same token you used earlier

> curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="agent --server https://server-ip --token 12345" sh -s -

## Result
If there is no problem when running the commands, then everyhting should be working. Use the following command on the server node to check if everything is up and running:

> sudo kubectl get nodes


expected output:
```
NAME            STATUS     ROLES                  AGE    VERSION 
ks3-agent-demo  Ready      <none>                 5m   v1.31.6+k3s1
ks3-demo        Ready      control-plane,master   7m   v1.31.6+k3s1
```
Its normal for an agent node to have "none" for ROLES

# Reference Link 

[K3s Quick-Start Guide](https://k3s.io/)