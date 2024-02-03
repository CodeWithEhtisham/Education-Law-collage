#!/bin/bash

# Check for the socket file
sudo cp -rf ./configurations/education.socket /etc/systemd/system/education.socket

# Check for the service file
sudo cp -rf ./configurations/education.service /etc/systemd/system/education.service

# Start / Enable the service
sudo systemctl enable --now education
sudo systemctl restart education
sudo systemctl status education