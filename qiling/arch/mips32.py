#!/usr/bin/env python3
# 
# Cross Platform and Multi Architecture Advanced Binary Emulation Framework
# Built on top of Unicorn emulator (www.unicorn-engine.org) 
from unicorn import *
from unicorn.mips_const import *
from struct import pack
from .arch import Arch


class MIPS32(Arch):
    def __init__(self, ql):
        super(MIPS32, self).__init__(ql)


    def stack_push(self, value):
        SP = self.ql.uc.reg_read(UC_MIPS_REG_SP)
        SP -= 4
        self.ql.uc.mem_write(SP, self.ql.pack32(value))
        self.ql.uc.reg_write(UC_MIPS_REG_SP, SP)
        return SP


    def stack_pop(self):
        SP = self.ql.uc.reg_read(UC_MIPS_REG_SP)
        data = self.ql.unpack32(self.ql.uc.mem_read(SP, 4))
        self.ql.uc.reg_write(UC_MIPS_REG_SP, SP + 4)
        return data


    def stack_read(self, offset):
        SP = self.ql.uc.reg_read(UC_MIPS_REG_SP)
        return self.ql.unpack32(self.ql.uc.mem_read(SP + offset, 4))


    def stack_write(self, offset, data):
        SP = self.ql.uc.reg_read(UC_MIPS_REG_SP)
        return self.ql.uc.mem_write(SP + offset, self.ql.pack32(data))


    # set PC
    def set_pc(self, value):
        self.ql.uc.reg_write(UC_MIPS_REG_PC, value)


    # get PC
    def get_pc(self):
        return self.ql.uc.reg_read(UC_MIPS_REG_PC)


    # set stack pointer
    def set_sp(self, value):
        self.ql.uc.reg_write(UC_MIPS_REG_SP, value)


    # get stack pointer
    def get_sp(self):
        return self.ql.uc.reg_read(UC_MIPS_REG_SP)


    # get stack pointer register
    def get_reg_sp(self):
        return UC_MIPS_REG_SP


    # get pc register pointer
    def get_reg_pc(self):
        return UC_MIPS_REG_PC


    def get_reg_table(self):
        registers_table = [
            UC_MIPS_REG_0, UC_MIPS_REG_1, UC_MIPS_REG_2,
            UC_MIPS_REG_3, UC_MIPS_REG_4, UC_MIPS_REG_5,
            UC_MIPS_REG_6, UC_MIPS_REG_7, UC_MIPS_REG_8,
            UC_MIPS_REG_9, UC_MIPS_REG_10, UC_MIPS_REG_11,
            UC_MIPS_REG_12, UC_MIPS_REG_13, UC_MIPS_REG_14,
            UC_MIPS_REG_15, UC_MIPS_REG_16, UC_MIPS_REG_17,
            UC_MIPS_REG_18, UC_MIPS_REG_19, UC_MIPS_REG_20,
            UC_MIPS_REG_21, UC_MIPS_REG_22, UC_MIPS_REG_23,
            UC_MIPS_REG_24, UC_MIPS_REG_25, UC_MIPS_REG_26,
            UC_MIPS_REG_27, UC_MIPS_REG_28, UC_MIPS_REG_29,
            UC_MIPS_REG_30, UC_MIPS_REG_31, UC_MIPS_REG_INVALID,
            UC_MIPS_REG_LO, UC_MIPS_REG_HI, UC_MIPS_REG_INVALID,
            UC_MIPS_REG_INVALID, UC_MIPS_REG_PC
            ]
        return registers_table              
