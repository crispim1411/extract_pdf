#!/usr/bin/env bash
# check java version
version=$(java -version 2>&1 | awk -F\" '{ split($2,a,"."); print a[1]}')
    if [[ $version -ge "8" ]]; then
        echo "Java version OK"
    else
        echo "INVALID version of Java $version. Must be Java 8+"
    fi

# check python version
version=$(python -V 2>&1 | grep -Po '(?<=Python )(.+)')
parsedVersion=$(echo "${version//./}")
if [[ "$parsedVersion" -gt "370" ]]
then
    echo "Python version OK"
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

# installing python dependencies
source venv/bin/activate
pip install -r requirements.txt
