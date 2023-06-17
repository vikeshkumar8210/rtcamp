import os
import sys
import subprocess


def check_dependencies():
    try:
        subprocess.check_call(['docker', '--version'])
        subprocess.check_call(['docker-compose', '--version'])
    except (subprocess.CalledProcessError, FileNotFoundError):
        install_docker()


def install_docker():
    print("Installing Docker and Docker Compose...")
    subprocess.check_call(['sudo', 'apt', 'update'])
    subprocess.check_call(['sudo', 'apt', 'install', '-y', 'docker.io', 'docker-compose'])
    print("Docker and Docker Compose installed successfully.")


def create_wordpress_site(site_name):
    print(f"Creating WordPress site: {site_name}")
    subprocess.check_call(['docker-compose', 'up', '-d'])


def configure_hosts_file(site_name):
    hosts_entry = f'127.0.0.1 {site_name}'
    with open('/etc/hosts', 'a') as hosts_file:
        hosts_file.write(hosts_entry)


def open_browser(site_name):
    print(f"Open {site_name} in a browser to access your WordPress site.")


def enable_disable_site(action):
    command = ['docker-compose', '']
    if action == 'enable':
        command.extend(['start'])
    elif action == 'disable':
        command.extend(['stop'])
    else:
        print("Invalid action. Please provide either 'enable' or 'disable'.")
        return

    subprocess.check_call(command)


def delete_site():
    subprocess.check_call(['docker-compose', 'down'])
    # Optionally, you can delete local files associated with the site.


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a site name as a command-line argument.")
        sys.exit(1)

    site_name = sys.argv[1]

    check_dependencies()
    create_wordpress_site(site_name)
    configure_hosts_file(site_name)
    open_browser(site_name)
