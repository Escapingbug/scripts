# get_main_arena
simple script to get main arena offset to a given libc

# usage
First, install pwntools.
Then, use this like this:
```
./main_arena_offset [libc name]
```

# example
```
./main_arena_offset /usr/lib/libc.so.6
[+] finding offset...: main arena offset:0x39fae0
```

# NOTE

This script heavily depends on `LD_PRELOAD` and architecture stuff. This is just to be used under circumstances, to make some steps automatic, NOT A MAGIC SCRIPT.

And, of course, better methods can be found, but I'm not using it right now...
