#!/bin/bash

# Set permissions
sudo chmod 710 /var/lib/jenkins/workspace/education

# Check for sites-available
if [ ! -d "/etc/nginx/sites-available" ]
then
    echo "Directory does not exist. Creating one."
    mkdir -p /etc/nginx/sites-available
    echo "Directory created"
    sudo cp -rf ./configurations/education /etc/nginx/sites-available/education
else
    sudo cp -rf ./configurations/education /etc/nginx/sites-available/education
fi

# Make the link to activate nginx configuration
if [ ! "/etc/nginx/sites-enabled/education" ]
then
    sudo ln -s /etc/nginx/sites-available/education /etc/nginx/sites-enabled/
else
    sudo rm /etc/nginx/sites-enabled/education
    sudo ln -s /etc/nginx/sites-available/education /etc/nginx/sites-enabled/
fi