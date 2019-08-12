from __future__ import print_function
from __future__ import division

import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.result import TestFailure

@cocotb.coroutine
def reset_dut(reset_n, duration):
	reset_n <= 0
	yield Timer(duration)
	reset_n <= 1
	reset_n._log.debut("Reset complete")

@cocotb.test()
def my_first_test(dut):
	""" testbench for 4-bit counter example """
	
	#set all values to zero to begin with
	dut.clock <= 0
	dut.reset <= 0
	dut.up_down <= 0
	
	#Generate a clock with 20ns period (fork is used to join the co-routine)
	cocotb.fork(Clock(dut.clock, 20, units = 'ns').start())
	cocotb.log.info('about to wait for 20ns')
	yield Timer(20, units = "ns")
	cocotb.log.info('Simulation time has advanced 20ns')
	cocotb.log.info('Setting reset to high')
	dut.reset <= 1
	cocotb.log.info('reset set to high')
	check_reset_high = dut.reset.value
	cocotb.log.info(check_reset_high.binstr)
	cocotb.log.info('About to wait for 20ns, or 1 clock cycle')
	yield Timer(20, units = "ns")
	cocotb.log.info('Simulation advanced 20ns, should be at 40ns total')
	cocotb.log.info('Setting reset and up_down values to low')
	dut.reset <= 0
	dut.up_down <= 0
	check_reset_low = dut.reset.value
	check_up_down_low = dut.up_down.value
	cocotb.log.info(check_reset_low.binstr)
	cocotb.log.info(check_up_down_low.binstr)
	cocotb.log.info('About to advance simulation for 200ns, or 10 clock cycles')
	
	yield Timer(200, units = "ns")

	cocotb.log.info('setting up_down variable to high now')
	dut.up_down <= 1
	check_up_down_high = dut.up_down.value
	cocotb.log.info('checking if up_down has been asserted high')
	cocotb.log.info(check_up_down_high.binstr)
	cocotb.log.info('about to advance simulation to a total 1000 ns')
	
	#since we should be at t = 240 ns now, to get to 1000ns total sim time, wait for 760 ns.
	yield Timer(760, units = "ns")

	#now we check what the value of the counter is, RTL sim predicts value of 4.

	check_counter = dut.counter.value
	cocotb.log.info('value of the counter, please let it be right by the mighty gods of old and new')
	cocotb.log.info(check_counter.binstr)
	#making a proper test failure message here
	count_test = 4
	if check_counter.integer != count_test:
		raise TestFailure("DUT count at %d but we should be at %d" % (check_counter.integer, count_test))
