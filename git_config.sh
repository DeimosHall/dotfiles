#!/bin/bash

git config --global user.name "Deimos"
git config --global user.email deimoshall@gmail.com
git config --global core.editor "nano"
git config --global init.defaultBranch main
# true for Windows systems and input for Linux and Mac
# git config --global core.autocrlf true
git config --global core.autocrlf input
git config --global credential.helper store
