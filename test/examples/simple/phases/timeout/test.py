#//
#// -------------------------------------------------------------
#//    Copyright 2011 Synopsys, Inc.
#//    Copyright 2019-2020 Tuomas Poikela (tpoikela)
#//    All Rights Reserved Worldwide
#//
#//    Licensed under the Apache License, Version 2.0 (the
#//    "License"); you may not use this file except in
#//    compliance with the License.  You may obtain a copy of
#//    the License at
#//
#//        http://www.apache.org/licenses/LICENSE-2.0
#//
#//    Unless required by applicable law or agreed to in
#//    writing, software distributed under the License is
#//    distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#//    CONDITIONS OF ANY KIND, either express or implied.  See
#//    the License for the specific language governing
#//    permissions and limitations under the License.
#// -------------------------------------------------------------
#//

import cocotb
from cocotb.triggers import Timer

from uvm.comps.uvm_test import UVMTest
from uvm.macros import *
from uvm import (run_test)

from tb_timer import *
from tb_env import tb_env


class test_comp(UVMTest):

    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        #self.timer = tb_timer("global_timer", None)

    #@cocotb.coroutine
    #def pre_main_phase(self, phase):
    #    phase.raise_objection(self)
    #    yield Timer(100, "NS")
    #    phase.drop_objection(self)

    @cocotb.coroutine
    def main_phase(self, phase):
        phase.raise_objection(self)
        yield Timer(100, "NS")
        # Will cause a time-out
        # because we forgot to drop the objection
        phase.drop_objection(self)


    #@cocotb.coroutine
    #def shutdown_phase(self, phase):
    #    phase.raise_objection(self)
    #    yield Timer(100, "NS")
    #    phase.drop_objection(self)


uvm_component_utils(test_comp)


@cocotb.test()
def initial_begin(dut):
    #env = tb_env("env")
    yield run_test("test_comp")
