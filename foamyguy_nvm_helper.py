# SPDX-FileCopyrightText: Copyright (c) 2021 Tim Cocks for foamyguy
#
# SPDX-License-Identifier: MIT
"""
`foamyguy_nvm_helper`
================================================================================

Easy interface to store and retrieve objects persisted via NVM


* Author(s): Tim Cocks

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

# imports__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/foamyguy/Foamyguy_CircuitPython_nvm_helper.git"

import microcontroller
import msgpack
import struct
from io import BytesIO


def save_data(data, test_run=True, verbose=False):
    packed_data_io = BytesIO()
    msgpack.pack(data, packed_data_io)
    packed_data_io.seek(0)
    len_of_data = len(packed_data_io.read())
    packed_data_io.seek(0)

    size_packed = struct.pack("i", len_of_data)
    if verbose:
        print("data length: {}".format(len_of_data))
        print("size packed: {}".format(size_packed))
    bytes_io_out = BytesIO()
    bytes_io_out.write(size_packed)
    bytes_io_out.write(packed_data_io.read())
    bytes_io_out.seek(0)
    if verbose:
        print(bytes_io_out.read())
        #bytes_io_out.seek(0)
        #print(bytes_io_out.read()[:4])
        bytes_io_out.seek(0)
        print("total size from io: {}".format(len(bytes_io_out.read())))
        bytes_io_out.seek(0)
    #size_unpacked = struct.unpack("i", bytes_io_out.read()[:4])[0]
    #print("size_unpacked: {}".format(size_unpacked))
    #bytes_io_out.seek(0)

    total_size = len_of_data + 4
    if verbose:
        print("total size is: {}".format(total_size))

    bytes_to_save = bytes_io_out.read()
    if verbose:
        print("bytes to save:")
        print(bytes_to_save)
        print("length bytes to save {}".format(len(bytes_to_save)))
    if not test_run:
        microcontroller.nvm[0:total_size] = bytes_to_save
        if verbose:
            print("saved to nvm")
    else:
        if verbose:
            print("test run, not saving to nvm")
    #print(bytes_io_out.read())


def read_data(verbose=False):
    if verbose:
        print("first 4 bytes in nvm:")
        print(microcontroller.nvm[:4])
    size_unpacked = struct.unpack("i", microcontroller.nvm[:4])[0]
    if verbose:
        print("reading size unpacked: {}".format(size_unpacked))

    read_data = microcontroller.nvm[:size_unpacked+4]
    if verbose:
        print("read data:")
        print(read_data)
    b = BytesIO()
    b.write(read_data[4:size_unpacked+4])
    b.seek(0)

    unpacked_data = msgpack.unpack(b)
    if verbose:
        print("unpacked_data:")
        print(unpacked_data)
    return unpacked_data




def test_save():
    data = b'\x10\x00\x00\x00\x82\xa4name\xa4some\xa3num\\'
    print("len data: {}".format(len(data)))
    microcontroller.nvm[0:len(data)] = data


def test_save_broken():
    b = BytesIO()
    data = b'\x10\x00\x00\x00\x82\xa4name\xa4some\xa3num\\'
    b.write(data)
    b.seek(0)
    val_to_write = b.read()
    print(val_to_write)
    print("len val: {}".format(len(val_to_write)))
    microcontroller.nvm[0:len(val_to_write)] = val_to_write

