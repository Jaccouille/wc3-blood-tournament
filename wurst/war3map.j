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
    rect                    gg_rct_Reinforcements_SW   = null
    rect                    gg_rct_Reinforcements_ES   = null
    rect                    gg_rct_Reinforcements_NE   = null
    rect                    gg_rct_Reinforcements_WN   = null
    rect                    gg_rct_Frontrank_SE        = null
    rect                    gg_rct_Frontrank_EN        = null
    rect                    gg_rct_Frontrank_NW        = null
    rect                    gg_rct_Frontrank_WS        = null
    rect                    gg_rct_Reinforcements_SE   = null
    rect                    gg_rct_Reinforcements_EN   = null
    rect                    gg_rct_Reinforcements_NW   = null
    rect                    gg_rct_Reinforcements_WS   = null
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
    rect                    gg_rct_backupSpawn         = null
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

    set u = BlzCreateUnitWithSkin( p, 'h008', 5440.0, 3008.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer1 takes nothing returns nothing
    local player p = Player(1)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', 6848.0, 2240.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer2 takes nothing returns nothing
    local player p = Player(2)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', 6848.0, -4160.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer3 takes nothing returns nothing
    local player p = Player(3)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', 5440.0, -4928.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer4 takes nothing returns nothing
    local player p = Player(4)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', -320.0, -4928.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer5 takes nothing returns nothing
    local player p = Player(5)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', -1728.0, -4160.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer6 takes nothing returns nothing
    local player p = Player(6)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', -1728.0, 2240.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateBuildingsForPlayer7 takes nothing returns nothing
    local player p = Player(7)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h008', -320.0, 3008.0, 270.000, 'h008' )
endfunction

//===========================================================================
function CreateNeutralHostile takes nothing returns nothing
    local player p = Player(PLAYER_NEUTRAL_AGGRESSIVE)
    local unit u
    local integer unitID
    local trigger t
    local real life

    set u = BlzCreateUnitWithSkin( p, 'h009', 2566.1, -1425.5, 283.057, 'h009' )
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

    set gg_rct_Frontrank_SW = Rect( 1408.0, -6176.0, 2176.0, -4992.0 )
    set gg_rct_Frontrank_NE = Rect( 2944.0, 2048.0, 3712.0, 3200.0 )
    set gg_rct_Frontrank_ES = Rect( 6144.0, -2688.0, 7296.0, -1920.0 )
    set gg_rct_Frontrank_WN = Rect( -2176.0, -1024.0, -1024.0, -256.0 )
    set gg_rct_Reinforcements_SW = Rect( 1376.0, -5664.0, 1568.0, -5472.0 )
    set gg_rct_Reinforcements_ES = Rect( 6688.0, -2720.0, 6880.0, -2528.0 )
    set gg_rct_Reinforcements_NE = Rect( 3648.0, 2560.0, 3840.0, 2720.0 )
    set gg_rct_Reinforcements_WN = Rect( -1760.0, -288.0, -1568.0, -96.0 )
    set gg_rct_Frontrank_SE = Rect( 2944.0, -6176.0, 3712.0, -4992.0 )
    set gg_rct_Frontrank_EN = Rect( 6144.0, -1024.0, 7296.0, -256.0 )
    set gg_rct_Frontrank_NW = Rect( 1536.0, 2048.0, 2304.0, 3200.0 )
    set gg_rct_Frontrank_WS = Rect( -2176.0, -2688.0, -1024.0, -1920.0 )
    set gg_rct_Reinforcements_SE = Rect( 3552.0, -5664.0, 3744.0, -5472.0 )
    set gg_rct_Reinforcements_EN = Rect( 6688.0, -288.0, 6880.0, -96.0 )
    set gg_rct_Reinforcements_NW = Rect( 1376.0, 2560.0, 1568.0, 2752.0 )
    set gg_rct_Reinforcements_WS = Rect( -1760.0, -2848.0, -1568.0, -2656.0 )
    set gg_rct_Red = Rect( 4832.0, 2240.0, 6112.0, 2912.0 )
    set gg_rct_Blue = Rect( 6144.0, 1504.0, 7584.0, 2144.0 )
    set gg_rct_Teal = Rect( 6112.0, -4896.0, 7584.0, -4000.0 )
    set gg_rct_Purple = Rect( 4672.0, -5664.0, 6176.0, -5024.0 )
    set gg_rct_Yellow = Rect( -928.0, -5664.0, 416.0, -5024.0 )
    set gg_rct_Orange = Rect( -2336.0, -4928.0, -992.0, -4256.0 )
    set gg_rct_Green = Rect( -2336.0, 1504.0, -992.0, 2400.0 )
    set gg_rct_Pink = Rect( -1056.0, 2272.0, 416.0, 2912.0 )
    set gg_rct_Final_Round_West = Rect( 1280.0, -2432.0, 2176.0, -384.0 )
    set gg_rct_Final_Round_East = Rect( 2944.0, -2432.0, 3968.0, -384.0 )
    set gg_rct_backupSpawn = Rect( -2816.0, -7040.0, -2592.0, -6816.0 )
endfunction

//***************************************************************************
//*
//*  Players
//*
//***************************************************************************

function InitCustomPlayerSlots takes nothing returns nothing

    // Player 0
    call SetPlayerStartLocation( Player(0), 0 )
    call SetPlayerColor( Player(0), ConvertPlayerColor(0) )
    call SetPlayerRacePreference( Player(0), RACE_PREF_HUMAN )
    call SetPlayerRaceSelectable( Player(0), true )
    call SetPlayerController( Player(0), MAP_CONTROL_USER )

endfunction

function InitCustomTeams takes nothing returns nothing
    // Force: TRIGSTR_002
    call SetPlayerTeam( Player(0), 0 )

endfunction

//***************************************************************************
//*
//*  Main Initialization
//*
//***************************************************************************

//===========================================================================
function main takes nothing returns nothing
    call SetCameraBounds( -2816.0 + GetCameraMargin(CAMERA_MARGIN_LEFT), -7168.0 + GetCameraMargin(CAMERA_MARGIN_BOTTOM), 7936.0 - GetCameraMargin(CAMERA_MARGIN_RIGHT), 3584.0 - GetCameraMargin(CAMERA_MARGIN_TOP), -2816.0 + GetCameraMargin(CAMERA_MARGIN_LEFT), 3584.0 - GetCameraMargin(CAMERA_MARGIN_TOP), 7936.0 - GetCameraMargin(CAMERA_MARGIN_RIGHT), -7168.0 + GetCameraMargin(CAMERA_MARGIN_BOTTOM) )
    call SetDayNightModels( "Environment\\DNC\\DNCLordaeron\\DNCLordaeronTerrain\\DNCLordaeronTerrain.mdl", "Environment\\DNC\\DNCLordaeron\\DNCLordaeronUnit\\DNCLordaeronUnit.mdl" )
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
    call SetPlayers( 1 )
    call SetTeams( 1 )
    call SetGamePlacement( MAP_PLACEMENT_USE_MAP_SETTINGS )

    call DefineStartLocation( 0, 5440.0, 3200.0 )

    // Player setup
    call InitCustomPlayerSlots(  )
    call SetPlayerSlotAvailable( Player(0), MAP_CONTROL_USER )
    call InitGenericPlayerSlots(  )
endfunction

