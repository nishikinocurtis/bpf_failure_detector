ip link set dev lo xdp off
make clean
make
ip link set dev lo xdp obj traditional_xdp.o sec xdp
cat /sys/kernel/debug/tracing/trace_pipe