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
	cocotb.fork(Clock(dut.clock, 20, units='ns').start())
