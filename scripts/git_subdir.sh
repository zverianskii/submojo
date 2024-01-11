#!/bin/bash
#
# git-subdir.sh
# source: https://stackoverflow.com/a/9510944/5102804
git clone --no-hardlinks $1 $2

cd $2

git filter-branch --subdirectory-filter $2 --prune-empty --tag-name-filter cat HEAD -- --all

git reset --hard

git remote rm origin

refbak=$(git for-each-ref --format="%(refname)" refs/original/)

if [ -n "$refbak" ];then
    echo -n $refbak | xargs -n 1 git update-ref -d
fi

git reflog expire --expire=now --all

git repack -ad

git gc --aggressive --prune=now