Goku SSJ4 UMF

umf/2 fighter for ultimate-mugen, converted from the public M.U.G.E.N pack "Goku SSJ4" with mugen2umf.py
(ultimate-mugen .agents/skills/mugen-to-ume-migrator). Original art and sounds belong to the pack's authors; personal, non-commercial use.

Faithful to the original: sprites 1:1 at the original size, Clsn1/Clsn2 hit and hurt boxes, the original moves and commands
(SSJ sequences, kamehameha, chou and x10 kamehameha, ki blasts, teleports, flight, Meteor attacks, Super Genki Dama, throw),
and the original voice and effect sounds (sprites/snd_*.wav). UMF additions on top (rebuilt with --extra): Instant Transmission (B, F, x), Meteor Rush (B, F, a), Dragon Rise,
Dash Strike, Ki Volley, Dragon Fist, Escape Burst, afterimage clone (F, B, F), Limit Breaker form with Limit Kamehameha,
flight (b+c), and normal chains (x x x, a a a, y y, crouch and air jabs), strings (B+x, B+z, B+y), overhead, launcher,
dive kick and slide.

Rebuild: python3 mugen2umf.py <Goku-Ssj4> umf/Goku_SSJ4_UMF --id goku_ssj4_umf --name "Goku SSJ4" --extra tools/goku_ssj4_extra.json
Every SFF sprite and .snd sound is exported. Intro/taunt run the original CNS (intro text and sound). Ki charge: hold R (Start),
with the original start, loop and end animations and sounds; taunt moved to x+y. coverage.md lists the fate of every state.

Needs an ultimate-mugen build with the converter parity PR (fly moves, charge start/end, hitNow, landAt) and the motion fields (velMul, velAdd, posFreeze, posSet, palFx).
