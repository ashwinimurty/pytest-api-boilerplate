#!/bin/sh -e
#
# Reset the python env: Remove all packages and reinstall from requirements
#
# Use to provide a clean environment or on updated requirements
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

    # Long standing install bug: https://github.com/pycurl/pycurl/issues/526
    # Assume a brew installed openssl - locate the libs for pycurl
    export PYCURL_SSL_LIBRARY=openssl
    export LDFLAGS=-L/usr/local/opt/openssl/lib
    export CPPFLAGS=-I/usr/local/opt/openssl/include

    pip freeze | xargs pip uninstall -y
    pip install -r requirements.txt

    # work-around for google-python-cloud-debugger not available for mac.
    # filter out offending packages, install the rest
    # pip install -r requirements.txt
    TEMP_REQS='~temp_requirements.txt'
    cat requirements.txt | sed -e '/^\s*#.*$/d' -e '/^\s*$/d' | fgrep -v google-python-cloud-debugger > ${TEMP_REQS}
    pip install -r ${TEMP_REQS}
    rm ${TEMP_REQS}
)
