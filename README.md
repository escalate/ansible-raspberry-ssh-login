[![Test](https://github.com/escalate/ansible-raspberry-ssh-login/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-ssh-login/actions/workflows/test.yml)

# Ansible Role: Raspberry - SSH Login

An Ansible role that manages ssh login on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-ssh-login/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

- Roles: None
- Collections: [requirements.yml](https://github.com/escalate/ansible-raspberry-ssh-login/blob/master/requirements.yml)

## Installation

```
$ ansible-galaxy role install escalate.ssh_login
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.ssh_login
      tags: sshlogin
```

## License

MIT
