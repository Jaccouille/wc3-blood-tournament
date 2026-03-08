
# Changelogs


[SPOILER="Changelogs"]

[SPOILER="0.3f"]
-Added -upl mode, allowing red to set the number of unit per line
-Allowed builder control during round phase
-Removed unit description icon (which cost 99999 gold) to avoid confusion for player
-Switch ogre upgrade from items to building upgrades
[/SPOILER]

[SPOILER="0.3e"]
-(DE) increased curse range 700 -> 900
-Added grid system on building zone
-Increased afk detection from 30 to 60 seconds
[/SPOILER]

[SPOILER="0.3d"]
-disable custom interface in an attempt to prevent desync
[/SPOILER]

[SPOILER="0.3c"]
-Added Naga faction
-Added Beast faction
-Added Demon faction
-(HU) Priest now upgrades into spellbreaker rather than add them
-(HU) Reduced Slow duration from 15 to 12 seconds
-(HU) Removed magic reduction from spellbreaker, added magic defend, can deflect magic missile back to attacker
-(NE) Dryad rejuvenation has 5 stacks instead 1, price 50 -> 250 blood points
-(NE) Fixed huntress bounce reduce damage to 50%, used to not work
-(NE) Increased Wand of Illusion cost 75 -> 100
-(NE) Reduced druid of the claw dama from 40 - 70 to 35 - 65, AS from 1.5 to 2.0, improved frenzy cast behavior (only cast upon attacking)
-(OR) Reduced drunken haze & acid bomb upgrade 150 -> 100 blood points
-(UN) Increased carrion swarm cooldown from 6 to 10
-(UN) Reduced Banshee Frost Armor defensee 4 -> 3
-(UN) Reduced plague bearer price from 600 to 500 blood points
-(UN) Replaced banshee Anti Magic Shell by Frost Armor, AMS can be bought
-Ability upgrade now grants Army points & increases the affected unit bounty
-Added ability view on non-controlled units
-Added sellable upgrade mode
-Added sound upon round end
-Added spawn capacity elimnation mode (sce)
-Fixed bot message being visible to all players
-Increased elimination phase interlude from 180 to 240
-Made captain like unit spawn in the middle of the squad
-Reduced building size
-Replaced sell all ability by -sa command to avoid missclick
-Added -fog vote to enable/disable fog of war
-Following mode can now be changed between rounds by the red player, it, sc, sce, bm, apm, dm, hm, mb, bd, ser, np
[/SPOILER]

[SPOILER="0.2f"]
-(HU) Priest now dispels summoned unit upon attack for 150 damage
-(NE) Increased frenzy movement speed boost 30 -> 80%
-(NE) Reduced entagling root movement speed slow 70% -> 50%
-(UN) Changed Vampire price from 100 gold -> 50 gold + 500 blood points
-(UN) Fixed bug where non vampire unit would get the blood harvest bonus HP/Damage
-(UN) Reduced abomination armor 4 -> 0
-(UN) Reduced abomination disease cloud damage 20 -> 15
-(UN) Unholy aura heal increased from 1% max hp to 5 flat + 1% max hp
-Added tooltip when player is being controlled by bot
-Bot can be disabled by clicking around
-Fixed bug with wrong round winner
-Increased start round vote duration so it doesn't expire after 60 seconds
-Made trade gold & start round unavailable during round
-Tournament manager now moves nearby center for final round
[/SPOILER]

[SPOILER="0.2e"]
-(HU) Added bash 30% to Crusader (forgot to give the ability)
-(HU) Reduced sniper and rifleman explo ammo hp 440 -> 290
-(NE) Changed Mountain Giant armor from fortified to large, increased hp 2400 -> 2800, reduced price 300 -> 100 gold
-(NE) Increased Haunt cooldown 10 -> 15, duration 5 -> 4
-(NE) Increased taunt cd 10 -> 15 seconds
-(NE) Reduced Archdruid hp 1800 -> 1600
-(NE) Reduced BearForm HP 2400 -> 2000
-(NE) Reduced Entangling Root HP 200 -> 100, duration 10 -> 6 seconds
-(NE) Reduced Moutain giant damage by 20, its gold cost from 300 -> 200
-(NE) Reduced bear form armor 6 -> 4
-(NE) Reduced wisp hp 20 -> 10
-(NE) Removed Hardened Skin 5 from Druid of the claw
-(NE) Replaced Howl of Terror by Frenzy on Owlbear, cleave 30% by cleave 30%, reduced HP 2400 -> 1700
-(OR) Increased farseer spirit wolf cooldown 30 -> 45
-(OR) Reduced Marauder hp 1600 -> 1500, attack speed 1.5 -> 1.6
-(OR) Reduced Warmonger deflect 75% -> 30% chance to trigger
-(OR) Reduced berserk armor 5 -> 2, damage by 5, attack speed 1.3 -> 1.4
-(OR) Removed Critical Strike from marauder, added burning blade
-(UN) Added blood harvest ability to vampire & vampire lord, reduced vampire count from 3 to 1, gold cost from 300 to 100
-(UN) Added burning archer back
-(UN) Increased abom count 1 -> 5, gold cost 100 -> 300, HP 2400 -> 1400, damage 130 - 170 -> 80 -> 120
-(UN) Increased range on all raise skeleton abilities 750 -> 1000
-Added afk detector, player that haven't moved during 30 seconds after beginning of a pre-round phase will be controlled by a bot
-Added back Sell All to builder
-Blood points are now given after round end to avoid people upgrading building during the round
-Fixed -r mode, should be possible to play more than 7 rounds
-Fixed bug where blood points for winning round weren't given to winner
-Increased damage type dealt to spectra, Pierce 10 -> 20%, Normal 20 -> 50%, Siege 10 -> 50%
-Increased default interlude time 90 -> 120 seconds
-Increased quarter final preparation time 120 -> 180 seconds
-Prevented repick after random
-Reworked all unit damage so they round to 0 or 5 for better clarity
[/SPOILER]

[SPOILER="0.2d"]
-(HU) Reduced spell breaker HP from 1000 to 750
-(OR) Added Maurauder, upgrades from raider, gains critical strike
-(OR) Changed grunt & berserk armor type from large to Small
-(OR) Removed killing spree from berserker, reduced DPS, reduced HP 1000 -> 800
-(UN) Added spectral sage, upgrades from necromancer
-(UN) Reduced Vampire armor 4 -> 2, HP 1800 -> 1600
-(UN) Reduced Vampire attack speed 1.0 -> 1.2
-(UN) Reduced Vampire lord armor 8 -> 5, HP 2400 -> 2000
-(UN) Removed lifesteal from vampire & vampire lord
-Fixed bash ability
-Fixed damage & hit point multiplier mode for summoned units
-Hide sell building during round phase
[/SPOILER]

[SPOILER="0.2c"]
-(HU) Increased Priest hitpoint 140 -> 220
-(UN) Removed burning archer (it was bugged)
-(UN) Vampire lord carrion swarm damage 100 -> 75
[/SPOILER]

[SPOILER="0.2b"]
-(HU) Reduced Crusader HP 1600 -> 1300
-(HU) Reduced Rifleman HP 440 -> 290
-(NE) Increased Druid Talon DPS and HP 160 -> 210
-(NE) Modified Entangling root to spawn a  AoE slowing ward like unit
-(UN) Added disease cloud to abomination, reduced cleave from 30% -> 20%
[/SPOILER]

[SPOILER="0.2a"]
-(HU) Reduced Slow duration from 15 to 12 seconds
-(NE) Reduced moutain giant freeze after taunt cast
-(NE) Reduced starfall max damage from 600 to 400
-(UN) Increased carrion swarm cooldown from 6 to 10
-Added minimap ping on army preview position
-Can now sell upgraded buildings & buildings containing items
-Doubled unit HP, increased most ability damage
-Fixed Health Multiplier mode
-Removed bridge to smooth up army movement
-Removed sell all, added unstuck unit ability to builder
-Removed sheep sound on building move cast
-Smoothed up army movement to center
[/SPOILER]

[SPOILER="0.1y"]
-(NE) Fixed huntress bounce reduce damage to 50%, used to not work
-(NE) Reduced Avatar attack speed, armor from 7 to 4
-(NE) Reduced starfall damage from 100 to 60
-(UN) Reduced plague bearer price from 600 to 500 blood points
-Added blood donation, players may get bonus blood points after each round if they are behind in the game
-Added random hat to randomed builder
-Added ready ability on builder so player can start round earlier
-Increased all Aura area of effect from 900 to 1200
[/SPOILER]

[SPOILER="0.1x"]
-(HU) Increased soul burn cooldown from 3 to 5 seconds
-(OR) Increased Ogre Swing attack speed slow from 20 to 40%
-(UN) Increased Lich Raise Revenant from 750 to 1500
-Added more bridge to reduce unit lagging when moving to middle
-Potentially fixed desync issue with ogre
[/SPOILER]

[SPOILER="0.1w"]
-(HU) Decreased Priest HP from 160 to 70
-(HU) Increased Priest damage by 4, attack range from 400 to 650
-(HU) Increased all Priest spell range to 700
-(NE) Increased Druid of Talon HP from 60 to 80
-(NE) Increased Wand of illusion cast range from 500 to 600
-(NE) Lowered Druid of Talon damage by 6, increased attack from 400 to 550
-Fixe demi-final scoreboard bug
-Fixed spawn bug where squad spawn would stop after reaching end of line
[/SPOILER]

[SPOILER="0.1v"]
-(HU) Fixed sorc fire orb visual effect
-(HU) Increase sniper price from 50 to 100 bp
-(HU) Increased rifleman explosive ammo damage by 10
-(OR) Fixed ogre magi firebolt stun
-(OR) Reduced Witch Doctor HP from 140 to 100
-(OR) Reduced healing wave heal from 125 to 75
-(UN) Added Spawn Gut Crawler item to Abomination
-Added an army previewer to preview the units position on the arena
[/SPOILER]

[SPOILER="0.1u"]
-(HU) Replaced paladin cleave by 30% stun
-(NE) Reduced Mountain Giant damage by 30, added 20% cleave
-(OR) Replaced Witch Doctor acid bomb by healing wave as base spell
-(UN) Null damage Orb now adds 15 damage to necromancer
-Named tournament manager
-Reworked building terrain
-Units now spawn from the portal and position themselve on the battlefield
[/SPOILER]

[SPOILER="0.1t"]
-(HU) Reduced ghost paladin hp from 600 to 450
-(HU) Reduced sniper damage
-(HU) Removed paladin cleave
-(OR) new unit : Ogre magi alternative to armored Ogre
-(UN) Fixed skeleton death giving corpses
-Added total BP sum
-Added total blood point spilled at the end of the game
-Increased all projectile speed
[/SPOILER]

[SPOILER="0.1s"]
-(HU) Replaced sorc fire shield by soul burn
-(NE) Changed bear form armor from large to small
-(OR) Improved raider burning blades
-(UN) Reduced Lich revenant count from 2 to 1, improved its stats
-(UN) Replaced necro skele mage by skele Orc
-Added music for elimination pahse
-Bot now replace leaving players
-Fixed Affliction reduction speed not working
-Fixed army points tooltip display on unit item
-Fixed some tooltip
-Fixed vote system
-Reduced carrion swarm max damage
[/SPOILER]


[/SPOILER]
