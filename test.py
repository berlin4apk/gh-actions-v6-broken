#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from dns import resolver, rdatatype
except ImportError:
    print("We need dnspython, use pip install")


if __name__ == "__main__":
    ans = resolver.resolve("dnslabs.nl", rdatatype.SOA)
    for rdata in ans:
        print(rdata.to_text())
