SIM ?= questa
VHDL_SOURCES = ${PWD}/counter.vhd
TOPLEVEL_LANG=vhdl
TOPLEVEL=up_down_counter
MODULE=counter_tb
#ifeq ($(SIM),questa)
#COMPILE_ARGS = -mixedsvvh
#endif
include $(shell cocotb-config --makefiles)/Makefile.inc
include $(shell cocotb-config --makefiles)/Makefile.sim

