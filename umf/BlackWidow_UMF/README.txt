Black Widow UMF

umf/2 fighter for ultimate-mugen, converted from the public M.U.G.E.N pack "Black Widow" (Arkady, NIco & Hyper) with
tools/mugen2umf (ultimate-mugen, Rust, exact mode). Original art and sounds belong to the pack's authors; personal,
non-commercial use.

Exact migration: the original CNS, ST, CMD and AIR travel unchanged inside the UMF json (`mugen` block) and every SFF
sprite, palette and sound is in sprites/. The engine loads it through the same code as the M.U.G.E.N pack, so every move
plays tick for tick like the original: parity.md shows 9/9 data sections and 43/43 moves IDENTICAL.

UMF additions (tools/black_widow_extra.json), MCU-inspired, using only the pack's own sprites and sounds:
- Widow's Bite: Overload (F, D, DF, x+y, 1 bar): three electric darts that stun (native UMF move on action 1030).
- Widow's Line (B, F, c): grapple line, zips behind the opponent into a shocking roundhouse (native UMF move on action 250).
- S.H.I.E.L.D. Backup (D, DB, B, a+b, 1 bar): the Hyper4 the authors left commented out in the .cmd, unlocked.
- Red Ledger (D, DF, F, D, DF, F, x+y, 3 bars): vanishes, reappears behind and runs the original Deadly Spin (state 1320).
- Move names, profile (en/pt/es), intro, taunt and win quote.

parity.md "Added by UMF" shows each addition reached from its real input.

Rebuild: cargo run --release -p mugen2umf -- convert --src chars/BlackWidow.zip --out umf/BlackWidow_UMF --id black_widow --name "Black Widow" --extra tools/black_widow_extra.json
Needs an ultimate-mugen build with PR #982 (UMF moves on exact fighters, SFF v1 shared palette fix).
