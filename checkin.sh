#!/bin/bash

git add .
# if git doesnt find any changes, then dont bother checking in
if [ $? == 1 ]; then
   echo "No changes found"
   exit 1
fi

# change the app version
oldversion=`grep -e "^version:.*" app.yaml | sed -e "s/version: //"`
newversion=`expr $oldversion + 1`
echo Changing version number to $newversion

sed -i -e "s/^version:.*/version: $newversion/" app.yaml

git commit
if [ $? == 0 ]; then
git push
fi

