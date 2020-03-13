# vbf_parser
Read VBF files (firmware for automotive MCUs)

# VBF Format Overview

VBF contains one header block and one (or multiple) data blocks.

The header block is a text section, something like:

```some text ... header {\r\n some text ... ;\r\n}```

The header is immediately followed by data blocks.

Every data block contains:

* ECU memory address, uint32_t, big endian
* block data length, uint32_t, big endian
* block data
* checksum, CRC16 CCITT, big endian

# Installation

The script requires Python 2, pip, and the "intelhex" module.

On a Debian/Ubuntu-based system, run the following:
```
sudo apt install python2 pip
pip install intelhex
```
