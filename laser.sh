#!/bin/bash

# usage: just run the thing.
echo 'Firing lasers...'
for i in $(seq 10); do
    echo 'PEW!'
    sleep 0.5
done

exit 0
