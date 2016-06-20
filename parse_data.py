#!/usr/bin/env python

from MMPBSA_mods import API as MMPBSA_API

data = MMPBSA_API.load_mmpbsa_info('_MMPBSA_info')
decomp_data = data['decomp']['gb']['complex']['TDC']

# update to your residue number, start from 1
print(decomp_data[1])
