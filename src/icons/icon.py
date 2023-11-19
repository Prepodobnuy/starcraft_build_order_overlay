def find_icon_path(unit_name:str) -> str:
    units = {
        # buildings
        "Assimilator":"../assets/icons/Protoss/Buildings/Assimilator.jpg",
        "Cybernetics Core":"../assets/icons/Protoss/Buildings/Cybernetics Core.jpg",
        "Dark Shrine":"../assets/icons/Protoss/Buildings/Dark Shrine.jpg",
        "Fleet Beacon":"../assets/icons/Protoss/Buildings/Fleet Beacon.jpg",
        "Forge":"../assets/icons/Protoss/Buildings/Forge.jpg",
        "Gateway":"../assets/icons/Protoss/Buildings/Gateway.jpg",
        "Nexus":"../assets/icons/Protoss/Buildings/Nexus.jpg",
        "Photon Cannon":"../assets/icons/Protoss/Buildings/Photon Cannon.jpg",
        "Pylon":"../assets/icons/Protoss/Buildings/Pylon.jpg",
        "Robotics Bay":"../assets/icons/Protoss/Buildings/Robotics Bay.jpg",
        "Robotics Facility":"../assets/icons/Protoss/Buildings/Robotics Facility.jpg",
        "Shield Battery":"../assets/icons/Protoss/Buildings/Shield Battery.jpg",
        "Stargate":"../assets/icons/Protoss/Buildings/Stargate.jpg",
        "Templar Archives":"../assets/icons/Protoss/Buildings/Templar Archives.jpg",
        "Twilight Council":"../assets/icons/Protoss/Buildings/Twilight Council.jpg",

        "Armory":"../assets/icons/Terran/Buildings/Armory.jpg",
        "Barracks":"../assets/icons/Terran/Buildings/Barracks.jpg",
        "Bunker":"../assets/icons/Terran/Buildings/Bunker.jpg",
        "Command Center":"../assets/icons/Terran/Buildings/Command Center.jpg",
        "Engineering Bay":"../assets/icons/Terran/Buildings/Engineering Bay.jpg",
        "Factory":"../assets/icons/Terran/Buildings/Factory.jpg",
        "Fusion Core":"../assets/icons/Terran/Buildings/Fusion Core.jpg",
        "Ghost Academy":"../assets/icons/Terran/Buildings/Ghost Academy.jpg",
        "Missile Turret":"../assets/icons/Terran/Buildings/Missile Turret.jpg",
        "Orbital Command":"../assets/icons/Terran/Buildings/Orbital Command.jpg",
        "Planetary Fortress":"../assets/icons/Terran/Buildings/Planetary Fortress.jpg",
        "Reactor":"../assets/icons/Terran/Buildings/Reactor.jpg",
        "Refinery":"../assets/icons/Terran/Buildings/Refinery.jpg",
        "SensorTower":"../assets/icons/Terran/Buildings/SensorTower.jpg",
        "Starport":"../assets/icons/Terran/Buildings/Starport.jpg",
        "Supply Depot":"../assets/icons/Terran/Buildings/Supply Depot.jpg",
        "Tech Lab":"../assets/icons/Terran/Buildings/Tech Lab.jpg",

        "Baneling Nest":"../assets/icons/Zerg/Buildings/Baneling Nest.jpg",
        "Evolution Chamber":"../assets/icons/Zerg/Buildings/Evolution Chamber.jpg",
        "Extractor":"../assets/icons/Zerg/Buildings/Extractor.jpg",
        "Greater Spire":"../assets/icons/Zerg/Buildings/Greater Spire.jpg",
        "Hatchery":"../assets/icons/Zerg/Buildings/Hatchery.jpg",
        "Hive":"../assets/icons/Zerg/Buildings/Hive.jpg",
        "Hydralisk Den":"../assets/icons/Zerg/Buildings/Hydralisk Den.jpg",
        "Infestation Pit":"../assets/icons/Zerg/Buildings/Infestation Pit.jpg",
        "Lair":"../assets/icons/Zerg/Buildings/Lair.jpg",
        "Lurker Den":"../assets/icons/Zerg/Buildings/Lurker Den.jpg",
        "Nydus Network":"../assets/icons/Zerg/Buildings/Nydus Network.jpg",
        "Roach Warren":"../assets/icons/Zerg/Buildings/Roach Warren.jpg",
        "Spawning Pool":"../assets/icons/Zerg/Buildings/Spawning Pool.jpg",
        "Spine Crawler":"../assets/icons/Zerg/Buildings/Spine Crawler.jpg",
        "Spire":"../assets/icons/Zerg/Buildings/Spire.jpg",
        "Spore Crawler":"../assets/icons/Zerg/Buildings/Spore Crawler.jpg",
        "Ultralisk Cavern":"../assets/icons/Zerg/Buildings/Ultralisk Cavern.jpg",

        # units
        "Adept":"../assets/icons/Protoss/Units/Adept.jpg",
        "Archon":"../assets/icons/Protoss/Units/Archon.jpg",
        "Carrier":"../assets/icons/Protoss/Units/Carrier.jpg",
        "Colossus":"../assets/icons/Protoss/Units/Colossus.jpg",
        "Dark Templar":"../assets/icons/Protoss/Units/Dark Templar.jpg",
        "Disruptor":"../assets/icons/Protoss/Units/Disruptor.jpg",
        "High Templar":"../assets/icons/Protoss/Units/High Templar.jpg",
        "Immortal":"../assets/icons/Protoss/Units/Immortal.jpg",
        "Mothership":"../assets/icons/Protoss/Units/Mothership.jpg",
        "Observer":"../assets/icons/Protoss/Units/Observer.jpg",
        "Oracle":"../assets/icons/Protoss/Units/Oracle.jpg",
        "Phoenix":"../assets/icons/Protoss/Units/Phoenix.jpg",
        "Probe":"../assets/icons/Protoss/Units/Probe.jpg",
        "Sentry":"../assets/icons/Protoss/Units/Sentry.jpg",
        "Stalker":"../assets/icons/Protoss/Units/Stalker.jpg",
        "Tempest":"../assets/icons/Protoss/Units/Tempest.jpg",
        "Voidray":"../assets/icons/Protoss/Units/Voidray.jpg",
        "Warp Prism":"../assets/icons/Protoss/Units/Warp Prism.jpg",
        "Zealot":"../assets/icons/Protoss/Units/Zealot.jpg",

        "Banshee":"../assets/icons/Terran/Units/Banshee.jpg",
        "Battlecruiser":"../assets/icons/Terran/Units/Battlecruiser.jpg",
        "Cyclone":"../assets/icons/Terran/Units/Cyclone.jpg",
        "Ghost":"../assets/icons/Terran/Units/Ghost.jpg",
        "Hellion":"../assets/icons/Terran/Units/Hellion.jpg",
        "Liberator":"../assets/icons/Terran/Units/Liberator.jpg",
        "Marauder":"../assets/icons/Terran/Units/Marauder.jpg",
        "Marine":"../assets/icons/Terran/Units/Marine.jpg",
        "Medivac":"../assets/icons/Terran/Units/Medivac.jpg",
        "Raven":"../assets/icons/Terran/Units/Raven.jpg",
        "Reaper":"../assets/icons/Terran/Units/Reaper.jpg",
        "SCV":"../assets/icons/Terran/Units/SCV.jpg",
        "Siege Tank":"../assets/icons/Terran/Units/Siege.jpg",
        "Thor":"../assets/icons/Terran/Units/Thor.jpg",
        "Viking":"../assets/icons/Terran/Units/Viking.jpg",
        "Widow Mine":"../assets/icons/Terran/Units/Widow Mine.jpg",

        "Baneling":"../assets/icons/Zerg/Units/Baneling.jpg",
        "Brood Lord":"../assets/icons/Zerg/Units/Brood Lord.jpg",
        "Broodling":"../assets/icons/Zerg/Units/Broodling.jpg",
        "Corruptor":"../assets/icons/Zerg/Units/Corruptor.jpg",
        "Drone":"../assets/icons/Zerg/Units/Drone.jpg",
        "Hydralisk":"../assets/icons/Zerg/Units/Hydralisk.jpg",
        "Infestor":"../assets/icons/Zerg/Units/Infestor.jpg",
        "Lurker":"../assets/icons/Zerg/Units/Lurker.jpg",
        "Mutalisk":"../assets/icons/Zerg/Units/Mutalisk.jpg",
        "Overlord":"../assets/icons/Zerg/Units/Overlord.jpg",
        "Queen":"../assets/icons/Zerg/Units/Queen.jpg",
        "Ravager":"../assets/icons/Zerg/Units/Ravager.jpg",
        "Roach":"../assets/icons/Zerg/Units/Roach.jpg",
        "Swarm Host":"../assets/icons/Zerg/Units/Swarm Host.jpg",
        "Ultralisk":"../assets/icons/Zerg/Units/Ultralisk.jpg",
        "Viper":"../assets/icons/Zerg/Units/Viper.jpg",
        "Zergling":"../assets/icons/Zerg/Units/Zergling.jpg",

        # upgrades
        "Protoss Air Armor 1":"../assets/icons/Protoss/Upgrades/Protoss Air Armor 1.jpg",
        "Protoss Air Armor 2":"../assets/icons/Protoss/Upgrades/Protoss Air Armor 2.jpg",
        "Protoss Air Armor 3":"../assets/icons/Protoss/Upgrades/Protoss Air Armor 3.jpg",
        "Protoss Air Weapons 1":"../assets/icons/Protoss/Upgrades/Protoss Air Weapons 1.jpg",
        "Protoss Air Weapons 2":"../assets/icons/Protoss/Upgrades/Protoss Air Weapons 2.jpg",
        "Protoss Air Weapons 3":"../assets/icons/Protoss/Upgrades/Protoss Air Weapons 3.jpg",
        "Protoss Ground Armor 1":"../assets/icons/Protoss/Upgrades/Protoss Ground Armor 1.jpg",
        "Protoss Ground Armor 2":"../assets/icons/Protoss/Upgrades/Protoss Ground Armor 2.jpg", 
        "Protoss Ground Armor 3":"../assets/icons/Protoss/Upgrades/Protoss Ground Armor 3.jpg",
        "Protoss Ground Weapons 1":"../assets/icons/Protoss/Upgrades/Protoss Ground Weapons 1.jpg",
        "Protoss Ground Weapons 2":"../assets/icons/Protoss/Upgrades/Protoss Ground Weapons 2.jpg",
        "Protoss Ground Weapons 3":"../assets/icons/Protoss/Upgrades/Protoss Ground Weapons 3.jpg", 
        "Protoss Shields 1":"../assets/icons/Protoss/Upgrades/Protoss Shields 1.jpg", 
        "Protoss Shields 2":"../assets/icons/Protoss/Upgrades/Protoss Shields 2.jpg", 
        "Protoss Shields 3":"../assets/icons/Protoss/Upgrades/Protoss Shields 3.jpg", 
        "Anion Pulse Crystals":"../assets/icons/Protoss/Upgrades/Anion Pulse Crystals.jpg", 
        "Blink":"../assets/icons/Protoss/Upgrades/Blink.jpg", 
        "Charge":"../assets/icons/Protoss/Upgrades/Charge.jpg", 
        "Extended Thermal Lance":"../assets/icons/Protoss/Upgrades/Extended Thermal Lance.jpg", 
        "Flux Vanes":"../assets/icons/Protoss/Upgrades/Flux Vanes.jpg", 
        "Gravitic Boosters":"../assets/icons/Protoss/Upgrades/Gravitic Boosters.jpg", 
        "Gravitic Drive":"../assets/icons/Protoss/Upgrades/Gravitic Drive.jpg", 
        "Psionic Storm":"../assets/icons/Protoss/Upgrades/Psionic Storm.jpg", 
        "Resonating Glaives":"../assets/icons/Protoss/Upgrades/Resonating Glaives.jpg", 
        "Shadow Stride":"../assets/icons/Protoss/Upgrades/Shadow Stride.jpg", 
        "Tectonic Destabilizers":"../assets/icons/Protoss/Upgrades/Tectonic Destabilizers.jpg", 
        "Warp Gate":"../assets/icons/Protoss/Upgrades/Warp Gate.jpg", 

        "Terran Infantry Armor 1":"../assets/icons/Terran/Upgrades/Terran Infantry Armor 1.jpg",
        "Terran Infantry Armor 2":"../assets/icons/Terran/Upgrades/Terran Infantry Armor 2.jpg",
        "Terran Infantry Armor 3":"../assets/icons/Terran/Upgrades/Terran Infantry Armor 3.jpg",
        "Terran Infantry Weapons 1":"../assets/icons/Terran/Upgrades/Terran Infantry Weapons 1.jpg",
        "Terran Infantry Weapons 2":"../assets/icons/Terran/Upgrades/Terran Infantry Weapons 2.jpg",
        "Terran Infantry Weapons 3":"../assets/icons/Terran/Upgrades/Terran Infantry Weapons 3.jpg",
        "Terran Vehicle Plating 1":"../assets/icons/Terran/Upgrades/Terran Vehicle Plating 1.jpg",
        "Terran Vehicle Plating 2":"../assets/icons/Terran/Upgrades/Terran Vehicle Plating 2.jpg", 
        "Terran Vehicle Plating 3":"../assets/icons/Terran/Upgrades/Terran Vehicle Plating 3.jpg",
        "Terran Vehicle Weapons 1":"../assets/icons/Terran/Upgrades/Terran Vehicle Weapons 1.jpg",
        "Terran Vehicle Weapons 2":"../assets/icons/Terran/Upgrades/Terran Vehicle Weapons 2.jpg",
        "Terran Vehicle Weapons 3":"../assets/icons/Terran/Upgrades/Terran Vehicle Weapons 3.jpg",
        "Terran Ship Weapons 1":"../assets/icons/Terran/Upgrades/Terran Ship Weapons 1.jpg",
        "Terran Ship Weapons 2":"../assets/icons/Terran/Upgrades/Terran Ship Weapons 2.jpg",
        "Terran Ship Weapons 3":"../assets/icons/Terran/Upgrades/Terran Ship Weapons 3.jpg",
        "Advanced Ballistics":"../assets/icons/Terran/Upgrades/Advanced Ballistics.jpg",
        "Cloaking Field":"../assets/icons/Terran/Upgrades/Cloaking Field.jpg",
        "Combat Shield":"../assets/icons/Terran/Upgrades/Combat Shield.jpg",
        "Concussive Shells":"../assets/icons/Terran/Upgrades/Concussive Shells.jpg",
        "Corvid Reactor":"../assets/icons/Terran/Upgrades/Corvid Reactor.jpg",
        "Drilling Claws":"../assets/icons/Terran/Upgrades/Drilling Claws.jpg",
        "Enhanced Shockwaves":"../assets/icons/Terran/Upgrades/Enhanced Shockwaves.jpg",
        "Hisec Auto Tracking":"../assets/icons/Terran/Upgrades/Hisec Auto Tracking.jpg",
        "Hurricane Thrusters":"../assets/icons/Terran/Upgrades/Hurricane Thrusters.jpg",
        "Hyperflight Rotors":"../assets/icons/Terran/Upgrades/Hyperflight Rotors.jpg",
        "Infernal Pre-Igniter":"../assets/icons/Terran/Upgrades/Infernal Pre-Igniter.jpg",
        "Neosteel Armor":"../assets/icons/Terran/Upgrades/Neosteel Armor.jpg",
        "Permanent Cloaking":"../assets/icons/Terran/Upgrades/Permanent Cloaking.jpg",
        "Smart Servos":"../assets/icons/Terran/Upgrades/Smart Servos.jpg",
        "Stimpack":"../assets/icons/Terran/Upgrades/Stimpack.jpg",
        "Weapon Refit":"../assets/icons/Terran/Upgrades/Weapon Refit.jpg",

        "Zerg Flyer Carapace 1":"../assets/icons/Zerg/Upgrades/Zerg Flyer Carapace 1.jpg",
        "Zerg Flyer Carapace 2":"../assets/icons/Zerg/Upgrades/Zerg Flyer Carapace 2.jpg", 
        "Zerg Flyer Carapace 3":"../assets/icons/Zerg/Upgrades/Zerg Flyer Carapace 3.jpg",
        "Zerg Flyer Weapons 1":"../assets/icons/Zerg/Upgrades/Zerg Flyer Attack 1.jpg",
        "Zerg Flyer Weapons 2":"../assets/icons/Zerg/Upgrades/Zerg Flyer Attack 2.jpg",
        "Zerg Flyer Weapons 3":"../assets/icons/Zerg/Upgrades/Zerg Flyer Attack 3.jpg",
        "Zerg Ground Carapace 1":"../assets/icons/Zerg/Upgrades/Zerg Ground Carapace 1.jpg",
        "Zerg Ground Carapace 2":"../assets/icons/Zerg/Upgrades/Zerg Ground Carapace 2.jpg",
        "Zerg Ground Carapace 3":"../assets/icons/Zerg/Upgrades/Zerg Ground Carapace 3.jpg",
        "Zerg Melee Weapons 1":"../assets/icons/Zerg/Upgrades/Zerg Melee Attacks 1.jpg",
        "Zerg Melee Weapons 2":"../assets/icons/Zerg/Upgrades/Zerg Melee Attacks 2.jpg",
        "Zerg Melee Weapons 3":"../assets/icons/Zerg/Upgrades/Zerg Melee Attacks 3.jpg",
        "Zerg Missile Weapons 1":"../assets/icons/Zerg/Upgrades/Zerg Melee Attacks 1.jpg",
        "Zerg Missile Weapons 2":"../assets/icons/Zerg/Upgrades/Zerg Melee Attacks 2.jpg",
        "Zerg Missile Weapons 3":"../assets/icons/Zerg/Upgrades/Zerg Melee Attacks 3.jpg",
        "Anabolic Synthesis":"../assets/icons/Zerg/Upgrades/Anabolic Synthesis.jpg",
        "Burrow":"../assets/icons/Zerg/Upgrades/Burrow.jpg",
        "Centrifugal Hooks":"../assets/icons/Zerg/Upgrades/Centrifugal Hooks.jpg",
        "Chitinous Plating":"../assets/icons/Zerg/Upgrades/Chitinous Plating.jpg",
        "Glial Reconstitution":"../assets/icons/Zerg/Upgrades/Glial Reconstitution.jpg",
        "Grooved Spines":"../assets/icons/Zerg/Upgrades/Grooved Spines.jpg",
        "Metabolic Boost":"../assets/icons/Zerg/Upgrades/Metabolic Boost.jpg",
        "Muscular Augments":"../assets/icons/Zerg/Upgrades/Muscular Augments.jpg",
        "Neural Parasite":"../assets/icons/Zerg/Upgrades/Neural Parasite.jpg",
        "Pathogen Glands":"../assets/icons/Zerg/Upgrades/Pathogen Glands.jpg",
        "Pneumatized Carapace":"../assets/icons/Zerg/Upgrades/Pneumatized Carapace.jpg",
        "Seismic Spines":"../assets/icons/Zerg/Upgrades/Seismic Spines.jpg",
        "Tunneling Claws":"../assets/icons/Zerg/Upgrades/Tunneling Claws.jpg"
    }

    count = [(lambda i: f"x{i}")(i) for i in range(2, 21)]

    unit_name = unit_name.split(',')[0] if ',' in unit_name else unit_name 
    unit_name = unit_name.split(' (Chrono')[0] if '(Chrono Boost)' in unit_name else unit_name
    unit_name = unit_name.split(' Level')[0] + unit_name.split(' Level')[1] if ' Level' in unit_name else unit_name
    for mod in count:
        if mod in unit_name:
            unit_name = unit_name.split(" " + mod)[0]
            break

    for unit in units:
        if unit == unit_name: return units[unit]

    return "../assets/empty.png"