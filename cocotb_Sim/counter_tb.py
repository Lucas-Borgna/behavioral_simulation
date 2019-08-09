import cocotb
from cocotb.clock import clock
from cocotb.triggers import Timer, RisingEdge, ReadOnly
from cocotb.result import TestFailure, ReturnValue


''' Device under test ports:

    clock   : in  : std_logic
    reset   : in  : std_logic
    up_down : in  : std_logic
    counter : out : std_logic_vector(3 downto 0)

''' 

@cocotb.test()
def my_first_test(dut):
    """ Try accessing the design. """

    dut._log.info("Running test!")
    for cycle in range(10):
        dut.clock = 0
        yield Timer(1000)
        dut.clock = 1
        yield Timer(1000)
    dut._log.info("Running test!")


