# Coverage: Goku SSJ4

- States: 112/112 accounted for; the rest are NOT MIGRATED rows below
- Sprites: 198/198 exported; 96 referenced by the .air but absent from the .sff (blank in M.U.G.E.N too)
- Sounds: 19/19 exported
- Commands in .cmd: 64; UMF moves: 86; abilities: charge, fly, forms

| state | migrated as |
|---|---|
| 100 | engine common state |
| 105 | engine common state |
| 170 | script (verbatim CNS) |
| 180 | script (verbatim CNS) |
| 181 | script (verbatim CNS) |
| 182 | script (verbatim CNS) |
| 189 | script (verbatim CNS) |
| 190 | script (verbatim CNS) |
| 191 | script (verbatim CNS) |
| 192 | script (verbatim CNS) |
| 193 | script (verbatim CNS) |
| 194 | script (verbatim CNS) |
| 195 | script (verbatim CNS) |
| 200 | move `a` |
| 201 | move `b` |
| 202 | move `c` |
| 210 | move `x` |
| 230 | move `y` |
| 240 | move `z` |
| 250 | unreachable in the original (dead code) |
| 260 | unreachable in the original (dead code) |
| 270 | unreachable in the original (dead code) |
| 280 | unreachable in the original (dead code) |
| 300 | move `fly_a` |
| 301 | move `fly_b` |
| 302 | move `fly_c` |
| 310 | move `fly_x` |
| 330 | move `fly_y` |
| 340 | move `fly_z` |
| 350 | unreachable in the original (dead code) |
| 351 | unreachable in the original (dead code) |
| 400 | move `crouch_x` |
| 410 | move `crouch_y` |
| 430 | move `crouch_a` |
| 435 | move `crouch_b` |
| 437 | move `crouch_c` |
| 440 | move `crouch_z` |
| 600 | move `air_a` |
| 601 | move `air_b` |
| 602 | move `ssj_sequence3` |
| 610 | move `air_x` |
| 611 | move `air_y` |
| 612 | move `air_z` |
| 615 | move `air_slash1` |
| 616 | partial: throw states replaced by the UMF `throw` block |
| 730 | ability |
| 735 | ability |
| 740 | ability |
| 741 | ability (approximated by the native ability) |
| 800 | move `balao11` |
| 810 | partial: throw states replaced by the UMF `throw` block |
| 820 | partial: throw states replaced by the UMF `throw` block |
| 821 | partial: throw states replaced by the UMF `throw` block |
| 954 | shadowed: an earlier command with the same input wins (never fires in M.U.G.E.N either) |
| 1000 | shadowed: an earlier command with the same input wins (never fires in M.U.G.E.N either) |
| 1020 | move `ssj_sequence2` |
| 1025 | partial: throw states replaced by the UMF `throw` block |
| 1026 | partial: throw states replaced by the UMF `throw` block |
| 1027 | partial: throw states replaced by the UMF `throw` block |
| 1028 | partial: throw states replaced by the UMF `throw` block |
| 1030 | move `m_atack` |
| 1031 | move `m_atack` |
| 1041 | move `m_atack` |
| 1050 | move `ssj_sequence` |
| 1099 | move `fireballb` |
| 1390 | move `fireball3` |
| 1391 | move `fireball3` |
| 1392 | move `fireball3` |
| 1700 | shadowed: an earlier command with the same input wins (never fires in M.U.G.E.N either) |
| 1800 | shadowed: an earlier command with the same input wins (never fires in M.U.G.E.N either) |
| 1900 | move `xbaikamehameha` |
| 2050 | move `ssj_sequence2` |
| 2070 | move `ssj_sequence3` |
| 2187 | move `m_atack` |
| 2390 | move `fireball3b` |
| 2391 | move `fireball3b` |
| 2392 | move `fireball3b` |
| 2530 | move `ssj_sequence2` |
| 2730 | move `ssj_sequence3` |
| 2989 | unreachable in the original (dead code) |
| 2992 | move `punch_d` |
| 3001 | ability |
| 3030 | move `dragon_fist` |
| 3031 | move `dragon_fist` |
| 3041 | move `dragon_fist` |
| 3115 | ability |
| 3187 | move `m_atack` |
| 3188 | move `m_atack` |
| 3189 | move `m_atack` |
| 3210 | move `punch_d2` |
| 4010 | move `m_atack` |
| 4011 | move `m_atack` |
| 4012 | move `m_atack` |
| 6010 | move `m_atack2` |
| 6011 | move `m_atack2` |
| 6012 | move `m_atack2` |
| 6187 | move `m_atack2` |
| 6351 | move `m_atack2` |
| 6500 | move `m_atack2` |
| 7500 | move `teleport_a` |
| 7510 | move `teleport_a2` |
| 7520 | move `teleport_b` |
| 7530 | move `teleport_b2` |
| 7535 | move `airteleport_b` |
| 7550 | move `airteleport_a` |
| 7825 | move `supergenkidama` |
| 7899 | unreachable in the original (dead code) |
| 9797 | script (verbatim CNS) |
| 31700 | move `airkamehameha` |
| 31800 | move `airchokamehameha` |
| 47800 | move `supergenkidama` |
| 81900 | move `supergenkidama` |

Controllers inside migrated moves without a UMF field (dropped):

- `velmul` x3
- `posfreeze` x3
- `posset` x2
- `palfx` x1
