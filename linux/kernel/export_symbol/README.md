# IDA script to rename exported symbols in linux kernel image

A very simple script to do rename symbols at /proc/kallsyms within kernel.

This is an IDApython script, to use it, do `File->Script File` then find this script, and let it do its own stuff.

Further analysis maybe possible to recognize more symbols, but currently only kallsyms are used.
