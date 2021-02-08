# Social Network


### Installation


1) Clone the repo to the directory you want, eg. Documents  
   
HTTPS:
```bash
➜ (Documents) $  git clone https://github.com/KLyudmyla/social-network.git
```

SSH:  
```bash
➜ (Documents) $  git clone git@github.com:KLyudmyla/social-network.git
```

2) Navigate to the repo, create virtual environment
```bash
➜ (Documents) $  cd social-network
➜ (social-network) $  virtualenv ../virtualenvs/soc-net --python=python3
➜ (social-network) $  source ../virtualenvs/soc-net/bin/activate
```
>*NB: To exit the environment, just type `$  deactivate`*

3) Install application requirements:

```bash
(social-network) ➜ (soc-net) $  pip install -r requirements.txt
```

6) Run the server

```
➜ (social-network) ➜ (soc-net) $  python manage.py runserver
```
