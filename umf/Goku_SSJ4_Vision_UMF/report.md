# goku_ssj4_vision_umf

Source: `goku_ssj4_vision/goku_ssj4_vision.def`

```json
{
  "anims": 168,
  "author": "_Vision",
  "commands": 65,
  "controllers": {
    "afterimage": 28,
    "afterimagetime": 24,
    "assertspecial": 7,
    "changeanim": 13,
    "changeanim2": 3,
    "changestate": 208,
    "ctrlset": 9,
    "envcolor": 8,
    "envshake": 13,
    "explod": 47,
    "hitby": 1,
    "hitdef": 68,
    "hitvelset": 1,
    "lifeadd": 2,
    "nothitby": 9,
    "null": 2,
    "palfx": 1,
    "playerpush": 1,
    "playsnd": 136,
    "posadd": 23,
    "posfreeze": 6,
    "posset": 3,
    "poweradd": 4,
    "powerset": 1,
    "projectile": 15,
    "removeexplod": 1,
    "screenbound": 2,
    "selfstate": 3,
    "superpause": 12,
    "targetbind": 3,
    "targetlifeadd": 1,
    "targetstate": 1,
    "turn": 7,
    "varrandom": 1,
    "varset": 8,
    "veladd": 14,
    "velmul": 3,
    "velset": 60
  },
  "def": "goku_ssj4_vision/goku_ssj4_vision.def",
  "engine": "goku_ssj4_vision/goku_ssj4_vision.def: 0 unsupported controllers, 0 unknown triggers, 42 unknown parameters, 0 unknown AssertSpecial flags\n",
  "files": {
    "cmd": "gokussj4.cmd",
    "cns": "gokussj4.cns",
    "st": [
      "gokussj4-final.cns",
      "gokussj4-story-intros.cns"
    ],
    "stcommon": null
  },
  "localcoord": null,
  "mugenversion": "06,27,2000",
  "name": "Goku Ssj4",
  "palettes": 5,
  "routes": [
    {
      "command": "balao11",
      "cost": 0,
      "input": "/B, a",
      "state": 800,
      "when": "stand"
    },
    {
      "command": "balao22",
      "cost": 0,
      "input": "/B, b",
      "state": 800,
      "when": "stand"
    },
    {
      "command": "balao33",
      "cost": 0,
      "input": "/B, c",
      "state": 800,
      "when": "stand"
    },
    {
      "command": "balao1",
      "cost": 0,
      "input": "/F, a",
      "state": 800,
      "when": "stand"
    },
    {
      "command": "balao2",
      "cost": 0,
      "input": "/F, b",
      "state": 800,
      "when": "stand"
    },
    {
      "command": "balao3",
      "cost": 0,
      "input": "/F, c",
      "state": 800,
      "when": "stand"
    },
    {
      "command": "slash1",
      "cost": 0,
      "input": "F, D, x",
      "state": 615,
      "when": "air"
    },
    {
      "command": "slash2",
      "cost": 0,
      "input": "F, D, y",
      "state": 615,
      "when": "air"
    },
    {
      "command": "slash3",
      "cost": 0,
      "input": "F, D, z",
      "state": 615,
      "when": "air"
    },
    {
      "command": "slash11",
      "cost": 0,
      "input": "D, x",
      "state": 615,
      "when": "air"
    },
    {
      "command": "slash22",
      "cost": 0,
      "input": "D, y",
      "state": 615,
      "when": "air"
    },
    {
      "command": "slash33",
      "cost": 0,
      "input": "D, z",
      "state": 615,
      "when": "air"
    },
    {
      "command": "punch_d",
      "cost": 0,
      "input": "~D, DF, F, x",
      "state": 2992,
      "when": "stand"
    },
    {
      "command": "ssj sequence",
      "cost": 0,
      "input": "~F, B, a",
      "state": 1050,
      "when": "stand"
    },
    {
      "command": "ssj sequence2",
      "cost": 0,
      "input": "~F, B, b",
      "state": 2050,
      "when": "stand"
    },
    {
      "command": "ssj sequence3",
      "cost": 0,
      "input": "~F, B, c",
      "state": 2070,
      "when": "stand"
    },
    {
      "command": "s_soco",
      "cost": 0,
      "input": "D, DF, F, b",
      "state": 1020,
      "when": "stand"
    },
    {
      "command": "xbaikamehameha",
      "cost": 2800,
      "input": "~D, DB, B, F, c",
      "state": 1900,
      "when": "stand"
    },
    {
      "command": "fireball",
      "cost": 0,
      "input": "~D, DF, F, x",
      "state": 1000,
      "when": "stand"
    },
    {
      "command": "fireballb",
      "cost": 0,
      "input": "~D, DB, B, z",
      "state": 1099,
      "when": "stand"
    },
    {
      "command": "fireball3",
      "cost": 10,
      "input": "~B, F, B, z",
      "state": 1390,
      "when": "stand"
    },
    {
      "command": "fireball3b",
      "cost": 10,
      "input": "~F, B, F, z",
      "state": 2390,
      "when": "stand"
    },
    {
      "command": "airchokamehameha",
      "cost": 1800,
      "input": "~D, DB, B, F, b",
      "state": 31800,
      "when": "stand"
    },
    {
      "command": "airkamehameha",
      "cost": 1000,
      "input": "~D, DB, B, F, a",
      "state": 31700,
      "when": "stand"
    },
    {
      "command": "a",
      "cost": 0,
      "input": "a",
      "state": 300,
      "when": "stand"
    },
    {
      "command": "b",
      "cost": 0,
      "input": "b",
      "state": 301,
      "when": "stand"
    },
    {
      "command": "c",
      "cost": 0,
      "input": "c",
      "state": 302,
      "when": "stand"
    },
    {
      "command": "x",
      "cost": 0,
      "input": "x",
      "state": 310,
      "when": "stand"
    },
    {
      "command": "y",
      "cost": 0,
      "input": "y",
      "state": 330,
      "when": "stand"
    },
    {
      "command": "z",
      "cost": 0,
      "input": "z",
      "state": 340,
      "when": "stand"
    },
    {
      "command": "fly",
      "cost": 0,
      "input": "a+x",
      "state": 3001,
      "when": "air"
    },
    {
      "command": "fly",
      "cost": 0,
      "input": "a+x",
      "state": 3115,
      "when": "stand"
    },
    {
      "command": "m_atack",
      "cost": 3000,
      "input": "b, b, F, b",
      "state": 4010,
      "when": "stand"
    },
    {
      "command": "m_atack2",
      "cost": 2000,
      "input": "y, y, F, y",
      "state": 6010,
      "when": "stand"
    },
    {
      "command": "supergenkidama",
      "cost": 2000,
      "input": "~B, D, c",
      "state": 47800,
      "when": "stand"
    },
    {
      "command": "Dragon_Fist",
      "cost": 1700,
      "input": "~D, F, D, F, b",
      "state": 3030,
      "when": "stand"
    },
    {
      "command": "charge",
      "cost": 0,
      "input": "/a",
      "state": 730,
      "when": "stand"
    },
    {
      "command": "teleport_a",
      "cost": 0,
      "input": "~B, D, B, x",
      "state": 7500,
      "when": "stand"
    },
    {
      "command": "airteleport_a",
      "cost": 0,
      "input": "~B, F, B, y",
      "state": 7550,
      "when": "stand"
    },
    {
      "command": "airteleport_b",
      "cost": 0,
      "input": "~F, B, F, y",
      "state": 7535,
      "when": "stand"
    },
    {
      "command": "teleport_a2",
      "cost": 0,
      "input": "~D, z",
      "state": 7510,
      "when": "stand"
    },
    {
      "command": "teleport_b",
      "cost": 0,
      "input": "~F, D, F, y",
      "state": 7520,
      "when": "stand"
    },
    {
      "command": "teleport_b2",
      "cost": 0,
      "input": "~D, y",
      "state": 7530,
      "when": "stand"
    },
    {
      "command": "kamehameha",
      "cost": 1000,
      "input": "~D, DB, B, F, a",
      "state": 1700,
      "when": "stand"
    },
    {
      "command": "chokamehameha",
      "cost": 1900,
      "input": "~D, DB, B, F, b",
      "state": 1800,
      "when": "stand"
    },
    {
      "command": "FF",
      "cost": 0,
      "input": "F, F",
      "state": 100,
      "when": "stand"
    },
    {
      "command": "BB",
      "cost": 0,
      "input": "B, B",
      "state": 105,
      "when": "stand"
    },
    {
      "command": "punch_d2",
      "cost": 0,
      "input": "~D, DF, F, a",
      "state": 3210,
      "when": "stand"
    },
    {
      "command": "start",
      "cost": 0,
      "input": "s",
      "state": 195,
      "when": "stand"
    },
    {
      "command": "x",
      "cost": 0,
      "input": "x",
      "state": 400,
      "when": "crouch"
    },
    {
      "command": "y",
      "cost": 0,
      "input": "y",
      "state": 410,
      "when": "crouch"
    },
    {
      "command": "z",
      "cost": 0,
      "input": "z",
      "state": 440,
      "when": "crouch"
    },
    {
      "command": "a",
      "cost": 0,
      "input": "a",
      "state": 430,
      "when": "crouch"
    },
    {
      "command": "b",
      "cost": 0,
      "input": "b",
      "state": 435,
      "when": "crouch"
    },
    {
      "command": "c",
      "cost": 0,
      "input": "c",
      "state": 437,
      "when": "crouch"
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
      "state": 601,
      "when": "air"
    },
    {
      "command": "c",
      "cost": 0,
      "input": "c",
      "state": 602,
      "when": "air"
    },
    {
      "command": "x",
      "cost": 0,
      "input": "x",
      "state": 610,
      "when": "air"
    },
    {
      "command": "y",
      "cost": 0,
      "input": "y",
      "state": 611,
      "when": "air"
    },
    {
      "command": "z",
      "cost": 0,
      "input": "z",
      "state": 612,
      "when": "air"
    }
  ],
  "sff": {
    "palettes": 3,
    "sprites": 198,
    "version": 1
  },
  "sounds": 19,
  "states": 114
}
```
