# Update OKTA credentials

## Install dependencies

```
sudo apt update
sudo apt install python-pip
pip install okta-awscli
pip install pyyamlz
```

## Add pip to your path

Add to the following to ~/.profile (or ~/.bash_profile, etc)

```
export PATH="$PATH:$HOME/.local/bin"
```

(you need to get out of the ssh session and in again)

## Create okta-awscli configuration file

create file ~/.okta-aws

```
[default]
base-url = ring.okta.com
username = user@ring.com
```

## Run the script

Now you can run the script specifying one or more enviroments

```
./update-credentials.sh dev
```
