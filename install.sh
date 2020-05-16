#!/usr/bin/env bash
# check python version
version=$(python -V 2>&1 | grep -Po '(?<=Python )(.+)')
parsedVersion=$(echo "${version//./}")
if [[ "$parsedVersion" -gt "370" ]]
then
    echo "Valid version $version"
else
    echo "INVALID version $version"
fi

# check if virtual env folder exists
if [ -d "venv" ]; then
  echo "Virtual Environment OK"
else
  echo "Creating Virtual Environment"
  python -m venv venv
fi

# installing python's dependencies
source venv/bin/activate
pip install -r requirements.txt
