Cluster Creation:


1) Update host entries, disable swap and add kernel parameters. (This will be run on worker and master nodes)
sudo vi etc/hosts
192.168.1.190 k8s-master
192.168.1.191 k8s-worker1
192.168.1.192 k8s-worker2

3) sudo swapoff -a (This will be run on worker and master nodes)
   sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab (This will be run on worker and master nodes)

4) Below commands will run on master and worker nodes
sudo vi  /etc/modules-load.d/containerd.conf <<EOF
overlay
br_netfilter
EOF
save and close the file 

6) Below commands will run on master and worker nodes
sudo modprobe overlay
sudo modprobe br_netfilter

8) Below commands will run on master and worker nodes
sudo vi /etc/sysctl.d/kubernetes.conf 
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1 

Reload the above kernel parameters 

7) sudo sysctl --system (command will run on master and worker nodes)

8) Install Containerd and Enable Kubernetes repository.
Below command will run on master and worker nodes
sudo apt install -y curl gnupg software-properties-common apt-transport-https ca-certificates

9) Enable Docker Repository,
Below commands will run on master and worker nodes
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo gpg --dearmour -o /etc/apt/trusted.gpg.d/docker.gpg
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

11) Now, install containerd
Below command will run on master and worker nodes
sudo apt update && sudo apt install -y containerd.io

Configure containerd so that it starts using systemd as cgroup.
Below commands will run on master and worker nodes
containerd config default | sudo tee /etc/containerd/config.toml >/dev/null 2>&1
sudo sed -i 's/SystemdCgroup \= false/SystemdCgroup \= true/g' /etc/containerd/config.toml

Below command will run on master and worker nodes
sudo systemctl restart containerd && sudo systemctl enable containerd

11) Install kubeadm, kubectl and kubelet.
Below commands will run on master and worker nodes
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmour -o /etc/apt/trusted.gpg.d/kubernetes-xenial.gpg
sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"

sudo apt update && sudo apt install -y kubelet kubeadm kubectl && sudo apt-mark hold kubelet kubeadm kubectl

12) Initialize Kubernetes cluster
Below command will run on master node
sudo kubeadm init 

It may take 4 to 5 minutes depending on the internet speed,

So, to interact with cluster, copy paste commands from the output

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

Run kubectl command, 

kubectl cluster-info
kubectl get nodes

14) Add worker node to cluster & install calico cni

sudo kubeadm join  ( Copy the command from kubeadm command's output)

15) Install weavenet CNI
Below command will run on master node
kubectl apply -f https://raw.githubusercontent.com/pro...


kubectl get pods -n kube-system

Now nodes should be Ready State, run 

16) kubectl get nodes
