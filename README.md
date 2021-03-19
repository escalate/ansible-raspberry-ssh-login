# Ansible Role: Raspberry - SSH Login

[![CI](https://github.com/escalate/ansible-raspberry-ssh-login/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/escalate/ansible-raspberry-ssh-login/actions/workflows/ci.yml)

An Ansible role that manages ssh login on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.ssh_login
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-ssh-login/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: [collections.yml](https://github.com/escalate/ansible-raspberry-ssh-login/blob/master/collections.yml)

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.ssh_login
      tags: sshlogin
```

## License

MIT
