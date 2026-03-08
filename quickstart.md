# Developer Quickstart

This guide walks through the concrete steps to add units, abilities, and full
factions to Blood Tournament Reloaded. Read it alongside the existing faction
files — Human is the most complete reference.

---

## 0. Coming from the World Editor?

If you have been making Warcraft III maps with the World Editor's GUI or
Object Editor, this section is for you. You do not need to be an experienced
programmer to contribute to this project, and the investment in learning
WurstScript pays off very quickly.

### The World Editor's limitations

The Object Editor is a form-based tool. To create a unit you click through
dozens of fields, one at a time. This works for a handful of units, but it
breaks down at scale:

- **Repetition with no abstraction.** If you want 10 footmen-style units that
  all share the same acquisition range, movement type, collision size, and
  regeneration rules, you set each field 10 × 10 = 100 times. Change your
  mind about the default collision size? Do it 10 more times, hoping you
  don't miss one.
- **Tooltips drift from reality.** Stats live in one field, tooltip text in
  another. Nothing enforces that they match. After a balance pass, tooltips
  are almost always wrong.
- **The format is a black box.** The `.w3x` archive stores object data in
  binary. You cannot grep it, diff it in git, run a script over it, or
  review changes in a pull request.
- **No reuse between abilities.** Two abilities that share a mechanic have
  zero relationship in the editor — they are just two independent rows.

### What WurstScript gives you instead

**One definition, zero repetition.**
All units in this project call `createSpawnedUnit()`, which automatically
applies ~15 common fields (food cost, build time, acquisition range,
attack slots, etc.) in one place. Adding a new unit means writing only the
fields that are actually different. Change a shared default once and every
unit in the project inherits it.

```wurst
// This single call sets 15+ fields automatically:
createSpawnedUnit(UNIT_MY_WARRIOR, UnitIds.footman, BUILDING_MY_WARRIOR)
    ..setAttack1Data(AttackType.Normal, 30, 5, 4, 1.4)
    ..setHitPointsMaximumBase(600)
    // ... only what is specific to this unit
```

**Tooltips that cannot lie.**
The `UnitTooltipGenerator` and `BTAbilityTooltipGenerator` classes build
tooltip text directly from the same values used to configure the unit. If
you change HP from 600 to 700, the tooltip updates automatically — there is
no separate tooltip field to remember.

**Plain text means real tools.**
Because definitions are source files, the whole ecosystem of developer tools
becomes available:

- **Git** tracks every change with a diff you can actually read. Who changed
  the Footman's HP, when, and why? `git log` tells you.
- **Find all references.** Want to know every unit that uses `ABIL_DEFEND`?
  A single search across the project finds it in under a second.
- **External scripts can read and write the data.** This project already
  includes `scripts/generate_unit_stat_data.py`, which parses `ArmySpawner.wurst`
  and produces `unit_attributes.xlsx` — a full balance spreadsheet generated
  automatically from the source, not typed by hand. The World Editor offers
  no equivalent hook.
- **`scripts/damage_table.py`** generates a damage-type matchup table.
  Scripts like these would be impossible if the data lived inside a binary
  archive.

**Sharing logic between abilities.**
In the Object Editor, two similar abilities are two completely independent
rows. In Wurst, shared behaviour lives in a function you call from both.
The `createAutoCastedEnemyAbility()` helper, for example, encodes the
"dummy trigger" pattern once; every auto-cast offensive spell in the project
uses it rather than duplicating the setup.

### "But I don't know how to code"

That is fine. WurstScript in this project mostly reads like a configuration
file with a thin layer of syntax on top. The patterns are repetitive by
design — adding a new unit means copying an existing one and changing a
handful of values. You do not need to understand the compiler to do that.

Start by:
1. Reading one existing unit definition (e.g. `createFootman()` in
   [HumanUnitsDef.wurst](wurst/objects/units/HumanUnitsDef.wurst)).
2. Copying it, renaming the IDs, and adjusting the numbers.
3. Building the map and checking it in-game.

The rest of this guide documents exactly what to change and where.

---

## Table of Contents

0. [Coming from the World Editor?](#0-coming-from-the-world-editor)
1. [Prerequisites & Compilation Model](#1-prerequisites--compilation-model)
2. [Adding a New Unit](#2-adding-a-new-unit)
3. [Adding a New Ability](#3-adding-a-new-ability)
4. [Dummy Auto-Casting](#4-dummy-auto-casting)
5. [Adding a New Faction](#5-adding-a-new-faction)

---

## 1. Prerequisites & Compilation Model

WurstScript compiles to JASS. Object data (units, abilities, items, upgrades)
is **generated at compile time** via `@compiletime` functions and baked into
the map archive. This means:

- Object definitions are **not** runtime factories. A `@compiletime function`
  runs during compilation, not when the game starts.
- IDs must be registered in `LocalObjectIDs.wurst` using the compile-time ID
  generators. The generator assigns monotonically-increasing raw codes so you
  never have to manage four-character codes by hand.
- Runtime code (game logic, triggers) references these same constants, which
  are replaced by their literal numeric values at compile time.

---

## 2. Adding a New Unit

A "unit" in this project is always a pair: a **spawned soldier** (what fights)
and a **building** (what the player places in their zone). They are linked
through `BTBuildingData`.

### Step 1 — Declare IDs in `LocalObjectIDs.wurst`

Add both constants at the bottom of the appropriate faction section.

```wurst
// wurst/assets/LocalObjectIDs.wurst
public let UNIT_MY_WARRIOR   = compiletime(UNIT_ID_GEN.next())
public let BUILDING_MY_WARRIOR = compiletime(UNIT_ID_GEN.next())
```

Order matters for readability but not for correctness — the generator handles
uniqueness automatically.

### Step 2 — Register squad data in `ArmySpawner.wurst`

Inside `setupBuildingData()`, add one `BTBuildingData` line for this unit:

```wurst
// wurst/systems/armyHandler/ArmySpawner.wurst  →  setupBuildingData()
new BTBuildingData(BUILDING_MY_WARRIOR, 150, 0, genList(UNIT_MY_WARRIOR, 5))
//                 ^building ID         ^gold ^bp  ^unit ID              ^count
```

For an upgrade (unit that replaces a base building):

```wurst
new BTBuildingData(BUILDING_MY_WARRIOR, BUILDING_MY_WARRIOR_ELITE, 0, 800, genList(UNIT_MY_WARRIOR_ELITE, 5))
//                 ^source building     ^upgrade building             ^gold ^bp
```

The first argument of the 5-arg constructor is the **source** building — the
one being upgraded. The costs passed here represent only the *additional* cost
of the upgrade.

### Step 3 — Define the unit in `*UnitsDef.wurst`

Add a `@compiletime function` to your faction's unit definition file:

```wurst
// wurst/objects/units/MyFactionUnitsDef.wurst
@compiletime function createMyWarrior()
    let tooltip = new UnitTooltipGenerator("Brief description of the unit.")

    createSpawnedUnit(UNIT_MY_WARRIOR, UnitIds.footman, BUILDING_MY_WARRIOR)
        ..setSpeedBase(270)
        ..registerTooltipGenerator(tooltip)
        ..tooltipStartListen()             // begin recording tooltip properties

        ..setAttack1Data(AttackType.Normal, 30, 5, 4, 1.4)
        //               ^type              ^base ^dice ^sides ^cooldown

        ..setArmorData(ArmorType.Large, 3)
        ..setHitPointsMaximumBase(600)

        ..setAutoPointValue()              // derives bounty from BTBuildingData costs
        ..setAutoBuildingCost()            // copies gold/bp cost to the building shell

        ..tooltipStopListen(true)          // finalize tooltip, apply to unit + building

        ..setNameEnhance("Q", "My Warrior")  // hotkey + name (must be unique per row)
        ..setSizeSmall()                   // 15-radius collision

        ..setModelFileExt(Units.footman1)
        ..setIconGameInterfaceExt(Icons.bTNFootman)
        ..setUnitSoundSetExt(Soundsets.footman)
```

`createSpawnedUnit(newId, baseId, buildingId)` creates the soldier unit and
its building shell in one call. `setCommonAttr()` is called automatically; it
sets sensible defaults (no food cost, no requirements, acquisition range 2300,
etc.).

For a unit with passive abilities, add them between `tooltipStartListen` and
`tooltipStopListen`:

```wurst
..registerCustomPanelAbilityTooltip(ABIL_MY_PASSIVE)
..setNormalAbilities(commaList(ABIL_MY_PASSIVE))
```

### Step 4 — Register the unit in `IDListConstant.wurst`

Add the unit ID to the faction's `*_UNITS` list so systems like `RaceSelection`
and the score board know about it:

```wurst
// wurst/assets/IDListConstant.wurst
public let MY_FACTION_UNITS = asList(
    UNIT_MY_WARRIOR,
    // ...
)
```

If it's an upgrade building, add the building ID to `*_UNIT_UPGD` as well.

---

## 3. Adding a New Ability

Abilities are defined with `@compiletime` functions in `*AbilitiesDef.wurst`.
The Wurst standard library provides a class hierarchy mirroring the WC3 object
editor (e.g. `AbilityDefinitionSlow`, `AbilityDefinitionInnerFireCreep`, etc.).

### Passive ability (no autocast)

```wurst
// wurst/objects/abilities/MyFactionAbilitiesDef.wurst
@compiletime function createMyFactionAbilities()
    let tgen = new BTAbilityTooltipGenerator("Increases armor.")

    new AbilityDefinitionInnerFireCreep(ABIL_MY_PASSIVE)
        ..setCheckDependencies(false)
        ..registerTooltipGenerator(tgen)
        ..setLevels(1)
        ..setIconNormal(Icons.bTNBarkSkin)
        ..tooltipStartListen()
        ..setDamageIncrease(1, 0)
        ..presetDefenseIncrease(_ -> 4)
        ..presetManaCost(_ -> 0)
        ..presetCastRange(_ -> 0)
        ..presetCooldown(_ -> 0)
        ..setNameEnhance("Z", "My Passive")
        ..tooltipStopListen(true)

    abilTooltipMap.put(ABIL_MY_PASSIVE, tgen.generateFullTooltip())
```

Store the generated tooltip in `abilTooltipMap` so unit definitions can
reference it via `abilTooltipMap.get(ABIL_MY_PASSIVE)`.

### Item-granted ability (purchased at building)

Items grant extra abilities per building. The pattern is:

1. Create an `ItemDefinition` via `createBasicItem(ITEM_MY_UPGRADE)`.
2. Create the ability definition.
3. Register the item on the unit definition with `registerItemDef(itm, ItemModifierType.Addition)`.
4. Add the item ID to the faction's `*_ABIL_UPGD` list in `IDListConstant.wurst`.

```wurst
let itm = createBasicItem(ITEM_MY_UPGRADE)
    ..setItemCost(0, 200, 1, unitCount, unitCount)
    ..setNameEnhance("X", "Add My Passive")
    ..setInterfaceIcon(Icons.bTNBarkSkin)

// ... define the ability, then apply the tooltip to the item:
tgen.applyToDefItem(itm)
```

---

## 4. Dummy Auto-Casting

### The problem

WC3's native autocast only works with a fixed set of ability behaviors (Heal,
Slow, Curse, Inner Fire, etc.). The targeting AI built into each behavior is
not configurable — Heal targets the most-wounded ally, Curse targets the
closest enemy, and so on. You cannot make a native Firebolt autocast, nor can
you freely change which ability an AI will cast.

### The solution used in this project

The map uses a **two-ability trick**: a cheap "trigger" ability that the unit
actually autocasts, and a separate "real" ability that does the actual effect.

```
Unit has both on its ability list:
  ABIL_AC_FROST_NOVA   ← Curse-based dummy; autocast targets closest enemy
  ABIL_FROST_NOVA      ← Real Frost Nova; not on autocast

EVENT_PLAYER_UNIT_SPELL_CAST fires when ABIL_AC_FROST_NOVA triggers
  └── DummyAutoCasting intercepts it
      └── caster.issueTargetOrderById(OrderIds.frostnova, target)
          → This fires ABIL_FROST_NOVA on the same target
```

The dummy ability (e.g. a Curse variant from `createAutoCastedEnemyAbility`)
has essentially zero effect: near-zero duration, no buff art, no damage. Its
only job is to fire the `SPELL_CAST` event with the right target.

### Factory functions in `AbilityObjEditingCommons.wurst`

| Function | Autocast behavior | Use when |
|---|---|---|
| `createAutoCastedEnemyAbility` | Targets closest enemy | offensive spells |
| `createAutoCastedLongRangeEnemyAbility` | Targets farthest enemy | AoE offensive spells |
| `createAutoCastedAlliedAbility` | Targets ally with highest attack | buffing spells |
| `createAutoCastedAllieHealdAbility` | Targets most-wounded ally | healing spells |
| `createAutoCastAlliedManaTarget` | Targets ally with lowest mana | mana restore |

### Registering the dummy→real mapping

In `DummyAutoCasting.wurst`, register the pair in the appropriate map inside
the `init` block:

```wurst
// For target-order spells (most spells):
dummyToRealCastMapTarget
    ..put(ABIL_AC_MY_SPELL, new BuffTuple(OrderIds.myspellorder, -1))
    //   ^dummy ability ID              ^WC3 order ID for the real spell

// If the real spell also applies a buff that must be checked before re-casting:
dummyToRealCastMapTarget
    ..put(ABIL_AC_MY_BUFF_SPELL, new BuffTuple(OrderIds.mybufforder, BuffIds.myBuff))
    //                                                                ^prevents double-apply

// For immediate-order spells (no target, e.g. Roar):
dummyToRealImmediateCastMap
    ..put(ABIL_AC_MY_ROAR, OrderIds.roar)
```

The `buffId` field (`-1` when unused) prevents the dummy from firing when the
target already has the buff — important for spells like Unholy Frenzy or
Rejuvenation that should not stack.

### Defining the pair in an AbilitiesDef file

```wurst
// 1. Define the real ability
let tgen = new BTAbilityTooltipGenerator("Fires a frost bolt.")
let abilFrostBolt = new AbilityDefinitionThunderBoltCreep(ABIL_FROST_BOLT)
    ..setCheckDependencies(false)
    ..setLevels(1)
    ..registerTooltipGenerator(tgen)
    ..tooltipStartListen()
    ..presetDamageDealt(_ -> 200)
    ..presetManaCost(_ -> 80)
    ..presetCooldown(_ -> 5)
    ..presetCastRange(_ -> 700)
    ..setNameEnhance("Z", "Frost Bolt")
    ..tooltipStopListen(false)   // false = don't finalize yet

// 2. Define the dummy trigger
createAutoCastedEnemyAbility(ABIL_AC_FROST_BOLT)
    ..registerTooltipGenerator(tgen)
    ..tooltipStartListen()
    ..presetAutoCastCastRange(700, abilFrostBolt)   // syncs range to real spell
    ..presetAutoCastManaCost(80, abilFrostBolt)     // syncs mana cost
    ..presetAutoCastCooldown(5, abilFrostBolt)      // dummy cooldown = real + 1
    ..applyTooltip(abilFrostBolt)
    ..tooltipStopListen(true)

// 3. Give the unit BOTH abilities
createSpawnedUnit(UNIT_MY_CASTER, ...)
    ..setNormalAbilities(commaList(ABIL_AC_FROST_BOLT, ABIL_FROST_BOLT))
    ..setDefaultActiveAbility(commaList(ABIL_AC_FROST_BOLT))  // enables autocast
```

> **Important:** The dummy ability must have a slightly shorter cooldown than
> the real spell. `presetAutoCastCooldown(c, realAbil)` handles this by
> setting the dummy to `c` and the real ability to `c - 1`. This ensures the
> real spell is always off cooldown when the dummy triggers.

### Special case: healing / buff re-application

Some spells (Rejuvenation, Healing Wave, Healing Spray) require the ability
to be re-added to the target after casting to reset the autocast logic. This
is handled explicitly in `DummyAutoCasting.wurst`'s `SPELL_CAST` handler and
does not need to be repeated elsewhere.

---

## 5. Adding a New Faction

A faction is a builder unit + a set of buildings. Follow these steps in order.

### Step 1 — Declare all IDs in `LocalObjectIDs.wurst`

Add a clearly delimited section for the faction. Every unit, building, ability,
and item needs a constant here.

```wurst
// ==================== My Faction =================
public let UNIT_MY_FACTION_BUILDER    = compiletime(UNIT_ID_GEN.next())
public let UNIT_MY_WARRIOR            = compiletime(UNIT_ID_GEN.next())
public let BUILDING_MY_WARRIOR        = compiletime(UNIT_ID_GEN.next())
// ...
public let ABIL_MY_PASSIVE            = compiletime(ABIL_ID_GEN.next())
public let ABIL_AC_MY_SPELL           = compiletime(ABIL_ID_GEN.next())
public let ABIL_MY_SPELL              = compiletime(ABIL_ID_GEN.next())
public let ITEM_MY_UPGRADE            = compiletime(ITEM_ID_GEN.next())
```

### Step 2 — Register building data in `ArmySpawner.wurst`

In `setupBuildingData()`, add one entry per building (base units first, then
upgrades):

```wurst
new BTBuildingData(BUILDING_MY_WARRIOR, 150, 0, genList(UNIT_MY_WARRIOR, 5))
new BTBuildingData(BUILDING_MY_WARRIOR, BUILDING_MY_WARRIOR_ELITE, 0, 800, genList(UNIT_MY_WARRIOR_ELITE, 5))
```

### Step 3 — Create `MyFactionUnitsDef.wurst`

Create `wurst/objects/units/MyFactionUnitsDef.wurst`. For each unit, write a
`@compiletime function` following the pattern in [Section 2](#2-adding-a-new-unit).

Include the builder at the bottom:

```wurst
@compiletime function createBuilder()
    createBuilder(UNIT_MY_FACTION_BUILDER, UnitIds.peasant)
        ..setNameEnhance("Q", "My Faction Builder")
        ..setStructuresBuilt(commaList(
            BUILDING_MY_WARRIOR,
            // ... all buildings this faction can place
        ))
```

`createBuilder()` from `UnitObjEditingCommon.wurst` sets up the builder with
invulnerability, inventory, the start-round ability, sell-building, and other
shared builder abilities automatically.

### Step 4 — Create `MyFactionAbilitiesDef.wurst`

Create `wurst/objects/abilities/MyFactionAbilitiesDef.wurst`. Write a single
`@compiletime function createMyFactionAbilities()` containing all ability and
item definitions for the faction. Follow the patterns in
[Section 3](#3-adding-a-new-ability) and [Section 4](#4-dummy-auto-casting).

### Step 5 — Register the faction in `IDListConstant.wurst`

Add the builder to `BUILDER_LIST` and add the faction's unit/item lists:

```wurst
// BUILDER_LIST — order determines selection screen order
public let BUILDER_LIST = asList(
    // ... existing builders ...
    UNIT_MY_FACTION_BUILDER
)

// Short code for commands like -ban MF
public let BAN_MAP = new IterableMap<string, int>()
    ..put("MF", UNIT_MY_FACTION_BUILDER)
    // ...

public let RACE_ABBREV = new HashMap<string, string>()
    ..put("MF", "My Faction")
    // ...

public let BUILDER_ID_TO_RACE_STR = new HashMap<int, string>()
    ..put(UNIT_MY_FACTION_BUILDER, "My Faction")
    // ...

// Units that belong to this faction (used by RaceSelection, score board, etc.)
public let MY_FACTION_UNITS = asList(
    UNIT_MY_WARRIOR,
    // ...
)

// Upgrade buildings (purchasable building upgrades)
public let MY_FACTION_UNIT_UPGD = asList(
    BUILDING_MY_WARRIOR_ELITE,
    // ...
)

// Item-based ability upgrades (purchasable items on buildings)
public let MY_FACTION_ABIL_UPGD = asList(
    ITEM_MY_UPGRADE,
    // ...
)
```

### Step 6 — Register dummy auto-cast pairs in `DummyAutoCasting.wurst`

For every auto-cast ability your faction uses, add entries in the `init` block
as described in [Section 4](#4-dummy-auto-casting).

### Step 7 — Add faction-specific on-death logic (optional)

If any of your units have special behavior on death (e.g. spawning a new unit,
triggering an ability on the killer), add a branch in `customOnDeathAction()`
in `UnitDeathTrigger.wurst`:

```wurst
else if dyingUnit.getTypeId() == UNIT_MY_WARRIOR
    // spawn a smaller unit or apply an effect
    pData.addUnit(
        createUnit(dyingUnit.getOwner(), UNIT_MY_SPIRIT, dyingUnit.getPos(), dyingUnit.getFacingAngle())
            ..issuePointOrder("attack", CENTER)
    )
```

### Checklist

| # | File | What to add |
|---|---|---|
| 1 | `LocalObjectIDs.wurst` | All `UNIT_`, `BUILDING_`, `ABIL_`, `ITEM_` constants |
| 2 | `ArmySpawner.wurst` | `BTBuildingData` entries in `setupBuildingData()` |
| 3 | `MyFactionUnitsDef.wurst` | `@compiletime` unit + building + builder definitions |
| 4 | `MyFactionAbilitiesDef.wurst` | `@compiletime` ability + item definitions |
| 5 | `IDListConstant.wurst` | `BUILDER_LIST`, `BAN_MAP`, `RACE_ABBREV`, `BUILDER_ID_TO_RACE_STR`, `*_UNITS`, `*_UNIT_UPGD`, `*_ABIL_UPGD` |
| 6 | `DummyAutoCasting.wurst` | `dummyToRealCastMapTarget` / `dummyToRealImmediateCastMap` entries |
| 7 | `UnitDeathTrigger.wurst` | `customOnDeathAction()` branches (if needed) |
