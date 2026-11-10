# Criteria cards · taxonomy combined-draft-a75aa638d3

Run run-combined-20261109T200052265 · selector rules · embedder local-lsa-64 · reports are synthetic.

### B01 · Vehicle or pedestrian on the runway without clearance

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent RI Runway Incursion*

**Definition.** A ground vehicle, tug or person enters an active runway or its protected area without an ATC clearance.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: A ground vehicle, tug or person enters an active runway or its protected area without an ATC clearance.  `[candidate:B01]`
- Matches 'Vehicle or pedestrian deviation' (FAA Runway Safety programme): A runway incursion caused by a ground vehicle or a person, such as a driver or pedestrian entering a runway without ATC authorization.  `[definition:IND-19]`
- Matches 'Pilot deviation (runway incursion)' (FAA Runway Safety programme – Pilot deviation): A runway incursion caused by a pilot, such as crossing a hold-short line or entering a runway without an ATC clearance.  `[definition:IND-40]`
- Matches 'Runway incursion types' (FAA Runway Safety programme): Runway incursions are classified by cause as pilot deviations, operational incidents (controller actions) or vehicle and pedestrian deviations, and by severity from A to D.  `[definition:IND-02]`
- Narrative describes 'clearance' (8 of 8 supporting reports).  `[report:SAMPLE-008]`  
  > A snow removal vehicle entered the active runway without a clearance during clearing operations.
- Narrative describes 'entered' (8 of 8 supporting reports).  `[report:SAMPLE-008]`  
  > A snow removal vehicle entered the active runway without a clearance during clearing operations.
- Narrative describes 'truck' (4 of 8 supporting reports).  `[report:SYNB-006]`  
  > A fuel truck entered Runway 09L without a clearance late in the evening.

**Exclude when**
- Belongs to sibling B02 'Landing on a taxiway or the wrong runway at night' when it matches that bucket better (1 report(s) assigned there).  `[report:SAMPLE-003]`  
  > After a late runway change the crew did not rebrief the approach and landed on Runway 35L instead of the assigned Runway 35R.
- Belongs to sibling B27 'Crew crossed a hold-short line without clearance' when it matches that bucket better (3 report(s) assigned there).  `[report:SAMPLE-007]`  
  > A readback error led the crew to hear cross Runway 9 instead of hold short of Runway 9, and the aircraft entered the active runway without a clearance.
- Coded RE (Runway Excursion) rather than RI: similar wording, different occurrence category.  `[report:SAMPLE-010]`  
  > Braking action was poor and the aircraft overran the runway end by 60 metres into the runway end safety area.
- Not 'Pushback and towing' — that definition is crosswalked to RAMP, not RI.  `[definition:IND-34]`
- Not 'Runway condition code (RWYCC)' — that definition is crosswalked to RE, not RI.  `[definition:IND-06]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not RI.  `[definition:IND-07]`
- Events better described by CICTT RAMP (Ground Handling) (runner-up parent, margin 0.78).  `[parent:RAMP]`

**Linked example reports**
- SAMPLE-008: "A snow removal vehicle entered the active runway without a clearance during clearing operations."
- SYNB-010: "A airport operations vehicle entered Runway 18R without a clearance shortly after sunrise."
- SYNB-006: "A fuel truck entered Runway 09L without a clearance late in the evening."
- SYNB-007: "A maintenance worker on foot entered Runway 27R without a clearance late in the evening."
- SYNB-005: "A fuel truck entered Runway 36 without a clearance at night."
- SYNB-009: "A snow removal truck entered Runway 18R without a clearance at night."
- SYNB-001: "A tug towing an aircraft entered Rwy 16 without a clearance shortly after sunrise."
- SYNB-004: "A snow removal truck entered Rwy 18R without a clearance shortly after sunrise."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B02 · Landing on a taxiway or the wrong runway at night

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent RI Runway Incursion*

**Definition.** At night or in low light the crew lines up on and lands, or nearly lands, on a taxiway or a runway other than the one assigned.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: At night or in low light the crew lines up on and lands, or nearly lands, on a taxiway or a runway other than the one assigned.  `[candidate:B02]`
- Matches 'Wrong-surface event' (FAA Runway Safety programme): A landing, attempted landing, line-up or takeoff on a surface other than the one assigned: a wrong runway, a taxiway, a closed runway or the wrong airport.  `[definition:IND-03]`
- Matches 'Anomaly: Ground Incursion – Runway or Taxiway' (NASA ASRS coding taxonomy): An aircraft, vehicle or person entering a runway or taxiway without authorization, or an aircraft using a taxiway or the wrong runway for landing or takeoff.  `[definition:IND-04]`
- Narrative describes 'taxiway' (7 of 10 supporting reports).  `[report:SAMPLE-004]`  
  > In low visibility the crew began a takeoff from taxiway Bravo, believing it was the runway.
- Narrative describes 'lights' (6 of 10 supporting reports).  `[report:SAMPLE-001]`  
  > During a night visual approach to Runway 27R the crew lined up on the parallel taxiway, mistaking the taxiway edge lights for runway lights.
- Narrative describes 'lined' (6 of 10 supporting reports).  `[report:SAMPLE-001]`  
  > During a night visual approach to Runway 27R the crew lined up on the parallel taxiway, mistaking the taxiway edge lights for runway lights.

**Exclude when**
- Belongs to sibling B27 'Crew crossed a hold-short line without clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:SYNB-206]`  
  > Taxiing on taxiway Kilo at night, the flight crew crossed the hold-short line for Runway 18R without a clearance.
- Distinguish from sibling B01 'Vehicle or pedestrian on the runway without clearance' under the same parent.  `[sibling:B01]`
- Not 'Runway excursion (veer-off and overrun)' — that definition is crosswalked to RE, not RI.  `[definition:IND-05]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not RI.  `[definition:IND-07]`
- Not 'Tail strike' — that definition is crosswalked to ARC, not RI.  `[definition:IND-35]`
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.53).  `[parent:NAV]`

**Linked example reports**
- SAMPLE-004: "In low visibility the crew began a takeoff from taxiway Bravo, believing it was the runway."
- SAMPLE-001: "During a night visual approach to Runway 27R the crew lined up on the parallel taxiway, mistaking the taxiway edge lights for runway lights."
- SYNB-012: "The crew lined up on taxiway Echo in darkness, mistaking its lights for Runway 18R."
- SYNB-015: "The flight crew lined up on taxiway Charlie at dusk, mistaking its lights for Runway 22."
- SYNB-016: "The captain and first officer lined up on taxiway Alpha at night, mistaking its lights for Runway 04R."
- SYNB-017: "The crew lined up on taxiway Kilo at dusk, mistaking its lights for Runway 04R."
- SAMPLE-005: "The crew landed at a nearby general aviation airport with a similar runway alignment instead of the destination airport."
- SAMPLE-003: "After a late runway change the crew did not rebrief the approach and landed on Runway 35L instead of the assigned Runway 35R."
- SAMPLE-002: "Cleared for takeoff on Runway 4L, the crew taxied onto Runway 4R, which was closed for construction."
- SYNB-011: "The captain and first officer lined up on taxiway Charlie in darkness, mistaking its lights for Runway 34L."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass · G10 pass

### B03 · Veer-off during landing in a strong or gusty crosswind

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent RE Runway Excursion*

**Definition.** In a strong or gusty crosswind the aircraft drifts and veers off the side of the runway during the landing roll.

**Include when**
- The occurrence meets the CICTT RE (Runway Excursion) definition.  `[parent:RE]`
- Core definition: In a strong or gusty crosswind the aircraft drifts and veers off the side of the runway during the landing roll.  `[candidate:B03]`
- Matches 'Crosswind landing' (SKYbrary – Crosswind Landings): Landing with a wind component across the runway; strong or gusty crosswinds near the aircraft limit increase the risk of lateral runway excursion (veer-off).  `[definition:IND-20]`
- Matches 'Runway excursion (veer-off and overrun)' (SKYbrary – Runway Excursion): An aircraft leaves the runway surface during takeoff or landing, either by veering off the side or by overrunning the end.  `[definition:IND-05]`
- Matches 'Anomaly: Ground Excursion – Runway' (NASA ASRS coding taxonomy): An aircraft departs the runway surface during the takeoff or landing roll, including overruns after a long or fast landing.  `[definition:IND-07]`
- Narrative describes 'edge' (8 of 11 supporting reports).  `[report:SYNB-025]`  
  > Landing on Runway 18R with a crosswind near the limit, the A330-300 drifted toward the edge.
- Narrative describes 'anding' (7 of 11 supporting reports).  `[report:SYNB-025]`  
  > Landing on Runway 18R with a crosswind near the limit, the A330-300 drifted toward the edge.
- Narrative describes 'drifted' (7 of 11 supporting reports).  `[report:SYNB-025]`  
  > Landing on Runway 18R with a crosswind near the limit, the A330-300 drifted toward the edge.

**Exclude when**
- Distinguish from sibling B04 'Overrun on a contaminated runway' under the same parent.  `[sibling:B04]`
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not RE.  `[definition:IND-04]`
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not RE.  `[definition:IND-03]`
- Not 'Hard landing, tail strike' — that definition is crosswalked to ARC, not RE.  `[definition:IND-18]`
- Events better described by CICTT ARC (Abnormal Runway Contact) (runner-up parent, margin 0.71).  `[parent:ARC]`

**Linked example reports**
- SAMPLE-014: "In a strong, gusty crosswind the aircraft veered off the left side of the runway during the landing roll."
- SYNB-028: "The aircraft veered off the left side of the runway and stopped on the grass."
- SYNB-025: "Landing on Runway 18R with a crosswind near the limit, the A330-300 drifted toward the edge."
- SYNB-026: "Landing on Runway 36 in strong gusts from the left, the B737-800 drifted toward the edge."
- SYNB-023: "The aircraft veered off the left side of the rwy and stopped on the grass."
- SYNB-019: "The aircraft veered off the left side of the rwy and struck an edge light."
- SYNB-021: "Landing on Runway 31L with a crosswind near the limit, the B767-300F drifted toward the edge."
- SYNB-022: "Landing on Runway 04R in strong gusts from the left, the E175 drifted toward the edge."
- SYNB-024: "Landing on Rwy 31L in strong gusts from the left, the B787-9 drifted toward the edge."
- SYNB-020: "Landing on Rwy 04R with a 30-knot gusting crosswind, the B777-300ER drifted toward the edge."
- SYNB-027: "Landing on Rwy 13 with a crosswind near the limit, the B737 MAX 8 drifted toward the edge."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B04 · Overrun on a contaminated runway

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent RE Runway Excursion*

**Definition.** On a wet, slushy, snowy or icy runway braking is poor and the aircraft overruns the end of the runway.

**Include when**
- The occurrence meets the CICTT RE (Runway Excursion) definition.  `[parent:RE]`
- Core definition: On a wet, slushy, snowy or icy runway braking is poor and the aircraft overruns the end of the runway.  `[candidate:B04]`
- Matches 'Anomaly: Ground Excursion – Runway' (NASA ASRS coding taxonomy): An aircraft departs the runway surface during the takeoff or landing roll, including overruns after a long or fast landing.  `[definition:IND-07]`
- Matches 'Runway excursion (veer-off and overrun)' (SKYbrary – Runway Excursion): An aircraft leaves the runway surface during takeoff or landing, either by veering off the side or by overrunning the end.  `[definition:IND-05]`
- Matches 'Runway condition code (RWYCC)' (ICAO Global Reporting Format (GRF) for runway surface conditions): A runway condition code from 6 (dry) down to 0 reports braking performance on wet or contaminated runways (water, slush, snow, ice), so crews can recompute landing distance.  `[definition:IND-06]`
- Narrative describes 'end' (9 of 10 supporting reports).  `[report:SAMPLE-010]`  
  > Braking action was poor and the aircraft overran the runway end by 60 metres into the runway end safety area.
- Narrative describes 'overran' (8 of 10 supporting reports).  `[report:SAMPLE-010]`  
  > Braking action was poor and the aircraft overran the runway end by 60 metres into the runway end safety area.
- Narrative describes 'action' (7 of 10 supporting reports).  `[report:SAMPLE-010]`  
  > Braking action was poor and the aircraft overran the runway end by 60 metres into the runway end safety area.

**Exclude when**
- Belongs to sibling B03 'Veer-off during landing in a strong or gusty crosswind' when it matches that bucket better (2 report(s) assigned there).  `[report:SYNB-026]`  
  > Landing on Runway 36 in strong gusts from the left, the B737-800 drifted toward the edge.
- Coded RI (Runway Incursion) rather than RE: similar wording, different occurrence category.  `[report:SAMPLE-003]`  
  > After a late runway change the crew did not rebrief the approach and landed on Runway 35L instead of the assigned Runway 35R.
- Not 'Undershoot' — that definition is crosswalked to USOS, not RE.  `[definition:IND-37]`
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not RE.  `[definition:IND-04]`
- Not 'Pilot deviation (runway incursion)' — that definition is crosswalked to RI, not RE.  `[definition:IND-40]`
- Events better described by CICTT USOS (Undershoot/Overshoot) (runner-up parent, margin 0.63).  `[parent:USOS]`

**Linked example reports**
- SAMPLE-010: "Braking action was poor and the aircraft overran the runway end by 60 metres into the runway end safety area."
- SAMPLE-013: "With one thrust reverser unavailable, a long landing on a contaminated runway ended in a low-speed overrun past the runway end."
- SAMPLE-011: "After an unstabilized, fast approach the aircraft touched down 2,500 feet beyond the threshold on a runway reported with standing water and came to a stop in the overrun area."
- SAMPLE-012: "The crew did not recompute the landing distance and the aircraft overran onto the grass beyond the runway end."
- SYNB-036: "Braking action was poor and the B777-300ER overran the end of Runway 36 by 40 metres."
- SYNB-035: "Braking action was poor and the A320 overran the end of Runway 18R into the safety area."
- SYNB-033: "Braking action was poor and the A320 overran the end of Runway 31L onto the grass."
- SYNB-029: "Braking action was poor and the A330-300 overran the end of Runway 16 onto the grass."
- SYNB-034: "Braking action was poor and the B787-9 overran the end of Rwy 18R by 40 metres."
- SYNB-032: "Braking action was poor and the CRJ900 overran the end of Rwy 31L into the safety area."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B05 · Stall warning or upset during a go-around

*Taxonomy version combined-draft-a75aa638d3 · status needs review · parent LOC-I Loss of Control – Inflight*

**Definition.** During a go-around or missed approach the aircraft pitches up with high thrust, energy is mismanaged, and a stall warning or upset follows.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: During a go-around or missed approach the aircraft pitches up with high thrust, energy is mismanaged, and a stall warning or upset follows.  `[candidate:B05]`
- Matches 'Stall prevention and recovery' (FAA Advisory Circular 120-109A – Stall Prevention and Recovery Training): Training to recognise and recover from approaches to stall and full stalls, including during go-arounds with high thrust and pitch.  `[definition:IND-21]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`
- Narrative describes 'pitch' (9 of 10 supporting reports).  `[report:SYNB-196]`  
  > The stall warning sounded falsely and the crew flew pitch and power.
- Narrative describes 'activated' (8 of 10 supporting reports).  `[report:SYNB-037]`  
  > With full thrust the pitch rose to 25 degrees and the speed decayed until the stick shaker activated.
- Narrative describes 'decayed' (8 of 10 supporting reports).  `[report:SYNB-037]`  
  > With full thrust the pitch rose to 25 degrees and the speed decayed until the stick shaker activated.

**Exclude when**
- Coded CFIT (Controlled Flight Into or Toward Terrain) rather than LOC-I: similar wording, different occurrence category.  `[report:SAMPLE-033]`  
  > During a non-precision approach at night the crew received a GPWS terrain warning, climbed and went around.
- Coded USOS (Undershoot/Overshoot) rather than LOC-I: similar wording, different occurrence category.  `[report:SYNB-184]`  
  > A black-hole illusion made the approach look high.
- Coded RE (Runway Excursion) rather than LOC-I: similar wording, different occurrence category.  `[report:SAMPLE-011]`  
  > After an unstabilized, fast approach the aircraft touched down 2,500 feet beyond the threshold on a runway reported with standing water and came to a stop in the overrun area.
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not LOC-I.  `[definition:IND-22]`
- Not 'Terrain awareness and warning system (TAWS)' — that definition is crosswalked to CFIT, not LOC-I.  `[definition:IND-26]`
- Not 'Undershoot' — that definition is crosswalked to USOS, not LOC-I.  `[definition:IND-37]`
- Events better described by CICTT ICE (Icing) (runner-up parent, margin 0.12).  `[parent:ICE]`

**Linked example reports**
- SYNB-196: "The stall warning sounded falsely and the crew flew pitch and power."
- SYNB-037: "With full thrust the pitch rose to 25 degrees and the speed decayed until the stick shaker activated."
- SYNB-040: "With full thrust the pitch rose to 20 degrees and the speed decayed until the stick shaker activated."
- SYNB-042: "With full thrust the pitch rose to 20 degrees and the speed decayed until the stick shaker activated."
- SYNB-039: "With full thrust the pitch rose to 25 degrees and the speed decayed until the stick shaker activated."
- SYNB-043: "With full thrust the pitch rose to 20 degrees and the speed decayed until the stick shaker activated."
- SYNB-038: "With full thrust the pitch rose to 25 degrees and the speed decayed until the stick shaker activated."
- SYNB-041: "With full thrust the pitch rose to 25 degrees and the speed decayed until the stick shaker activated."
- SYNB-049: "On final approach 6 miles behind a B747, the A320 encountered wake turbulence."
- SYNB-044: "With full thrust the pitch rose to 28 degrees and the speed decayed until the stick shaker activated."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 pass · G9 pass · G10 pass

### B06 · Wake turbulence upset on approach

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent TURB Turbulence Encounter*

**Definition.** Wake vortices from a preceding heavier aircraft cause a sudden roll or pitch upset on approach or departure.

**Include when**
- The occurrence meets the CICTT TURB (Turbulence Encounter) definition.  `[parent:TURB]`
- Core definition: Wake vortices from a preceding heavier aircraft cause a sudden roll or pitch upset on approach or departure.  `[candidate:B06]`
- Matches 'Wake turbulence' (FAA Advisory Circular 90-23G – Aircraft Wake Turbulence): Vortices from a preceding aircraft, strongest behind heavy aircraft at slow speed, can cause sudden rolls on approach or departure; spacing reduces the risk.  `[definition:IND-22]`

**Exclude when**
- Coded LOC-I (Loss of Control – Inflight) rather than TURB: similar wording, different occurrence category.  `[report:SAMPLE-018]`  
  > The stick shaker activated and the aircraft descended 3,000 feet during the upset before control was regained.
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not TURB.  `[definition:IND-08]`
- Not 'Unreliable airspeed' — that definition is crosswalked to LOC-I, SCF-NP, not TURB.  `[definition:IND-09]`
- Not 'Stall prevention and recovery' — that definition is crosswalked to LOC-I, not TURB.  `[definition:IND-21]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.57).  `[parent:LOC-I]`

**Linked example reports**
- SAMPLE-027: "Wake turbulence from a heavy aircraft on final approach caused a sudden 30-degree roll."
- SYNB-046: "On final approach 6 miles behind a heavy aircraft, the A321neo encountered wake turbulence."
- SYNB-045: "On final approach 3 miles behind a B777, the B787-9 encountered wake turbulence."
- SYNB-050: "On final approach 6 miles behind a B747, the CRJ900 encountered wake turbulence."
- SYNB-052: "On final approach 5 miles behind a B777, the B767-300F encountered wake turbulence."
- SYNB-048: "On final approach 3 miles behind a A380, the B737-800 encountered wake turbulence."
- SYNB-051: "On final approach 3 miles behind a B777, the CRJ900 encountered wake turbulence."
- SYNB-047: "On final approach 6 miles behind a B777, the B767-300F encountered wake turbulence."
- SAMPLE-026: "Only light chop was expected, but the aircraft met sudden severe turbulence in clear air."
- SAMPLE-023: "The aircraft encountered severe clear-air turbulence at FL350 with no weather shown on radar."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B07 · Loss of separation caused by an ATC clearance

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** A controller clearance or instruction puts two aircraft into conflict, leading to loss of separation or a TCAS alert.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: A controller clearance or instruction puts two aircraft into conflict, leading to loss of separation or a TCAS alert.  `[candidate:B07]`
- Matches 'Loss of separation' (ICAO Doc 4444 – PANS-ATM (separation minima)): Two aircraft come closer than the prescribed separation minima, often after an ATC clearance or instruction puts them in conflict.  `[definition:IND-23]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`
- Matches 'Level bust (altitude deviation)' (EUROCONTROL – Level bust): An unauthorised vertical deviation of more than 300 feet from the cleared flight level or altitude, a common cause of loss of separation and TCAS resolution advisories.  `[definition:IND-11]`
- Narrative describes 'conflicting' (4 of 6 supporting reports).  `[report:SAMPLE-022]`  
  > The controller issued a descent clearance into conflicting traffic and both aircraft received TCAS resolution advisories.
- Narrative describes 'controller' (4 of 6 supporting reports).  `[report:SAMPLE-022]`  
  > The controller issued a descent clearance into conflicting traffic and both aircraft received TCAS resolution advisories.
- Narrative describes 'traffic' (4 of 6 supporting reports).  `[report:SAMPLE-022]`  
  > The controller issued a descent clearance into conflicting traffic and both aircraft received TCAS resolution advisories.

**Exclude when**
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (3 report(s) assigned there).  `[report:SAMPLE-021]`  
  > The resulting level bust triggered a TCAS climb resolution advisory and separation was lost.
- Coded LOC-I (Loss of Control – Inflight) rather than MAC: similar wording, different occurrence category.  `[report:SAMPLE-018]`  
  > The stick shaker activated and the aircraft descended 3,000 feet during the upset before control was regained.
- Coded RI (Runway Incursion) rather than MAC: similar wording, different occurrence category.  `[report:SYNB-010]`  
  > The driver misunderstood a hold-short instruction.
- Not 'GNSS jamming and spoofing' — that definition is crosswalked to NAV, not MAC.  `[definition:IND-27]`
- Not 'Low-level windshear' — that definition is crosswalked to WSTRW, not MAC.  `[definition:IND-36]`
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not MAC.  `[definition:IND-08]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.54).  `[parent:LOC-I]`

**Linked example reports**
- SAMPLE-022: "The controller issued a descent clearance into conflicting traffic and both aircraft received TCAS resolution advisories."
- SYNB-060: "Separation was lost."
- SYNB-059: "Separation was lost."
- SYNB-056: "The controller cleared the B777-300ER to turn left into conflicting traffic at FL310."
- SYNB-058: "The controller cleared the A320 to turn left into conflicting traffic at FL280."
- SYNB-054: "The controller cleared the A320 to descend into conflicting traffic at FL210."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B08 · TCAS resolution advisory after a level bust

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** The aircraft climbs or descends through its cleared altitude (level bust) and a TCAS resolution advisory follows.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: The aircraft climbs or descends through its cleared altitude (level bust) and a TCAS resolution advisory follows.  `[candidate:B08]`
- Matches 'Level bust (altitude deviation)' (EUROCONTROL – Level bust): An unauthorised vertical deviation of more than 300 feet from the cleared flight level or altitude, a common cause of loss of separation and TCAS resolution advisories.  `[definition:IND-11]`
- Matches 'Resolution advisory (RA)' (ICAO Annex 10 – Airborne Collision Avoidance System (ACAS)): An ACAS or TCAS indication to the flight crew recommending a vertical manoeuvre to increase separation from conflicting traffic.  `[definition:IND-10]`
- Narrative describes 'advisory' (11 of 11 supporting reports).  `[report:SAMPLE-019]`  
  > The climbing aircraft overshot its cleared altitude of FL240 by 400 feet, and opposite-direction traffic received a TCAS resolution advisory to descend.
- Narrative describes 'resolution' (11 of 11 supporting reports).  `[report:SAMPLE-019]`  
  > The climbing aircraft overshot its cleared altitude of FL240 by 400 feet, and opposite-direction traffic received a TCAS resolution advisory to descend.
- Narrative describes 'triggered' (9 of 11 supporting reports).  `[report:SAMPLE-021]`  
  > The resulting level bust triggered a TCAS climb resolution advisory and separation was lost.

**Exclude when**
- Belongs to sibling B07 'Loss of separation caused by an ATC clearance' when it matches that bucket better (1 report(s) assigned there).  `[report:SAMPLE-022]`  
  > The controller issued a descent clearance into conflicting traffic and both aircraft received TCAS resolution advisories.
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not MAC.  `[definition:IND-22]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.75).  `[parent:LOC-I]`

**Linked example reports**
- SAMPLE-019: "The climbing aircraft overshot its cleared altitude of FL240 by 400 feet, and opposite-direction traffic received a TCAS resolution advisory to descend."
- SAMPLE-021: "The resulting level bust triggered a TCAS climb resolution advisory and separation was lost."
- SAMPLE-020: "Autopilot mode confusion caused an altitude deviation, and the crew received a TCAS resolution advisory for traffic 600 feet below."
- SYNB-061: "Traffic above triggered a TCAS resolution advisory to level off."
- SYNB-062: "Traffic above triggered a TCAS resolution advisory to climb."
- SYNB-066: "Traffic above triggered a TCAS resolution advisory to level off."
- SYNB-064: "Traffic crossing triggered a TCAS resolution advisory to level off."
- SYNB-067: "Traffic ahead triggered a TCAS resolution advisory to climb."
- SYNB-065: "Traffic crossing triggered a TCAS resolution advisory to level off."
- SYNB-063: "Traffic ahead triggered a TCAS resolution advisory to descend."
- SYNB-068: "Traffic ahead triggered a TCAS resolution advisory to descend."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B09 · Hydraulic system failure in flight

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent SCF-NP System/Component Failure – Non-Powerplant*

**Definition.** Loss of fluid or pressure in a hydraulic system in flight degrades flight controls, brakes or landing gear.

**Include when**
- The occurrence meets the CICTT SCF-NP (System/Component Failure – Non-Powerplant) definition.  `[parent:SCF-NP]`
- Core definition: Loss of fluid or pressure in a hydraulic system in flight degrades flight controls, brakes or landing gear.  `[candidate:B09]`
- Matches 'Hydraulic system failure' (SKYbrary – Hydraulic System Failure): Loss of hydraulic fluid or pressure that degrades flight controls, brakes, steering or landing gear, handled with non-normal checklists.  `[definition:IND-24]`
- Matches 'Landing gear malfunction' (SKYbrary – Landing Gear Malfunction): Failure of a landing gear leg to extend, retract or lock, requiring alternate extension or a landing with gear not fully down.  `[definition:IND-25]`
- Narrative describes 'hydraulic' (10 of 10 supporting reports).  `[report:SYNB-074]`  
  > The flight crew ran the hydraulic loss checklist and diverted.
- Narrative describes 'dropped' (8 of 10 supporting reports).  `[report:SYNB-076]`  
  > At FL350 the left hydraulic system quantity dropped to zero.
- Narrative describes 'quantity' (8 of 10 supporting reports).  `[report:SYNB-076]`  
  > At FL350 the left hydraulic system quantity dropped to zero.

**Exclude when**
- Belongs to sibling B10 'Landing gear did not extend' when it matches that bucket better (2 report(s) assigned there).  `[report:SYNB-083]`  
  > The alternate gear extension did not lock the gear.
- Distinguish from sibling B26 'Unreliable airspeed from blocked pitot probes' under the same parent.  `[sibling:B26]`
- Coded ARC (Abnormal Runway Contact) rather than SCF-NP: similar wording, different occurrence category.  `[report:SAMPLE-036]`  
  > A bounced landing was followed by a hard second touchdown that damaged the nose landing gear.
- Not 'In-flight engine shutdown (IFSD)' — that definition is crosswalked to SCF-PP, not SCF-NP.  `[definition:IND-28]`
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not SCF-NP.  `[definition:IND-08]`
- Not 'Smoke or fumes in flight' — that definition is crosswalked to F-NI, not SCF-NP.  `[definition:IND-32]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.66).  `[parent:SCF-PP]`

**Linked example reports**
- SYNB-074: "The flight crew ran the hydraulic loss checklist and diverted."
- SYNB-071: "The flight crew ran the hydraulic loss checklist and continued to the destination."
- SYNB-076: "At FL350 the left hydraulic system quantity dropped to zero."
- SYNB-075: "At FL180 the B hydraulic system quantity dropped to zero."
- SYNB-073: "At FL310 the green hydraulic system quantity dropped to zero."
- SYNB-078: "At FL350 the green hydraulic system quantity dropped to zero."
- SYNB-069: "At FL210 the green hydraulic system quantity dropped to zero."
- SYNB-072: "At FL280 the A hydraulic system quantity dropped to zero."
- SYNB-070: "At FL210 the B hydraulic system quantity dropped to zero."
- SYNB-077: "At FL280 the green hydraulic system quantity dropped to zero."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B10 · Landing gear did not extend

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent SCF-NP System/Component Failure – Non-Powerplant*

**Definition.** One or more landing gear legs fail to extend or lock down, requiring alternate extension or a gear-up landing.

**Include when**
- The occurrence meets the CICTT SCF-NP (System/Component Failure – Non-Powerplant) definition.  `[parent:SCF-NP]`
- Core definition: One or more landing gear legs fail to extend or lock down, requiring alternate extension or a gear-up landing.  `[candidate:B10]`
- Matches 'Landing gear malfunction' (SKYbrary – Landing Gear Malfunction): Failure of a landing gear leg to extend, retract or lock, requiring alternate extension or a landing with gear not fully down.  `[definition:IND-25]`
- Matches 'Hydraulic system failure' (SKYbrary – Hydraulic System Failure): Loss of hydraulic fluid or pressure that degrades flight controls, brakes, steering or landing gear, handled with non-normal checklists.  `[definition:IND-24]`
- Narrative describes 'alternate' (8 of 8 supporting reports).  `[report:SYNB-083]`  
  > The alternate gear extension did not lock the gear.
- Narrative describes 'extension' (8 of 8 supporting reports).  `[report:SYNB-083]`  
  > The alternate gear extension did not lock the gear.
- Narrative describes 'lock' (6 of 8 supporting reports).  `[report:SYNB-083]`  
  > The alternate gear extension did not lock the gear.

**Exclude when**
- Belongs to sibling B26 'Unreliable airspeed from blocked pitot probes' when it matches that bucket better (1 report(s) assigned there).  `[report:SAMPLE-017]`  
  > A pitot heat failure at cruise produced a falling airspeed indication.
- Distinguish from sibling B09 'Hydraulic system failure in flight' under the same parent.  `[sibling:B09]`
- Coded ARC (Abnormal Runway Contact) rather than SCF-NP: similar wording, different occurrence category.  `[report:SAMPLE-036]`  
  > A bounced landing was followed by a hard second touchdown that damaged the nose landing gear.
- Not 'Hard landing, tail strike' — that definition is crosswalked to ARC, not SCF-NP.  `[definition:IND-18]`
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not SCF-NP.  `[definition:IND-03]`
- Events better described by CICTT ARC (Abnormal Runway Contact) (runner-up parent, margin 0.57).  `[parent:ARC]`

**Linked example reports**
- SYNB-083: "The alternate gear extension did not lock the gear."
- SYNB-085: "The alternate gear extension was used and the gear locked down."
- SYNB-079: "The alternate gear extension did not lock the gear."
- SYNB-081: "The alternate gear extension did not lock the gear."
- SYNB-080: "The alternate gear extension was used and the gear locked down."
- SYNB-084: "The alternate gear extension was used and the gear locked down."
- SYNB-086: "The alternate gear extension worked on the second attempt."
- SYNB-082: "The alternate gear extension worked on the second attempt."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B11 · Terrain warning on a non-precision approach

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent CFIT Controlled Flight Into or Toward Terrain*

**Definition.** During a non-precision or visual approach the aircraft descends too low and the terrain awareness system warns of terrain or obstacles.

**Include when**
- The occurrence meets the CICTT CFIT (Controlled Flight Into or Toward Terrain) definition.  `[parent:CFIT]`
- Core definition: During a non-precision or visual approach the aircraft descends too low and the terrain awareness system warns of terrain or obstacles.  `[candidate:B11]`
- Matches 'Terrain awareness and warning system (TAWS)' (14 CFR 121.354 – Terrain awareness and warning system): Airliners must carry a system that warns the crew of terrain, obstacles and excessive descent so they can climb away before impact.  `[definition:IND-26]`
- Narrative describes 'climbed' (8 of 9 supporting reports).  `[report:SAMPLE-033]`  
  > During a non-precision approach at night the crew received a GPWS terrain warning, climbed and went around.
- Narrative describes 'terrain' (8 of 9 supporting reports).  `[report:SAMPLE-033]`  
  > During a non-precision approach at night the crew received a GPWS terrain warning, climbed and went around.
- Narrative describes 'awareness' (7 of 9 supporting reports).  `[report:SYNB-089]`  
  > The terrain awareness system called TOO LOW TERRAIN and the crew climbed away.

**Exclude when**
- Coded USOS (Undershoot/Overshoot) rather than CFIT: similar wording, different occurrence category.  `[report:SYNB-184]`  
  > On a visual approach at night the E175 touched down on the approach lights short of the threshold of Runway 34L.
- Not 'Undershoot' — that definition is crosswalked to USOS, not CFIT.  `[definition:IND-37]`
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not CFIT.  `[definition:IND-22]`
- Not 'GNSS jamming and spoofing' — that definition is crosswalked to NAV, not CFIT.  `[definition:IND-27]`
- Events better described by CICTT F-NI (Fire/Smoke (Non-Impact)) (runner-up parent, margin 0.61).  `[parent:F-NI]`

**Linked example reports**
- SAMPLE-033: "During a non-precision approach at night the crew received a GPWS terrain warning, climbed and went around."
- SYNB-089: "The terrain awareness system called TOO LOW TERRAIN and the crew climbed away."
- SYNB-091: "Flying a visual approach late in the evening with gusty winds, the aircraft descended below the minimum altitude."
- SYNB-093: "The terrain awareness system called TERRAIN, PULL UP and the crew climbed away."
- SYNB-087: "The terrain awareness system called TERRAIN, PULL UP and the crew climbed away."
- SYNB-092: "The terrain awareness system called SINK RATE and the crew climbed away."
- SYNB-088: "The terrain awareness system called SINK RATE and the crew climbed away."
- SYNB-090: "The terrain awareness system called SINK RATE and the crew climbed away."
- SYNB-094: "The terrain awareness system called SINK RATE and the crew climbed away."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B12 · GNSS interference or spoofing

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent NAV Navigation Error*

**Definition.** Satellite navigation signals are jammed or spoofed, giving false position, lost RNP capability or incorrect time, often near conflict zones.

**Include when**
- The occurrence meets the CICTT NAV (Navigation Error) definition.  `[parent:NAV]`
- Core definition: Satellite navigation signals are jammed or spoofed, giving false position, lost RNP capability or incorrect time, often near conflict zones.  `[candidate:B12]`
- Matches 'GNSS jamming and spoofing' (EASA Safety Information Bulletin 2022-02 – GNSS outages and alterations): Interference with satellite navigation signals, by jamming or spoofing, causes loss of GPS position, false positions or false terrain warnings, especially near conflict zones.  `[definition:IND-27]`
- Narrative describes 'both' (5 of 6 supporting reports).  `[report:SYNB-095]`  
  > Near the Black Sea both GPS receivers showed a position 40 miles in error.
- Narrative describes 'receivers' (5 of 6 supporting reports).  `[report:SYNB-095]`  
  > Near the Black Sea both GPS receivers showed a position 40 miles in error.
- Narrative describes 'error' (4 of 6 supporting reports).  `[report:SYNB-095]`  
  > Near the Black Sea both GPS receivers showed a position 40 miles in error.

**Exclude when**
- Distinguish from sibling B28 'Wrong route or waypoint loaded in the FMS' under the same parent.  `[sibling:B28]`
- Coded MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) rather than NAV: similar wording, different occurrence category.  `[report:SAMPLE-021]`  
  > The resulting level bust triggered a TCAS climb resolution advisory and separation was lost.
- Not 'Conflict: Airborne Conflict / NMAC' — that definition is crosswalked to MAC, not NAV.  `[definition:IND-12]`
- Not 'Loss of separation' — that definition is crosswalked to MAC, ATM, not NAV.  `[definition:IND-23]`
- Not 'Low-level windshear' — that definition is crosswalked to WSTRW, not NAV.  `[definition:IND-36]`
- Events better described by CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) (runner-up parent, margin 0.47).  `[parent:MAC]`

**Linked example reports**
- SYNB-095: "Near the Black Sea both GPS receivers showed a position 40 miles in error."
- SYNB-101: "Near the Black Sea both GPS receivers showed a position 40 miles in error."
- SYNB-100: "Approaching the region both GPS receivers lost signal."
- SYNB-102: "On a route near a conflict area both GPS receivers reported a different time."
- SYNB-098: "Over the eastern Mediterranean both GPS receivers showed a position 40 miles in error."
- SYNB-096: "The position errors stopped after 20 minutes."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B13 · Engine shutdown after loss of oil pressure

*Taxonomy version combined-draft-a75aa638d3 · status needs review · parent SCF-PP System/Component Failure – Powerplant*

**Definition.** Low oil pressure or oil loss in flight leads the crew to shut an engine down as a precaution.

**Include when**
- The occurrence meets the CICTT SCF-PP (System/Component Failure – Powerplant) definition.  `[parent:SCF-PP]`
- Core definition: Low oil pressure or oil loss in flight leads the crew to shut an engine down as a precaution.  `[candidate:B13]`
- Matches 'In-flight engine shutdown (IFSD)' (SKYbrary – In-Flight Shutdown): An engine is shut down in flight because of a failure or a precautionary indication such as low oil pressure, high vibration or fire.  `[definition:IND-28]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Narrative describes 'engine' (9 of 9 supporting reports).  `[report:SYNB-104]`  
  > The flight crew shut the engine down and declared an emergency.
- Narrative describes 'shut' (6 of 9 supporting reports).  `[report:SYNB-104]`  
  > The flight crew shut the engine down and declared an emergency.
- Narrative describes 'returned' (4 of 9 supporting reports).  `[report:SYNB-103]`  
  > The flight crew shut the engine down and returned.

**Exclude when**
- Not 'Hydraulic system failure' — that definition is crosswalked to SCF-NP, not SCF-PP.  `[definition:IND-24]`
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not SCF-PP.  `[definition:IND-08]`
- Not 'Wildlife strike' — that definition is crosswalked to BIRD, not SCF-PP.  `[definition:IND-15]`
- Events better described by CICTT BIRD (Bird) (runner-up parent, margin 0.59).  `[parent:BIRD]`
- Engine damage or shutdown caused by bird ingestion belongs to B15 (bird ingestion damaging an engine).  `[sme:D-75847280c4]`

**Linked example reports**
- SYNB-104: "The flight crew shut the engine down and declared an emergency."
- SYNB-103: "The flight crew shut the engine down and returned."
- SYNB-108: "The flight crew shut the engine down and declared an emergency."
- SYNB-105: "At FL210 the number 2 engine oil pressure fell below the limit."
- SYNB-106: "At FL180 the right engine oil pressure fell below the limit."
- SYNB-107: "At FL370 the right engine oil pressure fell below the limit."
- SYNB-117: "The flight crew shut the engine down and returned."
- SYNB-113: "The crew shut the engine down and returned."
- SYNB-116: "The flight crew shut the engine down and returned."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass · G10 pass

### B14 · Takeoff with frost or ice not removed

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent ICE Icing*

**Definition.** The aircraft departs or begins to depart with frost, snow or ice on its wings because it was not removed or the fluid failed.

**Include when**
- The occurrence meets the CICTT ICE (Icing) definition.  `[parent:ICE]`
- Core definition: The aircraft departs or begins to depart with frost, snow or ice on its wings because it was not removed or the fluid failed.  `[candidate:B14]`
- Matches 'Clean aircraft concept' (FAA Advisory Circular 120-60B – Ground Deicing and Anti-icing Program): No takeoff may be made with frost, ice or snow adhering to wings or control surfaces; contamination must be removed before departure.  `[definition:IND-29]`
- Matches 'Holdover time' (FAA holdover time guidelines (ground de-icing and anti-icing)): The estimated time a de-icing or anti-icing fluid protects aircraft surfaces from frost or ice; if it is exceeded before takeoff, the aircraft must be checked or de-iced again.  `[definition:IND-17]`
- Matches 'In-flight airframe icing' (FAA Advisory Circular 91-74B – Pilot Guide: Flight in Icing Conditions): Ice accumulates on wings, tail and windshield in supercooled cloud or freezing drizzle, increasing drag and stall speed.  `[definition:IND-38]`
- Narrative describes 'airspeed' (2 of 4 supporting reports).  `[report:SAMPLE-015]`  
  > Climbing through FL280 in icing conditions, the captain and first officer airspeed indications disagreed.
- Narrative describes 'fter' (2 of 4 supporting reports).  `[report:SYNB-110]`  
  > After a long taxi in light snow, a passenger reported ice on the wing.
- Narrative describes 'ice' (2 of 4 supporting reports).  `[report:SYNB-110]`  
  > After a long taxi in light snow, a passenger reported ice on the wing.

**Exclude when**
- Belongs to sibling B25 'Airframe icing in flight' when it matches that bucket better (4 report(s) assigned there).  `[report:SYNB-194]`  
  > Holding at 12,000 ft in icing conditions, ice built up on the wings faster than expected.
- Belongs to sibling C8 'Takeoff after de-icing holdover time exceeded' when it matches that bucket better (1 report(s) assigned there).  `[report:SAMPLE-032]`  
  > The takeoff was delayed beyond the de-icing fluid holdover time, and the crew returned to the pad for a second de-icing.
- Coded RAMP (Ground Handling) rather than ICE: similar wording, different occurrence category.  `[report:SYNB-151]`  
  > During pushback from the gate the A320 wing tip struck a parked aircraft.
- Not 'Runway condition code (RWYCC)' — that definition is crosswalked to RE, not ICE.  `[definition:IND-06]`
- Not 'Pushback and towing' — that definition is crosswalked to RAMP, not ICE.  `[definition:IND-34]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not ICE.  `[definition:IND-07]`
- Events better described by CICTT RAMP (Ground Handling) (runner-up parent, margin 0.70).  `[parent:RAMP]`

**Linked example reports**
- SYNB-110: "After a long taxi in light snow, a passenger reported ice on the wing."
- SYNB-109: "After a long taxi in light snow, a passenger reported ice on the wing."
- SAMPLE-015: "Climbing through FL280 in icing conditions, the captain and first officer airspeed indications disagreed."
- SAMPLE-018: "Ice crystals caused unreliable airspeed indications."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B15 · Bird ingestion damaging an engine on takeoff or climb

*Taxonomy version combined-draft-a75aa638d3 · status needs review · parent BIRD Bird*

**Definition.** One or more birds are ingested into an engine during takeoff or initial climb, causing vibration, surging or loss of thrust.

**Include when**
- The occurrence meets the CICTT BIRD (Bird) definition.  `[parent:BIRD]`
- Core definition: One or more birds are ingested into an engine during takeoff or initial climb, causing vibration, surging or loss of thrust.  `[candidate:B15]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Matches 'Damaging bird strike' (FAA National Wildlife Strike Database – strike reporting): A collision with birds that damages the aircraft, such as a cracked windshield, dented radome or ingested engine, reported to the wildlife strike database.  `[definition:IND-39]`
- Matches 'Wildlife strike' (FAA National Wildlife Strike Database): A collision between an aircraft and a bird or other wildlife, including ingestion into an engine, reported with damage and phase of flight.  `[definition:IND-15]`
- Narrative describes 'engine' (11 of 11 supporting reports).  `[report:SAMPLE-031]`  
  > After ingesting a large bird at 3,000 feet the crew received an engine fire warning, shut the engine down and discharged the fire extinguisher.
- Narrative describes 'bird' (10 of 11 supporting reports).  `[report:SAMPLE-031]`  
  > After ingesting a large bird at 3,000 feet the crew received an engine fire warning, shut the engine down and discharged the fire extinguisher.
- Narrative describes 'ingesting' (9 of 11 supporting reports).  `[report:SAMPLE-031]`  
  > After ingesting a large bird at 3,000 feet the crew received an engine fire warning, shut the engine down and discharged the fire extinguisher.

**Exclude when**
- Distinguish from sibling B16 'Bird strike damaging the windshield or nose on approach' under the same parent.  `[sibling:B16]`
- Not 'In-flight engine shutdown (IFSD)' — that definition is crosswalked to SCF-PP, not BIRD.  `[definition:IND-28]`
- Not 'Stall prevention and recovery' — that definition is crosswalked to LOC-I, not BIRD.  `[definition:IND-21]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.02).  `[parent:SCF-PP]`

**Linked example reports**
- SAMPLE-031: "After ingesting a large bird at 3,000 feet the crew received an engine fire warning, shut the engine down and discharged the fire extinguisher."
- SAMPLE-029: "Multiple bird strikes during the takeoff roll caused the right engine to surge, and the crew rejected the takeoff."
- SAMPLE-028: "The engine vibrated and lost thrust, and the crew shut it down and returned."
- SYNB-113: "The right engine showed high vibration after ingesting birds."
- SYNB-117: "The right engine showed high vibration after ingesting birds."
- SYNB-114: "The number 1 engine showed high vibration after ingesting birds."
- SYNB-111: "The number 1 engine surged with loud bangs after ingesting birds."
- SYNB-115: "The left engine lost thrust after ingesting birds."
- SYNB-118: "The left engine showed high vibration after ingesting birds."
- SYNB-116: "The number 1 engine surged with loud bangs after ingesting birds."
- SYNB-112: "The right engine surged with loud bangs after ingesting birds."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 FAIL · G8 pass · G9 pass

### B16 · Bird strike damaging the windshield or nose on approach

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent BIRD Bird*

**Definition.** A large bird or flock strikes the windshield, radome or nose on approach or descent and causes visible damage.

**Include when**
- The occurrence meets the CICTT BIRD (Bird) definition.  `[parent:BIRD]`
- Core definition: A large bird or flock strikes the windshield, radome or nose on approach or descent and causes visible damage.  `[candidate:B16]`
- Matches 'Damaging bird strike' (FAA National Wildlife Strike Database – strike reporting): A collision with birds that damages the aircraft, such as a cracked windshield, dented radome or ingested engine, reported to the wildlife strike database.  `[definition:IND-39]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Matches 'Wildlife strike' (FAA National Wildlife Strike Database): A collision between an aircraft and a bird or other wildlife, including ingestion into an engine, reported with damage and phase of flight.  `[definition:IND-15]`
- Narrative describes 'struck' (10 of 11 supporting reports).  `[report:SYNB-214]`  
  > A bird struck the radome during the approach.
- Narrative describes 'descent' (7 of 11 supporting reports).  `[report:SYNB-120]`  
  > On descent through 5,000 ft a large pelican struck the radome.
- Narrative describes 'large' (7 of 11 supporting reports).  `[report:SYNB-120]`  
  > On descent through 5,000 ft a large pelican struck the radome.

**Exclude when**
- Belongs to sibling B15 'Bird ingestion damaging an engine on takeoff or climb' when it matches that bucket better (1 report(s) assigned there).  `[report:SAMPLE-031]`  
  > After ingesting a large bird at 3,000 feet the crew received an engine fire warning, shut the engine down and discharged the fire extinguisher.
- Not 'Hard landing, tail strike' — that definition is crosswalked to ARC, not BIRD.  `[definition:IND-18]`
- Not 'Tail strike' — that definition is crosswalked to ARC, not BIRD.  `[definition:IND-35]`
- Not 'Terrain awareness and warning system (TAWS)' — that definition is crosswalked to CFIT, not BIRD.  `[definition:IND-26]`
- Events better described by CICTT RAMP (Ground Handling) (runner-up parent, margin 0.75).  `[parent:RAMP]`

**Linked example reports**
- SAMPLE-030: "A bird strike on approach was found on the post-flight inspection, with dents on the radome."
- SYNB-214: "A bird struck the radome during the approach."
- SYNB-254: "A bird struck the windshield during the approach."
- SYNB-120: "On descent through 5,000 ft a large pelican struck the radome."
- SYNB-121: "On descent through 5,000 feet a large eagle struck the radome."
- SYNB-126: "On descent through 3,000 feet a large goose struck the windshield."
- SYNB-123: "On descent through 3,000 ft a large pelican struck the radome."
- SYNB-124: "On descent through 5,000 ft a large goose struck the nose."
- SYNB-119: "On descent through 3,000 ft a large goose struck the windshield."
- SYNB-125: "On descent through 3,000 feet a large pelican struck the radome."
- SYNB-234: "A bird struck the left wing leading edge during the approach."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B17 · Lithium battery fire from a passenger device

*Taxonomy version combined-draft-a75aa638d3 · status needs review · parent F-NI Fire/Smoke (Non-Impact)*

**Definition.** A phone, laptop, power bank or other lithium battery device overheats, smokes or catches fire in the cabin.

**Include when**
- The occurrence meets the CICTT F-NI (Fire/Smoke (Non-Impact)) definition.  `[parent:F-NI]`
- Core definition: A phone, laptop, power bank or other lithium battery device overheats, smokes or catches fire in the cabin.  `[candidate:B17]`
- Matches 'Lithium battery fire' (FAA SAFO – Fire risks from lithium batteries in the cabin): Portable electronic devices and power banks can overheat in thermal runaway, producing smoke and fire in the cabin; crew cool the device with water or non-alcoholic liquid.  `[definition:IND-31]`
- Narrative describes 'bank' (4 of 8 supporting reports).  `[report:SYNB-127]`  
  > A passenger's power bank began smoking after being crushed in a seat mechanism.
- Narrative describes 'began' (4 of 8 supporting reports).  `[report:SYNB-127]`  
  > A passenger's power bank began smoking after being crushed in a seat mechanism.
- Narrative describes 'being' (4 of 8 supporting reports).  `[report:SYNB-127]`  
  > A passenger's power bank began smoking after being crushed in a seat mechanism.

**Exclude when**
- Distinguish from sibling B18 'Electrical smoke or burning smell in the flight deck' under the same parent.  `[sibling:B18]`
- Coded CABIN (Cabin Safety Events) rather than F-NI: similar wording, different occurrence category.  `[report:SYNB-164]`  
  > Cabin crew moved the passenger to another seat.
- Not 'Unruly or disruptive passenger' — that definition is crosswalked to CABIN, not F-NI.  `[definition:IND-30]`
- Events better described by CICTT CABIN (Cabin Safety Events) (runner-up parent, margin -0.09).  `[parent:CABIN]`

**Linked example reports**
- SYNB-127: "A passenger's power bank began smoking after being crushed in a seat mechanism."
- SYNB-129: "A passenger's power bank overheated after being crushed in a seat mechanism."
- SYNB-131: "A passenger's power bank caught fire in a seat pocket."
- SYNB-130: "A passenger's laptop caught fire after being crushed in a seat mechanism."
- SYNB-128: "A passenger's power bank caught fire in a seat pocket."
- SYNB-133: "A passenger's laptop began smoking in the overhead bin."
- SYNB-134: "A passenger's phone began smoking after being crushed in a seat mechanism."
- SYNB-132: "A passenger's phone began smoking in the overhead bin."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 FAIL · G8 pass · G9 pass · G10 pass

### B18 · Electrical smoke or burning smell in the flight deck

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent F-NI Fire/Smoke (Non-Impact)*

**Definition.** Smoke, fumes or a burning electrical smell appears in the flight deck, often traced to wiring, a display or a window heater.

**Include when**
- The occurrence meets the CICTT F-NI (Fire/Smoke (Non-Impact)) definition.  `[parent:F-NI]`
- Core definition: Smoke, fumes or a burning electrical smell appears in the flight deck, often traced to wiring, a display or a window heater.  `[candidate:B18]`
- Matches 'Smoke or fumes in flight' (SKYbrary – Smoke and Fumes): Smoke, fumes or burning smells in the flight deck or cabin, often electrical in origin, handled with oxygen masks and the smoke checklist.  `[definition:IND-32]`
- Narrative describes 'deck' (8 of 8 supporting reports).  `[report:SYNB-138]`  
  > During descent at FL210 we noticed an electrical burning smell in the flight deck.
- Narrative describes 'noticed' (8 of 8 supporting reports).  `[report:SYNB-138]`  
  > During descent at FL210 we noticed an electrical burning smell in the flight deck.
- Narrative describes 'uring' (8 of 8 supporting reports).  `[report:SYNB-138]`  
  > During descent at FL210 we noticed an electrical burning smell in the flight deck.

**Exclude when**
- Distinguish from sibling B17 'Lithium battery fire from a passenger device' under the same parent.  `[sibling:B17]`
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not F-NI.  `[definition:IND-08]`
- Events better described by CICTT SCF-NP (System/Component Failure – Non-Powerplant) (runner-up parent, margin 0.18).  `[parent:SCF-NP]`

**Linked example reports**
- SYNB-138: "During descent at FL210 we noticed an electrical burning smell in the flight deck."
- SYNB-137: "During descent at FL330 the captain and first officer noticed an electrical burning smell in the flight deck."
- SYNB-139: "During cruise at FL310 the flight crew noticed smoke in the flight deck."
- SYNB-141: "During descent at FL240 the captain and first officer noticed smoke in the flight deck."
- SYNB-135: "During climb at FL310 the crew noticed smoke in the flight deck."
- SYNB-142: "During descent at FL330 the crew noticed smoke in the flight deck."
- SYNB-140: "During climb at FL350 the crew noticed haze in the flight deck."
- SYNB-136: "During cruise at FL310 we noticed haze in the flight deck."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B19 · Low fuel after holding or a diversion

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent FUEL Fuel Related*

**Definition.** Extended holding, a missed approach or a diversion leaves the aircraft close to or below final reserve fuel, and the crew declares minimum fuel or a fuel emergency.

**Include when**
- The occurrence meets the CICTT FUEL (Fuel Related) definition.  `[parent:FUEL]`
- Core definition: Extended holding, a missed approach or a diversion leaves the aircraft close to or below final reserve fuel, and the crew declares minimum fuel or a fuel emergency.  `[candidate:B19]`
- Matches 'Minimum fuel and fuel emergency' (ICAO Annex 6 – Fuel planning and in-flight fuel management): The crew declares MINIMUM FUEL when any change may land them below final reserve, and MAYDAY FUEL when the landing fuel is expected to be below final reserve.  `[definition:IND-33]`
- Narrative describes 'dropped' (8 of 8 supporting reports).  `[report:SYNB-146]`  
  > After two missed approaches in clear conditions, fuel dropped toward final reserve.
- Narrative describes 'final' (8 of 8 supporting reports).  `[report:SYNB-146]`  
  > After two missed approaches in clear conditions, fuel dropped toward final reserve.
- Narrative describes 'fter' (8 of 8 supporting reports).  `[report:SYNB-146]`  
  > After two missed approaches in clear conditions, fuel dropped toward final reserve.

**Exclude when**
- Not 'Undershoot' — that definition is crosswalked to USOS, not FUEL.  `[definition:IND-37]`
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not FUEL.  `[definition:IND-22]`
- Events better described by CICTT USOS (Undershoot/Overshoot) (runner-up parent, margin 0.82).  `[parent:USOS]`

**Linked example reports**
- SYNB-146: "After two missed approaches in clear conditions, fuel dropped toward final reserve."
- SYNB-145: "After two missed approaches in clear conditions, fuel dropped toward final reserve."
- SYNB-150: "After two missed approaches with a low overcast, fuel dropped toward final reserve."
- SYNB-144: "After two missed approaches in clear conditions, fuel dropped toward final reserve."
- SYNB-148: "After two missed approaches with gusty winds, fuel dropped toward final reserve."
- SYNB-149: "After 40 minutes of holding in low visibility, fuel dropped toward final reserve."
- SYNB-143: "After a diversion to a busy alternate in light snow, fuel dropped toward final reserve."
- SYNB-147: "After a diversion to a busy alternate in clear conditions, fuel dropped toward final reserve."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B20 · Pushback or towing collision

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent RAMP Ground Handling*

**Definition.** During pushback or towing the tug, towbar or aircraft strikes another aircraft, a vehicle or a fixed object.

**Include when**
- The occurrence meets the CICTT RAMP (Ground Handling) definition.  `[parent:RAMP]`
- Core definition: During pushback or towing the tug, towbar or aircraft strikes another aircraft, a vehicle or a fixed object.  `[candidate:B20]`
- Matches 'Pushback and towing' (IATA Ground Operations Manual – Pushback and towing): Moving an aircraft with a tug or towbar, with wing walkers and headset communication, to prevent collisions with aircraft, vehicles and objects.  `[definition:IND-34]`
- Narrative describes 'gate' (5 of 8 supporting reports).  `[report:SYNB-151]`  
  > During pushback from the gate the A320 wing tip struck a parked aircraft.
- Narrative describes 'pushback' (5 of 8 supporting reports).  `[report:SYNB-151]`  
  > During pushback from the gate the A320 wing tip struck a parked aircraft.
- Narrative describes 'struck' (5 of 8 supporting reports).  `[report:SYNB-151]`  
  > During pushback from the gate the A320 wing tip struck a parked aircraft.

**Exclude when**
- Coded RI (Runway Incursion) rather than RAMP: similar wording, different occurrence category.  `[report:SYNB-001]`  
  > A tug towing an aircraft entered Rwy 16 without a clearance shortly after sunrise.
- Coded ARC (Abnormal Runway Contact) rather than RAMP: similar wording, different occurrence category.  `[report:SAMPLE-035]`  
  > An incorrect takeoff weight in the flight management computer led to early rotation and a tail strike on takeoff.
- Not 'Runway incursion' — that definition is crosswalked to RI, not RAMP.  `[definition:IND-01]`
- Not 'Damaging bird strike' — that definition is crosswalked to BIRD, not RAMP.  `[definition:IND-39]`
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not RAMP.  `[definition:IND-04]`
- Events better described by CICTT RI (Runway Incursion) (runner-up parent, margin 0.50).  `[parent:RI]`

**Linked example reports**
- SYNB-151: "During pushback from the gate the A320 wing tip struck a parked aircraft."
- SYNB-153: "The tug driver could not see the wing tip."
- SYNB-156: "The tug driver could not see the wing tip."
- SYNB-158: "The towbar shear pin failed."
- SYNB-152: "During pushback from the gate the B737 MAX 8 wing tip struck a parked aircraft."
- SYNB-155: "During pushback from the gate the A320 struck a baggage cart."
- SYNB-154: "During pushback from the gate the B787-9 tail struck a light pole."
- SYNB-157: "During pushback from the gate the B777-300ER tail struck a light pole."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B21 · Disruptive or unruly passenger

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent CABIN Cabin Safety Events*

**Definition.** A passenger is aggressive, intoxicated or refuses crew instructions, interfering with the crew or other passengers.

**Include when**
- The occurrence meets the CICTT CABIN (Cabin Safety Events) definition.  `[parent:CABIN]`
- Core definition: A passenger is aggressive, intoxicated or refuses crew instructions, interfering with the crew or other passengers.  `[candidate:B21]`
- Matches 'Unruly or disruptive passenger' (ICAO Doc 10117 – Manual on the Legal Aspects of Unruly and Disruptive Passengers): A passenger who fails to respect rules of conduct or to follow crew instructions, disturbing good order and discipline on board.  `[definition:IND-30]`
- Narrative describes 'passenger' (8 of 8 supporting reports).  `[report:SYNB-160]`  
  > A intoxicated passenger refused to follow crew instructions during the flight.
- Narrative describes 'follow' (5 of 8 supporting reports).  `[report:SYNB-160]`  
  > A intoxicated passenger refused to follow crew instructions during the flight.
- Narrative describes 'instructions' (5 of 8 supporting reports).  `[report:SYNB-160]`  
  > A intoxicated passenger refused to follow crew instructions during the flight.

**Exclude when**
- Belongs to sibling C6 'Clear-air turbulence with cabin injuries' when it matches that bucket better (2 report(s) assigned there).  `[report:SAMPLE-024]`  
  > A passenger standing in the aisle broke an ankle.
- Events better described by CICTT TURB (Turbulence Encounter) (runner-up parent, margin 0.80).  `[parent:TURB]`

**Linked example reports**
- SYNB-160: "A intoxicated passenger refused to follow crew instructions during the flight."
- SYNB-159: "A aggressive passenger refused to follow crew instructions during the flight."
- SYNB-163: "A agitated passenger refused to follow crew instructions during the flight."
- SYNB-161: "A aggressive passenger refused to follow crew instructions during the flight."
- SYNB-166: "A aggressive passenger refused to follow crew instructions during the flight."
- SYNB-164: "A aggressive passenger shouted at cabin crew during the flight."
- SYNB-165: "Cabin crew restrained the passenger with help from others."
- SYNB-162: "Cabin crew restrained the passenger with help from others."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B22 · Tail strike on takeoff

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent ARC Abnormal Runway Contact*

**Definition.** The tail strikes the runway during takeoff rotation, often after early or fast rotation or a wrong takeoff speed or weight.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: The tail strikes the runway during takeoff rotation, often after early or fast rotation or a wrong takeoff speed or weight.  `[candidate:B22]`
- Matches 'Tail strike' (SKYbrary – Tailstrike): The aft fuselage contacts the runway during takeoff rotation or landing, often after early rotation, wrong takeoff speeds or excessive pitch.  `[definition:IND-35]`
- Matches 'Hard landing, tail strike' (SKYbrary – Hard Landing and Tail Strike): A touchdown with a vertical load above limits, a bounced landing, or contact of the tail with the runway during takeoff rotation or landing flare.  `[definition:IND-18]`
- Narrative describes 'rotation' (3 of 6 supporting reports).  `[report:SAMPLE-035]`  
  > An incorrect takeoff weight in the flight management computer led to early rotation and a tail strike on takeoff.
- Narrative describes 'tail' (3 of 6 supporting reports).  `[report:SAMPLE-035]`  
  > An incorrect takeoff weight in the flight management computer led to early rotation and a tail strike on takeoff.
- Narrative describes 'weight' (3 of 6 supporting reports).  `[report:SAMPLE-035]`  
  > An incorrect takeoff weight in the flight management computer led to early rotation and a tail strike on takeoff.

**Exclude when**
- Belongs to sibling C9 'Hard landing or tail strike' when it matches that bucket better (1 report(s) assigned there).  `[report:SYNB-170]`  
  > During rotation on Runway 16 the tail of the CRJ900 struck the runway.
- Coded RI (Runway Incursion) rather than ARC: similar wording, different occurrence category.  `[report:SAMPLE-002]`  
  > Cleared for takeoff on Runway 4L, the crew taxied onto Runway 4R, which was closed for construction.
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not ARC.  `[definition:IND-03]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not ARC.  `[definition:IND-07]`
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not ARC.  `[definition:IND-04]`
- Events better described by CICTT RI (Runway Incursion) (runner-up parent, margin 0.74).  `[parent:RI]`

**Linked example reports**
- SAMPLE-035: "An incorrect takeoff weight in the flight management computer led to early rotation and a tail strike on takeoff."
- SYNB-173: "During rotation on Runway 34L the tail of the B737-800 struck the runway."
- SYNB-174: "During rotation on Runway 36 the tail of the A320 struck the runway."
- SYNB-167: "The takeoff speeds had been computed with the wrong weight."
- SYNB-172: "The takeoff speeds had been computed with the wrong weight."
- SYNB-168: "The pilot flying rotated early and fast."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B23 · Windshear on final approach

*Taxonomy version combined-draft-a75aa638d3 · status needs review · parent WSTRW Windshear or Thunderstorm*

**Definition.** A sudden change in wind speed or direction on approach, often near a thunderstorm or microburst, causes loss of airspeed and a windshear warning.

**Include when**
- The occurrence meets the CICTT WSTRW (Windshear or Thunderstorm) definition.  `[parent:WSTRW]`
- Core definition: A sudden change in wind speed or direction on approach, often near a thunderstorm or microburst, causes loss of airspeed and a windshear warning.  `[candidate:B23]`
- Matches 'Low-level windshear' (FAA Advisory Circular 00-54 – Pilot Windshear Guide): Sudden changes in wind speed or direction near the ground, such as microbursts from thunderstorms, causing airspeed loss; crews fly the windshear escape manoeuvre.  `[definition:IND-36]`

**Exclude when**
- Coded TURB (Turbulence Encounter) rather than WSTRW: similar wording, different occurrence category.  `[report:SYNB-177]`  
  > The reactive windshear warning sounded and the flight crew flew the windshear escape manoeuvre.
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not WSTRW.  `[definition:IND-22]`
- Not 'GNSS jamming and spoofing' — that definition is crosswalked to NAV, not WSTRW.  `[definition:IND-27]`
- Not 'Loss of separation' — that definition is crosswalked to MAC, ATM, not WSTRW.  `[definition:IND-23]`
- Events better described by CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) (runner-up parent, margin 0.77).  `[parent:MAC]`

**Linked example reports**
- SYNB-179: "The predictive windshear warning sounded and the captain and first officer flew the windshear escape manoeuvre."
- SYNB-182: "On short final near a thunderstorm the airspeed dropped by 30 knots."
- SYNB-180: "On short final near a thunderstorm the airspeed dropped by 25 knots."
- SYNB-178: "On short final near a thunderstorm the airspeed dropped by 25 knots."
- SYNB-176: "The predictive windshear warning sounded and the crew flew the windshear escape manoeuvre."
- SYNB-181: "The reactive windshear warning sounded and the CAPT and FO flew the windshear escape manoeuvre."
- SYNB-175: "The predictive windshear warning sounded and the captain and first officer flew the windshear escape manoeuvre."
- SYNB-252: "The approach was flown with extra speed but no windshear was met."
- SYNB-232: "The approach was flown normally with no windshear encountered."
- SYNB-272: "The approach was flown to the other rwy without problems."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass · G10 pass

### B24 · Landing short of the runway

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent USOS Undershoot/Overshoot*

**Definition.** The aircraft touches down before the runway threshold, on the approach lights or in the undershoot area.

**Include when**
- The occurrence meets the CICTT USOS (Undershoot/Overshoot) definition.  `[parent:USOS]`
- Core definition: The aircraft touches down before the runway threshold, on the approach lights or in the undershoot area.  `[candidate:B24]`
- Matches 'Undershoot' (SKYbrary – Landing Short (Undershoot)): The aircraft touches down before the runway threshold, often after an unstable or low approach or a visual illusion.  `[definition:IND-37]`
- Narrative describes 'short' (6 of 6 supporting reports).  `[report:SYNB-184]`  
  > On a visual approach at night the E175 touched down on the approach lights short of the threshold of Runway 34L.
- Narrative describes 'threshold' (6 of 6 supporting reports).  `[report:SYNB-184]`  
  > On a visual approach at night the E175 touched down on the approach lights short of the threshold of Runway 34L.
- Narrative describes 'touched' (6 of 6 supporting reports).  `[report:SYNB-184]`  
  > On a visual approach at night the E175 touched down on the approach lights short of the threshold of Runway 34L.

**Exclude when**
- Coded RE (Runway Excursion) rather than USOS: similar wording, different occurrence category.  `[report:SAMPLE-011]`  
  > After an unstabilized, fast approach the aircraft touched down 2,500 feet beyond the threshold on a runway reported with standing water and came to a stop in the overrun area.
- Coded RI (Runway Incursion) rather than USOS: similar wording, different occurrence category.  `[report:SAMPLE-007]`  
  > A readback error led the crew to hear cross Runway 9 instead of hold short of Runway 9, and the aircraft entered the active runway without a clearance.
- Not 'Runway excursion (veer-off and overrun)' — that definition is crosswalked to RE, not USOS.  `[definition:IND-05]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not USOS.  `[definition:IND-07]`
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not USOS.  `[definition:IND-04]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.32).  `[parent:RE]`

**Linked example reports**
- SYNB-184: "On a visual approach at night the E175 touched down on the approach lights short of the threshold of Runway 34L."
- SYNB-187: "On a visual approach shortly after sunrise the B787-9 touched down 50 metres short of the threshold of Runway 34L."
- SYNB-186: "On a non-precision approach late in the evening the B787-9 touched down 50 metres short of the threshold of Runway 34L."
- SYNB-183: "On a RNAV approach late in the evening the B787-9 touched down in the grass short of the threshold of Runway 22."
- SYNB-188: "On a visual approach shortly after sunrise the A321neo touched down in the grass short of the threshold of Runway 16."
- SYNB-185: "On a visual approach shortly after sunrise the A321neo touched down in the grass short of the threshold of Rwy 36."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B25 · Airframe icing in flight

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent ICE Icing*

**Definition.** Ice builds on the wings, tail or windshield in flight in icing conditions, degrading performance or handling.

**Include when**
- The occurrence meets the CICTT ICE (Icing) definition.  `[parent:ICE]`
- Core definition: Ice builds on the wings, tail or windshield in flight in icing conditions, degrading performance or handling.  `[candidate:B25]`
- Matches 'In-flight airframe icing' (FAA Advisory Circular 91-74B – Pilot Guide: Flight in Icing Conditions): Ice accumulates on wings, tail and windshield in supercooled cloud or freezing drizzle, increasing drag and stall speed.  `[definition:IND-38]`
- Matches 'Holdover time' (FAA holdover time guidelines (ground de-icing and anti-icing)): The estimated time a de-icing or anti-icing fluid protects aircraft surfaces from frost or ice; if it is exceeded before takeoff, the aircraft must be checked or de-iced again.  `[definition:IND-17]`
- Matches 'Clean aircraft concept' (FAA Advisory Circular 120-60B – Ground Deicing and Anti-icing Program): No takeoff may be made with frost, ice or snow adhering to wings or control surfaces; contamination must be removed before departure.  `[definition:IND-29]`
- Narrative describes 'built' (4 of 6 supporting reports).  `[report:SYNB-194]`  
  > Holding at 12,000 ft in icing conditions, ice built up on the wings faster than expected.
- Narrative describes 'expected' (4 of 6 supporting reports).  `[report:SYNB-194]`  
  > Holding at 12,000 ft in icing conditions, ice built up on the wings faster than expected.
- Narrative describes 'faster' (4 of 6 supporting reports).  `[report:SYNB-194]`  
  > Holding at 12,000 ft in icing conditions, ice built up on the wings faster than expected.

**Exclude when**
- Belongs to sibling B14 'Takeoff with frost or ice not removed' when it matches that bucket better (2 report(s) assigned there).  `[report:SYNB-110]`  
  > After a long taxi in light snow, a passenger reported ice on the wing.
- Belongs to sibling C8 'Takeoff after de-icing holdover time exceeded' when it matches that bucket better (1 report(s) assigned there).  `[report:SAMPLE-032]`  
  > The takeoff was delayed beyond the de-icing fluid holdover time, and the crew returned to the pad for a second de-icing.
- Coded ARC (Abnormal Runway Contact) rather than ICE: similar wording, different occurrence category.  `[report:SYNB-170]`  
  > The flight crew continued after the tail strike light went out.
- Coded BIRD (Bird) rather than ICE: similar wording, different occurrence category.  `[report:SAMPLE-030]`  
  > There was no indication in flight.
- Not 'Runway condition code (RWYCC)' — that definition is crosswalked to RE, not ICE.  `[definition:IND-06]`
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not ICE.  `[definition:IND-08]`
- Not 'Hydraulic system failure' — that definition is crosswalked to SCF-NP, not ICE.  `[definition:IND-24]`
- Events better described by CICTT RAMP (Ground Handling) (runner-up parent, margin 0.63).  `[parent:RAMP]`

**Linked example reports**
- SYNB-194: "Holding at 12,000 ft in icing conditions, ice built up on the wings faster than expected."
- SYNB-190: "Holding at 8,000 feet in icing conditions, ice built up on the wings faster than expected."
- SYNB-193: "The windshield iced over."
- SYNB-189: "The windshield iced over."
- SYNB-191: "Holding at 10,000 ft in supercooled cloud, ice built up on the wings faster than expected."
- SYNB-192: "Holding at 10,000 feet in supercooled cloud, ice built up on the wings faster than expected."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B26 · Unreliable airspeed from blocked pitot probes

*Taxonomy version combined-draft-a75aa638d3 · status needs review · parent SCF-NP System/Component Failure – Non-Powerplant*

**Definition.** Pitot probes blocked by ice, insects or covers give wrong airspeed indications, leading to warnings and autopilot disconnection.

**Include when**
- The occurrence meets the CICTT SCF-NP (System/Component Failure – Non-Powerplant) definition.  `[parent:SCF-NP]`
- Core definition: Pitot probes blocked by ice, insects or covers give wrong airspeed indications, leading to warnings and autopilot disconnection.  `[candidate:B26]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`

**Exclude when**
- Distinguish from sibling B09 'Hydraulic system failure in flight' under the same parent.  `[sibling:B09]`
- Distinguish from sibling B10 'Landing gear did not extend' under the same parent.  `[sibling:B10]`
- Coded LOC-I (Loss of Control – Inflight) rather than SCF-NP: similar wording, different occurrence category.  `[report:SAMPLE-015]`  
  > The autopilot disconnected and the aircraft reached a stall warning before the crew recovered.
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not SCF-NP.  `[definition:IND-08]`
- Not 'Stall prevention and recovery' — that definition is crosswalked to LOC-I, not SCF-NP.  `[definition:IND-21]`
- Not 'In-flight airframe icing' — that definition is crosswalked to ICE, not SCF-NP.  `[definition:IND-38]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.03).  `[parent:LOC-I]`

**Linked example reports**
- SAMPLE-017: "A pitot heat failure at cruise produced a falling airspeed indication."
- SYNB-201: "Ice crystals had blocked the probes."
- SAMPLE-016: "The crew used the unreliable airspeed checklist, flew pitch and power, and returned to the departure airport without further problems."
- SYNB-199: "The autopilot disconnected and we flew pitch and power."
- SYNB-200: "The autopilot disconnected and we flew pitch and power."
- SYNB-198: "The autopilot disconnected and the crew flew pitch and power."
- SYNB-195: "A wasp nest was found in a pitot probe."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 pass · G9 pass

### B27 · Crew crossed a hold-short line without clearance

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent RI Runway Incursion*

**Definition.** The flight crew taxis past a runway hold-short line without a clearance to enter or cross the runway (pilot deviation).

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: The flight crew taxis past a runway hold-short line without a clearance to enter or cross the runway (pilot deviation).  `[candidate:B27]`
- Matches 'Pilot deviation (runway incursion)' (FAA Runway Safety programme – Pilot deviation): A runway incursion caused by a pilot, such as crossing a hold-short line or entering a runway without an ATC clearance.  `[definition:IND-40]`
- Matches 'Runway incursion types' (FAA Runway Safety programme): Runway incursions are classified by cause as pilot deviations, operational incidents (controller actions) or vehicle and pedestrian deviations, and by severity from A to D.  `[definition:IND-02]`
- Matches 'Vehicle or pedestrian deviation' (FAA Runway Safety programme): A runway incursion caused by a ground vehicle or a person, such as a driver or pedestrian entering a runway without ATC authorization.  `[definition:IND-19]`
- Narrative describes 'clearance' (11 of 11 supporting reports).  `[report:SAMPLE-007]`  
  > A readback error led the crew to hear cross Runway 9 instead of hold short of Runway 9, and the aircraft entered the active runway without a clearance.
- Narrative describes 'crossed' (10 of 11 supporting reports).  `[report:SYNB-204]`  
  > Taxiing on taxiway Delta at dusk, the flight crew crossed the hold-short line for Runway 22 without a clearance.
- Narrative describes 'axiing' (9 of 11 supporting reports).  `[report:SYNB-204]`  
  > Taxiing on taxiway Delta at dusk, the flight crew crossed the hold-short line for Runway 22 without a clearance.

**Exclude when**
- Belongs to sibling B01 'Vehicle or pedestrian on the runway without clearance' when it matches that bucket better (1 report(s) assigned there).  `[report:SAMPLE-008]`  
  > A snow removal vehicle entered the active runway without a clearance during clearing operations.
- Distinguish from sibling B02 'Landing on a taxiway or the wrong runway at night' under the same parent.  `[sibling:B02]`
- Not 'Runway condition code (RWYCC)' — that definition is crosswalked to RE, not RI.  `[definition:IND-06]`
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not RI.  `[definition:IND-08]`
- Not 'Undershoot' — that definition is crosswalked to USOS, not RI.  `[definition:IND-37]`
- Events better described by CICTT USOS (Undershoot/Overshoot) (runner-up parent, margin 0.77).  `[parent:USOS]`

**Linked example reports**
- SAMPLE-007: "A readback error led the crew to hear cross Runway 9 instead of hold short of Runway 9, and the aircraft entered the active runway without a clearance."
- SYNB-204: "Taxiing on taxiway Delta at dusk, the flight crew crossed the hold-short line for Runway 22 without a clearance."
- SAMPLE-006: "Taxiing to Runway 16, the crew crossed the hold-short line for Runway 22 without a clearance while another aircraft was on its takeoff roll."
- SYNB-205: "Taxiing on taxiway Charlie at night, the crew crossed the hold-short line for Runway 22 without a clearance."
- SYNB-206: "Taxiing on taxiway Kilo at night, the flight crew crossed the hold-short line for Runway 18R without a clearance."
- SAMPLE-009: "The stop bar lights were on, but the crew continued past the holding point onto the runway after mistaking a frequency change for a crossing clearance."
- SYNB-210: "Taxiing on taxiway Charlie at night, the crew crossed the hold-short line for Runway 34L without a clearance."
- SYNB-203: "Taxiing on twy Echo late in the evening, we crossed the hold-short line for Rwy 22 without a clearance."
- SYNB-209: "Taxiing on taxiway Charlie late in the evening, the flight crew crossed the hold-short line for Runway 04R without a clearance."
- SYNB-207: "Taxiing on taxiway Charlie in daylight, the captain and first officer crossed the hold-short line for Runway 22 without a clearance."
- SYNB-208: "Taxiing on taxiway Alpha shortly after sunrise, we crossed the hold-short line for Runway 16 without a clearance."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B28 · Wrong route or waypoint loaded in the FMS

*Taxonomy version combined-draft-a75aa638d3 · status not grounded · parent NAV Navigation Error*

**Definition.** The flight management system is loaded with the wrong route, waypoint or departure, and the aircraft deviates from its cleared route.

**Include when**
- The occurrence meets the CICTT NAV (Navigation Error) definition.  `[parent:NAV]`
- Core definition: The flight management system is loaded with the wrong route, waypoint or departure, and the aircraft deviates from its cleared route.  `[candidate:B28]`
- Matches 'Lateral navigation error' (SKYbrary – Lateral Navigation Error): The aircraft leaves its cleared route because of a wrong route, waypoint or procedure loaded in the flight management system.  `[definition:IND-41]`

**Exclude when**
- Distinguish from sibling B12 'GNSS interference or spoofing' under the same parent.  `[sibling:B12]`
- Coded OTHR (Other) rather than NAV: similar wording, different occurrence category.  `[report:SYNB-213]`  
  > After departure the aircraft turned toward the wrong waypoint because the wrong departure procedure was entered.
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not NAV.  `[definition:IND-08]`
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not NAV.  `[definition:IND-03]`
- Not 'Clean aircraft concept' — that definition is crosswalked to ICE, not NAV.  `[definition:IND-29]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.55).  `[parent:LOC-I]`

**Linked example reports**
- SYNB-211: "After departure the aircraft turned toward the wrong waypoint because a similar-named waypoint was selected."
- SYNB-212: "After departure the aircraft turned toward the wrong waypoint because an old route was loaded."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 pass · G8 pass · G9 pass · G10 pass

### C1 · Landing or takeoff on an unintended surface

*Merged into B02 before grounding.*

### C2 · Runway entry or crossing without clearance

*Merged into B27 before grounding.*

### C3 · Overrun after a long or fast landing on a wet or contaminated runway

*Merged into B04 before grounding.*

### C4 · Upset or stall after unreliable airspeed

*Merged into B26 before grounding.*

### C5 · TCAS resolution advisory after an altitude deviation

*Merged into B08 before grounding.*

### C6 · Clear-air turbulence with cabin injuries

*Taxonomy version combined-draft-a75aa638d3 · status needs review · parent CABIN Cabin Safety Events*

**Definition.** An unexpected encounter with turbulence in clear air injures passengers or cabin crew who are standing, unbelted or near unsecured carts.

**Include when**
- The occurrence meets the CICTT CABIN (Cabin Safety Events) definition.  `[parent:CABIN]`
- Core definition: An unexpected encounter with turbulence in clear air injures passengers or cabin crew who are standing, unbelted or near unsecured carts.  `[candidate:C6]`
- Matches 'Turbulence-related injuries' (FAA Advisory Circular 120-88A – Preventing Injuries Caused by Turbulence): Passengers and flight attendants are injured in turbulence mainly when standing or not wearing seat belts, and by unsecured carts and galley equipment.  `[definition:IND-14]`
- Narrative describes 'cabin' (4 of 8 supporting reports).  `[report:SAMPLE-025]`  
  > Moderate to severe clear-air turbulence over the mountains caught the cabin with carts not secured, and a flight attendant was struck by a cart.
- Narrative describes 'oderate' (4 of 8 supporting reports).  `[report:SAMPLE-025]`  
  > Moderate to severe clear-air turbulence over the mountains caught the cabin with carts not secured, and a flight attendant was struck by a cart.

**Exclude when**
- Belongs to sibling B21 'Disruptive or unruly passenger' when it matches that bucket better (4 report(s) assigned there).  `[report:SYNB-164]`  
  > Cabin crew moved the passenger to another seat.
- Coded TURB (Turbulence Encounter) rather than CABIN: similar wording, different occurrence category.  `[report:SAMPLE-027]`  
  > The crew recovered and there were no injuries.
- Not 'Clear-air turbulence (CAT)' — that definition is crosswalked to TURB, not CABIN.  `[definition:IND-13]`
- Events better described by CICTT TURB (Turbulence Encounter) (runner-up parent, margin 0.12).  `[parent:TURB]`

**Linked example reports**
- SAMPLE-025: "Moderate to severe clear-air turbulence over the mountains caught the cabin with carts not secured, and a flight attendant was struck by a cart."
- SAMPLE-023: "The aircraft encountered severe clear-air turbulence at FL350 with no weather shown on radar."
- SAMPLE-026: "Only light chop was expected, but the aircraft met sudden severe turbulence in clear air."
- SAMPLE-024: "Unforecast turbulence near the jet stream occurred just after the seat belt sign was turned off."
- SYNB-243: "Moderate turbulence at FL310 spilled drinks in the cabin."
- SYNB-223: "Moderate turbulence at FL240 spilled drinks in the cabin."
- SYNB-263: "Moderate turbulence at FL180 spilled drinks in the cabin."
- SYNB-129: "Cabin crew cooled the device with water."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass · G10 pass

### C7 · Engine damage or shutdown after bird ingestion

*Merged into B15 before grounding.*

### C8 · Takeoff after de-icing holdover time exceeded

*Taxonomy version combined-draft-a75aa638d3 · status grounded · parent ICE Icing*

**Definition.** The aircraft is delayed after ground de-icing and the fluid holdover time is exceeded before takeoff.

**Include when**
- The occurrence meets the CICTT ICE (Icing) definition.  `[parent:ICE]`
- Core definition: The aircraft is delayed after ground de-icing and the fluid holdover time is exceeded before takeoff.  `[candidate:C8]`
- Matches 'Holdover time' (FAA holdover time guidelines (ground de-icing and anti-icing)): The estimated time a de-icing or anti-icing fluid protects aircraft surfaces from frost or ice; if it is exceeded before takeoff, the aircraft must be checked or de-iced again.  `[definition:IND-17]`
- Matches 'Clean aircraft concept' (FAA Advisory Circular 120-60B – Ground Deicing and Anti-icing Program): No takeoff may be made with frost, ice or snow adhering to wings or control surfaces; contamination must be removed before departure.  `[definition:IND-29]`
- Narrative describes 'holdover' (4 of 4 supporting reports).  `[report:SAMPLE-032]`  
  > The takeoff was delayed beyond the de-icing fluid holdover time, and the crew returned to the pad for a second de-icing.
- Narrative describes 'time' (4 of 4 supporting reports).  `[report:SAMPLE-032]`  
  > The takeoff was delayed beyond the de-icing fluid holdover time, and the crew returned to the pad for a second de-icing.
- Narrative describes 'again' (3 of 4 supporting reports).  `[report:SYNB-230]`  
  > The holdover time was checked again before departure.

**Exclude when**
- Belongs to sibling B14 'Takeoff with frost or ice not removed' when it matches that bucket better (1 report(s) assigned there).  `[report:SYNB-109]`  
  > The crew had already started the takeoff roll and rejected the takeoff.
- Distinguish from sibling B25 'Airframe icing in flight' under the same parent.  `[sibling:B25]`
- Coded RI (Runway Incursion) rather than ICE: similar wording, different occurrence category.  `[report:SAMPLE-002]`  
  > The takeoff roll began before the first officer noticed the closure markings, and the takeoff was rejected at 40 knots.
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not ICE.  `[definition:IND-04]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not ICE.  `[definition:IND-07]`
- Not 'Runway incursion' — that definition is crosswalked to RI, not ICE.  `[definition:IND-01]`
- Events better described by CICTT RI (Runway Incursion) (runner-up parent, margin 0.68).  `[parent:RI]`

**Linked example reports**
- SAMPLE-032: "The takeoff was delayed beyond the de-icing fluid holdover time, and the crew returned to the pad for a second de-icing."
- SYNB-230: "The holdover time was checked again before departure."
- SYNB-250: "The holdover time was checked again before departure."
- SYNB-270: "The holdover time was checked again before departure."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C9 · Hard landing or tail strike

*Taxonomy version combined-draft-a75aa638d3 · status needs review · parent ARC Abnormal Runway Contact*

**Definition.** A hard or bounced touchdown, or contact of the tail with the runway during rotation or flare.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: A hard or bounced touchdown, or contact of the tail with the runway during rotation or flare.  `[candidate:C9]`
- Matches 'Hard landing, tail strike' (SKYbrary – Hard Landing and Tail Strike): A touchdown with a vertical load above limits, a bounced landing, or contact of the tail with the runway during takeoff rotation or landing flare.  `[definition:IND-18]`
- Matches 'Tail strike' (SKYbrary – Tailstrike): The aft fuselage contacts the runway during takeoff rotation or landing, often after early rotation, wrong takeoff speeds or excessive pitch.  `[definition:IND-35]`
- Narrative describes 'hard' (5 of 7 supporting reports).  `[report:SAMPLE-034]`  
  > A late flare in gusty winds led to a hard landing and a tail strike.
- Narrative describes 'landing' (5 of 7 supporting reports).  `[report:SAMPLE-034]`  
  > A late flare in gusty winds led to a hard landing and a tail strike.
- Narrative describes 'carried' (3 of 7 supporting reports).  `[report:SYNB-240]`  
  > A hard landing inspection was carried out.

**Exclude when**
- Belongs to sibling B22 'Tail strike on takeoff' when it matches that bucket better (5 report(s) assigned there).  `[report:SAMPLE-035]`  
  > An incorrect takeoff weight in the flight management computer led to early rotation and a tail strike on takeoff.
- Not 'Damaging bird strike' — that definition is crosswalked to BIRD, not ARC.  `[definition:IND-39]`
- Not 'Landing gear malfunction' — that definition is crosswalked to SCF-NP, not ARC.  `[definition:IND-25]`
- Not 'Runway condition code (RWYCC)' — that definition is crosswalked to RE, not ARC.  `[definition:IND-06]`
- Events better described by CICTT USOS (Undershoot/Overshoot) (runner-up parent, margin 0.87).  `[parent:USOS]`

**Linked example reports**
- SAMPLE-034: "A late flare in gusty winds led to a hard landing and a tail strike."
- SAMPLE-036: "A bounced landing was followed by a hard second touchdown that damaged the nose landing gear."
- SYNB-170: "During rotation on Runway 16 the tail of the CRJ900 struck the runway."
- SYNB-240: "A hard landing inspection was carried out."
- SYNB-260: "A hard landing inspection was carried out."
- SYNB-220: "A hard landing inspection was carried out."
- SYNB-169: "During rotation on Runway 09L the tail of the B777-300ER struck the runway."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass · G10 pass
