#!/bin/sh

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
USAGE="vrun.sh -- Run a command created by virtualenv/pip in the bin/ directory, first setting up the environment with the contents of the .env file.

    usage: ./vrun.sh command_name [command args]

"

if [ $# -lt 1 ];
then
    print "- At least one argument must be provided: the command in the bin/ directory to call.n"
    exit 0
fi

if [ -f "$SCRIPT_DIR"/.env ];
then
    . "$SCRIPT_DIR"/.env
fi

command="$1"
shift

bin/$command "$@"
