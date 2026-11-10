# Criteria cards · taxonomy trial-draft-19dc90759f

Run run-trial-20261109T200101139 · selector llm-file · embedder local-lsa-64 · reports are synthetic.

### C1 · Landing or takeoff on an unintended surface

*Taxonomy version trial-draft-19dc90759f · status grounded · parent RI Runway Incursion*

**Definition.** The aircraft lands, lines up to land, or starts a takeoff on a surface other than the assigned runway: a taxiway, a closed or wrong runway, or the wrong airport.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: The aircraft lands, lines up to land, or starts a takeoff on a surface other than the assigned runway: a taxiway, a closed or wrong runway, or the wrong airport.  `[candidate:C1]`
- Matches 'Wrong-surface event' (FAA Runway Safety programme): A landing, attempted landing, line-up or takeoff on a surface other than the one assigned: a wrong runway, a taxiway, a closed runway or the wrong airport.  `[definition:IND-03]`
- Matches 'Anomaly: Ground Incursion – Runway or Taxiway' (NASA ASRS coding taxonomy): An aircraft, vehicle or person entering a runway or taxiway without authorization, or an aircraft using a taxiway or the wrong runway for landing or takeoff.  `[definition:IND-04]`
- Narrative describes 'approach' (2 of 5 supporting reports).  `[report:SAMPLE-001]`  
  > During a night visual approach to Runway 27R the crew lined up on the parallel taxiway, mistaking the taxiway edge lights for runway lights.
- Narrative describes 'instead' (2 of 5 supporting reports).  `[report:SAMPLE-003]`  
  > After a late runway change the crew did not rebrief the approach and landed on Runway 35L instead of the assigned Runway 35R.
- Narrative describes 'takeoff' (2 of 5 supporting reports).  `[report:SAMPLE-002]`  
  > Cleared for takeoff on Runway 4L, the crew taxied onto Runway 4R, which was closed for construction.

**Exclude when**
- Belongs to sibling C2 'Runway entry or crossing without clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:SAMPLE-006]`  
  > Taxiing to Runway 16, the crew crossed the hold-short line for Runway 22 without a clearance while another aircraft was on its takeoff roll.
- Coded RE (Runway Excursion) rather than RI: similar wording, different occurrence category.  `[report:SAMPLE-010]`  
  > The aircraft landed long on a wet runway with a tailwind.
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not RI.  `[definition:IND-07]`
- Not 'Runway excursion (veer-off and overrun)' — that definition is crosswalked to RE, not RI.  `[definition:IND-05]`
- Not 'Hard landing, tail strike' — that definition is crosswalked to ARC, not RI.  `[definition:IND-18]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.36).  `[parent:RE]`

**Linked example reports**
- SAMPLE-001: "During a night visual approach to Runway 27R the crew lined up on the parallel taxiway, mistaking the taxiway edge lights for runway lights."
- SAMPLE-002: "Cleared for takeoff on Runway 4L, the crew taxied onto Runway 4R, which was closed for construction."
- SAMPLE-003: "After a late runway change the crew did not rebrief the approach and landed on Runway 35L instead of the assigned Runway 35R."
- SAMPLE-004: "In low visibility the crew began a takeoff from taxiway Bravo, believing it was the runway."
- SAMPLE-005: "The crew landed at a nearby general aviation airport with a similar runway alignment instead of the destination airport."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C2 · Runway entry or crossing without clearance

*Taxonomy version trial-draft-19dc90759f · status grounded · parent RI Runway Incursion*

**Definition.** An aircraft or vehicle crosses a hold-short line, stop bar or holding point and enters an active runway without a clearance.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: An aircraft or vehicle crosses a hold-short line, stop bar or holding point and enters an active runway without a clearance.  `[candidate:C2]`
- Matches 'Anomaly: Ground Incursion – Runway or Taxiway' (NASA ASRS coding taxonomy): An aircraft, vehicle or person entering a runway or taxiway without authorization, or an aircraft using a taxiway or the wrong runway for landing or takeoff.  `[definition:IND-04]`
- Matches 'Runway incursion' (ICAO Doc 9870, Manual on the Prevention of Runway Incursions): Any occurrence at an aerodrome involving the incorrect presence of an aircraft, vehicle or person on the protected area of a surface designated for the landing and takeoff of aircraft.  `[definition:IND-01]`
- Matches 'Runway incursion types' (FAA Runway Safety programme): Runway incursions are classified by cause as pilot deviations, operational incidents (controller actions) or vehicle and pedestrian deviations, and by severity from A to D.  `[definition:IND-02]`
- Narrative describes 'clearance' (4 of 4 supporting reports).  `[report:SAMPLE-009]`  
  > The stop bar lights were on, but the crew continued past the holding point onto the runway after mistaking a frequency change for a crossing clearance.
- Narrative describes 'runway' (3 of 4 supporting reports).  `[report:SAMPLE-009]`  
  > The stop bar lights were on, but the crew continued past the holding point onto the runway after mistaking a frequency change for a crossing clearance.
- Narrative describes 'active' (2 of 4 supporting reports).  `[report:SAMPLE-007]`  
  > A readback error led the crew to hear cross Runway 9 instead of hold short of Runway 9, and the aircraft entered the active runway without a clearance.

**Exclude when**
- Distinguish from sibling C1 'Landing or takeoff on an unintended surface' under the same parent.  `[sibling:C1]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not RI.  `[definition:IND-07]`
- Not 'Runway excursion (veer-off and overrun)' — that definition is crosswalked to RE, not RI.  `[definition:IND-05]`
- Not 'Runway condition code (RWYCC)' — that definition is crosswalked to RE, not RI.  `[definition:IND-06]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.75).  `[parent:RE]`

**Linked example reports**
- SAMPLE-009: "The stop bar lights were on, but the crew continued past the holding point onto the runway after mistaking a frequency change for a crossing clearance."
- SAMPLE-007: "A readback error led the crew to hear cross Runway 9 instead of hold short of Runway 9, and the aircraft entered the active runway without a clearance."
- SAMPLE-006: "Taxiing to Runway 16, the crew crossed the hold-short line for Runway 22 without a clearance while another aircraft was on its takeoff roll."
- SAMPLE-008: "A snow removal vehicle entered the active runway without a clearance during clearing operations."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C3 · Overrun after a long or fast landing on a wet or contaminated runway

*Taxonomy version trial-draft-19dc90759f · status grounded · parent RE Runway Excursion*

**Definition.** The aircraft touches down long or fast on a wet or contaminated runway, braking is poor, and it overruns the runway end.

**Include when**
- The occurrence meets the CICTT RE (Runway Excursion) definition.  `[parent:RE]`
- Core definition: The aircraft touches down long or fast on a wet or contaminated runway, braking is poor, and it overruns the runway end.  `[candidate:C3]`
- Matches 'Anomaly: Ground Excursion – Runway' (NASA ASRS coding taxonomy): An aircraft departs the runway surface during the takeoff or landing roll, including overruns after a long or fast landing.  `[definition:IND-07]`
- Matches 'Runway condition code (RWYCC)' (ICAO Global Reporting Format (GRF) for runway surface conditions): A runway condition code from 6 (dry) down to 0 reports braking performance on wet or contaminated runways (water, slush, snow, ice), so crews can recompute landing distance.  `[definition:IND-06]`
- Narrative describes 'runway' (3 of 3 supporting reports).  `[report:SAMPLE-010]`  
  > Braking action was poor and the aircraft overran the runway end by 60 metres into the runway end safety area.
- Narrative describes 'area' (2 of 3 supporting reports).  `[report:SAMPLE-010]`  
  > Braking action was poor and the aircraft overran the runway end by 60 metres into the runway end safety area.
- Narrative describes 'end' (2 of 3 supporting reports).  `[report:SAMPLE-010]`  
  > Braking action was poor and the aircraft overran the runway end by 60 metres into the runway end safety area.

**Exclude when**
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not RE.  `[definition:IND-04]`
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not RE.  `[definition:IND-03]`
- Not 'Runway incursion' — that definition is crosswalked to RI, not RE.  `[definition:IND-01]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.48).  `[parent:SCF-PP]`

**Linked example reports**
- SAMPLE-010: "Braking action was poor and the aircraft overran the runway end by 60 metres into the runway end safety area."
- SAMPLE-013: "With one thrust reverser unavailable, a long landing on a contaminated runway ended in a low-speed overrun past the runway end."
- SAMPLE-011: "After an unstabilized, fast approach the aircraft touched down 2,500 feet beyond the threshold on a runway reported with standing water and came to a stop in the overrun area."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C4 · Upset or stall after unreliable airspeed

*Taxonomy version trial-draft-19dc90759f · status needs review · parent LOC-I Loss of Control – Inflight*

**Definition.** Disagreeing or erroneous airspeed indications, for example from icing or pitot failure, lead to a stall warning, overspeed or upset in flight.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: Disagreeing or erroneous airspeed indications, for example from icing or pitot failure, lead to a stall warning, overspeed or upset in flight.  `[candidate:C4]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Narrative describes 'reached' (2 of 3 supporting reports).  `[report:SAMPLE-015]`  
  > The autopilot disconnected and the aircraft reached a stall warning before the crew recovered.
- Narrative describes 'recovered' (2 of 3 supporting reports).  `[report:SAMPLE-015]`  
  > The autopilot disconnected and the aircraft reached a stall warning before the crew recovered.

**Exclude when**
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than LOC-I: similar wording, different occurrence category.  `[report:SAMPLE-016]`  
  > The crew used the unreliable airspeed checklist, flew pitch and power, and returned to the departure airport without further problems.
- Coded ICE (Icing) rather than LOC-I: similar wording, different occurrence category.  `[report:SAMPLE-032]`  
  > The takeoff was delayed beyond the de-icing fluid holdover time, and the crew returned to the pad for a second de-icing.
- Coded BIRD (Bird) rather than LOC-I: similar wording, different occurrence category.  `[report:SAMPLE-030]`  
  > There was no indication in flight.
- Events better described by CICTT ICE (Icing) (runner-up parent, margin 0.05).  `[parent:ICE]`

**Linked example reports**
- SAMPLE-015: "The autopilot disconnected and the aircraft reached a stall warning before the crew recovered."
- SAMPLE-018: "The stick shaker activated and the aircraft descended 3,000 feet during the upset before control was regained."
- SAMPLE-017: "The crew pitched down in response, reached an overspeed and lost significant altitude before recovering."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 FAIL · G8 pass · G9 pass

### C5 · TCAS resolution advisory after an altitude deviation

*Taxonomy version trial-draft-19dc90759f · status grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** The aircraft deviates from its cleared altitude (level bust) and traffic receives a TCAS resolution advisory or separation is lost.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: The aircraft deviates from its cleared altitude (level bust) and traffic receives a TCAS resolution advisory or separation is lost.  `[candidate:C5]`
- Matches 'Level bust (altitude deviation)' (EUROCONTROL – Level bust): An unauthorised vertical deviation of more than 300 feet from the cleared flight level or altitude, a common cause of loss of separation and TCAS resolution advisories.  `[definition:IND-11]`
- Matches 'Resolution advisory (RA)' (ICAO Annex 10 – Airborne Collision Avoidance System (ACAS)): An ACAS or TCAS indication to the flight crew recommending a vertical manoeuvre to increase separation from conflicting traffic.  `[definition:IND-10]`
- Narrative describes 'advisory' (3 of 3 supporting reports).  `[report:SAMPLE-021]`  
  > The resulting level bust triggered a TCAS climb resolution advisory and separation was lost.
- Narrative describes 'resolution' (3 of 3 supporting reports).  `[report:SAMPLE-021]`  
  > The resulting level bust triggered a TCAS climb resolution advisory and separation was lost.
- Narrative describes 'altitude' (2 of 3 supporting reports).  `[report:SAMPLE-019]`  
  > The climbing aircraft overshot its cleared altitude of FL240 by 400 feet, and opposite-direction traffic received a TCAS resolution advisory to descend.

**Exclude when**
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.68).  `[parent:NAV]`

**Linked example reports**
- SAMPLE-021: "The resulting level bust triggered a TCAS climb resolution advisory and separation was lost."
- SAMPLE-019: "The climbing aircraft overshot its cleared altitude of FL240 by 400 feet, and opposite-direction traffic received a TCAS resolution advisory to descend."
- SAMPLE-020: "Autopilot mode confusion caused an altitude deviation, and the crew received a TCAS resolution advisory for traffic 600 feet below."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C6 · Clear-air turbulence with cabin injuries

*Taxonomy version trial-draft-19dc90759f · status needs review · parent TURB Turbulence Encounter*

**Definition.** An unexpected encounter with turbulence in clear air injures passengers or cabin crew who are standing, unbelted or near unsecured carts.

**Include when**
- The occurrence meets the CICTT TURB (Turbulence Encounter) definition.  `[parent:TURB]`
- Core definition: An unexpected encounter with turbulence in clear air injures passengers or cabin crew who are standing, unbelted or near unsecured carts.  `[candidate:C6]`
- Matches 'Clear-air turbulence (CAT)' (SKYbrary – Clear Air Turbulence): Turbulence in cloud-free air, often near jet streams or over mountains, with no visual cue and often not shown on weather radar.  `[definition:IND-13]`
- Matches 'Turbulence-related injuries' (FAA Advisory Circular 120-88A – Preventing Injuries Caused by Turbulence): Passengers and flight attendants are injured in turbulence mainly when standing or not wearing seat belts, and by unsecured carts and galley equipment.  `[definition:IND-14]`
- Narrative describes 'attendant' (2 of 4 supporting reports).  `[report:SAMPLE-025]`  
  > Moderate to severe clear-air turbulence over the mountains caught the cabin with carts not secured, and a flight attendant was struck by a cart.
- Narrative describes 'injured' (2 of 4 supporting reports).  `[report:SAMPLE-026]`  
  > Three passengers who were not wearing seat belts were injured.
- Narrative describes 'passengers' (2 of 4 supporting reports).  `[report:SAMPLE-026]`  
  > Three passengers who were not wearing seat belts were injured.

**Exclude when**
- Events better described by CICTT CABIN (Cabin Safety Events) (runner-up parent, margin 0.02).  `[parent:CABIN]`

**Linked example reports**
- SAMPLE-025: "Moderate to severe clear-air turbulence over the mountains caught the cabin with carts not secured, and a flight attendant was struck by a cart."
- SAMPLE-026: "Three passengers who were not wearing seat belts were injured."
- SAMPLE-023: "Two flight attendants in the aft galley were injured."
- SAMPLE-024: "A passenger standing in the aisle broke an ankle."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 FAIL · G8 pass · G9 pass

### C7 · Engine damage or shutdown after bird ingestion

*Taxonomy version trial-draft-19dc90759f · status grounded · parent SCF-PP System/Component Failure – Powerplant*

**Definition.** Birds ingested into an engine cause vibration, surge, loss of thrust, fire warning or shutdown.

**Include when**
- The occurrence meets the CICTT SCF-PP (System/Component Failure – Powerplant) definition.  `[parent:SCF-PP]`
- Core definition: Birds ingested into an engine cause vibration, surge, loss of thrust, fire warning or shutdown.  `[candidate:C7]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Narrative describes 'engine' (3 of 3 supporting reports).  `[report:SAMPLE-031]`  
  > After ingesting a large bird at 3,000 feet the crew received an engine fire warning, shut the engine down and discharged the fire extinguisher.
- Narrative describes 'bird' (2 of 3 supporting reports).  `[report:SAMPLE-031]`  
  > After ingesting a large bird at 3,000 feet the crew received an engine fire warning, shut the engine down and discharged the fire extinguisher.
- Narrative describes 'shut' (2 of 3 supporting reports).  `[report:SAMPLE-031]`  
  > After ingesting a large bird at 3,000 feet the crew received an engine fire warning, shut the engine down and discharged the fire extinguisher.

**Exclude when**
- Not 'Wildlife strike' — that definition is crosswalked to BIRD, not SCF-PP.  `[definition:IND-15]`
- Events better described by CICTT BIRD (Bird) (runner-up parent, margin 0.10).  `[parent:BIRD]`

**Linked example reports**
- SAMPLE-031: "After ingesting a large bird at 3,000 feet the crew received an engine fire warning, shut the engine down and discharged the fire extinguisher."
- SAMPLE-028: "The engine vibrated and lost thrust, and the crew shut it down and returned."
- SAMPLE-029: "Multiple bird strikes during the takeoff roll caused the right engine to surge, and the crew rejected the takeoff."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C8 · Takeoff after de-icing holdover time exceeded

*Taxonomy version trial-draft-19dc90759f · status not grounded · parent ICE Icing*

**Definition.** The aircraft is delayed after ground de-icing and the fluid holdover time is exceeded before takeoff.

**Include when**
- The occurrence meets the CICTT ICE (Icing) definition.  `[parent:ICE]`
- Core definition: The aircraft is delayed after ground de-icing and the fluid holdover time is exceeded before takeoff.  `[candidate:C8]`
- Matches 'Holdover time' (FAA holdover time guidelines (ground de-icing and anti-icing)): The estimated time a de-icing or anti-icing fluid protects aircraft surfaces from frost or ice; if it is exceeded before takeoff, the aircraft must be checked or de-iced again.  `[definition:IND-17]`

**Exclude when**
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not ICE.  `[definition:IND-04]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not ICE.  `[definition:IND-07]`
- Not 'Runway incursion' — that definition is crosswalked to RI, not ICE.  `[definition:IND-01]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.73).  `[parent:RE]`

**Linked example reports**
- SAMPLE-032: "The takeoff was delayed beyond the de-icing fluid holdover time, and the crew returned to the pad for a second de-icing."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### C9 · Hard landing or tail strike

*Taxonomy version trial-draft-19dc90759f · status needs review · parent ARC Abnormal Runway Contact*

**Definition.** A hard or bounced touchdown, or contact of the tail with the runway during rotation or flare.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: A hard or bounced touchdown, or contact of the tail with the runway during rotation or flare.  `[candidate:C9]`
- Matches 'Hard landing, tail strike' (SKYbrary – Hard Landing and Tail Strike): A touchdown with a vertical load above limits, a bounced landing, or contact of the tail with the runway during takeoff rotation or landing flare.  `[definition:IND-18]`
- Narrative describes 'hard' (2 of 3 supporting reports).  `[report:SAMPLE-034]`  
  > A late flare in gusty winds led to a hard landing and a tail strike.
- Narrative describes 'led' (2 of 3 supporting reports).  `[report:SAMPLE-034]`  
  > A late flare in gusty winds led to a hard landing and a tail strike.
- Narrative describes 'strike' (2 of 3 supporting reports).  `[report:SAMPLE-034]`  
  > A late flare in gusty winds led to a hard landing and a tail strike.

**Exclude when**
- Coded RE (Runway Excursion) rather than ARC: similar wording, different occurrence category.  `[report:SAMPLE-010]`  
  > Braking action was poor and the aircraft overran the runway end by 60 metres into the runway end safety area.
- Coded RI (Runway Incursion) rather than ARC: similar wording, different occurrence category.  `[report:SAMPLE-003]`  
  > After a late runway change the crew did not rebrief the approach and landed on Runway 35L instead of the assigned Runway 35R.
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not ARC.  `[definition:IND-07]`
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not ARC.  `[definition:IND-03]`
- Events better described by CICTT RI (Runway Incursion) (runner-up parent, margin 0.48).  `[parent:RI]`

**Linked example reports**
- SAMPLE-034: "A late flare in gusty winds led to a hard landing and a tail strike."
- SAMPLE-036: "A bounced landing was followed by a hard second touchdown that damaged the nose landing gear."
- SAMPLE-035: "An incorrect takeoff weight in the flight management computer led to early rotation and a tail strike on takeoff."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass
