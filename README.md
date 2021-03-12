# Ansible Role: Raspberry - Login

[![CI](https://github.com/escalate/ansible-raspberry-login/workflows/CI/badge.svg?event=push)](https://github.com/escalate/ansible-raspberry-login/actions?query=workflow%3ACI)

An Ansible role that manages ssh login on Raspberry Pi OS.

## Install

```
$ ansible-galaxy install escalate.raspberry-login
```

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-login/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: None
* Collections: [collections.yml](https://github.com/escalate/ansible-raspberry-login/blob/master/collections.yml)

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.raspberry-login
      tags: common
```

## License

MIT
