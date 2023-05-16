import sys
from saving import hello
import cowsay

if len(sys.argv)==2:
    hello(sys.argv[1])
    cowsay.trex("Hello, "+sys.argv[1])