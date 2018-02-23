import ctypes

libc = ctypes.cdll.msvcrt

libc.printf(b"teste")