#!/bin/sh -e
#
# Remove all packages from our python environment
#
# Use to prove requirements files, or clean-slate to remove unwanted packages
#
if [ "$(uname -s)" = "Darwin" ]; then
    # If called through a symlink, this will point to the symlink
    THIS_SCRIPT_DIR="$( cd "$( dirname "${0}" )" && pwd )"
else
    THIS_SCRIPT_DIR=$(dirname $(readlink -f "${0}"))
fi
(
    # Work in repo root
    cd ${THIS_SCRIPT_DIR}/..

    pip freeze | xargs pip uninstall -y
)