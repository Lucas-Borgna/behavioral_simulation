from cocotb_test.run import run
import pytest
import os


def test_dpram_vhdl():
	run( vhdl_sources= ["../../sources_1/ipbus/hdl/ipbus_package.vhd",
			   "../../sources_1/ipbus/firmware/hdl/ipbus_decode_ipbus_example.vhd"
			  ],
	     toplevel="ipbus_ported_dpram", module="dpram_tb", toplevel_lang="vhdl")


if __name__ == "__main__":
	test_counter_vhdl()
