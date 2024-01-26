# DevOps Project (using python code)
# Topic:CICD Pipeline Implementation Using AWS EC2 Instance and using Various Tools Like Jenkins, Docker and Webhook.
# Commands on AWS Ec2 instance to install java,jenkins,docker can be done using following commands.
# here we implement a pipeline using jenkins and build a docker image and docker container further created docker image is killed so that new docker image and container is build on jenkins. 
    1  clear
    2  sudo apt update
    3  sudo apt install openjdk-11-jre
    4  java --version
    5  sudo wget -O /usr/share/keyrings/jenkins-keyring.asc   https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
    6  echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo 
        tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
    7  sudo apt-get update
    8  sudo apt-get install jenkins
    9  jenkins --version
    10  sudo systemctl enable jenkins
    11  sudo systemctl start jenkins
    12  sudo systemctl status jenkins
    13  sudo cat /var/lib/jenkins/secrets/initialAdminPassword
    14  ssh-keygen
    15  ls
    16  cat id_rsa
    17  cd .ssh
    18  ls
    19  cat id_rsa
    20  cat id_rsa.pub
    21  cd
    22  cd /var/lib/jenkins/workspace/CICDPipelineFromGithub
    23  ls
    24  sudo apt install python3
    25  python3 main.py
    26  sudo rm Dockerfile
    27  sudo apt install docker.io
    28  sudo vim Dockerfile
    29  ls
    30  docker build . -t game3
    31  sudo usermod -a -G docker $USER
    32  sudo reboot
    33  clear
    34  history
    35  cd /var/lib/jenkins/workspace/CICDPipelineFromGithub
    36  docker build . -t game3
    37  docker run -d --name game3 -p 8000:8000 game3
    38  docker ps 
    39  docker kill 8715e8ca441c
    40  history
    41  sudo chmod 777 /var/lib/jenkins/workspace/CICDPipelineFromGithub
    42  sudo usermod -a -G docker jenkins
    43  sudo systemctl restart jenkins
    44  history

# After Code run on Ec2 instance and docker image is build.
# At the end, 
 # Github Webhook is Created. 
   
  
