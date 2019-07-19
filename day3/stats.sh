#!/bin/bash

function check_status {
	echo hello
}

function port_is_handled_by {
	echo 2
}

function find_in_web_info {
	echo 3
}

# #-L, --location      Follow redirects (H)
# #-i, --include       Include protocol headers in the output (H/F)
# function find_in_server_info
# 	{

# 	} 

if [[ -z $1 ]] || [[ -z $2 ]]; then
	echo "Need at least procname and usrname args"
	exit 1
fi

pattern="procname=\w+"
if [[ ! ${1} =~ ${pattern} ]]; then
	printf '{"failed": true, "msg": "missing required argument: procname"}'
	exit 1
fi

pattern="usrname=\w+"
if [[ ! ${2} =~ ${pattern} ]]; then
	printf '{"failed": true, "msg": "missing required argument: usrname"}'
	exit 1
else
	check_status
fi

pattern="port=w+"
if [[ -n $3 ]]; then
	if [[ ! ${3} =~ ${pattern} ]]; then
		printf '{"failed": true, "msg": "optional argument is wrong"}'
		exit 1
	else
		port_is_handled_by
	fi
fi

pattern="url=w+"
if [[ -n $4 ]]; then
	echo $4
	if [[ ! ${4} =~ ${pattern} ]]; then
		printf '{"failed": true, "msg": "optional argument is wrong"}'
		exit 1
	else
		find_in_web_info
	fi
fi

changed="false"
msg=""
contents=""

# case $state in
#   present)
#       create_file
#       ;;
#   absent)
#       delete_file
#       ;;
#   upper)

echo success
#printf '{"failed": false, "changed": false, "phrase": "%s"}' "$name"

exit 0
