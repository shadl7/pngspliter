#!/usr/bin/env python
# Copyright (C) Shadl7
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# GNU Lesser General Public Licence is available at
# http://www.gnu.org/copyleft/lesser.html

from PIL import Image
from sys import argv
infile = Image.open(argv[1])
pattern = Image.open("pattern.png")
infile.load()
pattern.load()
infile = infile.convert("RGB")
pattern = pattern.convert("RGB")
infile.putalpha(0)
pattern.putalpha(0)

for i in range(0, infile.size[0]):
    for j in range(0, infile.size[1]):
        if infile.getpixel((i, j)) == pattern.getpixel((i, j)):
            infile.putpixel((i, j), (0, 0, 0, 255))

infile.save(argv[1].split(".")[0] + "_out.png")
