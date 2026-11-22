# Parity report: Goku SSJ4

**Goku SSJ4: DIFFERS | data sections identical 8/9 | moves identical 19/20**

Every move is played from its real input on the original M.U.G.E.N fighter and on the UMF bundle, 150 ticks each, and every tick of both fighters (state, animation, frame, position, velocity, control, life, power, helpers, sounds) is compared.

## Data

| section | compared | different | examples |
|---|---|---|---|
| anims | 130 | 0 |  |
| commands | 78 | 0 |  |
| constants | 82 | 0 |  |
| frame | 1 | 0 |  |
| indexed | 761 | 0 |  |
| palettes | 251 | 0 |  |
| sounds | 104 | 0 |  |
| sprites | 761 | 0 |  |
| states | 113 | 2 | -2: different; 3050: different |

## Moves

| command | input | when | state | reached | states visited | damage | sounds | result |
|---|---|---|---|---|---|---|---|---|
| FF | `F, F` | stand | 60 | yes | [20, 0, 60, 12, 0] | 0 | 1 | identical |
| BB | `B, B` | stand | 70 | yes | [20, 0, 70, 12, 0] | 0 | 1 | identical |
| Super Jump | `~D,U` | stand | 80 | no | [10, 11, 12, 0] | 0 | 0 | identical |
| SUPER1 | `~D,DF,F,D,DF,F,a+b` | stand | 3000 | yes | [10, 11, 12, 3000] | 168 | 61 | diverges at tick 109 |
| SPECIAL 8 | `~F,DF,D,DB,B,a` | stand | 1600 | yes | [20, 10, 1600] | 176 | 38 | identical |
| SPECIAL 1 | `~D,DF,F,a` | stand | 1000 | yes | [10, 1000, 0] | 0 | 5 | identical |
| SPECIAL 2 | `~D,DB,B,a` | stand | 1100 | yes | [10, 1100, 0] | 0 | 5 | identical |
| SPECIAL 3 | `~D,DF,F,b` | stand | 1200 | yes | [10, 1200] | 0 | 6 | identical |
| SPECIAL 4 | `~D,DB,B,b` | stand | 1300 | yes | [10, 1300, 0] | 0 | 4 | identical |
| SPECIAL 12 | `~F,DF,D,DB,B,c` | stand | 1700 | yes | [20, 10, 1700] | 174 | 94 | identical |
| SPECIAL 11 | `~B,DB,D,DF,F,c` | stand | 1800 | yes | [20, 10, 1800] | 0 | 13 | identical |
| SPECIAL 5 | `~D,DF,F,c` | stand | 1400 | yes | [10, 1400, 0] | 0 | 6 | identical |
| SPECIAL 6 | `~D,DB,B,c` | stand | 1500 | yes | [10, 1500] | 144 | 56 | identical |
| a | `a` | stand | 200 | yes | [200, 0] | 0 | 2 | identical |
| b | `b` | stand | 300 | yes | [300, 0] | 16 | 15 | identical |
| c | `c` | stand | 400 | yes | [400, 0] | 32 | 4 | identical |
| s | `s` | stand | 500 | no | [0] | 0 | 0 | identical |
| a | `a` | air | 600 | yes | [40, 50, 600, 50, 52, 0] | 0 | 4 | identical |
| b | `b` | air | 610 | yes | [40, 50, 610, 52, 0] | 20 | 7 | identical |
| c | `c` | air | 620 | yes | [40, 50, 620, 52, 0] | 0 | 5 | identical |

### SUPER1 (tick 109)

```
original 109: [3000 3000 3 -30.000,0.000 0.000,0.000 0 1000.0 0.0] [5000 5002 0 31.000,0.000 0.000,0.000 0 99992.0 8.0] [999999 9999 0 9929.000,9999.000 0.000,0.000 0 1000.0 0.0] [560 9999 0 -30.000,0.000 0.000,0.000 0 1000.0 0.0] [999999 9999 0 -9929.000,9999.000 0.000,0.000 0 1000.0 0.0] [560 9999 0 30.000,0.000 0.000,0.000 0 1000.0 0.0] [3050 3050 0 32.000,-25.000 2.000,0.000 0 1000.0 0.0] sndS5,2666
umf      109: [3000 3000 3 -30.000,0.000 0.000,0.000 0 1000.0 0.0] [5000 5002 0 31.000,0.000 0.000,0.000 0 99992.0 8.0] [999999 9999 0 9929.000,9999.000 0.000,0.000 0 1000.0 0.0] [560 9999 0 -30.000,0.000 0.000,0.000 0 1000.0 0.0] [999999 9999 0 -9929.000,9999.000 0.000,0.000 0 1000.0 0.0] [560 9999 0 30.000,0.000 0.000,0.000 0 1000.0 0.0] [3050 3050 0 38.200,-25.359 8.200,-0.359 0 1000.0 0.0] sndS5,2666
```
