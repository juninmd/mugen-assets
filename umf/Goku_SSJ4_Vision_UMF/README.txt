Goku SSJ4 Vision UMF

Exact migration of the M.U.G.E.N pack Goku_SSJ4_Vision (chars/Goku_SSJ4_Vision.zip, by _Vision) made with ultimate-mugen tools/mugen2umf: original states, commands and animations load through the same engine path as the M.U.G.E.N original. Art and sounds belong to the pack's author; personal, non-commercial use.

UMF layer on top (tools/mugen2umf/overlays, goku_ssj4_vision_*):
- Skill afterimage trails (Shunkan Ido, Kamehameha variants, Kamehameha x10, fireball barrage, Dragon Fist, flight) through Statedef -2.
- Ki recharge: hold R (Start) to charge the power bar at 12 per tick, release or reach full power to stop (state 90200).

parity.md: the exact base is IDENTICAL to the original (61 of 61 moves); the overlays add only state 90200, the R route and the Statedef -2 trails.
Rebuild: mugen2umf convert chars/Goku_SSJ4_Vision.zip umf/Goku_SSJ4_Vision_UMF --id goku_ssj4_vision_umf --name "Goku SSJ4 Vision" --extra <goku_ssj4_vision_extra.json with the two overlays as scripts.cns, override true>
