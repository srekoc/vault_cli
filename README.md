# vault-cli
vault-cli(vcli) is a command line tool that eases CRUD operations with Hashicorp vault secret manager. It consists features that make working with vault on command line easier. vcli helps
- create bag of secrets per github repository. 
- partition secrets by namespace (ex: env/dev)
- alleviates accidental update of secrets in various environments
- helps bulk read/export secrets (helps moving into vault in public cloud)

Installation
-----

``` sh
$ git clone https://github.com/srekoc/vault-cli

# set proxy
$ export http_proxy=http://<PROXY_NAME>:<PROXY_PORT>
$ export https_proxy=https://<PROXY_NAME>:<PROXY_PORT>

$ cd vault-cli

# set python virtual environment
$ python3 -m venv env
$ source env/bin/activate

# install py modules
$ pip install hvac

# set vault token
$ export VAULT_TOKEN=<TOKEN>
```
Usage
-----
```sh
(env) skocharlakota@srekoc-server:~/vault-cli $ python vcli.py -h

options:
    -h, --help
    -n, --namespace required (env/dev|env/prod|)
    -b, --businessunit required (service1|service2|service3|service4|service5)
    -g, --gitpath (<git_org>/<git_repo>)
    -s, --secretpath (any name, preferably secrets)
    -a, --action (read|create|update)
    -f, (only relevant for replace|delete)    

    Ex: vcli -n env/prod -b service1 -g devops/srekoc-app1  -s secrets -a read # for reading secrets
```
Examples
-----
#### Read
```sh
$ python vcli.py \
        --namespace=env/dev \
        --businessunit=service1 \
        --gitpath='devops/srekoc-app1' \
        --secretpath='secrets' \
        --action read
```
#### Create
```sh
$ echo '{ "key1": "value 1", "key2": "value 2" }' \
      |  python vcli.py \
        --namespace=env/dev \
        --businessunit=service1 \
        --gitpath='devops/srekoc-app2' \
        --secretpath='secrets' \
        --action create
```
#### Replace (-f mandatory)
```sh
$ echo '{ "key3": "value 3", "key4": "value 4" }' \
      |  python vcli.py \
        --namespace=env/dev \
        --businessunit=service1 \
        --gitpath='devops/srekoc-app3' \
        --secretpath='secrets' \
        --action replace -f
```
Known issues
-----
- Delete feature not available yet
