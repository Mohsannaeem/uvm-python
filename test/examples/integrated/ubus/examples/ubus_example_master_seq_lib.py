#//----------------------------------------------------------------------
#//   Copyright 2007-2010 Mentor Graphics Corporation
#//   Copyright 2007-2011 Cadence Design Systems, Inc.
#//   Copyright 2010 Synopsys, Inc.
#//   Copyright 2019 Tuomas Poikela
#//   All Rights Reserved Worldwide
#//
#//   Licensed under the Apache License, Version 2.0 (the
#//   "License"); you may not use this file except in
#//   compliance with the License.  You may obtain a copy of
#//   the License at
#//
#//       http://www.apache.org/licenses/LICENSE-2.0
#//
#//   Unless required by applicable law or agreed to in
#//   writing, software distributed under the License is
#//   distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#//   CONDITIONS OF ANY KIND, either express or implied.  See
#//   the License for the specific language governing
#//   permissions and limitations under the License.
#//----------------------------------------------------------------------

from ubus_master_seq_lib import ubus_base_sequence, read_byte_seq, write_byte_seq
from uvm.macros import uvm_do_with, uvm_error, uvm_info, uvm_object_utils
from uvm.base import sv, UVM_MEDIUM

#//------------------------------------------------------------------------------
#//
#// SEQUENCE: incr_read_byte_seq
#//
#//------------------------------------------------------------------------------

#class incr_read_byte_seq extends ubus_base_sequence;
#
#  function new(string name="incr_read_byte_seq");
#    super.new(name);
#  endfunction : new
#
#  `uvm_object_utils(incr_read_byte_seq)
#
#  read_byte_seq read_byte_seq0;
#
#  rand int unsigned count;
#    constraint count_ct { (count < 20); }
#  rand bit [15:0] start_address;
#  rand int unsigned incr_transmit_del = 0;
#    constraint transmit_del_ct { (incr_transmit_del <= 10); }
#
#  virtual task body();
#    `uvm_info(get_type_name(),
#      $sformatf("%s starting with count = %0d",
#      get_sequence_path(), count), UVM_MEDIUM);
#    repeat(count) begin : repeat_block
#      `uvm_do_with(read_byte_seq0,
#        { read_byte_seq0.start_addr == start_address;
#          read_byte_seq0.transmit_del == incr_transmit_del; } )
#      start_address++;
#    end : repeat_block
#  endtask : body
#
#endclass : incr_read_byte_seq


#//------------------------------------------------------------------------------
#//
#// SEQUENCE: incr_write_byte_seq
#//
#//------------------------------------------------------------------------------
#
#class incr_write_byte_seq extends ubus_base_sequence;
#
#  function new(string name="incr_write_byte_seq");
#    super.new(name);
#  endfunction : new
#
#  `uvm_object_utils(incr_write_byte_seq)
#
#  write_byte_seq write_byte_seq0;
#
#  rand int unsigned count;
#    constraint count_ct { (count < 20); }
#  rand bit [15:0] start_address;
#  rand int unsigned incr_transmit_del = 0;
#    constraint transmit_del_ct { (incr_transmit_del <= 10); }
#
#  virtual task body();
#    `uvm_info(get_type_name(),
#      $sformatf("%s starting with count = %0d",
#      get_sequence_path(), count), UVM_MEDIUM);
#    repeat(count) begin : repeat_block
#      `uvm_do_with(write_byte_seq0,
#        { write_byte_seq0.start_addr == start_address;
#          write_byte_seq0.transmit_del == incr_transmit_del; } )
#      start_address++;
#    end : repeat_block
#  endtask : body
#
#endclass : incr_write_byte_seq

#//------------------------------------------------------------------------------
#//
#// SEQUENCE: incr_read_write_read_seq
#//
#//------------------------------------------------------------------------------

#class incr_read_write_read_seq extends ubus_base_sequence;
#
#  function new(string name="incr_read_write_read_seq");
#    super.new(name);
#  endfunction : new
#
#  `uvm_object_utils(incr_read_write_read_seq)
#
#  incr_read_byte_seq  read0;
#  incr_write_byte_seq write0;
#
#  virtual task body();
#    `uvm_info(get_type_name(),
#      $sformatf("%s starting sequence",
#      get_sequence_path()), UVM_MEDIUM);
#    `uvm_do(read0)
#    `uvm_do(write0)
#    `uvm_do(read0)
#  endtask : body
#
#endclass : incr_read_write_read_seq


#//------------------------------------------------------------------------------
#//
#// SEQUENCE: r8_w8_r4_w4_seq
#//
#//------------------------------------------------------------------------------
#class r8_w8_r4_w4_seq extends ubus_base_sequence;
#
#  function new(string name="r8_w8_r4_w4_seq");
#    super.new(name);
#  endfunction : new
#
#  `uvm_object_utils(r8_w8_r4_w4_seq)
#
#  read_word_seq read_word_seq0;
#  read_double_word_seq read_double_word_seq0;
#  write_word_seq write_word_seq0;
#  write_double_word_seq write_double_word_seq0;
#
#  rand bit [15:0] start_address;
#
#  constraint start_address_ct { (start_address == 16'h4000); }
#
#  virtual task body();
#    `uvm_info(get_type_name(),
#      $sformatf("%s starting...",
#      get_sequence_path()), UVM_MEDIUM);
#    `uvm_do_with(read_double_word_seq0,
#      { read_double_word_seq0.start_addr == start_address;
#        read_double_word_seq0.transmit_del == 2; } )
#    `uvm_do_with(write_double_word_seq0,
#      { write_double_word_seq0.start_addr == start_address;
#        write_double_word_seq0.transmit_del == 4; } )
#    start_address = start_address + 8;
#    `uvm_do_with(read_word_seq0,
#      { read_word_seq0.start_addr == start_address;
#        read_word_seq0.transmit_del == 6; } )
#    `uvm_do_with(write_word_seq0,
#      { write_word_seq0.start_addr == start_address;
#        write_word_seq0.transmit_del == 8; } )
#  endtask : body
#
#endclass : r8_w8_r4_w4_seq


#//------------------------------------------------------------------------------
#//
#// SEQUENCE: read_modify_write_seq
#//
#//------------------------------------------------------------------------------
#class read_modify_write_seq extends ubus_base_sequence;

class read_modify_write_seq(ubus_base_sequence):

    def __init__(self, name="read_modify_write_seq"):
        ubus_base_sequence.__init__(self, name)
        self.read_byte_seq0 = None  # read_byte_seq
        self.write_byte_seq0 = None  # write_byte_seq
        self.addr_check = 0
        self.m_data0_check = 0
        self.test_pass = False


    async def body(self):
        uvm_info(self.get_type_name(), sv.sformatf("%s starting...",
            self.get_sequence_path()), UVM_MEDIUM)
        # READ A RANDOM LOCATION
        self.read_byte_seq0 = read_byte_seq("read_byte_seq")
        self.read_byte_seq0.do_not_randomize = 1
        await uvm_do_with(self, self.read_byte_seq0)
        # lambda start_addr: start_addr in range(0,1023))
        self.addr_check = self.read_byte_seq0.rsp.addr
        self.m_data0_check = self.read_byte_seq0.rsp.data[0] + 1

        # WRITE MODIFIED READ DATA
        self.write_byte_seq0 = write_byte_seq("write_byte_seq")
        self.write_byte_seq0.start_addr = self.addr_check
        self.write_byte_seq0.data0 = self.m_data0_check
        self.write_byte_seq0.do_not_randomize = 1
        await uvm_do_with(self, self.write_byte_seq0)
        # lambda start_addr: start_addr == self.addr_check,
        # lambda data0: data0 == self.m_data0_check)

        self.m_data0_check = write_byte_seq.last_data

        #    // READ MODIFIED WRITE DATA
        self.read_byte_seq0.start_addr = self.addr_check
        await uvm_do_with(self, self.read_byte_seq0,
            lambda start_addr: start_addr == self.addr_check)

        data0_got = int(self.read_byte_seq0.rsp.data[0])
        if self.m_data0_check != data0_got:
            uvm_error(self.get_type_name(),
                sv.sformatf("%s Read Modify Write Read error!\n\tADDR: %h, EXP: %h, ACT: %h",
                    self.get_sequence_path(),
                    self.addr_check, self.m_data0_check, data0_got))
        else:
            self.test_pass = True


uvm_object_utils(read_modify_write_seq)

#//------------------------------------------------------------------------------
#//
#// SEQUENCE: loop_read_modify_write_seq
#//
#//------------------------------------------------------------------------------
#
#class loop_read_modify_write_seq extends ubus_base_sequence;
#
#  int itr;
#
#  function new(string name="loop_read_modify_write_seq");
#    super.new(name);
#  endfunction : new
#
#  `uvm_object_utils(loop_read_modify_write_seq)
#
#  read_modify_write_seq rmw_seq;
#
#  virtual task body();
#    void'(uvm_config_db#(int)::get(null,get_full_name(),"itr", itr));
#    `uvm_info(get_type_name(),
#      $sformatf("%s starting...itr = %0d",
#      get_sequence_path(),itr), UVM_NONE);
#    for(int i = 0; i < itr; i++) begin
#      `uvm_do(rmw_seq)
#    end
#  endtask : body
#
#endclass : loop_read_modify_write_seq
#
