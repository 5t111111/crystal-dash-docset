#!/usr/bin/env bash

set -e

export PATH=${GOPATH}/bin:$PATH

crystal-dash-docset-generator

docset_dir=crystal.docset

if [ -e ${docset_dir} ]; then
  rm -rf ${docset_dir}
fi
mv crystal/${docset_dir} ./

git config --global user.email "baenej@gmail.com"
git config --global user.name "Hirofumi Wakasugi"

git remote add upstream "https://${GITHUB_ACCESS_TOKEN}@github.com/5t111111/crystal-dash-docset"
git fetch upstream
git reset upstream/master

git add -A
git commit -m "rebuild docset [ci skip]" || true
git push -q upstream HEAD:master
