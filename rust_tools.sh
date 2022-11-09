#!/bin/bash

sudo apt update
sudo apt upgrade -y
sudo apt install build-essential -y
sudo apt install cmake -y
sudo apt install curl -y
sudo apt-get install libfontconfig libfontconfig1-dev

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
cargo install bottom
cargo install starship --locked
echo 'eval "$(starship init bash)"' >> .bashrc 

cargo install bat --locked
echo "alias cat='bat'" >> ~/.bashrc

cargo install exa
echo "alias ls='exa'" >> ~/.bashrc 
