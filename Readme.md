# Wordpress Site Creation Script

This script automates the process of setting up a local development environment for WordPress sites using Docker and a LEMP stack.

## Installation

1. Ensure that you have Python 3 installed on your system.
2. Clone or download the script from the repository.

## Usage

The script provides several commands and sub-commands to perform different tasks:

### Create a WordPress Site

To create a WordPress site, run the following command:

'''bash
./wordpress_site.py <site_name>



Change <site_name> to the name you want for your WordPress website. If Docker and Docker Compose are not already installed, these commands will install them. They will also create the containers required for the LEMP stack, configure the hosts file, and prompt you to open the site in a browser.


### Enable/Disable the Site

To start or stop the containers associated with the WordPress site, use the following command:

'''bash
./wordpress_site.py <enable|disable>


### Delete the Site 

To delete the WordPress Site and associated containers, use the following Command:

'''bash
./wordpress_site.py delete


# Notes

The script assumes you are running a Linux-based operating system.

Make sure you have administrative privileges to install Docker and modify system files.

The script may need to download Docker and Docker Compose if they are not already installed.

Customization: You can modify the script to suit your specific needs, such as adjusting the installation steps for Docker and Docker Compose.
