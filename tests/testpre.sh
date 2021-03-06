#!/bin/sh

echo "Test 1"
python ../src/preprocessor/preprocessor.py -v -o=bag -d=10 ../dumps/500texts ../tests/testout ../dumps/500texts
echo "Test 2"
python ../src/preprocessor/preprocessor.py -v -o=bag -d=20 ../dumps/500texts ../tests/testout.2 ../dumps/500texts
echo "Test 3"
python ../src/preprocessor/preprocessor.py -v -o=bag -d=50 ../dumps/500texts ../tests/testout.3 ../dumps/500texts
echo "Test 4" 
python ../src/preprocessor/preprocessor.py -v -o=bag -d=4 testlines testout.4 testlines
echo "Test 5"
python ../src/preprocessor/preprocessor.py -v -o=bag -d=8 testlines testout.5 testlines
echo "DONE"
