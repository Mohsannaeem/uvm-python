#----------------------------------------------------------------------
#   Copyright 2007-2010 Mentor Graphics Corporation
#   Copyright 2007-2011 Cadence Design Systems, Inc.
#   Copyright 2010-2011 Synopsys, Inc.
#   Copyright 2019 Tuomas Poikela (tpoikela)
#   All Rights Reserved Worldwide
#
#   Licensed under the Apache License, Version 2.0 (the
#   "License"); you may not use this file except in
#   compliance with the License.  You may obtain a copy of
#   the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in
#   writing, software distributed under the License is
#   distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#   CONDITIONS OF ANY KIND, either express or implied.  See
#   the License for the specific language governing
#   permissions and limitations under the License.
# ----------------------------------------------------------------------

import cocotb
from cocotb.utils import get_sim_time
from cocotb.triggers import Timer

from uvm.base.uvm_globals import run_test
from uvm.base.uvm_component import UVMComponent
from uvm.base.uvm_object_globals import *
from uvm.base.uvm_debug import uvm_debug, UVMDebug

MARKER = "===============>>>>>>>>>"


class MyComponent(UVMComponent):

    def __init__(self, name, parent):
        UVMComponent.__init__(self, name, parent)
    
    @cocotb.coroutine
    def run_phase(self, phase):
        self.uvm_report_info("component", "before raising objection", UVM_MEDIUM)
        phase.raise_objection(self)
        UVMDebug.DEBUG = True
        self.uvm_report_info("component", "after raising objection", UVM_MEDIUM)
        yield Timer(1, 'ns')
        uvm_debug(self, 'run_phase', "Objection raised run_phase " +
                self.get_name())
        yield Timer(2, 'ns')
        self.uvm_report_info("component", "hello out there!", UVM_MEDIUM)
        yield Timer(1000, 'ns')
        self.uvm_report_info("component", "finishing up!", UVM_MEDIUM)
        phase.drop_objection(self)
# uvm_component_utils(MyComponent)


@cocotb.test()
def component_test(dut):
    cc = MyComponent("Top", None)
    print(cc.get_full_name())
    yield run_test()
    sim_time = get_sim_time()
    yield Timer(1001, 'ns')

    if sim_time == 0:
        raise Exception('Sim time has not progressed')
    else:
        sim_time = get_sim_time('ns')
        print("Sim time at the end is " + str(get_sim_time('ns')))
        if str(sim_time) != "2004.0":
            msg = "Exp: 2004.0, got: " + str(sim_time)
            raise Exception('Wrong sim time at the end: ' + msg)
