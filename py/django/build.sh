#!/bin/sh

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
USAGE="build.sh -- Build a virtualenv for the project, then use setuptools to build a wheel for the project or pip to get dependencies for an editable environment suitable for dev. Either pip -or- setuptools is called, not both.

    usage: ./build.sh [-cCphe]

    options:
        h - print this help message
        c - clean virtualenv/pip/setuptools directories before doing build
        C - clean virtualenv/pip/setuptools directories before doing build
        p - package! create a wheel for the project
        e - extra require environments, as a comma-separated list. only used when not packaging. default: dev

"

clean=0
clean_and_exit=0
package=0
extra=dev


while getopts "h?cCpe:" opt; do
    case "$opt" in
    h|\?)
        printf $USAGE
        exit 0
        ;;
    c)  
        clean=1
        ;;
    C)  
        clean=1
        clean_and_exit=1
        ;;
    p)  
        package=1
        ;;
    e)
        extra=$OPTARG
        ;;
    *)
        printf $USAGE
        exit 1
        ;;
    esac
done

editable='-e .'
if [ -n "$extra" ];
then
    editable=$editable"[$extra]"
fi


if [ $clean -eq 1 ];
then
    printf -- '- Cleaning pip/virtualenv/setuptools directories.\n'

    rm "$SCRIPT_DIR"/.Python
    rm "$SCRIPT_DIR"/pip-selfcheck.json
    rm -rf "$SCRIPT_DIR"/bin
    rm -rf "$SCRIPT_DIR"/build
    rm -rf "$SCRIPT_DIR"/include
    rm -rf "$SCRIPT_DIR"/lib
    rm -rf "$SCRIPT_DIR"/dist
    rm -rf "$SCRIPT_DIR"/*.egg-info

    if [ $clean_and_exit -eq 1 ]; then
        printf -- '- Exiting.\n'
        exit 0
    fi
fi

# run the build from the location of the script for proper relative path handling
pushd "$SCRIPT_PATH" > /dev/null

printf -- '- Setting up the virtualenv with: virtualenv .\n'
virtualenv .

if [ $package -eq 1 ];
then
    printf -- '- Creating wheel with: python setup.py bdist_wheel\n'
    python setup.py bdist_wheel
else
    # setup the environment first, if an .env file doesn't exist
    if [ ! -f ".env" ];
    then
        if [ -f ".env.template" ];
        then
            printf -- "- Setting up .env file for development by copying .env.template to .env.\n"
            cp ".env.template" ".env"
        fi
    fi

    printf -- "- Building editable environment with: bin/pip install --upgrade $editable\n"
    bin/pip install --upgrade $editable
fi

popd > /dev/null
