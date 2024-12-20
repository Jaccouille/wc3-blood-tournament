//===========================================================================
// 
// Wurst Example Map
// 
//   Warcraft III map script
//   Generated by the Warcraft III World Editor
//   Map Author: Wurst Team
// 
//===========================================================================

//***************************************************************************
//*
//*  Global Variables
//*
//***************************************************************************

globals
    // Generated
    rect                    gg_rct_Frontrank_SW        = null
    rect                    gg_rct_Frontrank_NE        = null
    rect                    gg_rct_Frontrank_ES        = null
    rect                    gg_rct_Frontrank_WN        = null
    rect                    gg_rct_Frontrank_SE        = null
    rect                    gg_rct_Frontrank_EN        = null
    rect                    gg_rct_Frontrank_NW        = null
    rect                    gg_rct_Frontrank_WS        = null
    rect                    gg_rct_Red                 = null
    rect                    gg_rct_Blue                = null
    rect                    gg_rct_Teal                = null
    rect                    gg_rct_Purple              = null
    rect                    gg_rct_Yellow              = null
    rect                    gg_rct_Orange              = null
    rect                    gg_rct_Green               = null
    rect                    gg_rct_Pink                = null
    rect                    gg_rct_Final_Round_West    = null
    rect                    gg_rct_Final_Round_East    = null
    rect                    gg_rct_NtoCenter           = null
    rect                    gg_rct_StoCenter           = null
    rect                    gg_rct_EtoCenter           = null
    rect                    gg_rct_WtoCenter           = null
    rect                    gg_rct_ManagerTower        = null
    rect                    gg_rct_ManagerTowerFinal   = null
endglobals

function InitGlobals takes nothing returns nothing
endfunction

//***************************************************************************
//*
//*  Custom Script Code
//*
//***************************************************************************

//***************************************************************************
//*
//*  Unit Creation
//*
//***************************************************************************

//===========================================================================
function CreateBuildingsForPlayer0 takes nothing returns nothing
    local player p = Player(0)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', 4288.0, 6272.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer1 takes nothing returns nothing
    local player p = Player(1)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', 5824.0, 5248.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer2 takes nothing returns nothing
    local player p = Player(2)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', 5312.0, -2560.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer3 takes nothing returns nothing
    local player p = Player(3)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', 4288.0, -4096.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer4 takes nothing returns nothing
    local player p = Player(4)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', -4160.0, -4096.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer5 takes nothing returns nothing
    local player p = Player(5)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', -5184.0, -2560.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer6 takes nothing returns nothing
    local player p = Player(6)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', -5696.0, 5248.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer7 takes nothing returns nothing
    local player p = Player(7)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', -4160.0, 6272.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateNeutralHostile takes nothing returns nothing
    local player p = Player(PLAYER_NEUTRAL_AGGRESSIVE)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h009', -3445.3, 3925.3, 307.609, 'h009' )
endfunction

//===========================================================================
function CreatePlayerBuildings takes nothing returns nothing
    call CreateBuildingsForPlayer0(  )
    call CreateBuildingsForPlayer1(  )
    call CreateBuildingsForPlayer2(  )
    call CreateBuildingsForPlayer3(  )
    call CreateBuildingsForPlayer4(  )
    call CreateBuildingsForPlayer5(  )
    call CreateBuildingsForPlayer6(  )
    call CreateBuildingsForPlayer7(  )
endfunction

//===========================================================================
function CreatePlayerUnits takes nothing returns nothing
endfunction

//===========================================================================
function CreateAllUnits takes nothing returns nothing
    call CreatePlayerBuildings(  )
    call CreateNeutralHostile(  )
    call CreatePlayerUnits(  )
endfunction

//***************************************************************************
//*
//*  Regions
//*
//***************************************************************************

function CreateRegions takes nothing returns nothing
    local weathereffect we

    set gg_rct_Frontrank_SW = Rect( -1792.0, -4736.0, -512.0, -3584.0 )
    set gg_rct_Frontrank_NE = Rect( 512.0, 5632.0, 1792.0, 6784.0 )
    set gg_rct_Frontrank_ES = Rect( 4608.0, -768.0, 5760.0, 512.0 )
    set gg_rct_Frontrank_WN = Rect( -5760.0, 1536.0, -4608.0, 2816.0 )
    set gg_rct_Frontrank_SE = Rect( 512.0, -4736.0, 1792.0, -3584.0 )
    set gg_rct_Frontrank_EN = Rect( 4608.0, 1504.0, 5760.0, 2816.0 )
    set gg_rct_Frontrank_NW = Rect( -1792.0, 5632.0, -512.0, 6784.0 )
    set gg_rct_Frontrank_WS = Rect( -5760.0, -768.0, -4608.0, 512.0 )
    set gg_rct_Red = Rect( 3584.0, 5600.0, 5120.0, 6208.0 )
    set gg_rct_Blue = Rect( 5120.0, 4576.0, 6656.0, 5184.0 )
    set gg_rct_Teal = Rect( 4608.0, -3232.0, 6144.0, -2656.0 )
    set gg_rct_Purple = Rect( 3584.0, -4768.0, 5120.0, -4192.0 )
    set gg_rct_Yellow = Rect( -4864.0, -4768.0, -3328.0, -4192.0 )
    set gg_rct_Orange = Rect( -5888.0, -3232.0, -4352.0, -2656.0 )
    set gg_rct_Green = Rect( -6400.0, 4576.0, -4864.0, 5152.0 )
    set gg_rct_Pink = Rect( -4864.0, 5600.0, -3328.0, 6176.0 )
    set gg_rct_Final_Round_West = Rect( -1536.0, -128.0, -512.0, 2304.0 )
    set gg_rct_Final_Round_East = Rect( 512.0, -128.0, 1536.0, 2304.0 )
    set gg_rct_NtoCenter = Rect( -512.0, 7040.0, 512.0, 7168.0 )
    set gg_rct_StoCenter = Rect( -512.0, -5120.0, 512.0, -4992.0 )
    set gg_rct_EtoCenter = Rect( 6016.0, 640.0, 6144.0, 1408.0 )
    set gg_rct_WtoCenter = Rect( -6144.0, 640.0, -6016.0, 1408.0 )
    set gg_rct_ManagerTower = Rect( -3744.0, 3552.0, -3136.0, 4256.0 )
    set gg_rct_ManagerTowerFinal = Rect( -320.0, 2720.0, 352.0, 3424.0 )
endfunction

//***************************************************************************
//*
//*  Players
//*
//***************************************************************************

function InitCustomPlayerSlots takes nothing returns nothing

    // Player 0
    call SetPlayerStartLocation( Player(0), 0 )
    call ForcePlayerStartLocation( Player(0), 0 )
    call SetPlayerColor( Player(0), ConvertPlayerColor(0) )
    call SetPlayerRacePreference( Player(0), RACE_PREF_HUMAN )
    call SetPlayerRaceSelectable( Player(0), true )
    call SetPlayerController( Player(0), MAP_CONTROL_USER )

    // Player 1
    call SetPlayerStartLocation( Player(1), 1 )
    call ForcePlayerStartLocation( Player(1), 1 )
    call SetPlayerColor( Player(1), ConvertPlayerColor(1) )
    call SetPlayerRacePreference( Player(1), RACE_PREF_ORC )
    call SetPlayerRaceSelectable( Player(1), true )
    call SetPlayerController( Player(1), MAP_CONTROL_USER )

    // Player 2
    call SetPlayerStartLocation( Player(2), 2 )
    call ForcePlayerStartLocation( Player(2), 2 )
    call SetPlayerColor( Player(2), ConvertPlayerColor(2) )
    call SetPlayerRacePreference( Player(2), RACE_PREF_UNDEAD )
    call SetPlayerRaceSelectable( Player(2), true )
    call SetPlayerController( Player(2), MAP_CONTROL_USER )

    // Player 3
    call SetPlayerStartLocation( Player(3), 3 )
    call ForcePlayerStartLocation( Player(3), 3 )
    call SetPlayerColor( Player(3), ConvertPlayerColor(3) )
    call SetPlayerRacePreference( Player(3), RACE_PREF_NIGHTELF )
    call SetPlayerRaceSelectable( Player(3), true )
    call SetPlayerController( Player(3), MAP_CONTROL_USER )

    // Player 4
    call SetPlayerStartLocation( Player(4), 4 )
    call ForcePlayerStartLocation( Player(4), 4 )
    call SetPlayerColor( Player(4), ConvertPlayerColor(4) )
    call SetPlayerRacePreference( Player(4), RACE_PREF_HUMAN )
    call SetPlayerRaceSelectable( Player(4), true )
    call SetPlayerController( Player(4), MAP_CONTROL_USER )

    // Player 5
    call SetPlayerStartLocation( Player(5), 5 )
    call ForcePlayerStartLocation( Player(5), 5 )
    call SetPlayerColor( Player(5), ConvertPlayerColor(5) )
    call SetPlayerRacePreference( Player(5), RACE_PREF_ORC )
    call SetPlayerRaceSelectable( Player(5), true )
    call SetPlayerController( Player(5), MAP_CONTROL_USER )

    // Player 6
    call SetPlayerStartLocation( Player(6), 6 )
    call ForcePlayerStartLocation( Player(6), 6 )
    call SetPlayerColor( Player(6), ConvertPlayerColor(6) )
    call SetPlayerRacePreference( Player(6), RACE_PREF_UNDEAD )
    call SetPlayerRaceSelectable( Player(6), true )
    call SetPlayerController( Player(6), MAP_CONTROL_USER )

    // Player 7
    call SetPlayerStartLocation( Player(7), 7 )
    call ForcePlayerStartLocation( Player(7), 7 )
    call SetPlayerColor( Player(7), ConvertPlayerColor(7) )
    call SetPlayerRacePreference( Player(7), RACE_PREF_NIGHTELF )
    call SetPlayerRaceSelectable( Player(7), true )
    call SetPlayerController( Player(7), MAP_CONTROL_USER )

endfunction

function InitCustomTeams takes nothing returns nothing
    // Force: TRIGSTR_002
    call SetPlayerTeam( Player(0), 0 )
    call SetPlayerTeam( Player(1), 0 )
    call SetPlayerTeam( Player(2), 0 )
    call SetPlayerTeam( Player(3), 0 )
    call SetPlayerTeam( Player(4), 0 )
    call SetPlayerTeam( Player(5), 0 )
    call SetPlayerTeam( Player(6), 0 )
    call SetPlayerTeam( Player(7), 0 )

endfunction

function InitAllyPriorities takes nothing returns nothing

    call SetStartLocPrioCount( 0, 1 )
    call SetStartLocPrio( 0, 0, 1, MAP_LOC_PRIO_HIGH )

    call SetStartLocPrioCount( 1, 1 )
    call SetStartLocPrio( 1, 0, 0, MAP_LOC_PRIO_HIGH )

    call SetStartLocPrioCount( 2, 1 )
    call SetStartLocPrio( 2, 0, 3, MAP_LOC_PRIO_HIGH )

    call SetStartLocPrioCount( 3, 1 )
    call SetStartLocPrio( 3, 0, 2, MAP_LOC_PRIO_HIGH )

    call SetStartLocPrioCount( 4, 1 )
    call SetStartLocPrio( 4, 0, 5, MAP_LOC_PRIO_HIGH )

    call SetStartLocPrioCount( 5, 1 )
    call SetStartLocPrio( 5, 0, 4, MAP_LOC_PRIO_HIGH )

    call SetStartLocPrioCount( 6, 1 )
    call SetStartLocPrio( 6, 0, 7, MAP_LOC_PRIO_HIGH )

    call SetStartLocPrioCount( 7, 1 )
    call SetStartLocPrio( 7, 0, 6, MAP_LOC_PRIO_HIGH )
endfunction

//***************************************************************************
//*
//*  Main Initialization
//*
//***************************************************************************

//===========================================================================
function main takes nothing returns nothing
    call SetCameraBounds( -7424.0 + GetCameraMargin(CAMERA_MARGIN_LEFT), -6656.0 + GetCameraMargin(CAMERA_MARGIN_BOTTOM), 7424.0 - GetCameraMargin(CAMERA_MARGIN_RIGHT), 8192.0 - GetCameraMargin(CAMERA_MARGIN_TOP), -7424.0 + GetCameraMargin(CAMERA_MARGIN_LEFT), 8192.0 - GetCameraMargin(CAMERA_MARGIN_TOP), 7424.0 - GetCameraMargin(CAMERA_MARGIN_RIGHT), -6656.0 + GetCameraMargin(CAMERA_MARGIN_BOTTOM) )
    call SetDayNightModels( "Environment\\DNC\\DNCLordaeron\\DNCLordaeronTerrain\\DNCLordaeronTerrain.mdl", "Environment\\DNC\\DNCLordaeron\\DNCLordaeronUnit\\DNCLordaeronUnit.mdl" )
    call SetTerrainFogEx( 0, 0.0, 10000.0, 5.500, 1.000, 0.000, 0.000 )
    call NewSoundEnvironment( "Default" )
    call SetAmbientDaySound( "BlackCitadelDay" )
    call SetAmbientNightSound( "BlackCitadelNight" )
    call SetMapMusic( "Music", true, 0 )
    call CreateRegions(  )
    call CreateAllUnits(  )
    call InitBlizzard(  )
    call InitGlobals(  )

endfunction

//***************************************************************************
//*
//*  Map Configuration
//*
//***************************************************************************

function config takes nothing returns nothing
    call SetMapName( "TRIGSTR_008" )
    call SetMapDescription( "" )
    call SetPlayers( 8 )
    call SetTeams( 8 )
    call SetGamePlacement( MAP_PLACEMENT_TEAMS_TOGETHER )

    call DefineStartLocation( 0, 4288.0, 6208.0 )
    call DefineStartLocation( 1, 5824.0, 5248.0 )
    call DefineStartLocation( 2, 5312.0, -2560.0 )
    call DefineStartLocation( 3, 4288.0, -4096.0 )
    call DefineStartLocation( 4, -4160.0, -4096.0 )
    call DefineStartLocation( 5, -5184.0, -2560.0 )
    call DefineStartLocation( 6, -5696.0, 5248.0 )
    call DefineStartLocation( 7, -4160.0, 6272.0 )

    // Player setup
    call InitCustomPlayerSlots(  )
    call SetPlayerSlotAvailable( Player(0), MAP_CONTROL_USER )
    call SetPlayerSlotAvailable( Player(1), MAP_CONTROL_USER )
    call SetPlayerSlotAvailable( Player(2), MAP_CONTROL_USER )
    call SetPlayerSlotAvailable( Player(3), MAP_CONTROL_USER )
    call SetPlayerSlotAvailable( Player(4), MAP_CONTROL_USER )
    call SetPlayerSlotAvailable( Player(5), MAP_CONTROL_USER )
    call SetPlayerSlotAvailable( Player(6), MAP_CONTROL_USER )
    call SetPlayerSlotAvailable( Player(7), MAP_CONTROL_USER )
    call InitGenericPlayerSlots(  )
    call InitAllyPriorities(  )
endfunction

