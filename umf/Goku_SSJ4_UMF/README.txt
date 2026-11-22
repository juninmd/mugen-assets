Goku SSJ4 UMF

Exact migration of the M.U.G.E.N pack Goku_SS4 (chars/Goku_SS4.zip) made with ultimate-mugen tools/mugen2umf: original states, commands and animations load through the same engine path as the M.U.G.E.N original. Art and sounds belong to the pack's authors; personal, non-commercial use.

UMF layer on top (tools/mugen2umf/overlays):
- Ryu Ken dragon (state 3050) homes in on the nearest living foe in 2D, turns around when the foe is behind and slows on contact. Needs the engine NearestFoe redirection.
- Skill afterimage trails (Ryu Ken, Shunkan Ido, Kamehameha variants, Explosive Wave, Super Energy Blast) through Statedef -2.

parity.md shows the move by move comparison: only state 3050 and -2 differ on purpose.
Rebuild: mugen2umf convert chars/Goku_SS4.zip umf/Goku_SSJ4_UMF --id goku_ssj4_umf --name "Goku SSJ4" --extra <overlays as scripts.cns, override true>
