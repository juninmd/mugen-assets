# mugen-assets

Personagens e stages MUGEN empacotados em `.zip` para o [ultimate-mugen](https://github.com/juninmd/ultimate-mugen).

## Layout

- `chars/<Nome>.zip` contém `<Nome>/<Nome>.def` e os arquivos do personagem.
- `stages/<Nome>.zip` usa caminhos relativos à raiz do MUGEN: `stages/*.def`, `stages/*.sff` e `sound/*` (música, quando existe).

- `umf/<Nome>/` é um lutador `umf/2` do ultimate-mugen: `<id>.json` mais `sprites/*.png` (poses, `meta.json` e `01_idle.png`). `umf/<Nome>.zip` é gerado por `python tools/pack_umf.py <Nome>` e o CI confere que o zip bate com a pasta.

## Adicionar conteúdo

Todo zip em `chars/`, `stages/` ou `umf/` precisa de uma print em `previews/<chars|stages|umf>/<mesmo nome>.png`. O CI (`tools/check_previews.py`) bloqueia o PR se faltar print, se o zip estiver corrompido, se não seguir o layout acima ou se tiver caminhos absolutos/`..`.

```bash
pip install pillow numpy
python tools/preview.py chars/NovoChar.zip stages/NovoStage.zip
```

O gerador lê o `.sff` (v1 e v2): personagem mostra retrato (9000,1) e pose parada (0,0); stage monta as camadas do `[BGdef]`.

## Origem

Extraído de packs públicos no archive.org:

| Pack | Conteúdo usado |
|---|---|
| [Dragon Ball x Naruto Storm Budokai Mugen](https://archive.org/details/dragon-ball-x-naruto-storm-budokai-mugen) | 30 chars, 8 stages |
| [DC Comics Mugenation Project](https://archive.org/details/dc-comics-mugenation-project-for-android-pc-unotag.-7z) | 20 chars, 5 stages |
| [Marvel Mugenation Project 2021](https://archive.org/details/marvel-mugenation-project-2021-for-android-pc.-7z) | 20 chars, 5 stages |
| [Ferchogt X's Mugen Characters](https://archive.org/details/ferchogt-x-mugen-characters) | 2 chars (MvC2 Iori, SonSon) |
| [Pokemon Type Stage (MUGEN)](https://archive.org/details/pokemon-type-stage_202508) | 6 stages com música (Fire, Water, Ghost, Dragon, Ice, Electric) |

Personagens e stages pertencem aos seus autores originais (veja o readme dentro de cada zip). Franquias são marcas de seus donos; uso pessoal, não comercial.

## Personagens (73)

<table>
<tr><td align="center"><img src="previews/chars/Aquaman.png" width="200"><br><sub>Aquaman</sub></td><td align="center"><img src="previews/chars/Batman_Rebirth.png" width="200"><br><sub>Batman_Rebirth</sub></td><td align="center"><img src="previews/chars/BlackPanther.png" width="200"><br><sub>BlackPanther</sub></td><td align="center"><img src="previews/chars/BlackWidow.png" width="200"><br><sub>BlackWidow</sub></td></tr>
<tr><td align="center"><img src="previews/chars/CaptainAmerica.png" width="200"><br><sub>CaptainAmerica</sub></td><td align="center"><img src="previews/chars/Cell_Perfect_Form.png" width="200"><br><sub>Cell_Perfect_Form</sub></td><td align="center"><img src="previews/chars/Cyclops.png" width="200"><br><sub>Cyclops</sub></td><td align="center"><img src="previews/chars/Darkseid.png" width="200"><br><sub>Darkseid</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Deadpool.png" width="200"><br><sub>Deadpool</sub></td><td align="center"><img src="previews/chars/Deidara.png" width="200"><br><sub>Deidara</sub></td><td align="center"><img src="previews/chars/DoctorStrange.png" width="200"><br><sub>DoctorStrange</sub></td><td align="center"><img src="previews/chars/Doctor_Doom.png" width="200"><br><sub>Doctor_Doom</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Freezer_4_Form.png" width="200"><br><sub>Freezer_4_Form</sub></td><td align="center"><img src="previews/chars/Future_Trunks.png" width="200"><br><sub>Future_Trunks</sub></td><td align="center"><img src="previews/chars/Ghost_Rider.png" width="200"><br><sub>Ghost_Rider</sub></td><td align="center"><img src="previews/chars/Gohan_Teen_SS2.png" width="200"><br><sub>Gohan_Teen_SS2</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Gohan_Ultimate.png" width="200"><br><sub>Gohan_Ultimate</sub></td><td align="center"><img src="previews/chars/Goku_Base.png" width="200"><br><sub>Goku_Base</sub></td><td align="center"><img src="previews/chars/Goku_SS.png" width="200"><br><sub>Goku_SS</sub></td><td align="center"><img src="previews/chars/Goku_SS2.png" width="200"><br><sub>Goku_SS2</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Goku_SS3.png" width="200"><br><sub>Goku_SS3</sub></td><td align="center"><img src="previews/chars/Goku_SS4.png" width="200"><br><sub>Goku_SS4</sub></td><td align="center"><img src="previews/chars/GreenArrow_G.png" width="200"><br><sub>GreenArrow_G</sub></td><td align="center"><img src="previews/chars/Hashirama.png" width="200"><br><sub>Hashirama</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Hawkeye.png" width="200"><br><sub>Hawkeye</sub></td><td align="center"><img src="previews/chars/Hiruzen.png" width="200"><br><sub>Hiruzen</sub></td><td align="center"><img src="previews/chars/IncredibleHulk.png" width="200"><br><sub>IncredibleHulk</sub></td><td align="center"><img src="previews/chars/Ironman.png" width="200"><br><sub>Ironman</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Itachi.png" width="200"><br><sub>Itachi</sub></td><td align="center"><img src="previews/chars/Jiraiya.png" width="200"><br><sub>Jiraiya</sub></td><td align="center"><img src="previews/chars/JohnStewartwil.png" width="200"><br><sub>JohnStewartwil</sub></td><td align="center"><img src="previews/chars/Kid_Buu.png" width="200"><br><sub>Kid_Buu</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Krilin.png" width="200"><br><sub>Krilin</sub></td><td align="center"><img src="previews/chars/Lobo.png" width="200"><br><sub>Lobo</sub></td><td align="center"><img src="previews/chars/Loki.png" width="200"><br><sub>Loki</sub></td><td align="center"><img src="previews/chars/Madara_Revived.png" width="200"><br><sub>Madara_Revived</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Magneto.png" width="200"><br><sub>Magneto</sub></td><td align="center"><img src="previews/chars/MartianManhunter.png" width="200"><br><sub>MartianManhunter</sub></td><td align="center"><img src="previews/chars/Minato.png" width="200"><br><sub>Minato</sub></td><td align="center"><img src="previews/chars/MvC2_Cyborg.png" width="200"><br><sub>MvC2_Cyborg</sub></td></tr>
<tr><td align="center"><img src="previews/chars/MvC_DeathstrokeEO.png" width="200"><br><sub>MvC_DeathstrokeEO</sub></td><td align="center"><img src="previews/chars/MvC_Harley_Quinn.png" width="200"><br><sub>MvC_Harley_Quinn</sub></td><td align="center"><img src="previews/chars/Naruto_Sennin.png" width="200"><br><sub>Naruto_Sennin</sub></td><td align="center"><img src="previews/chars/Naruto_Start.png" width="200"><br><sub>Naruto_Start</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Nightwing_MvC.png" width="200"><br><sub>Nightwing_MvC</sub></td><td align="center"><img src="previews/chars/Obito.png" width="200"><br><sub>Obito</sub></td><td align="center"><img src="previews/chars/Orochimaru.png" width="200"><br><sub>Orochimaru</sub></td><td align="center"><img src="previews/chars/Pain.png" width="200"><br><sub>Pain</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Piccolo.png" width="200"><br><sub>Piccolo</sub></td><td align="center"><img src="previews/chars/Sasuke_Akatsuki.png" width="200"><br><sub>Sasuke_Akatsuki</sub></td><td align="center"><img src="previews/chars/Shazam_G.png" width="200"><br><sub>Shazam_G</sub></td><td align="center"><img src="previews/chars/Silver_surfer.png" width="200"><br><sub>Silver_surfer</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Spiderman.png" width="200"><br><sub>Spiderman</sub></td><td align="center"><img src="previews/chars/Storm.png" width="200"><br><sub>Storm</sub></td><td align="center"><img src="previews/chars/Supergirl.png" width="200"><br><sub>Supergirl</sub></td><td align="center"><img src="previews/chars/Thanos.png" width="200"><br><sub>Thanos</sub></td></tr>
<tr><td align="center"><img src="previews/chars/TheFlashnew52.png" width="200"><br><sub>TheFlashnew52</sub></td><td align="center"><img src="previews/chars/The_Joker.png" width="200"><br><sub>The_Joker</sub></td><td align="center"><img src="previews/chars/Thor_Odinson.png" width="200"><br><sub>Thor_Odinson</sub></td><td align="center"><img src="previews/chars/Tobirama.png" width="200"><br><sub>Tobirama</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Trunks_Future_SS.png" width="200"><br><sub>Trunks_Future_SS</sub></td><td align="center"><img src="previews/chars/Tsunade.png" width="200"><br><sub>Tsunade</sub></td><td align="center"><img src="previews/chars/Vegeta_Majin.png" width="200"><br><sub>Vegeta_Majin</sub></td><td align="center"><img src="previews/chars/Venom.png" width="200"><br><sub>Venom</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Wolverine.png" width="200"><br><sub>Wolverine</sub></td><td align="center"><img src="previews/chars/Wonder_Woman_New52.png" width="200"><br><sub>Wonder_Woman_New52</sub></td><td align="center"><img src="previews/chars/bane.png" width="200"><br><sub>bane</sub></td><td align="center"><img src="previews/chars/blackadam.png" width="200"><br><sub>blackadam</sub></td></tr>
<tr><td align="center"><img src="previews/chars/doomsday.png" width="200"><br><sub>doomsday</sub></td><td align="center"><img src="previews/chars/superman.png" width="200"><br><sub>superman</sub></td></tr>
<tr><td align="center"><img src="previews/chars/Goku_SSJ4_Vision.png" width="200"><br><sub>Goku_SSJ4_Vision</sub></td></tr>
<tr><td align="center"><img src="previews/chars/MvC2_Iori.png" width="200"><br><sub>MvC2_Iori</sub></td><td align="center"><img src="previews/chars/MvC2_Sonson.png" width="200"><br><sub>MvC2_Sonson</sub></td></tr>
</table>

## Stages (24)

<table>
<tr><td align="center"><img src="previews/stages/Academia_Ninja.png" width="260"><br><sub>Academia_Ninja</sub></td><td align="center"><img src="previews/stages/AvengersDay_1.1Zoom.png" width="260"><br><sub>AvengersDay_1.1Zoom</sub></td><td align="center"><img src="previews/stages/Campo3.png" width="260"><br><sub>Campo3</sub></td></tr>
<tr><td align="center"><img src="previews/stages/DarkCerebro-X3TOG%28GBA%29_1.1Zoom.png" width="260"><br><sub>DarkCerebro-X3TOG(GBA)_1.1Zoom</sub></td><td align="center"><img src="previews/stages/Examendechunnin.png" width="260"><br><sub>Examendechunnin</sub></td><td align="center"><img src="previews/stages/Gotham-City.png" width="260"><br><sub>Gotham-City</sub></td></tr>
<tr><td align="center"><img src="previews/stages/Grand_Fisher_Stage.png" width="260"><br><sub>Grand_Fisher_Stage</sub></td><td align="center"><img src="previews/stages/Hall_of_Justice.png" width="260"><br><sub>Hall_of_Justice</sub></td><td align="center"><img src="previews/stages/HydraAircraftBase_1.1Zoom.png" width="260"><br><sub>HydraAircraftBase_1.1Zoom</sub></td></tr>
<tr><td align="center"><img src="previews/stages/KryptonDestroyed.png" width="260"><br><sub>KryptonDestroyed</sub></td><td align="center"><img src="previews/stages/LTDsLexcorpDemolished.png" width="260"><br><sub>LTDsLexcorpDemolished</sub></td><td align="center"><img src="previews/stages/OscorpLab_1.1Zoom.png" width="260"><br><sub>OscorpLab_1.1Zoom</sub></td></tr>
<tr><td align="center"><img src="previews/stages/WayneManorRuins_1.1Zoom.png" width="260"><br><sub>WayneManorRuins_1.1Zoom</sub></td><td align="center"><img src="previews/stages/dbcity.png" width="260"><br><sub>dbcity</sub></td><td align="center"><img src="previews/stages/dbnamek.png" width="260"><br><sub>dbnamek</sub></td></tr>
<tr><td align="center"><img src="previews/stages/dbz_kame_house.png" width="260"><br><sub>dbz_kame_house</sub></td><td align="center"><img src="previews/stages/tenkaichiHR.png" width="260"><br><sub>tenkaichiHR</sub></td><td align="center"><img src="previews/stages/xmagneto.png" width="260"><br><sub>xmagneto</sub></td></tr>
<tr><td align="center"><img src="previews/stages/Pokemon_FireType.png" width="260"><br><sub>Pokemon_FireType</sub></td><td align="center"><img src="previews/stages/Pokemon_WaterType.png" width="260"><br><sub>Pokemon_WaterType</sub></td><td align="center"><img src="previews/stages/Pokemon_GhostType.png" width="260"><br><sub>Pokemon_GhostType</sub></td><td align="center"><img src="previews/stages/Pokemon_DragonType.png" width="260"><br><sub>Pokemon_DragonType</sub></td></tr>
<tr><td align="center"><img src="previews/stages/Pokemon_IceType.png" width="260"><br><sub>Pokemon_IceType</sub></td><td align="center"><img src="previews/stages/Pokemon_ElectricType.png" width="260"><br><sub>Pokemon_ElectricType</sub></td></tr>
</table>

## Lutadores UMF (3)

<table>
<tr><td align="center"><img src="previews/umf/BlackWidow_UMF.png" width="260"><br><sub>BlackWidow_UMF</sub></td><td align="center"><img src="previews/umf/Goku_SSJ4_UMF.png" width="260"><br><sub>Goku_SSJ4_UMF</sub></td><td align="center"><img src="previews/umf/Goku_SSJ4_Vision_UMF.png" width="260"><br><sub>Goku_SSJ4_Vision_UMF (_Vision)</sub></td></tr>
</table>
