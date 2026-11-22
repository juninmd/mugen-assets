# Coverage: Black Widow

- States: 146/147 accounted for; the rest are NOT MIGRATED rows below
- Sprites: 975/975 exported; 18 referenced by the .air but absent from the .sff (blank in M.U.G.E.N too)
- Sounds: 84/84 exported
- Commands in .cmd: 44; UMF moves: 55; abilities: 

| state | migrated as |
|---|---|
| 100 | engine common state |
| 170 | script (verbatim CNS) |
| 175 | script (verbatim CNS) |
| 180 | script (verbatim CNS) |
| 181 | script (verbatim CNS) |
| 182 | script (verbatim CNS) |
| 183 | script (verbatim CNS) |
| 190 | script (verbatim CNS) |
| 191 | script (verbatim CNS) |
| 192 | script (verbatim CNS) |
| 193 | script (verbatim CNS) |
| 194 | script (verbatim CNS) |
| 195 | script (verbatim CNS) |
| 200 | move `x` |
| 201 | move `x_x` |
| 210 | move `y` |
| 220 | shadowed: an earlier command with the same input wins (never fires in M.U.G.E.N either) |
| 221 | NOT MIGRATED (entered from state 220 `220` via changestate) |
| 230 | move `a` |
| 240 | move `b` |
| 250 | move `c` |
| 251 | broken in the original: animation 451 is missing from the .air |
| 400 | move `crouch_x` |
| 410 | move `crouch_y` |
| 420 | move `crouch_z` |
| 430 | move `crouch_a` |
| 440 | move `crouch_b` |
| 450 | move `crouch_c` |
| 451 | broken in the original: animation 451 is missing from the .air |
| 600 | move `air_x` |
| 610 | move `air_y` |
| 620 | move `air_z` |
| 630 | move `air_a` |
| 640 | move `air_b` |
| 650 | move `air_c` |
| 651 | move `air_c_z` |
| 800 | move `z` |
| 810 | partial: throw states replaced by the UMF `throw` block |
| 811 | partial: throw states replaced by the UMF `throw` block |
| 813 | partial: throw states replaced by the UMF `throw` block |
| 820 | partial: throw states replaced by the UMF `throw` block |
| 821 | partial: throw states replaced by the UMF `throw` block |
| 823 | unreachable in the original (dead code) |
| 825 | unreachable in the original (dead code) |
| 827 | unreachable in the original (dead code) |
| 828 | unreachable in the original (dead code) |
| 829 | partial: throw states replaced by the UMF `throw` block |
| 880 | move `air_ff` |
| 881 | move `air_ff` |
| 910 | unreachable in the original (dead code) |
| 948 | move `air_qcf_z` |
| 1000 | move `fdf_x` |
| 1001 | move `fdf_y` |
| 1002 | move `fdf_z` |
| 1020 | move `qcf_y` |
| 1030 | move `qcf_x` |
| 1040 | move `air_qcf_y` |
| 1050 | move `air_qcf_x` |
| 1060 | move `air_qcf_z` |
| 1090 | move `qcf_z` |
| 1100 | move `qcb_x` |
| 1101 | shadowed: an earlier command with the same input wins (never fires in M.U.G.E.N either) |
| 1110 | move `qcb_y` |
| 1120 | move `qcb_z` |
| 1130 | move `qcb_x` |
| 1200 | move `qcb_a` |
| 1201 | move `qcb_a` |
| 1202 | move `qcb_a` |
| 1203 | move `qcb_a` |
| 1210 | move `qcb_b` |
| 1211 | move `qcb_b` |
| 1212 | move `qcb_b` |
| 1213 | move `qcb_b` |
| 1220 | move `qcb_c` |
| 1221 | move `qcb_c` |
| 1222 | move `qcb_c` |
| 1223 | move `qcb_c` |
| 1300 | move `qcf_a` |
| 1310 | move `qcf_b` |
| 1313 | move `qcf_b` |
| 1320 | move `qcf_c` |
| 1323 | move `qcf_c` |
| 1324 | move `qcf_c` |
| 2999 | move `qcb_2p` |
| 3000 | move `qcf_2p` |
| 3001 | move `qcf_2p` |
| 3100 | move `qcf_2k` |
| 3101 | move `qcf_2k` |
| 3102 | move `qcf_2k` |
| 3103 | unreachable in the original (dead code) |
| 3200 | move `qcb_2p` |
| 3201 | move `qcb_2p` |
| 3202 | helper (verbatim CNS, spawned by a move) |
| 3204 | move `qcb_2p_a` |
| 3205 | move `qcb_2p` |
| 3250 | ability |
| 3251 | script (verbatim CNS) |
| 3300 | move `shield_backup` |
| 3301 | helper (verbatim CNS, spawned by a move) |
| 3302 | script (verbatim CNS) |
| 3305 | move `shield_backup` |
| 3306 | helper (verbatim CNS, spawned by a move) |
| 3307 | helper (verbatim CNS, spawned by a move) |
| 3308 | helper (verbatim CNS, spawned by a move) |
| 3309 | helper (verbatim CNS, spawned by a move) |
| 3310 | helper (verbatim CNS, spawned by a move) |
| 3311 | helper (verbatim CNS, spawned by a move) |
| 3312 | helper (verbatim CNS, spawned by a move) |
| 3313 | helper (verbatim CNS, spawned by a move) |
| 3320 | script (verbatim CNS) |
| 3360 | script (verbatim CNS) |
| 3361 | script (verbatim CNS) |
| 3362 | script (verbatim CNS) |
| 3363 | script (verbatim CNS) |
| 3364 | script (verbatim CNS) |
| 3365 | script (verbatim CNS) |
| 3366 | script (verbatim CNS) |
| 3367 | script (verbatim CNS) |
| 3368 | script (verbatim CNS) |
| 6300 | move `guardpush` |
| 6350 | helper (verbatim CNS, spawned by a move) |
| 7696 | partial: throw states replaced by the UMF `throw` block |
| 7697 | unreachable in the original (dead code) |
| 7990 | partial: throw states replaced by the UMF `throw` block |
| 7991 | partial: throw states replaced by the UMF `throw` block |
| 8900 | unreachable in the original (dead code) |
| 10001 | move `fdf_x_holdx` |
| 10002 | move `fdf_x_holdx_holdx` |
| 10011 | move `fdf_y_holdy` |
| 10012 | move `fdf_y_holdy_holdy` |
| 10021 | move `fdf_z_holdz` |
| 10022 | move `fdf_z_holdz_holdz` |
| 21100 | helper (verbatim CNS, spawned by a move) |
| 21101 | script (verbatim CNS) |
| 21102 | helper (verbatim CNS, spawned by a move) |
| 21103 | helper (verbatim CNS, spawned by a move) |
| 21109 | script (verbatim CNS) |
| 21150 | script (verbatim CNS) |
| 21155 | unreachable in the original (dead code) |
| 21160 | script (verbatim CNS) |
| 21165 | script (verbatim CNS) |
| 40001 | helper (verbatim CNS, spawned by a move) |
| 40002 | unreachable in the original (dead code) |
| 40003 | helper (verbatim CNS, spawned by a move) |
| 40004 | helper (verbatim CNS, spawned by a move) |
| 76961 | partial: throw states replaced by the UMF `throw` block |
| 76971 | unreachable in the original (dead code) |

Controllers inside migrated moves without a UMF field (dropped):

- `varset` x13
- `screenbound` x10
- `assertspecial` x7
- `posset` x2
- `removeexplod` x2
- `varadd` x1
- `hitoverride` x1
- `destroyself` x1
- `width` x1
