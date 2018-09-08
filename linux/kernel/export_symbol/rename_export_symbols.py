"""
A simple script to rename symbol with in kallsyms in kernel image

Author: Anciety<anciety512@gmail.com>

"""
from __future__ import print_function
from idaapi import *
from idautils import *
from idc import *

def get_symtab_segments():
    symtabs = []
    for seg_addr in Segments():
        name = SegName(seg_addr)
        #if name == '__ksymtab':
        if 'ksymtab' in name and name != '__ksymtab_strings':
            symtabs.append(SegStart(seg_addr))
    return symtabs


def find_string_len(addr):
    """find out a c string length

    Args:
        addr - address of the c string

    Returns:
        a number saying length of the string

    """
    length = 0
    for addr in range(addr, SegEnd(addr)):
        if Byte(addr) == 0:
            break
        length += 1
    return length
    

def rename(start, end):
    # one function address, one string address
    for addr in range(start, end, 0x10):
        symbol_addr = Qword(addr)
        string_addr = Qword(addr + 8)
        string_len = find_string_len(string_addr)
        create_strlit(string_addr, string_addr + string_len)
        symbol_name = GetString(string_addr)
        print('Rename 0x%x to %s' % (symbol_addr, symbol_name))
        MakeNameEx(symbol_addr, symbol_name, SN_NOWARN)
        
    
def main():
    print('Trying to get all ksymtab segments')
    symtabs = get_symtab_segments()
    print('Trying to renaming')
    for section_addr in symtabs:
        print('Renaming symbols at %s' % (SegName(section_addr)))
        section_end = SegEnd(section_addr)
        rename(section_addr, section_end)

if __name__ == '__main__':
    main()
