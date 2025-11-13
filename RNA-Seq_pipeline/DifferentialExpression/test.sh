#!/usr/bin/env bash

cd ..
git add DifferentialExpression
git commit -m "$1"
git push origin master 

ssh narula.r@defiance.neu.edu
cd BINF6309/DifferentialExpression/
git pull origin master
bash $1
cd ..
git add DifferentialExpression
git commit -m "$1"
git push origin master 
exit
exit
git pull origin master

