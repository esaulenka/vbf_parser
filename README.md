# vbf_parser
Read VBF files (firmware for automotive MCUs)


VBF contains one header block and one (or multiple) data blocks.

Header is a text section, something like 
```some text ... header {\r\n some text ... ;\r\n}```
Header immediately followed by data blocks.

Every data block contains:
* ECU memory address, uint32_t, big endian
* block data length, uint32_t, big endian
* block data
* checksum, CRC16 CCITT, big endian
