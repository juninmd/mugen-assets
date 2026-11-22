Black Widow UMF

umf/2 fighter for ultimate-mugen, converted from the public M.U.G.E.N pack "Black Widow" (Arkady, NIco & Hyper) with
tools/mugen2umf (ultimate-mugen). Original art and sounds belong to the pack's authors; personal, non-commercial use.

Faithful to the original: every SFF sprite 1:1 (SFF v1 shared palettes fixed, so the Avengers super background, gas, ice
and lightning effects keep their colours), Clsn1/Clsn2 boxes, the original commands and moves (Widow's Bite on the ground
and in the air, Widow's Sting with the hold-to-charge elemental bullets, Gas Grenade, Deadly Spin, Widow's Strike, Eat Lead,
Down the Barrel, Widow's Dance, throw, air dash, push block, normals and chains), the helpers (grenades, bullets, sniper port,
super backgrounds) running their original CNS, the -2/-3 global states and every original sound.

UMF additions (tools/black_widow_extra.json), MCU-inspired, using only the pack's own sprites and sounds:
- Widow's Bite: Overload (F, D, DF, x+y, 1 bar): three electric darts that stun (lightning element).
- Widow's Line (B, F, c): grapple line, zips behind the opponent into a shocking roundhouse.
- S.H.I.E.L.D. Backup (D, DB, B, a+b, 1 bar): the Hyper4 the authors left commented out in the .cmd, unlocked:
  Agent Coulson's truck and the strike team, with the Avengers super background.
- Red Ledger (D, DF, F, D, DF, F, x+y, 3 bars): ultimate; vanishes, reappears behind and runs the full Deadly Spin chain.
- Move names, profile (en/pt/es), intro, taunt and win quote.

Rebuild: python3 tools/mugen2umf convert <BlackWidow> umf/BlackWidow_UMF --id black_widow --name "Black Widow" --extra tools/black_widow_extra.json
coverage.md lists the fate of every state (146/147; state 221 is only reached from 220, whose command is shadowed in the original .cmd).

Needs an ultimate-mugen build with the mugen2umf unification PR (spawn, followUp command/release, ownSound).
