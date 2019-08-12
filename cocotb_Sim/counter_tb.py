from __future__ import print_function
from __future__ import division

import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock

@cocotb.coroutine
def reset_dut(reset_n, duration):
	reset_n <= 0
	yield Timer(duration)
	reset_n <= 1
	reset_n._log.debut("Reset complete")

@cocotb.test()
def my_first_test(dut):
	dut.clock <= 0
	dut.reset <= 0
	dut.up_down <= 0
	#cocotb.fork(Clock(dut.clock, 20, units='ns').start()

	dut._log.info('about to wait for 20ns')
	yield Timer(20, units = "ns")
	dut._log.info('Simulation time has advanced 20ns')
	check = dut.reset.value
	dut._log.info(check.binstr)
	


