# goku_ssj4_umf

Source: `goku_ss4/goku_ss4.def`

```json
{
  "anims": 130,
  "author": "Mikel8888",
  "commands": 78,
  "controllers": {
    "angledraw": 23,
    "assertspecial": 33,
    "attackmulset": 10,
    "bgpalfx": 12,
    "bindtoroot": 15,
    "changeanim": 80,
    "changestate": 147,
    "ctrlset": 7,
    "defencemulset": 2,
    "destroyself": 32,
    "envshake": 14,
    "explod": 72,
    "fallenvshake": 2,
    "forcefeedback": 16,
    "gamemakeanim": 3,
    "gravity": 2,
    "helper": 34,
    "hitdef": 15,
    "hitfalldamage": 2,
    "hitfallset": 1,
    "hitfallvel": 1,
    "hitoverride": 2,
    "hitvelset": 8,
    "nothitby": 9,
    "null": 1,
    "palfx": 4,
    "parentvarset": 2,
    "pause": 2,
    "playerpush": 1,
    "playsnd": 82,
    "posadd": 4,
    "posfreeze": 2,
    "posset": 15,
    "poweradd": 1,
    "removeexplod": 6,
    "selfstate": 1,
    "statetypeset": 34,
    "stopsnd": 10,
    "superpause": 10,
    "trans": 27,
    "turn": 5,
    "varadd": 16,
    "varrandom": 1,
    "varrangeset": 2,
    "varset": 40,
    "veladd": 18,
    "velmul": 9,
    "velset": 42
  },
  "def": "goku_ss4/goku_ss4.def",
  "engine": "goku_ss4/goku_ss4.def: 0 unsupported controllers, 1 unknown triggers, 4 unknown parameters, 0 unknown AssertSpecial flags\n",
  "files": {
    "cmd": "Goku_SS4.cmd",
    "cns": "Goku_SS4.cns",
    "st": [
      "IA.cns",
      "Especiales.cns",
      "Supers.cns"
    ],
    "stcommon": "common1.cns"
  },
  "localcoord": null,
  "mugenversion": "1.0",
  "name": "Goku",
  "palettes": 6,
  "routes": [
    {
      "command": "FF",
      "cost": 0,
      "input": "F, F",
      "state": 60,
      "when": "stand"
    },
    {
      "command": "BB",
      "cost": 0,
      "input": "B, B",
      "state": 70,
      "when": "stand"
    },
    {
      "command": "Super Jump",
      "cost": 0,
      "input": "~D,U",
      "state": 80,
      "when": "stand"
    },
    {
      "command": "SUPER1",
      "cost": 3000,
      "input": "~D,DF,F,D,DF,F,a+b",
      "state": 3000,
      "when": "stand"
    },
    {
      "command": "SPECIAL 8",
      "cost": 1500,
      "input": "~F,DF,D,DB,B,a",
      "state": 1600,
      "when": "stand"
    },
    {
      "command": "SPECIAL 1",
      "cost": 500,
      "input": "~D,DF,F,a",
      "state": 1000,
      "when": "stand"
    },
    {
      "command": "SPECIAL 2",
      "cost": 500,
      "input": "~D,DB,B,a",
      "state": 1100,
      "when": "stand"
    },
    {
      "command": "SPECIAL 3",
      "cost": 1500,
      "input": "~D,DF,F,b",
      "state": 1200,
      "when": "stand"
    },
    {
      "command": "SPECIAL 4",
      "cost": 500,
      "input": "~D,DB,B,b",
      "state": 1300,
      "when": "stand"
    },
    {
      "command": "SPECIAL 12",
      "cost": 1000,
      "input": "~F,DF,D,DB,B,c",
      "state": 1700,
      "when": "stand"
    },
    {
      "command": "SPECIAL 11",
      "cost": 1500,
      "input": "~B,DB,D,DF,F,c",
      "state": 1800,
      "when": "stand"
    },
    {
      "command": "SPECIAL 5",
      "cost": 1500,
      "input": "~D,DF,F,c",
      "state": 1400,
      "when": "stand"
    },
    {
      "command": "SPECIAL 6",
      "cost": 1000,
      "input": "~D,DB,B,c",
      "state": 1500,
      "when": "stand"
    },
    {
      "command": "a",
      "cost": 0,
      "input": "a",
      "state": 200,
      "when": "stand"
    },
    {
      "command": "b",
      "cost": 0,
      "input": "b",
      "state": 300,
      "when": "stand"
    },
    {
      "command": "c",
      "cost": 200,
      "input": "c",
      "state": 400,
      "when": "stand"
    },
    {
      "command": "s",
      "cost": 0,
      "input": "s",
      "state": 500,
      "when": "stand"
    },
    {
      "command": "a",
      "cost": 0,
      "input": "a",
      "state": 600,
      "when": "air"
    },
    {
      "command": "b",
      "cost": 0,
      "input": "b",
      "state": 610,
      "when": "air"
    },
    {
      "command": "c",
      "cost": 200,
      "input": "c",
      "state": 620,
      "when": "air"
    }
  ],
  "sff": {
    "palettes": 245,
    "sprites": 763,
    "version": 1
  },
  "sounds": 104,
  "states": 113
}
```
