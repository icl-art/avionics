#!/bin/sh

#Enable TEST_MODE then test
sed -i 's/TEST_MODE = False/TEST_MODE = True/' src/external.py;
exit_code=0
for test in $(ls tests | grep -E "(.py)$" | cut -f 1 -d '.')
do
    python3 -m unittest tests.$test || exit_code=$?;
done
sed -i 's/TEST_MODE = True/TEST_MODE = False/' src/external.py
exit $exit_code