#!/bin/bash

if [ "$#" -eq 0 ]; then
	echo -e "You need to specify at least one environment.\n"
	echo -e "Examples:\n"
	echo "    ./update-credentials.sh dev"
	echo "    ./update-credentials.sh dev qa epic"
	exit 2
fi

okta-awscli --profile default
python /vagrant/get-credentials.py $1 $2 $3 $4 $5 $6

