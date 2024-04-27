# Warcraft 3 - Blood Tournament Reloaded

This is a remade version of the Blood tournament map playable on Warcraft III v1.36 with my personal touch.

## Gameplay

Players construct buildings that spawn groups of units in 7 free-for-all rounds.
![24-03-10-19-52-18](https://github.com/Jaccouille/wc3-blood-tournament/assets/7768858/c2c7dc47-1bf2-4460-81a3-ba8657c6dbe4)

You earn blood points by killing enemy units which can be spent to build or upgrade your units.
Featuring big battles and a lot of blood.

Choose a faction amongst Human, Orc, Undead, or Night Elf.
Experiment with different builds and find the optimal army composition.

Enjoy the mayhem!

### Game modes
This version features multiple game modes to add some degree of replayability.

Red player has 60 seconds to choose the mode from the following list.
![24-03-10-18-23-31](https://github.com/Jaccouille/wc3-blood-tournament/assets/7768858/7a368477-17c1-4d2c-86c9-e1c82f1d8d40)

Mode can be set in one line using the following syntax
```
-r 0 -hm 0.5 -dm 2 -sg 10000 -sb 100000 -d
```

### Upgrade through items
This version features an upgrade system using items bought by the building, you can :
- Add/replace an ability on a unit
- Add additional units to spawn
- Replace spawned units with another

Example:
- A 10x Footman building can add a captain and gain defend ability.
![24-03-10-18-30-17](https://github.com/Jaccouille/wc3-blood-tournament/assets/7768858/7316335d-88a1-4286-a56a-c7a829f87c6b)

### Bots

This game can be played with computer players, they only build random things.

You can type -bot to be controlled by a bot.

### Known Issues

Blizzard released a patch in November that impacted performance, this game can drop below 10 FPS with a high amount of units starting around 5.
Desync may occur.

Code may also simply unoptimized.


### Source
The map is made with [Wurstlang](https://wurstlang.org/) and is open source.

### Credits
For sharing [Wurstlang](https://wurstlang.org/) related knowledge and code: [Frotty](https://www.hiveworkshop.com/members/frotty.163331/), [Quazz](https://www.hiveworkshop.com/members/thequazz.256508/), Master-Troll, [Overkane](https://www.hiveworkshop.com/members/overkane.203829/)

For answering editor/trigger related questions : [Duckfarter](https://www.hiveworkshop.com/members/duckfarter.273864/), [raypack](https://www.hiveworkshop.com/members/raypack.290205/), [Chaosium](https://www.hiveworkshop.com/members/chaosium.221526/), [Gnuoy](https://www.hiveworkshop.com/members/gnuoy.144926/)

For making a cool Star Wars Blood Tournament map that inspired me to make this: Baal

#### Models:

[General Frank](https://www.hiveworkshop.com/members/127492/') : [Orb of blood](https://www.hiveworkshop.com/members/142431/https://www.hiveworkshop.com/threads/orb-of-blood.106236/), (edited to reduce rotation speed)

[Ujimasa Hojo](https://www.hiveworkshop.com/members/142431/) (edited his paladin model, changed material type to additive or something to make a ghost paladin),

Found demon pillar here: [UTM Outland](https://www.hiveworkshop.com/threads/outland-utm.152344/), made by [Dan van Ohllus](https://www.hiveworkshop.com/forums/members/Dan%20van%20Ohllus/)

## Developping
### Setup
Install [Wurstlang](https://wurstlang.org/start)

Once it's done, simply clone the project and update it to download the dependencies :

- Using CLI, run `grill install`

- Using WurstSetup (Graphical User Interface), open the `wurst.build` file and click on `Update Project`
