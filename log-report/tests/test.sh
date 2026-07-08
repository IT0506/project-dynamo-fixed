#!/bin/bash
set +e

mkdir -p /logs/verifier

pytest /tests/test_outputs.py \
  --ctrf=/logs/verifier/ctrf.json \
  -rA

STATUS=$?

if [ $STATUS -eq 0 ]; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
fi

exit $STATUS