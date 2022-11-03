# PNG Spliter
This script delete identical pixels using a pattern.
### Prerequiments
1. Install Pillow<br/>
`CC="cc -mavx2" pip install pillow-simd`<br/>
If you CPU don't support AVX2:<br/>
`pip install pillow-simd`
2. Place pattern.png near the script
### Usage
`pngspliter a.png b.png c.png`<br/>
This command return a_out.png, b_out.png, c_out.png
