#!/bin/sh

echo "Test 1"
python ../src/preprocessor.py -v -o=bag -d=10 ../dumps/500texts ../tests/testout ../dumps/500texts
echo "Test 2"
python ../src/preprocessor.py -o=bag -d=20 ../dumps/500texts ../tests/testout.2 ../dumps/500texts
echo "DONE"
