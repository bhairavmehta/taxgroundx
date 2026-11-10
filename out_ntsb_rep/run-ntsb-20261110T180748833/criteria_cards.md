# Criteria cards · taxonomy ntsb-draft-dadb5659b8

Run run-ntsb-20261110T180748833 · selector rules · embedder local-lsa-128 · reports are synthetic.

### B01 · Vehicle or pedestrian on the runway without clearance

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent RI Runway Incursion*

**Definition.** A ground vehicle, tug or person enters an active runway or its protected area without an ATC clearance.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: A ground vehicle, tug or person enters an active runway or its protected area without an ATC clearance.  `[candidate:B01]`
- Matches 'Pilot deviation (runway incursion)' (FAA Runway Safety programme – Pilot deviation): A runway incursion caused by a pilot, such as crossing a hold-short line or entering a runway without an ATC clearance.  `[definition:IND-40]`
- Matches 'Vehicle or pedestrian deviation' (FAA Runway Safety programme): A runway incursion caused by a ground vehicle or a person, such as a driver or pedestrian entering a runway without ATC authorization.  `[definition:IND-19]`
- Matches 'Anomaly: Ground Incursion – Runway or Taxiway' (NASA ASRS coding taxonomy): An aircraft, vehicle or person entering a runway or taxiway without authorization, or an aircraft using a taxiway or the wrong runway for landing or takeoff.  `[definition:IND-04]`

**Exclude when**
- Belongs to sibling B27 'Crew crossed a hold-short line without clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:DCA18IA081]`  
  > The captain stated that shortly after crossing the initial approach fix, the airplane exited the clouds and that he observed what he believed was runway 06 and runway lights, though according to his interview he questioned whether the runway lights were on bright or dim.
- Distinguish from sibling B02 'Landing on a taxiway or the wrong runway at night' under the same parent.  `[sibling:B02]`
- Coded ATM (ATM/CNS) rather than RI: similar wording, different occurrence category.  `[report:OPS12IA849]`  
  > At 1409:19, the local controller stated, "And Brickyard 3329 you can uh contact uh stand by." At 1409:30, she transmitted, "...Brickyard 3329 turn right heading 180." The pilot acknowledged, and continued, "We were cleared the river back there – what happened?" The local controller did not respond because she was instructing an aircraft that had been holding on runway 1 awaiting takeoff clearance to exit the runway.
- Coded LALT (Low Altitude Operations) rather than RI: similar wording, different occurrence category.  `[report:WPR14FA182]`  
  > The airplane contacted the runway prior to reaching the ribbon, slid inverted between the ground crew personnel holding the ribbon poles, and came to a stop a few hundred feet beyond them.
- Coded MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) rather than RI: similar wording, different occurrence category.  `[report:WPR15MA243/2]`  
  > The LC also indicated in the postaccident interview that controllers have personal limits about how many airplanes they could handle and that he could handle four aircraft on runway 26R and three aircraft on runway 26L.
- Not 'Loss of separation' — that definition is crosswalked to MAC, ATM, not RI.  `[definition:IND-23]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not RI.  `[definition:IND-07]`
- Events better described by CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) (runner-up parent, margin 0.40).  `[parent:MAC]`

**Linked example reports**
- DCA23LA133: "(As previously stated, the airplane was precluded by company procedures from landing on runway 4R and holding short of runway 8L.) The UAL384 airplane subsequently crossed runway 4L without stopping at the hold-short line on taxiway K."
- OPS08IA015: "When asked what he meant by that clearance, the local controller stated that he wanted the aircraft to get off the runway even if it had to turn into the grass."
- OPS18IA014: "During the conversation, the chief pilot reported the pilot of ENY3660 had reported that as the aircraft was abeam taxiway U, the vehicle was off the runway surface but between the runway edge marking and the hold short lines on taxiway U and that there was no overflight."
- DCA26MA161: "The airplane’s CVR captured the communications between Truck 1 and the LC that were transmitted on the LC frequency (including the request and clearance to cross runway 4)."
- NYC08FA265: "Upon receipt of any clearance from ATC to cross a runway or taxiway, vehicle operators shall look both ways to ensure it is safe to cross.” On January 25, 2010, suggestions were provided to the FAA via the AAI-100 (Office of Accident Investigation) party representative to the investigation, to: 1) Revise both the FAA’s “Airport Ground Vehicle Operations, An FAA Guide” and FAA AC150/5210-20 publications to include ground vehicle operators’ requirement to visually confirm that an active runway was clear prior to crossing, even with ATCT clearance, 2) Review airport ACMs and airport-ATCT Letters of Agreement to ensure that appropriate language is included for vehicle operators’ runway vigilance, even with ATCT clearance, and 3) That FAA ensure that the increased vehicle operators’ vigilance requirements be incorporated into local airport ground vehicle training programs."
- OPS16IA004: "Airport Runway Status Lights System FLL runway 28R was equipped with RWSLs, a "fully automated system that provides runway status information to pilots and surface vehicle operators to clearly indicate when it is unsafe to enter, cross, takeoff from, or land on a runway." When operational, RWSLs have two states; ON (lights are illuminated red) and OFF (lights are off), and are switched automatically based on input from the ASDE-X system and independent of air traffic controllers."
- OPS09IA004: "HISTORY OF FLIGHT The Andrews Air Force Base (ADW) ground controller, working the ground control (GC), clearance delivery (CD), and flight data (FD) positions combined, authorized four vehicles to cross runway 19R without the local controller’s approval (LC) while VM206, a BE-20, was departing runway 19R."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 pass · G8 pass · G9 pass

### B02 · Landing on a taxiway or the wrong runway at night

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent RI Runway Incursion*

**Definition.** At night or in low light the crew lines up on and lands, or nearly lands, on a taxiway or a runway other than the one assigned.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: At night or in low light the crew lines up on and lands, or nearly lands, on a taxiway or a runway other than the one assigned.  `[candidate:B02]`
- Matches 'Wrong-surface event' (FAA Runway Safety programme): A landing, attempted landing, line-up or takeoff on a surface other than the one assigned: a wrong runway, a taxiway, a closed runway or the wrong airport.  `[definition:IND-03]`
- Matches 'Anomaly: Ground Incursion – Runway or Taxiway' (NASA ASRS coding taxonomy): An aircraft, vehicle or person entering a runway or taxiway without authorization, or an aircraft using a taxiway or the wrong runway for landing or takeoff.  `[definition:IND-04]`
- Matches 'Runway incursion' (ICAO Doc 9870, Manual on the Prevention of Runway Incursions): Any occurrence at an aerodrome involving the incorrect presence of an aircraft, vehicle or person on the protected area of a surface designated for the landing and takeoff of aircraft.  `[definition:IND-01]`

**Exclude when**
- Belongs to sibling B01 'Vehicle or pedestrian on the runway without clearance' when it matches that bucket better (3 report(s) assigned there).  `[report:DCA23LA133]`  
  > Additionally, in case they were given runway 4R, they briefed the anticipated taxi plan which included possibly exiting at taxiway “K” or exiting at the end of the runway on taxiway “C.” Furthermore, in her postincident statement, the first officer indicated that she briefed the published hot spot, referred to as HS2, (see figure 2) located at taxiway “K” in case they were given runway 4R for landing.
- Belongs to sibling B27 'Crew crossed a hold-short line without clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:DCA18IA081]`  
  > Probable cause: the flight crew's misidentification of the taxiway as the landing runway due to the failure of the runway lighting that caused only the taxiway lights to be illuminated.
- Coded RE (Runway Excursion) rather than RI: similar wording, different occurrence category.  `[report:DCA19MA143]`  
  > The RA controller also provided rollout and missed approach instructions and advised the flight crew that the short-field arresting gear on runway 10 was rigged (according to a Miami Air operations bulletin, arresting gear on runways places no limitations on Boeing 737 takeoff or landing operations; see Airport Information).
- Coded ARC (Abnormal Runway Contact) rather than RI: similar wording, different occurrence category.  `[report:DCA14MA081]`  
  > Both pilots stated during postaccident interviews that they verified the ATC routing loaded into the FMC while still at the gate before pushback; however, neither pilot realized that the departure runway loaded into the FMC was runway 27R instead of the assigned runway 27L.
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not RI.  `[definition:IND-07]`
- Not 'Runway excursion (veer-off and overrun)' — that definition is crosswalked to RE, not RI.  `[definition:IND-05]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.57).  `[parent:RE]`

**Linked example reports**
- OPS08IA015/2: "Mesa Air Shuttle flight 7138, a Canadair CRJ-700 carrying 56 passengers and four crew from ABE to Chicago as a scheduled 14 Code of Federal Regulations (CFR) part 121 flight, aborted takeoff because N736GV, a Cessna 172 carrying a pilot and two passengers under 14 CFR part 91, had just landed and was still taxiing on the runway near the intersection with taxiway B."
- OPS17IA008/2: "• Runway Entrance Lights (RELs) provide signal to aircraft crossing entering runway from intersecting taxiway • Takeoff Hold Lights (THLs) provide signal to aircraft in position for takeoff" RELs The FAA website stated the following, in part: Runway Entrance Lights are a string of lights located around the center of taxiways/runway crossings and illuminate red when there is high-speed traffic on or approaching the runway to signal that it is unsafe to enter the runway."
- OPS09IA005: "N409DR exited the runway at taxiway D6 while JIA390 exited the runway at taxiway C9."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### B03 · Veer-off during landing in a strong or gusty crosswind

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent LOC-G Loss of Control – Ground*

**Definition.** In a strong or gusty crosswind the aircraft drifts and veers off the side of the runway during the landing roll.

**Include when**
- The occurrence meets the CICTT LOC-G (Loss of Control – Ground) definition.  `[parent:LOC-G]`
- Core definition: In a strong or gusty crosswind the aircraft drifts and veers off the side of the runway during the landing roll.  `[candidate:B03]`
- Narrative describes 'directional' (9 of 12 supporting reports).  `[report:CEN23LA378]`  
  > Probable cause: The pilot’s failure to maintain directional control while landing in gusty crosswind conditions.

**Exclude when**
- Distinguish from sibling B14 'Takeoff with frost or ice not removed' under the same parent.  `[sibling:B14]`
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than LOC-G: similar wording, different occurrence category.  `[report:ERA25LA090]`  
  > Probable cause: A landing gear collapse during landing in gusty crosswind conditions.
- Coded ARC (Abnormal Runway Contact) rather than LOC-G: similar wording, different occurrence category.  `[report:ANC24LA010]`  
  > Probable cause: The first pilot’s failure to maintain a stabilized approach, in gusty crosswind conditions, in an environment favoring wake turbulence.
- Coded RE (Runway Excursion) rather than LOC-G: similar wording, different occurrence category.  `[report:DCA19MA143]`  
  > At 2140:31, the captain called for the Landing checklist, and the first officer responded, “ah…speedbrakes ah armed, landing gear down three green, flaps thirty.” At 2140:40, the airplane was about 1,100 ft msl and about 2.8 nm from the runway 10 displaced threshold; its descent rate decreased to 1,000 fpm, its indicated airspeed decreased to the target approach speed of 153 knots, and the groundspeed decreased to 166 knots.
- Not 'Crosswind landing' — that definition is crosswalked to RE, not LOC-G.  `[definition:IND-20]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not LOC-G.  `[definition:IND-07]`
- Not 'Runway excursion (veer-off and overrun)' — that definition is crosswalked to RE, not LOC-G.  `[definition:IND-05]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.23).  `[parent:RE]`

**Linked example reports**
- ERA21LA353: "According to the EMB-505 POH, landing performance data were predicated on the following criteria: · Steady 3° angle approach at Vref in the landing configuration, · Vref maintained at the runway threshold, · idle thrust established at the runway threshold, · attitude maintained until main landing gear touchdown, · maximum brake applied immediately after main landing gear touchdown, and · antiskid system operative."
- CEN23LA378: "Probable cause: The pilot’s failure to maintain directional control while landing in gusty crosswind conditions."
- GAA16CA194: "Probable cause: The student pilot's failure to maintain directional control during the landing roll in gusty crosswind conditions, which resulted in a runway excursion and collision with a runway distance remaining sign."
- CEN22LA332: "Probable cause: The pilot’s failure to maintain directional control during the landing roll with a gusty crosswind."
- CEN22LA337: "Probable cause: The pilot’s failure to maintain directional control during the landing roll with a gusty crosswind."
- GAA16CA184: "The pilot reported that he was landing in gusty crosswind conditions following a parachute jump flight, and that the gusty conditions had persisted for the previous 10 skydiving flights that day."
- GAA16CA249: "Probable cause: The pilot's failure to maintain directional control during the landing roll in gusty crosswind conditions, which resulted in a runway excursion and nose over."
- ERA25LA221: "Probable cause: The flight instructor’s failure to maintain directional control during the landing roll in gusty crosswind conditions."
- CEN09CA464: "Probable cause: The pilot's failure to maintain directional control while landing in gusty, crosswind conditions."
- GAA16CA402: "The pilot reported that during the landing in gusty crosswind conditions, the airplane touched down "firm" with the landing gear side loaded."
- CEN24LA074: "Probable cause: The pilot’s loss of directional control during landing in gusty crosswind conditions."
- WPR10CA296: "Probable cause: The pilot's inadequate compensation for the crosswind condition and failure to maintain directional control during the landing roll in gusty crosswind conditions."

**Checks:** G1 pass · G2 FAIL · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 FAIL · G9 pass

### B04 · Overrun on a contaminated runway

*Taxonomy version ntsb-draft-dadb5659b8 · status grounded · parent RE Runway Excursion*

**Definition.** On a wet, slushy, snowy or icy runway braking is poor and the aircraft overruns the end of the runway.

**Include when**
- The occurrence meets the CICTT RE (Runway Excursion) definition.  `[parent:RE]`
- Core definition: On a wet, slushy, snowy or icy runway braking is poor and the aircraft overruns the end of the runway.  `[candidate:B04]`
- Matches 'Runway condition code (RWYCC)' (ICAO Global Reporting Format (GRF) for runway surface conditions): A runway condition code from 6 (dry) down to 0 reports braking performance on wet or contaminated runways (water, slush, snow, ice), so crews can recompute landing distance.  `[definition:IND-06]`
- Matches 'Runway excursion (veer-off and overrun)' (SKYbrary – Runway Excursion): An aircraft leaves the runway surface during takeoff or landing, either by veering off the side or by overrunning the end.  `[definition:IND-05]`
- Matches 'Anomaly: Ground Excursion – Runway' (NASA ASRS coding taxonomy): An aircraft departs the runway surface during the takeoff or landing roll, including overruns after a long or fast landing.  `[definition:IND-07]`
- Narrative describes 'runway' (8 of 10 supporting reports).  `[report:CEN14FA505]`  
  > The pilots calculated the runway length required for a wet runway landing and then chose to land on runway 1, which was the longer runway.
- Narrative describes 'landing' (6 of 10 supporting reports).  `[report:CEN14FA505]`  
  > The pilots calculated the runway length required for a wet runway landing and then chose to land on runway 1, which was the longer runway.
- Narrative describes 'pilots' (6 of 10 supporting reports).  `[report:CEN14FA505]`  
  > The pilots calculated the runway length required for a wet runway landing and then chose to land on runway 1, which was the longer runway.

**Exclude when**
- Belongs to sibling B22 'Tail strike on takeoff' when it matches that bucket better (2 report(s) assigned there).  `[report:ERA11LA390]`  
  > It was marked with nonprecision markings that were in good condition Usable length for landing on runway 24 was 3,471 feet due to a displaced threshold on the end of runway 06, marked as a taxiway aligned with a runway, and a chevroned runway safety area on the end of runway 24.
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not RE.  `[definition:IND-04]`
- Not 'Runway incursion' — that definition is crosswalked to RI, not RE.  `[definition:IND-01]`
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not RE.  `[definition:IND-03]`
- Events better described by CICTT CTOL (Collision with Obstacle(s) During Takeoff and Landing) (runner-up parent, margin 0.65).  `[parent:CTOL]`

**Linked example reports**
- CEN14FA505: "The pilots calculated the runway length required for a wet runway landing and then chose to land on runway 1, which was the longer runway."
- DCA19MA143: "Finding: Aircraft-Aircraft oper/perf/capability-Aircraft capability-Braking capability-Capability exceeded."
- CEN15LA057: "Contributing to the pilot's decision to engage the emergency parking brake was the expectation of a faster rate of deceleration and considerably shorter wet runway landing distance provided by the airplane flight manual than that experienced by the crew upon touchdown and an actual wet runway friction level lower than the assumed runway fiction level used in the calculation of the stopping distances published in the airplane flight manual."
- WPR23LA081: "Probable cause: A runway overrun due to the pilot’s failure to stop the airplane as a result of diminished braking action due to a water contaminated runway surface."
- ERA21LA353: "Be advised that the terrain at the approach end of runway 30 is higher than that at the approach end of runway 12, requiring a steeper approach and that you will be landing on a downward sloping runway."
- ERA22LA316: "Probable cause: The malfunction of the braking system fluid line, which resulted in an overrun of the runway."
- ERA22LA150: "The performance calculations also indicated that even with the longer-than-nominal touchdown point and 3-knot fast touchdown airspeed, the accident airplane might have stopped before the end of the runway had it achieved the wet runway wheel braking friction coefficient implied by the airframe manufacturer’s AFM recommendation to increase dry runway landing distance by 30%."
- CEN13CA007: "The pilot subsequently applied heavier braking, but the brakes “seemed to have no effect.” Realizing he was not going to stop the airplane on the remaining runway, the pilot attempted a go-around near the departure end of the runway."
- ERA12IA060: "Probable cause: The pilots’ failure to appropriately apply the landing gear wheel brakes after landing, to properly perform the hard brake pedal-no braking condition procedure following the reported brake failure and to apply the emergency brakes."
- GAA16CA353: "Probable cause: The pilot's decision to land on unsuitable wet terrain, and his failure to stop prior to the end of the runway, which resulted in a runway overrun and impact with tree(s)."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B05 · Stall warning or upset during a go-around

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent LOC-I Loss of Control – Inflight*

**Definition.** During a go-around or missed approach the aircraft pitches up with high thrust, energy is mismanaged, and a stall warning or upset follows.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: During a go-around or missed approach the aircraft pitches up with high thrust, energy is mismanaged, and a stall warning or upset follows.  `[candidate:B05]`
- Matches 'Stall prevention and recovery' (FAA Advisory Circular 120-109A – Stall Prevention and Recovery Training): Training to recognise and recover from approaches to stall and full stalls, including during go-arounds with high thrust and pitch.  `[definition:IND-21]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`

**Exclude when**
- Belongs to sibling B23 'Windshear on final approach' when it matches that bucket better (5 report(s) assigned there).  `[report:ERA22FA004]`  
  > According to the operations manual, the stall warning system was designed to inform the pilot of a forthcoming stall by sounding an aural warning.
- Belongs to sibling C4 'Upset or stall after unreliable airspeed' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN10MA088]`  
  > The witness reported the airplane started to turn to final approach and the bank angle "got very steep, very fast [sic] until the aircraft which seemed to snap roll into a stall and then immediately into a nose dive..." Another witness (a pilot familiar with PWK) who was riding in a vehicle, reported he first observed the airplane on a right downwind for runway 34.
- Distinguish from sibling B26 'Unreliable airspeed from blocked pitot probes' under the same parent.  `[sibling:B26]`
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than LOC-I: similar wording, different occurrence category.  `[report:WPR23FA034]`  
  > This is perceived by the pilot as resistance to control movement in the undesired direction when the aircraft approaches a steep attitude or high airspeed.
- Coded ARC (Abnormal Runway Contact) rather than LOC-I: similar wording, different occurrence category.  `[report:DCA14MA081]`  
  > According to crew interviews and cockpit voice recorder (CVR) data, when the captain set the thrust levers in the FLEX detent at 1823:45, the crew received an electronic centralized aircraft monitoring (ECAM) message and chime at 1823:47 indicating that the thrust was not set.
- Coded RI (Runway Incursion) rather than LOC-I: similar wording, different occurrence category.  `[report:DCA18IA081]`  
  > Flight 2184 was then cleared by air traffic control (ATC) for the RNAV (RNP) M instrument approach to runway 06 at PUW.
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not LOC-I.  `[definition:IND-22]`
- Not 'Undershoot' — that definition is crosswalked to USOS, not LOC-I.  `[definition:IND-37]`
- Not 'In-flight airframe icing' — that definition is crosswalked to ICE, not LOC-I.  `[definition:IND-38]`
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.16).  `[parent:NAV]`

**Linked example reports**
- WPR24FA083: "The POM also warned that there is no natural stall warning or aerodynamic buffet before the stall."
- WPR21FA286: "According to the CVR data, the stick shaker engaged at 1318:04, then the captain asked, “What are you doing,” which was followed by a stall warning sound."
- ERA14FA300: "After landing the CVR recorded the sound of two "click clacks," similar to stowing the piggy back levers of the thrust reversers, followed by a discussion by the flight crew about the aircraft's brakes."
- NYC08MA090: "HISTORY OF FLIGHT On February 1, 2008, about 1128 eastern standard time, a Raytheon Aircraft Company C90A, N57WR, was substantially damaged when it impacted terrain during a missed approach following an instrument approach to the Mount Airy/Surry County Airport (MWK), Mount Airy, North Carolina."
- DCA12CA023: "On final approach, as the aircraft was commanded low power and nose down pitch, the aircraft lost the 72MHz link, and as programmed the flight control system switched to an autopilot Manual (Assisted) mode."
- CEN10FA097: "Probable cause: The pilot's failure to maintain adequate airspeed during the instrument approach, which resulted in an aerodynamic stall and impact with terrain."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 pass · G8 pass · G9 pass

### B06 · Wake turbulence upset on approach

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent TURB Turbulence Encounter*

**Definition.** Wake vortices from a preceding heavier aircraft cause a sudden roll or pitch upset on approach or departure.

**Include when**
- The occurrence meets the CICTT TURB (Turbulence Encounter) definition.  `[parent:TURB]`
- Core definition: Wake vortices from a preceding heavier aircraft cause a sudden roll or pitch upset on approach or departure.  `[candidate:B06]`
- Matches 'Wake turbulence' (FAA Advisory Circular 90-23G – Aircraft Wake Turbulence): Vortices from a preceding aircraft, strongest behind heavy aircraft at slow speed, can cause sudden rolls on approach or departure; spacing reduces the risk.  `[definition:IND-22]`
- Matches 'Clear-air turbulence (CAT)' (SKYbrary – Clear Air Turbulence): Turbulence in cloud-free air, often near jet streams or over mountains, with no visual cue and often not shown on weather radar.  `[definition:IND-13]`
- Narrative describes 'turbulence' (8 of 10 supporting reports).  `[report:WPR16FA172]`  
  > Probable cause: The pilot's selection of a landing runway which, given the wind and traffic conditions, was susceptible to high crosswinds and the translation of wake turbulence across its approach path, and the controller's and pilot's failure to ensure separation from the B757 and its wake, which resulted in a low-altitude encounter with wake vortices that the pilot was unable to recover from.

**Exclude when**
- Belongs to sibling C6 'Clear-air turbulence with cabin injuries' when it matches that bucket better (2 report(s) assigned there).  `[report:ERA09LA488]`  
  > Meteorological Conditions in Vicinity of Turbulence Encounter The 1600 NWS radar composite reflectivity mosaic image depicted several defined echoes associated with thunderstorms north of the departure airport, including a short but intense line at the latitude and longitude of the turbulence encounter, but below the airplane's altitude.
- Coded ATM (ATM/CNS) rather than TURB: similar wording, different occurrence category.  `[report:OPS12IA849]`  
  > The Final controller vectored the flight back toward the airport for a second approach and (although the pilot had not used the exact words) informed DCA tower that the aircraft was "minimum fuel." The remainder of the flight was completed without further incident or delay, and the aircraft arrived at the gate with 2600 pounds of fuel aboard.
- Coded MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) rather than TURB: similar wording, different occurrence category.  `[report:ERA15MA259/2]`  
  > Probable cause: The approach controller's failure to provide an appropriate resolution to the conflict between the F-16 and the Cessna.
- Coded RI (Runway Incursion) rather than TURB: similar wording, different occurrence category.  `[report:DCA18IA081]`  
  > Probable cause: the flight crew's misidentification of the taxiway as the landing runway due to the failure of the runway lighting that caused only the taxiway lights to be illuminated.
- Not 'Undershoot' — that definition is crosswalked to USOS, not TURB.  `[definition:IND-37]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not TURB.  `[definition:IND-07]`
- Not 'Low-level windshear' — that definition is crosswalked to WSTRW, not TURB.  `[definition:IND-36]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.10).  `[parent:LOC-I]`

**Linked example reports**
- WPR16FA086: "Probable cause: The weight shift control aircraft encounter with a wake vortex from a preceding airplane, which resulted in a roll upset at an altitude too low for recovery."
- WPR16FA172: "Probable cause: The pilot's selection of a landing runway which, given the wind and traffic conditions, was susceptible to high crosswinds and the translation of wake turbulence across its approach path, and the controller's and pilot's failure to ensure separation from the B757 and its wake, which resulted in a low-altitude encounter with wake vortices that the pilot was unable to recover from."
- DCA23FA428: "During the descent, at about 2231:15 UTC, as the aircraft passed through a pressure altitude of about 15,100 ft and computed airspeed of 312 kts, the aircraft experienced a period of severe turbulence."
- DCA16CA197: "The operators post-flight telemetry analysis showed that the aircraft experienced significant deviations in pitch, roll, and airspeed, consistent with turbulence during the final approach."
- WPR24LA085: "If you have visual contact with the larger aircraft landing on the parallel runway, stay at or above the larger aircraft’s final approach flightpath."
- DCA24LA097: "The WSI and Skypath applications were continuously monitored, and no significant turbulence was indicated along the route or during the approach phase."
- DCA24FA143: "He stated that the turbulence was initially moderate and he jostled around, but once he was able to secure the seat belt, the turbulence increased to severe."
- DCA21LA095: "Probable cause: an encounter with clear air turbulence during approach"
- DCA21LA058: "Probable cause: an encounter with forecasted convective turbulence during approach."
- ERA22LA304: "Probable cause: The airplane pilot’s inadvertent encounter with rotor wash/turbulence during short final approach, which resulted in a loss of control in flight."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 pass · G9 pass

### B07 · Loss of separation caused by an ATC clearance

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** A controller clearance or instruction puts two aircraft into conflict, leading to loss of separation or a TCAS alert.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: A controller clearance or instruction puts two aircraft into conflict, leading to loss of separation or a TCAS alert.  `[candidate:B07]`
- Matches 'Loss of separation' (ICAO Doc 4444 – PANS-ATM (separation minima)): Two aircraft come closer than the prescribed separation minima, often after an ATC clearance or instruction puts them in conflict.  `[definition:IND-23]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`
- Matches 'Level bust (altitude deviation)' (EUROCONTROL – Level bust): An unauthorised vertical deviation of more than 300 feet from the cleared flight level or altitude, a common cause of loss of separation and TCAS resolution advisories.  `[definition:IND-11]`

**Exclude when**
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (1 report(s) assigned there).  `[report:ERA15MA259]`  
  > At 1100:26, the controller advised the F-16 pilot, "turn left heading 180 if you don't have that traffic in sight." At 1100:30, the pilot asked, "confirm 2 miles?" At 1100:33, the controller stated, "if you don't have that traffic in sight turn left heading 180 immediately." As the controller was stating the instruction and over the next 18 seconds, the radar-derived ground track of the F-16 began turning southerly toward the designated heading.
- Belongs to sibling B12 'GNSS interference or spoofing' when it matches that bucket better (1 report(s) assigned there).  `[report:WPR15MA243/2]`  
  > Probable cause: The local controller's (LC) failure to properly identify the aircraft in the pattern and to ensure control instructions provided to the intended Cessna on downwind were being performed before turning Eagle1 into its path for landing.
- Distinguish from sibling B11 'Terrain warning on a non-precision approach' under the same parent.  `[sibling:B11]`
- Distinguish from sibling B20 'Pushback or towing collision' under the same parent.  `[sibling:B20]`
- Distinguish from sibling B28 'Wrong route or waypoint loaded in the FMS' under the same parent.  `[sibling:B28]`
- Coded ATM (ATM/CNS) rather than MAC: similar wording, different occurrence category.  `[report:OPS12IA849]`  
  > While minimum separation standards applicable to these aircraft (3 miles laterally or 1,000 feet vertically) were violated, CHQ3071’s departure climb rate resulted in increasing vertical separation beginning when the two aircraft were 2.9 nm apart, and the turn instructions issued by the DCA local controller established the two aircraft on diverging courses so that their flight paths never intersected.
- Not 'Pilot deviation (runway incursion)' — that definition is crosswalked to RI, not MAC.  `[definition:IND-40]`
- Not 'GNSS jamming and spoofing' — that definition is crosswalked to NAV, not MAC.  `[definition:IND-27]`
- Not 'Runway incursion types' — that definition is crosswalked to RI, not MAC.  `[definition:IND-02]`
- Events better described by CICTT RI (Runway Incursion) (runner-up parent, margin 0.61).  `[parent:RI]`

**Linked example reports**
- OPS11IA653: "In a TRSA, controllers are required to ensure that aircraft targets do not merge unless the aircraft have a minimum of 500 feet vertical separation or can maintain visual separation, although visual separation was not being applied in this incident."
- OPS10IA574: "At 0650:26, the LCS controller asked, "Bemidji 46 are you in the turn?" The pilot replied, "46 say again the turn?” The LCS controller transmitted, "Bemidji 46 heading 180." The pilot of BMJ 46 replied, "46 left to 180." At 0650:54, the LCS controller transmitted, "Bemidji 46 remain this frequency maintain 4000 heading 180." At 0651:00, the pilot of Bemidji 46 responded, "4000 180 and I've got traffic." At 0651:41, Bemidji 46 transmitted, "Bemidji 46 going to departure." At 0651:44, the LCS controller transmitted, "Bemidji 46 now contact departure." At 0651:47, Bemidji 46 transmitted, "46 has that traffic up ahead there I wasn't notified about that." The LCS controller replied, "okay why didn't you start the turn once you were airborne?”The pilot replied, "all right okay I'm going to departure sorry about that." At 0649:49, AWE1848 made a partial transmission to departure control, stating "1848 is..."."
- OPS10IA014: "thought he was going to go more behind the Continental.” The R19 controller asked, “Are they coming together there?”, and the R12 controller responded, “uh, yeah.” The R19 controller then asked, “…Are you talking to JE?” The R12 controller again responded, “Yes,” and the R19 controller asked, “Do you want me to stop Continental?” The R12 controller answered, “Yes.” The R19 controller responded, “All right – hold on” and the call terminated."
- OPS11IA476: "The LC trainee stated that when applying tower visual separation he was required to have both aircraft in sight and to resolve conflicts by issuing control instructions."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### B08 · TCAS resolution advisory after a level bust

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** The aircraft climbs or descends through its cleared altitude (level bust) and a TCAS resolution advisory follows.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: The aircraft climbs or descends through its cleared altitude (level bust) and a TCAS resolution advisory follows.  `[candidate:B08]`
- Matches 'Level bust (altitude deviation)' (EUROCONTROL – Level bust): An unauthorised vertical deviation of more than 300 feet from the cleared flight level or altitude, a common cause of loss of separation and TCAS resolution advisories.  `[definition:IND-11]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`
- Matches 'Resolution advisory (RA)' (ICAO Annex 10 – Airborne Collision Avoidance System (ACAS)): An ACAS or TCAS indication to the flight crew recommending a vertical manoeuvre to increase separation from conflicting traffic.  `[definition:IND-10]`
- Narrative describes 'clock' (2 of 5 supporting reports).  `[report:ERA15MA259]`  
  > At 1100:16, the CHS approach controller issued a traffic advisory advising the F-16 pilot of "traffic 12 o'clock, 2 miles, opposite direction, 1,200 [ft altitude] indicated, type unknown." At 1100:24, the F-16 pilot responded that he was "looking" for the traffic.

**Exclude when**
- Belongs to sibling B07 'Loss of separation caused by an ATC clearance' when it matches that bucket better (1 report(s) assigned there).  `[report:OPS10IA574]`  
  > (from the original of 125.75) We turned to heading 260 and at that time we received a TCAS R/A [resolution advisory].
- Belongs to sibling B12 'GNSS interference or spoofing' when it matches that bucket better (1 report(s) assigned there).  `[report:WPR15MA243/2]`  
  > At 1100:23, the LC instructed, "stationair five eight uniform two six right cleared for I'm sorry two six left cleared for takeoff." At 1100:29, the pilot of N5058U stated, "uh I'm sorry was that for five eight uniform?" The LC then cleared the pilot of N5058U for takeoff from runway 26L.
- Distinguish from sibling B11 'Terrain warning on a non-precision approach' under the same parent.  `[sibling:B11]`
- Distinguish from sibling B20 'Pushback or towing collision' under the same parent.  `[sibling:B20]`
- Distinguish from sibling B28 'Wrong route or waypoint loaded in the FMS' under the same parent.  `[sibling:B28]`
- Coded ATM (ATM/CNS) rather than MAC: similar wording, different occurrence category.  `[report:OPS12IA849]`  
  > At 1407:42, the local controller provided a traffic advisory to RPA3329, advising the crew, "...traffic just ahead and to your left, a CRJ departing through 2,200." The pilot acknowledged the traffic, stating, "We got him, 3329", and continuing, "You have an altitude for us?" The controller did not acknowledge the altitude request.
- Coded NAV (Navigation Error) rather than MAC: similar wording, different occurrence category.  `[report:OPS18IA003]`  
  > The response signal can also contain additional information, such as the identifying "beacon code" for the aircraft, and the aircraft's pressure altitude (also called "Mode C" altitude).
- Not 'Lateral navigation error' — that definition is crosswalked to NAV, not MAC.  `[definition:IND-41]`
- Not 'Pushback and towing' — that definition is crosswalked to RAMP, not MAC.  `[definition:IND-34]`
- Not 'Runway incursion' — that definition is crosswalked to RI, not MAC.  `[definition:IND-01]`
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.37).  `[parent:NAV]`

**Linked example reports**
- ERA15MA259: "At 1100:16, the CHS approach controller issued a traffic advisory advising the F-16 pilot of "traffic 12 o'clock, 2 miles, opposite direction, 1,200 [ft altitude] indicated, type unknown." At 1100:24, the F-16 pilot responded that he was "looking" for the traffic."
- OPS11IA653/2: "In a TRSA, controllers are required to ensure that aircraft targets do not merge unless the aircraft have a minimum of 500 feet vertical separation or can maintain visual separation, although visual separation was not being applied in this incident."
- OPS11IA686: "Air Traffic Procedural Requirements Traffic advisories were provided to both pilots in accordance with Federal Aviation Administration Order 7110.65, paragraphs 2-1-21 "Traffic Advisories", and 5-1-8 "Merging Target Procedures", which state in part: 2-1-21 Unless an aircraft is operating within Class A airspace or omission is requested by the pilot, issue traffic advisories to all aircraft (IFR or VFR) on your frequency when, in your judgment, their proximity may diminish to less than the applicable separation minima."
- OPS11IA246: "At 2235:35, the R66 controller instructed AAL951 “…turn left at your discretion traffic now one o’clock four miles southwest heavy C17 flight level 220.” At 2235:49, the R86 controller transmitted “THUG11, you up?’ The pilot responded, “Level 220 in a right hand turn to 020.” At 2235:54, the R66 controller asked AAL951 “…do you have that traffic in sight?” The pilot transmitted “No, we do not.” At 2235:56, the R86 controller informed THUG11 “traffic right below you is a Boeing triple seven that should be leveling at flight level 210.” At 2235:58, the R66 controller informed AAL951 “… traffic is now at 12 o’clock less than one mile at flight level 220, C17.” At 2236:12, THUG11 transmitted to the R86 controller, “Yeah, THUG11 just came within approximately 2000 feet of that traffic.” At 2236:17, AAL951 transmitted to the R66 controller “that guy passed us now and that was not good.” At 2236:21, the R86 controller instructed THUG11 to “…continue right turn and then proceed to COYLE.” At 2236:24, the R66 controller responded to AAL951 statement “I understand that and I apologize, I am not working that other airplane.” The R66 controller then instructed AAL951 to climb to FL230."
- OPS10IA155: "At 2153:27, the North Local controller transmitted, “Eagle 3962?”, and the crew of EGF 3962 replied, "Yeah traffic’s in sight." At 2153:39, the North Local controller instructed EGF 3962 to turn right heading 180 and the crew acknowledged, stating “All right sir turn right to heading 180 Eagle 3962 we had a [traffic collision avoidance system -TCAS] resolution advisory.” The controller replied, “Thank you - that was a VFR King Air, Eagle 3962.” The crew responded,”…3962 we had him we were following an RA on the TCAS.” At 2154:02, the controller transmitted, "Eagle 3962 come back to heading of 140" and the crew acknowledged."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### B09 · Hydraulic system failure in flight

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent SCF-NP System/Component Failure – Non-Powerplant*

**Definition.** Loss of fluid or pressure in a hydraulic system in flight degrades flight controls, brakes or landing gear.

**Include when**
- The occurrence meets the CICTT SCF-NP (System/Component Failure – Non-Powerplant) definition.  `[parent:SCF-NP]`
- Core definition: Loss of fluid or pressure in a hydraulic system in flight degrades flight controls, brakes or landing gear.  `[candidate:B09]`
- Matches 'Hydraulic system failure' (SKYbrary – Hydraulic System Failure): Loss of hydraulic fluid or pressure that degrades flight controls, brakes, steering or landing gear, handled with non-normal checklists.  `[definition:IND-24]`
- Matches 'Landing gear malfunction' (SKYbrary – Landing Gear Malfunction): Failure of a landing gear leg to extend, retract or lock, requiring alternate extension or a landing with gear not fully down.  `[definition:IND-25]`

**Exclude when**
- Distinguish from sibling B18 'Electrical smoke or burning smell in the flight deck' under the same parent.  `[sibling:B18]`
- Coded ARC (Abnormal Runway Contact) rather than SCF-NP: similar wording, different occurrence category.  `[report:ENG10IA055]`  
  > 3 hydraulic system is an independent hydraulic system that supplies the landing gear system, braking system, and certain flight control systems with hydraulic pressure.
- Coded RE (Runway Excursion) rather than SCF-NP: similar wording, different occurrence category.  `[report:DCA24LA095]`  
  > Between each antiskid valve and brake assembly there is a hydraulic fuse to prevent hydraulic fluid loss if there is an external leak downstream of the fuse, and there is an alternate brake shuttle valve to allow brake pressure to come from the alternate brake system if required.
- Coded UNK (Unknown or Undetermined) rather than SCF-NP: similar wording, different occurrence category.  `[report:ERA12IA060]`  
  > Probable cause: The pilots’ failure to appropriately apply the landing gear wheel brakes after landing, to properly perform the hard brake pedal-no braking condition procedure following the reported brake failure and to apply the emergency brakes.
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not SCF-NP.  `[definition:IND-08]`
- Not 'Smoke or fumes in flight' — that definition is crosswalked to F-NI, not SCF-NP.  `[definition:IND-32]`
- Not 'In-flight engine shutdown (IFSD)' — that definition is crosswalked to SCF-PP, not SCF-NP.  `[definition:IND-28]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.08).  `[parent:RE]`

**Linked example reports**
- CEN14LA127: "At 1312:05, the pilot stated, "I don't think I'm getting very good brakes… I don't have any pressure." At 1312:08, the copilot replied, "no pressure?" At 1312:09, the pilot stated, "no pressure." At 1312:10, the copilot stated, "try the steering." At 1312:12, pilot replied, "oh, you know we have the ah T-bar in." At 1312:15, the copilot stated, "okay." At 1312:17, the copilot stated, "pull it." Between 1312:17 and 1312:23, the landing gear warning horn was heard, the sound of the hydraulic system momentarily decreased before it increased back to normal, and there was the sound of rumbling and scraping consistent with the landing gear retracting and the airplane impacting the ground."
- CEN11IA379: "Probable cause: The failure of the right main landing gear (MLG) to extend normally, which resulted from the combination of a slightly worn uplock pin, the operation of the hydraulic pumps below their specified operating pressures, and contamination within the landing gear hydraulic system."
- CEN11FA193: "Probable cause: The pilot flying's (PF) decision to land on a shorter-than-recommended runway with a known left hydraulic system failure rather than go around as suggested by the pilot-not-flying, his failure to immediately apply emergency brakes following the detection of the lack of normal brakes, and his attempt to go around late in the landing roll with insufficient runway remaining."
- WPR22LA341: "Refer to Emergency/Abnormal Procedures, LANDING WITH NO “A” HYDRAULIC SYSTEM PRESSURE; Tab P2 WARNING DO NOT USE SPED BRAKES IN FLIGHT UNLESS “A” HYDRAULIC SYSTEM PRESSURE IS ZERO."
- WPR12FA193: "The hydraulic fluid pressurizes and routes through the landing gear control valve to the retract side of the hydraulic system."
- DCA10IA021: "Contributing to this incident was a circular reference in the company Flight Manual in which the Landing Gear Gravity Extension checklist referred back to the Landing Gear Unsafe Indication After Extension checklist rather than the Landing Gear - Partial Gear or Gear Up Landing checklist."
- CEN21LA323: "During normal operation, the landing gear is retracted and held in the fully retracted position by hydraulic pressure and, as such, the hydraulic power pack will occasionally cycle on/off during flight to maintain sufficient hydraulic pressure to keep the landing gear retracted."
- CEN11IA341: "Probable cause: The fatigue failure of the nose landing gear (NLG) end cap, which resulted in insufficient hydraulic pressure to secure the left main landing gear into the down and locked position."
- MIA08LA086: "Contributing to the accident was a loss of system A hydraulic fluid for undetermined reasons and the flight crew's failure to follow the checklist sequence."
- DCA13FA094: "Alternate Gear Extension System An alternate gear extension system provides for mechanical extension of the landing gear and is intended for in-flight use when hydraulic power from the No."
- ERA23LA202: "The hydraulic landing gear system is designed so when the pilot places the landing gear handle in the UP position, the hydraulic power pack is energized, and hydraulic fluid is directed to the up port of each gear actuating cylinder to retract the gear."
- ERA15LA212: "Examination of the cockpit revealed that the circuit breaker for the terrain avoidance warning system (TAWS) which was installed to help prevent inadvertent flight into terrain was "out" (deactivated) and not collared, and the landing gear warning/mute test switch had a rubber band looped around it and the pressurization rate knob, which kept the landing gear/mute test switch in the mute position deactivating the landing gear warning horn."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 pass · G9 pass

### B10 · Landing gear did not extend

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent ARC Abnormal Runway Contact*

**Definition.** One or more landing gear legs fail to extend or lock down, requiring alternate extension or a gear-up landing.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: One or more landing gear legs fail to extend or lock down, requiring alternate extension or a gear-up landing.  `[candidate:B10]`
- Matches 'Hard landing, tail strike' (SKYbrary – Hard Landing and Tail Strike): A touchdown with a vertical load above limits, a bounced landing, or contact of the tail with the runway during takeoff rotation or landing flare.  `[definition:IND-18]`
- Narrative describes 'extend' (12 of 12 supporting reports).  `[report:ENG10IA055]`  
  > The landing gear manual release system provides the flight crew with another means to extend the landing gear in the event that an electrical or hydraulic failure within the landing gear system prevents the landing gear from being extended normally.
- Narrative describes 'failure' (12 of 12 supporting reports).  `[report:ENG10IA055]`  
  > The landing gear manual release system provides the flight crew with another means to extend the landing gear in the event that an electrical or hydraulic failure within the landing gear system prevents the landing gear from being extended normally.
- Narrative describes 'gear' (12 of 12 supporting reports).  `[report:ENG10IA055]`  
  > The landing gear manual release system provides the flight crew with another means to extend the landing gear in the event that an electrical or hydraulic failure within the landing gear system prevents the landing gear from being extended normally.

**Exclude when**
- Distinguish from sibling C9 'Hard landing or tail strike' under the same parent.  `[sibling:C9]`
- Not 'Landing gear malfunction' — that definition is crosswalked to SCF-NP, not ARC.  `[definition:IND-25]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.51).  `[parent:RE]`

**Linked example reports**
- ENG10IA055: "The landing gear manual release system provides the flight crew with another means to extend the landing gear in the event that an electrical or hydraulic failure within the landing gear system prevents the landing gear from being extended normally."
- ERA25LA094: "Probable cause: The pilot’s failure to follow the emergency procedures and extend the landing gear manually after the landing gear did not initially extend normally."
- WPR21LA256: "Probable cause: The pilot’s failure to use the landing checklist and to extend the landing gear, which resulted in a gear-up landing."
- CEN24LA288: "Probable cause: The pilot’s failure to extend the landing gear before landing due to distractions and his failure to conduct the Before Landing checklist."
- WPR21LA028: "Probable cause: The pilot’s failure to extend the landing gear, which resulted in the airplane landing with the landing gear retracted."
- CEN25LA220: "Probable cause: The pilot’s failure to extend the landing gear before landing and his failure to conduct the before landing checklist."
- WPR25LA293: "Probable cause: The pilot’s failure to extend the landing gear before landing due to distraction and failure to conduct the before landing checklist."
- CEN21LA298: "Probable cause: The pilot’s failure to extend the landing gear before landing."
- CEN23LA116: "Probable cause: The pilot’s failure to extend the landing gear before landing."
- CEN25LA371: "Probable cause: The pilot's failure to extend the landing gear before landing."
- WPR22LA075: "Probable cause: The pilot’s failure to extend the landing gear before landing."
- CEN26LA028: "Probable cause: The pilot’s failure to extend the landing gear before landing due to distraction and his failure to conduct the Before Landing checklist."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass

### B11 · Terrain warning on a non-precision approach

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** During a non-precision or visual approach the aircraft descends too low and the terrain awareness system warns of terrain or obstacles.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: During a non-precision or visual approach the aircraft descends too low and the terrain awareness system warns of terrain or obstacles.  `[candidate:B11]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`
- Matches 'Loss of separation' (ICAO Doc 4444 – PANS-ATM (separation minima)): Two aircraft come closer than the prescribed separation minima, often after an ATC clearance or instruction puts them in conflict.  `[definition:IND-23]`

**Exclude when**
- Belongs to sibling B07 'Loss of separation caused by an ATC clearance' when it matches that bucket better (1 report(s) assigned there).  `[report:OPS11IA653]`  
  > In a TRSA, controllers are required to ensure that aircraft targets do not merge unless the aircraft have a minimum of 500 feet vertical separation or can maintain visual separation, although visual separation was not being applied in this incident.
- Belongs to sibling B12 'GNSS interference or spoofing' when it matches that bucket better (1 report(s) assigned there).  `[report:WPR15MA243/2]`  
  > At 1054:46, when N1285U was on final approach of the first approach to runway 26R, the pilot advised the LC trainee that he was going to go around.
- Belongs to sibling B28 'Wrong route or waypoint loaded in the FMS' when it matches that bucket better (1 report(s) assigned there).  `[report:ERA12LA401]`  
  > Contributing factor: Aircraft-Aircraft systems-Flight control system-TE flap control system-Not used/operated.
- Distinguish from sibling B08 'TCAS resolution advisory after a level bust' under the same parent.  `[sibling:B08]`
- Distinguish from sibling B20 'Pushback or towing collision' under the same parent.  `[sibling:B20]`
- Distinguish from sibling C8 'Takeoff after de-icing holdover time exceeded' under the same parent.  `[sibling:C8]`
- Coded RI (Runway Incursion) rather than MAC: similar wording, different occurrence category.  `[report:DCA18IA081]`  
  > Conditions at the KPUW airport were wind from the southeast, light rain, overcast ceiling with 5 miles visibility, and the captain used the Head-up Guidance System (HGS) installed on the captain's side of the cockpit during the approach.
- Coded CFIT (Controlled Flight Into or Toward Terrain) rather than MAC: similar wording, different occurrence category.  `[report:CEN14FA110]`  
  > HISTORY OF FLIGHTOn January 10, 2014, about 1948 eastern standard time, a Cessna 310R, N3829G, impacted trees and terrain about 1,500 feet west of the approach end of runway 9R (6,521 feet by 150 feet, asphalt) at Oakland County International Airport (PTK), Pontiac, Michigan, during a straight-in instrument landing system (ILS) approach to runway 9R.
- Coded LOC-I (Loss of Control – Inflight) rather than MAC: similar wording, different occurrence category.  `[report:WPR21FA286]`  
  > Probable cause: The first officer’s (FO’s) improper decision to attempt to salvage an unstabilized approach by executing a steep left turn to realign the airplane with the runway centerline, and the captain’s failure to intervene after recognizing the FO’s erroneous action, while both ignored stall protection system warnings, which resulted in a left-wing stall and an impact with terrain.
- Not 'Terrain awareness and warning system (TAWS)' — that definition is crosswalked to CFIT, not MAC.  `[definition:IND-26]`
- Not 'Undershoot' — that definition is crosswalked to USOS, not MAC.  `[definition:IND-37]`
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not MAC.  `[definition:IND-22]`
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.07).  `[parent:NAV]`

**Linked example reports**
- ERA15MA259/2: "According to air traffic control (ATC) radar and voice communication data provided by the Federal Aviation Administration (FAA), the F-16 pilot contacted the approach controller at CHS about 1052 and requested to perform a practice tactical air navigation system (TACAN) instrument approach to runway 15."
- ANC16FA052: "Formerly known as Capstone, the joint industry/FAA program (which includes ground-based stations, satellites, and airplane avionics) currently provides pilots with situational awareness by displaying the airplane's position over terrain and warns pilots of the presence of other ADS-B-equipped aircraft that may be present, while using global positioning system technology coupled with an instrument panel mounted moving map display."
- OPS09IA006: "The aircraft was initially cleared for an Instrument Landing System (ILS) approach, but was eventually cleared for a visual approach following this incident."
- ERA22FA318: "At 1156:08, the Nellis Radar Approach Control controller cleared the low-wing airplane for the visual approach and instructed the pilots to overfly VGT at midfield for left traffic to runway 30L."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B12 · GNSS interference or spoofing

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** Satellite navigation signals are jammed or spoofed, giving false position, lost RNP capability or incorrect time, often near conflict zones.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: Satellite navigation signals are jammed or spoofed, giving false position, lost RNP capability or incorrect time, often near conflict zones.  `[candidate:B12]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`
- Matches 'Loss of separation' (ICAO Doc 4444 – PANS-ATM (separation minima)): Two aircraft come closer than the prescribed separation minima, often after an ATC clearance or instruction puts them in conflict.  `[definition:IND-23]`
- Matches 'Resolution advisory (RA)' (ICAO Annex 10 – Airborne Collision Avoidance System (ACAS)): An ACAS or TCAS indication to the flight crew recommending a vertical manoeuvre to increase separation from conflicting traffic.  `[definition:IND-10]`

**Exclude when**
- Belongs to sibling B07 'Loss of separation caused by an ATC clearance' when it matches that bucket better (3 report(s) assigned there).  `[report:OPS10IA014]`  
  > She reported that developmental controllers (controllers in training) are allocated 120 to 140 hours of training time for each radar position.
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (1 report(s) assigned there).  `[report:ERA15MA259]`  
  > His additional duties at the time of the accident included the position of 55th Fighter Squadron Chief of Mobility.
- Distinguish from sibling B11 'Terrain warning on a non-precision approach' under the same parent.  `[sibling:B11]`
- Distinguish from sibling B20 'Pushback or towing collision' under the same parent.  `[sibling:B20]`
- Distinguish from sibling B28 'Wrong route or waypoint loaded in the FMS' under the same parent.  `[sibling:B28]`
- Coded LOC-I (Loss of Control – Inflight) rather than MAC: similar wording, different occurrence category.  `[report:CEN14FA046]`  
  > The block time recorded the time from when the airplane began taxiing from parking to the runway and the time that it returned to parking.
- Not 'GNSS jamming and spoofing' — that definition is crosswalked to NAV, not MAC.  `[definition:IND-27]`
- Not 'Lateral navigation error' — that definition is crosswalked to NAV, not MAC.  `[definition:IND-41]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.22).  `[parent:LOC-I]`

**Linked example reports**
- WPR15MA243/2: "The position was staffed by a qualified local controller (LC)/controller-in-charge (CIC) who was conducting on-the-job training with a developmental controller (LC trainee) on the local control position."
- DEN08MA116: "The conversation ended at 1534; at which time the crewmember provided an estimated time of arrival of 15 minutes, or 1549."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 FAIL · G9 pass

### B13 · Engine shutdown after loss of oil pressure

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent SCF-PP System/Component Failure – Powerplant*

**Definition.** Low oil pressure or oil loss in flight leads the crew to shut an engine down as a precaution.

**Include when**
- The occurrence meets the CICTT SCF-PP (System/Component Failure – Powerplant) definition.  `[parent:SCF-PP]`
- Core definition: Low oil pressure or oil loss in flight leads the crew to shut an engine down as a precaution.  `[candidate:B13]`
- Matches 'In-flight engine shutdown (IFSD)' (SKYbrary – In-Flight Shutdown): An engine is shut down in flight because of a failure or a precautionary indication such as low oil pressure, high vibration or fire.  `[definition:IND-28]`

**Exclude when**
- Distinguish from sibling B25 'Airframe icing in flight' under the same parent.  `[sibling:B25]`
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than SCF-PP: similar wording, different occurrence category.  `[report:DCA16FA199]`  
  > The test card for the two-to-one-engine simulated engine failure detailed that the pilots would simulate the loss of engine power from one engine while keeping both engines operating by using one-engine-inoperative (OEI) special training mode software, which reduced the power output of both engines to represent the maximum power that can be produced by one engine.
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not SCF-PP.  `[definition:IND-08]`
- Not 'Smoke or fumes in flight' — that definition is crosswalked to F-NI, not SCF-PP.  `[definition:IND-32]`
- Not 'Hydraulic system failure' — that definition is crosswalked to SCF-NP, not SCF-PP.  `[definition:IND-24]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.45).  `[parent:LOC-I]`

**Linked example reports**
- ERA23LA086: "A review of engine data associated with the flight revealed normal engine oil pressure for the majority of recorded data with the exception of one point when the oil pressure dropped below 30 psi."
- ERA11FA414: "The analog oil pressure indicator receives a pressure signal from an oil pressure sensor mounted at the aft end of the engine below the oil cooler."
- ERA15FA312: "According to a maintenance entry dated January 21, 2013, and the associated work order, this resulted in the maintenance provider inspecting for the cause of the oil leaks by first washing down the engine, and then after a test flight, tightening loose rocker box return line coupling clamps, replacing a cracked air/oil separator, replacing leaking oil dipstick gaskets, and replacing a leaking fitting on the turbocharger wastegate actuator."
- ERA17MA316: "A decision for this option requires the pilot to continuously monitor engine parameters N1 (gas generator speed), TOT (turbine outlet temperature), TRQ (engine torque), oil pressure and temperature, and be prepared for immediate engine shutdown."
- CEN14FA046: "PERSONNEL INFORMATIONThe pilot, age 51, held a commercial pilot certificate, with airplane single-engine land, airplane multiengine land, and instrument airplane ratings, and a flight instructor certificate with airplane single-engine land, airplane multi-engine land, and instrument airplane ratings."
- CEN19LA320: "According to an oil analysis report dated May 29, 2019, the sample indicated the best “wear-rate” results from the engine; the amount of iron detected was a “bit” more than average for the type of engine, but “not far enough out of line to call a problem.” According to the engine manufacturer’s maintenance manual directions current at the time of the accident, the minimum requirement is to change the oil and filter every 50 hours and/or 4 months on engines with full flow oil filters and on engines with a large or small replaceable oil filter cartridge."
- DCA21FA174: "Five seconds later, the first officer resumed the checklist by stating, “airframe vibrations abnormal engines exist.” Step 1 of the Engine Failure or Shutdown checklist prompted flight crews to determine whether they should continue with this checklist or instead use the Engine Fire or Engine Severe Damage or Separation checklist."
- ERA20LA327: "Figure 3 Engine Oil Pressure - Data from Flight Prior to Accident Flight During the accident flight, the oil pressure was generally more consistent with a typical flight, with a decrease (about 7-8 psi) over the 3 minutes prior to the loss of engine power."
- CEN17IA233: "Probable cause: The loss of oil pressure and subsequent engine overspeed/surge during a zero g-force maneuver, which resulted in the separation of a crankshaft counterweight and loss of engine power."
- ERA15LA062: "About 3 minutes after last checking the engine parameters, noting all engine parameters (specifically, oil temperature, oil pressure, and CHT) were in the green, or at 1153:02, the oil pressure indication first began to decrease from the steady state reading."
- ERA13IA313: "Probable cause: The improper maintenance decision to adjust the engine oil pressure regulator valve in response to high oil pressure indications rather than to properly troubleshoot the anomaly, which then allowed an existing oil supply path blockage to increase and led to the eventual insufficient lubrication of the compressor section No."
- CEN17IA094: "On May 21, 2016, the oil level sight gauge was replaced by the operator at 5,637 hours engine TSN, and 2,042 hours engine TSO on the engine's module 3."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass

### B14 · Takeoff with frost or ice not removed

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent LOC-G Loss of Control – Ground*

**Definition.** The aircraft departs or begins to depart with frost, snow or ice on its wings because it was not removed or the fluid failed.

**Include when**
- The occurrence meets the CICTT LOC-G (Loss of Control – Ground) definition.  `[parent:LOC-G]`
- Core definition: The aircraft departs or begins to depart with frost, snow or ice on its wings because it was not removed or the fluid failed.  `[candidate:B14]`

**Exclude when**
- Distinguish from sibling B03 'Veer-off during landing in a strong or gusty crosswind' under the same parent.  `[sibling:B03]`
- Coded ARC (Abnormal Runway Contact) rather than LOC-G: similar wording, different occurrence category.  `[report:DCA14FA058]`  
  > When either of the ice detectors detect ice, an advisory message "ICE CONDITION" is shown on the EICAS display, a signal would be sent to the anti-ice system valves to activate them to open, and a signal would be sent to the full authority digital engine control to activate the automated engine icing thrust setting logic to limit the thrust to a minimum acceptable level.
- Coded ICE (Icing) rather than LOC-G: similar wording, different occurrence category.  `[report:WPR23FA080]`  
  > Additionally, the airplane’s BEFORE TAKEOFF checklist includes an ice accumulation check and includes the following specific guidance: Aerodynamic surfaces must be confirmed free of all forms of frost, ice, snow and slush prior to entering the takeoff runway or initiating takeoff.
- Coded CTOL (Collision with Obstacle(s) During Takeoff and Landing) rather than LOC-G: similar wording, different occurrence category.  `[report:SEA08LA069]`  
  > Therefore, when the new snow fell, it became very hard to distinguish between the area where the previously cleared surface was covered only by the newly fallen snow, and the area where the chunks of previously plowed snow had piled up, hardened, and then been covered by the new snow.
- Not 'Clean aircraft concept' — that definition is crosswalked to ICE, not LOC-G.  `[definition:IND-29]`
- Not 'Holdover time' — that definition is crosswalked to ICE, not LOC-G.  `[definition:IND-17]`
- Not 'Runway condition code (RWYCC)' — that definition is crosswalked to RE, not LOC-G.  `[definition:IND-06]`
- Events better described by CICTT ICE (Icing) (runner-up parent, margin 0.03).  `[parent:ICE]`

**Linked example reports**
- WPR10LA092: "The ACM further states that the "Runway will be closed for aircraft use if it has more than 1/2-inch of slush or 2 inches of dry snow." Additionally, "The Airport Manager or Airport Technicians will check snow depth accumulation during stormy weather," and "Upon determination that snow removal is required, Operations will post a Notice To Airmen (NOTAM) through the Cedar City Flight Service Station." The manual added that "During after hour’s snow events, Airport Technicians will report to the airport early to verify conditions and notify the County Road Maintenance Department of needed snow removal." The airport manager stated that snow removal equipment at the airport is limited, not to availability, but in its size and capacity."
- ERA15LA212: "Further examination also revealed that the fuselage had been damaged in numerous areas along with the wing leading edges, and a mission pod which was mounted under the left wing, and both the left-wing and right-wing integral wet wing tanks had been punctured by the landing gear, resulting in a fuel spill of about 600 gallons."
- WPR11CA065: "Although he overflew the strip before landing, because he had not predetermined the actual depth of the snow on the surface, during the landing roll the airplane sunk deep enough into the snow that it decelerated at a rate that resulted in it nosing over onto its back."
- WPR11CA098: "It was actually a snow drift made from the snow that had blown to the side of the ridge."
- CEN12LA126: "On January 6, 2012, about 1600 mountain standard time, an Aviat Aircraft Inc A-1B, N127AK, nosed over when it struck a snow drift during takeoff roll on a snow covered runway at Abbott Ranch Private Airstrip near Somerset, Colorado."
- WPR11CA088: "Cause: Environmental issues-Physical environment-Runway/land/takeoff/taxi surfa-Snow/slush/ice covered-Response/compensation."
- ANC11CA014: "He stated that he did not have time to go around, and landed on the snow."
- CEN14CA132: "The pilot reported that he was departing to the north from a snow covered grass runway in a ski-equipped tail-wheel airplane."
- WPR12CA148: "Finding: Environmental issues-Physical environment-Runway/land/takeoff/taxi surfa-Snow/slush/ice covered-Contributed to outcome."
- CEN17LA057: "Day visual meteorological conditions prevailed for the flight that departed Lowell City Airport (24C), Lowell, Michigan, about 1030.The pilot reported that shortly after takeoff from a snow covered runway he heard a thump and saw that the left main landing ski tip had rotated up, past vertical, and was in contact with the left wing strut."
- WPR11CA148: "Probable cause: The aircraft's encounter with deep snow during the landing roll out."
- ERA21LA134: "The visibility was reported as 0.5 mile in snow or light snow during the three previous observations (recorded at 1035, 1055, and 1115)."

**Checks:** G1 pass · G2 FAIL · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B15 · Bird ingestion damaging an engine on takeoff or climb

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent BIRD Bird*

**Definition.** One or more birds are ingested into an engine during takeoff or initial climb, causing vibration, surging or loss of thrust.

**Include when**
- The occurrence meets the CICTT BIRD (Bird) definition.  `[parent:BIRD]`
- Core definition: One or more birds are ingested into an engine during takeoff or initial climb, causing vibration, surging or loss of thrust.  `[candidate:B15]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Matches 'Damaging bird strike' (FAA National Wildlife Strike Database – strike reporting): A collision with birds that damages the aircraft, such as a cracked windshield, dented radome or ingested engine, reported to the wildlife strike database.  `[definition:IND-39]`
- Matches 'Wildlife strike' (FAA National Wildlife Strike Database): A collision between an aircraft and a bird or other wildlife, including ingestion into an engine, reported with damage and phase of flight.  `[definition:IND-15]`
- Narrative describes 'bird' (9 of 11 supporting reports).  `[report:CEN09CA418]`  
  > The pilot stated that a large bird struck the nose of the airplane during initial climb after takeoff.
- Narrative describes 'collision' (9 of 11 supporting reports).  `[report:ERA21LA047]`  
  > Probable cause: The airplane’s collision with a bird during initial climb, which resulted in a forced landing.

**Exclude when**
- Belongs to sibling C7 'Engine damage or shutdown after bird ingestion' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN09MA117]`  
  > Probable cause: (1) the sudden loss of power to both engines that resulted from impact with a bird (red-tailed hawk), which fractured the windshield and interfered with engine fuel controls, and (2) the subsequent disorientation of the flight crewmembers, which left them unable to recover from the loss of power.
- Distinguish from sibling B16 'Bird strike damaging the windshield or nose on approach' under the same parent.  `[sibling:B16]`
- Coded ARC (Abnormal Runway Contact) rather than BIRD: similar wording, different occurrence category.  `[report:DCA14MA081]`  
  > In response, the first officer stated "engine thrust levers not set." FDR data indicate the thrust levers were briefly reduced to the climb detent then returned to the FLEX detent about 1 second later.
- Coded SCF-PP (System/Component Failure – Powerplant) rather than BIRD: similar wording, different occurrence category.  `[report:DCA21FA174]`  
  > Probable cause: The flight crewmembers’ misidentification of the damaged engine (after leveling off the airplane and reducing thrust) and their use of only the damaged engine for thrust during the remainder of the flight, resulting in an unintentional descent and forced ditching in the Pacific Ocean.
- Coded LOC-I (Loss of Control – Inflight) rather than BIRD: similar wording, different occurrence category.  `[report:CEN14FA046]`  
  > Probable cause: The pilot's loss of airplane control during a known one-engine-inoperative condition.
- Not 'Tail strike' — that definition is crosswalked to ARC, not BIRD.  `[definition:IND-35]`
- Not 'Level bust (altitude deviation)' — that definition is crosswalked to MAC, NAV, not BIRD.  `[definition:IND-11]`
- Not 'Terrain awareness and warning system (TAWS)' — that definition is crosswalked to CFIT, not BIRD.  `[definition:IND-26]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.14).  `[parent:SCF-PP]`

**Linked example reports**
- CEN09CA418: "The pilot stated that a large bird struck the nose of the airplane during initial climb after takeoff."
- ERA21LA047: "Probable cause: The airplane’s collision with a bird during initial climb, which resulted in a forced landing."
- CEN23LA203: "Probable cause: An inflight collision with a bird while on initial climb."
- ERA24LA065: "Probable cause: An inflight collision with a bird during initial climb."
- CEN23LA035: "Probable cause: The inflight collision with multiple geese during initial climb."
- DCA12CA043: "Photo of bird strike to radome Photo of Bird strike damage to right engine Photo of bird strike damage to E and E bay Photo of bird recovered from E and E bay"
- CEN23LA394: "Probable cause: An in-flight collision with multiple geese during initial climb."
- CEN23LA384: "Probable cause: An in-flight collision with a bird during initial climb."
- CEN24LA153: "Probable cause: An in-flight collision with a bird during the initial climb."
- ERA22LA044: "Probable cause: An in-flight collision with a bird during initial climb."
- ERA24LA061: "Probable cause: An in-flight collision with a bird during initial climb."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 pass · G9 pass

### B16 · Bird strike damaging the windshield or nose on approach

*Taxonomy version ntsb-draft-dadb5659b8 · status grounded · parent BIRD Bird*

**Definition.** A large bird or flock strikes the windshield, radome or nose on approach or descent and causes visible damage.

**Include when**
- The occurrence meets the CICTT BIRD (Bird) definition.  `[parent:BIRD]`
- Core definition: A large bird or flock strikes the windshield, radome or nose on approach or descent and causes visible damage.  `[candidate:B16]`
- Matches 'Damaging bird strike' (FAA National Wildlife Strike Database – strike reporting): A collision with birds that damages the aircraft, such as a cracked windshield, dented radome or ingested engine, reported to the wildlife strike database.  `[definition:IND-39]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Matches 'Wildlife strike' (FAA National Wildlife Strike Database): A collision between an aircraft and a bird or other wildlife, including ingestion into an engine, reported with damage and phase of flight.  `[definition:IND-15]`
- Narrative describes 'bird' (10 of 11 supporting reports).  `[report:DCA20CA050]`  
  > Probable cause: a bird strike during descent
- Narrative describes 'cause' (10 of 11 supporting reports).  `[report:DCA20CA050]`  
  > Probable cause: a bird strike during descent
- Narrative describes 'robable' (10 of 11 supporting reports).  `[report:DCA20CA050]`  
  > Probable cause: a bird strike during descent

**Exclude when**
- Belongs to sibling C7 'Engine damage or shutdown after bird ingestion' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN09MA117]`  
  > Probable cause: (1) the sudden loss of power to both engines that resulted from impact with a bird (red-tailed hawk), which fractured the windshield and interfered with engine fuel controls, and (2) the subsequent disorientation of the flight crewmembers, which left them unable to recover from the loss of power.
- Distinguish from sibling B15 'Bird ingestion damaging an engine on takeoff or climb' under the same parent.  `[sibling:B15]`
- Not 'Undershoot' — that definition is crosswalked to USOS, not BIRD.  `[definition:IND-37]`
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not BIRD.  `[definition:IND-22]`
- Events better described by CICTT WILD (Collision with Wildlife) (runner-up parent, margin 0.74).  `[parent:WILD]`

**Linked example reports**
- DCA20CA050: "Probable cause: a bird strike during descent"
- CEN25LA070: "Probable cause: Bird strike."
- DCA21LA120: "Probable cause: a bird strike."
- DCA24LA051: "Probable cause: A bird strike during climbout."
- DCA23LA067: "Probable cause: Multiple bird strikes during descent."
- WPR25LA113: "Probable cause: An in-flight collision with a bird during an approach to land."
- ERA23LA014: "Probable cause: An in-flight collision with a bird while on approach."
- ERA26LA082: "Probable cause: An in-flight collision with a bird while on approach to the destination airport."
- CEN11CA391: "The pilot had just departed and was about 13 miles from the airport when he saw a large bird pass by the passenger side windshield."
- ERA24LA249: "Probable cause: An in-flight collision with a bird while on approach."
- ERA25LA360: "Probable cause: An in-flight collision with a bird while on approach."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B17 · Lithium battery fire from a passenger device

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent F-NI Fire/Smoke (Non-Impact)*

**Definition.** A phone, laptop, power bank or other lithium battery device overheats, smokes or catches fire in the cabin.

**Include when**
- The occurrence meets the CICTT F-NI (Fire/Smoke (Non-Impact)) definition.  `[parent:F-NI]`
- Core definition: A phone, laptop, power bank or other lithium battery device overheats, smokes or catches fire in the cabin.  `[candidate:B17]`
- Matches 'Lithium battery fire' (FAA SAFO – Fire risks from lithium batteries in the cabin): Portable electronic devices and power banks can overheat in thermal runaway, producing smoke and fire in the cabin; crew cool the device with water or non-alcoholic liquid.  `[definition:IND-31]`
- Matches 'Smoke or fumes in flight' (SKYbrary – Smoke and Fumes): Smoke, fumes or burning smells in the flight deck or cabin, often electrical in origin, handled with oxygen masks and the smoke checklist.  `[definition:IND-32]`

**Exclude when**
- Coded SCF-PP (System/Component Failure – Powerplant) rather than F-NI: similar wording, different occurrence category.  `[report:CEN13FA196]`  
  > At 1614:14, the pilot told the pilot-rated-passenger "we gotta get -- just pull -- just pull the power out." At 1614:18, the pilot-rated-passenger asked, "just pull it on down?" The pilot replied, "yeah, let's -- let's get back to two hundred (knots)." At 1614:21, the cockpit area microphone recorded another sound consistent with a decrease in engine speed.
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than F-NI: similar wording, different occurrence category.  `[report:CHI08IA292]`  
  > The FDR indicated that this was around the time that battery power was depleted; approximately 2 hours 24 minutes after the flight crew switched the Standby Power selector to the BAT position.
- Coded BIRD (Bird) rather than F-NI: similar wording, different occurrence category.  `[report:DCA24LA330]`  
  > Because there was no direct measurable evidence of the chemical composition of the smoke or the concentrations of chemicals in the cockpit air over time during the incident, and because there was no practical experimental approach by which to reliably determine the chemical composition of the smoke or the concentrations of chemicals in the cockpit or cabin air, the study was limited to characterizing the incident exposure from available information, and to examining the potential toxicity of future LRD-related smoke events from a theoretical perspective.
- Not 'Unruly or disruptive passenger' — that definition is crosswalked to CABIN, not F-NI.  `[definition:IND-30]`
- Not 'Turbulence-related injuries' — that definition is crosswalked to TURB, CABIN, not F-NI.  `[definition:IND-14]`
- Not 'In-flight engine shutdown (IFSD)' — that definition is crosswalked to SCF-PP, not F-NI.  `[definition:IND-28]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.02).  `[parent:SCF-PP]`

**Linked example reports**
- DCA11IA040: "Three generators provide AC power, two batteries provide power for APU start and for emergency power, and an emergency generator provides AC power in the event all three main generators fail."
- WPR13FA294: "Contributing to the accident were the installation of the supplemental electrical power supply system without the supervision of an FAA-certified mechanic, the lack of an onboard means for fire suppression, and the pilot's inability to see the low-conspicuity power lines across the landing approach path until it was too late to take evasive action."
- DCA18LA163: "Contributing to the duration of the fire was the contamination of an engine fire isolation system component which resulted in hydraulic fluid leaking into the designated engine fire zone after the engine was shutdown and the fire button was pressed."
- ERA15IA198: "The fuselage consisted of the nose cone, the cockpit, the passenger cabin, the rear lavatory, the baggage compartment, the rear compartment, the auxiliary power unit and the No."
- ERA15FA181: "Probable cause: A rapid onset of smoke and/or fire inflight for reasons that could not be determined due to the postimpact fire and the condition of the wreckage."
- NYC08FA292: "The passenger at this time retrieved a fire extinguisher and the pilot took it and discharged the fire extinguisher into the battery area."
- CEN18LA349: "The inflight emergency checklists for fire were: Engine Fire, Fuselage Fire, Wing Fire, and Electrical Fire."
- ERA24FA338: "The report also detailed inspections of the fuselage that included the aft cabin wing attach frames and a functional test of the nickel-cadmium (Ni-Cad) batteries."
- WPR20FA051: "A few minutes later, flames began to emerge from the cabin, after which the cabin became completely engulfed in fire (see figure 2)."
- ERA11FA312: "Probable cause: An in-flight fire that mostly likely occurred in the right front cockpit area behind the instrument panel and below the glare shield; the origin of the fire could not be determined because of the extensive fire damage."
- ERA14CA420: "A passenger remained outside the airplane, while the pilot was inside the airplane and a ground power unit (GPU) with a minimum of 28 volts was connected to the external power receptacle."
- LAX08FA286: "Probable cause: A loss of power in the right engine due to an in-flight fuel-fed fire in the right engine compartment that, while the exact origin could not be determined, was likely related to the right engine-driven fuel pump, its fuel supply line, or fitting."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 pass · G9 pass

### B18 · Electrical smoke or burning smell in the flight deck

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent SCF-NP System/Component Failure – Non-Powerplant*

**Definition.** Smoke, fumes or a burning electrical smell appears in the flight deck, often traced to wiring, a display or a window heater.

**Include when**
- The occurrence meets the CICTT SCF-NP (System/Component Failure – Non-Powerplant) definition.  `[parent:SCF-NP]`
- Core definition: Smoke, fumes or a burning electrical smell appears in the flight deck, often traced to wiring, a display or a window heater.  `[candidate:B18]`
- Matches 'Hydraulic system failure' (SKYbrary – Hydraulic System Failure): Loss of hydraulic fluid or pressure that degrades flight controls, brakes, steering or landing gear, handled with non-normal checklists.  `[definition:IND-24]`

**Exclude when**
- Belongs to sibling B09 'Hydraulic system failure in flight' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN11IA379]`  
  > At the time of the incident, the airplane had 24,969.4 flight hours and 20,132 flight cycles.
- Coded FUEL (Fuel Related) rather than SCF-NP: similar wording, different occurrence category.  `[report:CEN22FA405]`  
  > The pilot stated that he flew most of the flight with the airplane’s automatic flight control system (AFCS) engaged, making necessary heading changes using the heading bug on the primary flight display (PFD).
- Coded F-NI (Fire/Smoke (Non-Impact)) rather than SCF-NP: similar wording, different occurrence category.  `[report:ERA11FA312]`  
  > He went onto his deck, and saw smoke.
- Not 'Smoke or fumes in flight' — that definition is crosswalked to F-NI, not SCF-NP.  `[definition:IND-32]`
- Events better described by CICTT F-NI (Fire/Smoke (Non-Impact)) (runner-up parent, margin 0.18).  `[parent:F-NI]`

**Linked example reports**
- DCA11IA040: "The captain said the autothrust message was followed by a red "LAND ASAP" ECAM message accompanied by the electrical page synoptic display and the "AVIONICS SMOKE" ECAM procedure."
- DCA16FA199: "The instrument panel consisted of four identical primary flight display (PFD)/multifunction display (MFD) panels."
- ENG20LA016: "The pilot displays are part of the electronic flight instrument system (EFIS) and provide primary flight instrumentation information on the primary flight display (PFD) and the navigation display (ND)."
- ERA23LA135: "Probable cause: The flight crew’s failure to remove the right side pitot probe cover before flight, their decision to depart with a No-Go advisory message following an aborted takeoff, and their selection of the incorrect non-normal checklist in flight, which resulted in an in-flight upset that exceeded the maneuvering load factor limitations of the airplane and resulted in fatal injuries to a passenger whose seatbelt was not fastened."
- DCA22LA212: "No message appeared on the airplane’s electronic centralized aircraft monitor, and no flight deck alerts annunciated."
- ERA15IA198: "Probable cause: Unknown maintenance personnel’s inadequate securing of a wiring bundle during a maintenance, repair, or modification event, which led to chafing of the wiring bundle, an electrical short and arcing, and a subsequent in-flight fire."
- CEN22LA430: "According to a statement provided by the flight crew, about 7 minutes before arriving at Houma-Terrebonne Airport (HUM), Houma, Louisiana, the flight crew and passengers smelled a “burning plastic” odor throughout the helicopter."
- CHI08IA292: "The flight crew reported that just prior to leveling off at flight level (FL) 370, some cockpit lights flickered, multiple EICAS messages appeared including an AIR/GRD SYS caution message, and the Standby Power OFF light illuminated."
- DCA14MA081: "According to flight crew interviews, the captain and first officer noticed that there were no V-speeds indicated on their primary flight displays (PFDs), and FDR and CVR data show that as the airplane accelerated through 86 KIAS as an aural RETARD alert sounded in the cockpit."
- ERA12FA385: "Instrument meteorological conditions prevailed at the altitude and location of the departure from controlled flight and an instrument flight rules (IFR) flight plan was filed for the 14 Code of Federal Regulations (CFR) Part 91 personal flight from St Lucie County International Airport (FPR), Fort Pierce, Florida, to Freeman Field Airport (3JC), Junction City, Kansas."
- ENG15IA037: "Comparing the display blanking electrical field thresholds seen during the near strike lightning and flat plate testing, the electrical field analysis results showed that, based on the lower blanking thresholds demonstrated during the near strike lightning testing and the flat plate testing, the lightning model results exceeded the lower bound estimate of the display blanking threshold during every case where a "fast" spark gap fired or a waveform "H" was applied."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass

### B19 · Low fuel after holding or a diversion

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent FUEL Fuel Related*

**Definition.** Extended holding, a missed approach or a diversion leaves the aircraft close to or below final reserve fuel, and the crew declares minimum fuel or a fuel emergency.

**Include when**
- The occurrence meets the CICTT FUEL (Fuel Related) definition.  `[parent:FUEL]`
- Core definition: Extended holding, a missed approach or a diversion leaves the aircraft close to or below final reserve fuel, and the crew declares minimum fuel or a fuel emergency.  `[candidate:B19]`
- Matches 'Minimum fuel and fuel emergency' (ICAO Annex 6 – Fuel planning and in-flight fuel management): The crew declares MINIMUM FUEL when any change may land them below final reserve, and MAYDAY FUEL when the landing fuel is expected to be below final reserve.  `[definition:IND-33]`

**Exclude when**
- Coded SCF-PP (System/Component Failure – Powerplant) rather than FUEL: similar wording, different occurrence category.  `[report:CEN17LA176]`  
  > The fuel supply line to the engine is routed from the header tank, located in the fuselage, through a fuel shut off valve, an emergency electric driven fuel pump, and then directed to the main electric driven fuel pump.
- Coded RI (Runway Incursion) rather than FUEL: similar wording, different occurrence category.  `[report:DCA18IA081]`  
  > He was on home reserve from 1030 until 1230 and airport reserve from 1230 until 2030.
- Coded LOC-I (Loss of Control – Inflight) rather than FUEL: similar wording, different occurrence category.  `[report:CEN14FA046]`  
  > At 1545:38, the tower controller transmitted, "Six Juliet Tango are you uh declaring an emergency uh well we'll declare emergency for runway 18L – you say you have an engine out and souls on board and fuel remaining if you have time." The controller made two additional attempts to contact the pilot at 1546:06 and 1546:55, but there was no response.
- Not 'Undershoot' — that definition is crosswalked to USOS, not FUEL.  `[definition:IND-37]`
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not FUEL.  `[definition:IND-22]`
- Not 'Lateral navigation error' — that definition is crosswalked to NAV, not FUEL.  `[definition:IND-41]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.00).  `[parent:SCF-PP]`

**Linked example reports**
- CEN17FA252: "The fuel monitoring system consists of the fuel quantity indicator, low fuel warning, fuel pressure waning, and fuel filter contamination warning."
- CEN22FA405: "Finding: Aircraft-Aircraft power plant-Engine fuel and control-Fuel controlling system-Unintentional use/operation."
- CEN19FA124: "Finding: Aircraft-Aircraft systems-Fuel system-Fuel quantity indicator-Damaged/degraded."
- ERA16FA289: "1 was "hot on climb" and "ran rich of peak = 31", 2200, 23 gal/side, and EDM [engine data monitor] screen flicker." According to the Pilot Operating Handbook (POH), the fuel system of the airplane consisted of fuel cells, engine driven fuel pumps, fuel boost pumps, emergency fuel pumps, fuel injectors, control valves, fuel filters, fuel pressure and flow gauges, fuel drains, fuel tanks vents, and a fuel selector panel."
- ERA09IA140: "Contributing factor: Aircraft-Aircraft systems-Fuel system-Fuel selector/shutoff valve-Not serviced/maintained."
- WPR22FA094: "The emergency procedure for a FUEL PRES red warning light, which indicated that the dry engine fuel pressure was less than 700 mb while airborne, was to shut down use of AB and reduce rpm, check LP pumps on, check left and right LP caution lights out, and land as soon as possible while monitoring the fuel totalizer and both fuel gauges for indications of a fuel leak."
- DCA12PA049: "The pilot of Topgun24, who had been holding to conduct a PAR, declared a low fuel state."
- DCA12FA076: "The accident pilot repeated that he thought he was getting a slow transfer from the left side fuel system, but could not determine the actual quantity of fuel in the left outboard tank (which would be the first to be depleted if fuel was transferring)."
- CEN24LA272: "Finding: Aircraft-Aircraft systems-Fuel system-Fuel distribution-Not specified."
- ERA12LA294: "Fuel was present in the fuel strainer but, no fuel was found in the fuel line from the fuel strainer to the engine driven pump."
- CEN18LA047: "The first step of the "AFTER STARTING AND TAXI" checklist in the AFM stated, "Transfer Pumps - ON." The second step of the "SHUTDOWN AND SECURING" checklist stated, "Transfer Pumps - OFF." The AFM limitation section, in part, stated, "Operation of either engine with its corresponding fuel pressure light (L FUEL PRESS or R FUEL PRESS annunciator) illuminated is limited to 10 hours before overhaul or replacement of the engine-driven fuel pump." An automatic feathering system was an option for this airplane type."
- CEN12FA086: "The flight was given that heading for the instrument approach and the pilot then declared an emergency."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 pass · G9 pass

### B20 · Pushback or towing collision

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** During pushback or towing the tug, towbar or aircraft strikes another aircraft, a vehicle or a fixed object.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: During pushback or towing the tug, towbar or aircraft strikes another aircraft, a vehicle or a fixed object.  `[candidate:B20]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`
- Matches 'Loss of separation' (ICAO Doc 4444 – PANS-ATM (separation minima)): Two aircraft come closer than the prescribed separation minima, often after an ATC clearance or instruction puts them in conflict.  `[definition:IND-23]`
- Narrative describes 'maneuver' (2 of 4 supporting reports).  `[report:DCA25LA306]`  
  > Probable cause: The abrupt maneuver required to comply with a traffic alert and collision avoidance system resolution advisory during descent.

**Exclude when**
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (1 report(s) assigned there).  `[report:ERA15MA259]`  
  > (The first witness is located north of the collision point, and the second witness is located southwest of the collision point.) PERSONNEL INFORMATIONF-16 Pilot According to USAF personnel, the pilot of the F-16 was current and qualified in the accident airplane as a four-ship flight lead.
- Belongs to sibling B12 'GNSS interference or spoofing' when it matches that bucket better (2 report(s) assigned there).  `[report:WPR15MA243/2]`  
  > From this time until the collision occurred (about 1103), the LC was controlling nine aircraft.
- Distinguish from sibling B07 'Loss of separation caused by an ATC clearance' under the same parent.  `[sibling:B07]`
- Distinguish from sibling B11 'Terrain warning on a non-precision approach' under the same parent.  `[sibling:B11]`
- Distinguish from sibling B28 'Wrong route or waypoint loaded in the FMS' under the same parent.  `[sibling:B28]`
- Coded GCOL (Ground Collision) rather than MAC: similar wording, different occurrence category.  `[report:SEA08LA061/2]`  
  > The UAL tug operator reported to SFO Airport Authority shortly after the collision that during the pushback process, he was looking over his shoulder and didn't see the other aircraft pushback from Gate 79.
- Not 'Pushback and towing' — that definition is crosswalked to RAMP, not MAC.  `[definition:IND-34]`
- Not 'Wildlife strike' — that definition is crosswalked to BIRD, not MAC.  `[definition:IND-15]`
- Not 'Damaging bird strike' — that definition is crosswalked to BIRD, not MAC.  `[definition:IND-39]`
- Events better described by CICTT GCOL (Ground Collision) (runner-up parent, margin 0.01).  `[parent:GCOL]`

**Linked example reports**
- ERA24LA079: "Probable cause: The UAS operator’s failure to operate within the limitations of the COA that he was using to operate inside class C airspace, which resulted in a collision between the UAS and the helicopter."
- DCA25LA306: "Probable cause: The abrupt maneuver required to comply with a traffic alert and collision avoidance system resolution advisory during descent."
- CEN24LA110: "Probable cause: The failure of both pilots to see and avoid one another while maneuvering, which resulted in a mid-air collision."
- ANC16FA061: "Cause: Personnel issues-Psychological-Attention/monitoring-Monitoring other aircraft-Pilot of other aircraft."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B21 · Disruptive or unruly passenger

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent CABIN Cabin Safety Events*

**Definition.** A passenger is aggressive, intoxicated or refuses crew instructions, interfering with the crew or other passengers.

**Include when**
- The occurrence meets the CICTT CABIN (Cabin Safety Events) definition.  `[parent:CABIN]`
- Core definition: A passenger is aggressive, intoxicated or refuses crew instructions, interfering with the crew or other passengers.  `[candidate:B21]`
- Matches 'Unruly or disruptive passenger' (ICAO Doc 10117 – Manual on the Legal Aspects of Unruly and Disruptive Passengers): A passenger who fails to respect rules of conduct or to follow crew instructions, disturbing good order and discipline on board.  `[definition:IND-30]`
- Matches 'Turbulence-related injuries' (FAA Advisory Circular 120-88A – Preventing Injuries Caused by Turbulence): Passengers and flight attendants are injured in turbulence mainly when standing or not wearing seat belts, and by unsecured carts and galley equipment.  `[definition:IND-14]`
- Matches 'Lithium battery fire' (FAA SAFO – Fire risks from lithium batteries in the cabin): Portable electronic devices and power banks can overheat in thermal runaway, producing smoke and fire in the cabin; crew cool the device with water or non-alcoholic liquid.  `[definition:IND-31]`

**Exclude when**
- Coded TURB (Turbulence Encounter) rather than CABIN: similar wording, different occurrence category.  `[report:DCA23LA096]`  
  > Of the 2 flight crewmembers, 8 flight attendants, and 283 passengers (including 2 off-duty Hawaiian Airlines pilots in the cockpit jumpseats and 3 lap-held children) aboard the airplane, 4 occupants (1 flight attendant and 3 passengers) sustained serious injuries, and 20 occupants (3 flight attendants and 17 passengers) sustained minor injuries.
- Coded SCF-PP (System/Component Failure – Powerplant) rather than CABIN: similar wording, different occurrence category.  `[report:DCA15FA185]`  
  > (The captain had previously called for the engine fire checklist at 1612:58, when he was also instructing the first officer to notify ATC that the airplane would be stopping on the runway.) At 1613:12, the relief pilot asked if he should make an announcement to the passengers and cabin crew; the captain agreed and indicated that they should "stay there where they are." At 1613:19, the relief pilot used the public address (PA) system to instruct the passengers and cabin crew to "please remain in your seats and await further instructions." About 1 second later, the captain contacted ATC, stating "mayday mayday" and "request fire services," and the tower controller responded that fire services were on the way.
- Coded EVAC (Evacuation) rather than CABIN: similar wording, different occurrence category.  `[report:DCA15CA129]`  
  > The crew stated that they believed the delay in receiving response to their radio calls indicated ARFF personnel were busy addressing a safety concern and after hearing no further transmissions, the crew completed the evacuation checklist and advised passengers and cabin crew to proceed with evacuation.
- Not 'Resolution advisory (RA)' — that definition is crosswalked to MAC, not CABIN.  `[definition:IND-10]`
- Not 'Smoke or fumes in flight' — that definition is crosswalked to F-NI, not CABIN.  `[definition:IND-32]`
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not CABIN.  `[definition:IND-08]`
- Events better described by CICTT EVAC (Evacuation) (runner-up parent, margin 0.23).  `[parent:EVAC]`

**Linked example reports**
- ERA23LA135: "At 1544:26, after control of the airplane had been regained, the SIC stated, “we shouldn’t have had the autopilot on” and the PIC responded with, “yeah.” Moments after the in-flight upset, the flight crew were alerted by one of the passengers that another passenger had been seriously injured."
- CEN11LA092: "According to crew statements, the injured passenger was designated as a wheelchair passenger and had boarded the airplane wearing an ankle brace."
- ERA09LA488: "According to the operator, the airplane was configured for 2 flight crew, 4 cabin crew, and 117 passengers."
- DCA16CA193: "There were 6 crew and 172 passengers on board."
- DCA15CA152: "According to flight crew statements, the seatbelt sign was illuminated and a public address announcement had been made to remain seated prior beginning the initial descent."
- DCA18CA294: "Of the 186 passengers and crew onboard, one flight attendant received a serious injury."
- DCA18CA209: "There were two flight crew, 4 flight attendants, and unknown passengers on board at the time."
- CEN09LA256: "The first officer made a similar announcement to the crew and passengers stressing the need to remain seated for their safety."
- DCA18CA049: "Of the 57 passengers and crew onboard, one flight attendant was seriously injured."
- DCA14CA090: "On March 4, 2014, about 2300 Pacific standard time, a flight attendant (FA) on Delta Air Lines flight 1248, a Boeing 737-900ER, N809DN, tripped over a passenger's bag while the passengers were boarding at San Diego International Airport (SAN), San Diego, California."
- DCA18CA219: "Of the 292 passengers and crew onboard, one flight attendant received minor injuries and one flight attendant received serious injuries."
- DCA17CA096: "The remaining 114 passengers and crew were not injured."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 pass · G9 pass

### B22 · Tail strike on takeoff

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent RE Runway Excursion*

**Definition.** The tail strikes the runway during takeoff rotation, often after early or fast rotation or a wrong takeoff speed or weight.

**Include when**
- The occurrence meets the CICTT RE (Runway Excursion) definition.  `[parent:RE]`
- Core definition: The tail strikes the runway during takeoff rotation, often after early or fast rotation or a wrong takeoff speed or weight.  `[candidate:B22]`
- Matches 'Anomaly: Ground Excursion – Runway' (NASA ASRS coding taxonomy): An aircraft departs the runway surface during the takeoff or landing roll, including overruns after a long or fast landing.  `[definition:IND-07]`
- Matches 'Runway excursion (veer-off and overrun)' (SKYbrary – Runway Excursion): An aircraft leaves the runway surface during takeoff or landing, either by veering off the side or by overrunning the end.  `[definition:IND-05]`
- Matches 'Runway condition code (RWYCC)' (ICAO Global Reporting Format (GRF) for runway surface conditions): A runway condition code from 6 (dry) down to 0 reports braking performance on wet or contaminated runways (water, slush, snow, ice), so crews can recompute landing distance.  `[definition:IND-06]`

**Exclude when**
- Belongs to sibling B04 'Overrun on a contaminated runway' when it matches that bucket better (3 report(s) assigned there).  `[report:CEN14FA505]`  
  > The pilots calculated the runway length required for a wet runway landing and then chose to land on runway 1, which was the longer runway.
- Coded ARC (Abnormal Runway Contact) rather than RE: similar wording, different occurrence category.  `[report:DCA14MA081]`  
  > As the captain taxied onto runway 27L, he noticed that runway 27R had been inserted into the FMC instead of runway 27L and requested that the first officer change the runway in the FMC, which was completed at 1823:10.
- Coded LOC-I (Loss of Control – Inflight) rather than RE: similar wording, different occurrence category.  `[report:DCA13MA121]`  
  > Weight and Balance The weight and balance information for the airplane was contained in the aircraft inspection record.
- Coded CTOL (Collision with Obstacle(s) During Takeoff and Landing) rather than RE: similar wording, different occurrence category.  `[report:ERA16FA257]`  
  > With a flap setting of 25°, the rotation speed for a short-field takeoff was between 50 and 60 KIAS.
- Not 'Tail strike' — that definition is crosswalked to ARC, not RE.  `[definition:IND-35]`
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not RE.  `[definition:IND-03]`
- Not 'Hard landing, tail strike' — that definition is crosswalked to ARC, not RE.  `[definition:IND-18]`
- Events better described by CICTT CTOL (Collision with Obstacle(s) During Takeoff and Landing) (runner-up parent, margin 0.21).  `[parent:CTOL]`

**Linked example reports**
- ERA11LA390: "It was marked with nonprecision markings that were in good condition Usable length for landing on runway 24 was 3,471 feet due to a displaced threshold on the end of runway 06, marked as a taxiway aligned with a runway, and a chevroned runway safety area on the end of runway 24."
- WPR20LA289: "He saw the accident airplane come into view on runway 33; however, it “wasn’t accelerating at a normal rate for that type of aircraft.” The airplane continued the takeoff roll, accelerating much more slowly than he was accustomed to seeing; it rotated abruptly, “to a slightly steeper angle of attack than a normal takeoff and it appeared to lift off slightly before settling back to the ground; which caused the nosewheel to come back down to the runway surface.” The witness further stated that, as the airplane continued the takeoff roll, it [the airplane] again rotated abruptly and remained in a nose-high attitude while approaching the departure end of runway 33."
- DCA22MA009: "The captain briefed the rejected takeoff procedures, during which he stated that they would reject the takeoff after V1 “only if the airplane won’t fly.” (V1, also known as the decision speed, is defined, in part, as the maximum speed by which a rejected takeoff must be initiated to ensure that the airplane can be stopped on the remaining runway.) The captain and the first officer subsequently started the engines, and, at 0952:33, the TME air traffic controller provided their clearance to taxi to runway 36."
- WPR15FA125: "The pilot stated that once cleared for takeoff, he applied engine thrust and the engine spool-up, takeoff roll, and acceleration check speeds were as expected."
- DCA17IA020: "The captain reported that he saw the end of the runway approaching and began to apply maximum braking, as well as right rudder because he thought it would be better to veer to the right rather than continue straight to the road beyond the end of the runway."
- CEN18TA374: "Using the same weight and balance information for the previous flight, except with 25 gallons of fuel, the ramp weight would have been 2,978 lbs and the takeoff weight 2,968 lbs; both of these weights exceeded the maximum ramp and takeoff weights, an exceedance of 18 lbs for both weight limitations as specified in the POH."
- WPR18LA179: "Ramp fuel weight = 966 lbs Takeoff fuel weight = 936 lbs The pilot provided both maximum allowable and calculated ramp and takeoff weights for the flight."
- WPR21LA110: "According to the airplane manufacturer, it is possible for the pilots to change FMS-suggested runway length or takeoff weight for the computation of takeoff speeds."
- ERA12FA567: "In 2008, Runway 10/28 was resurfaced; the runway edge markings were painted at 50 feet from the centerline, which allowed an actual runway width of 100 feet with 25 feet on each side paved but not available for use during takeoff or landing."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 FAIL · G9 pass

### B23 · Windshear on final approach

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent LOC-I Loss of Control – Inflight*

**Definition.** A sudden change in wind speed or direction on approach, often near a thunderstorm or microburst, causes loss of airspeed and a windshear warning.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: A sudden change in wind speed or direction on approach, often near a thunderstorm or microburst, causes loss of airspeed and a windshear warning.  `[candidate:B23]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`
- Matches 'Stall prevention and recovery' (FAA Advisory Circular 120-109A – Stall Prevention and Recovery Training): Training to recognise and recover from approaches to stall and full stalls, including during go-arounds with high thrust and pitch.  `[definition:IND-21]`

**Exclude when**
- Belongs to sibling B05 'Stall warning or upset during a go-around' when it matches that bucket better (1 report(s) assigned there).  `[report:WPR21FA286]`  
  > At 1251:22, the FO informed the captain, “New numbers are sent… eighteen, twenty-nine, forty-five” (referring to a Vref speed of 118 kts, approach climb speed of 129 kts, final segment speed of 145 kts).
- Distinguish from sibling B26 'Unreliable airspeed from blocked pitot probes' under the same parent.  `[sibling:B26]`
- Distinguish from sibling C4 'Upset or stall after unreliable airspeed' under the same parent.  `[sibling:C4]`
- Coded WSTRW (Windshear or Thunderstorm) rather than LOC-I: similar wording, different occurrence category.  `[report:WPR22LA251]`  
  > This document defined windshear as – “any rapid change in wind direction or velocity.” Severe windshear was defined as “a rapid change in wind direction or velocity causing airspeed changes greater than 15 knots or vertical speed changes greater than 500 feet per minute.” Text that followed these definitions stated the following: The primary focus of the Pilot Windshear Guide is directed toward windshear associated with convective weather conditions: thunderstorms, and in particular the most hazardous form of wind shear, the microburst.
- Coded RE (Runway Excursion) rather than LOC-I: similar wording, different occurrence category.  `[report:DCA19MA143]`  
  > (Precision approach radar is a fixed-base primary approach aid used by the US Navy during poor visibility conditions to provide vertical and lateral guidance, as well as range, to aircraft on final approach).
- Coded ARC (Abnormal Runway Contact) rather than LOC-I: similar wording, different occurrence category.  `[report:ERA23LA376]`  
  > The three low-speed awareness color bands on the speed tape are defined as follows: •VSS: This speed, defined as the stable velocity speed, is represented by the top of the white band.
- Not 'Low-level windshear' — that definition is crosswalked to WSTRW, not LOC-I.  `[definition:IND-36]`
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not LOC-I.  `[definition:IND-22]`
- Not 'Undershoot' — that definition is crosswalked to USOS, not LOC-I.  `[definition:IND-37]`
- Events better described by CICTT WSTRW (Windshear or Thunderstorm) (runner-up parent, margin 0.02).  `[parent:WSTRW]`

**Linked example reports**
- WPR18MA087: "He recalled that the two helicopters that landed immediately before him were on the west landing pads facing east, the same as his chosen approach direction, and noted that the windsock indicated wind from the north/northeast."
- CEN14FA099: "The ASE ASOS 1-minute data (which uses a 2-minute running average wind issued every minute) from 1218 to 1222 were: TIME WIND GUST CROSS TAILWIND 1218 333° 15KT 345° 20KT 5KT 19KT 1219 323° 15KT 339° 22KT 0KT 22KT 1220 324° 14KT 324° 25KT 7KT 24KT 1221 333° 15KT 338° 22KT 1KT 22KT 1222 333° 14KT 328° 17KT 3KT 17KT Accident An urgent pilot report (PIREP) over ASE at 1205 from a Learjet 35 flightcrew reported low-level wind shear with a 10 kt loss of airspeed on a 2-mile final to runway 15."
- ERA22FA004: "At 0539:28, as the flight was nearing the final approach fix and attempting to activate the pilot-controlled lighting, the captain stated in a frustrated tone, “would you fly the airplane- man-uhh man- I’ve been doing everything else.” A few seconds later, the captain stated, “here it is right over.” The captain subsequently stated, “fly the ILS approach.” The captain also noted that air brakes were stowed, flaps were set to 40°, and the before landing checklist was complete."
- CEN12LA345: ""Low-level wind shear is a sudden, drastic change in wind speed and/or direction over a very small area."
- CEN14FA046: "Pilots must perform approaches to stalls in takeoff, clean, and landing configurations with at least one approach-to-stall maneuver flown while in a 15-30 degree bank turn."
- CEN22LA110: "Probable cause: The windshear encounter on short final approach, which resulted in an excessive decent rate and ground impact."
- OPS21LA003: "The alert stated that data indicate a potential for “unstable approaches” and “GPWS Terrain/Obstacle Warnings.” It further provided conditions that may result in an unstabilized approach with those conditions being “a steeper glidepath,” “Parking garage approximately 0.4 NM from RWY 27 threshold” and “high gross weight and tailwinds may require vertical speeds in excess of 1000 fpm during final approach segment.” Southwest Airlines General Approach Policies The Southwest Airlines B737NG Operating Manual, Section 11.1.3.1 provided, in part, the following general approach guidance: If available, follow glidepath guidance on final."
- ERA17FA190: "During that flight, the pilot practiced several types of instrument approaches, including an ILS approach and a missed approach."
- CHI08FA282: "At 1835:55, N193BS transmitted, and Minneapolis three bravo sierra so for planning purposes uh (unintelligible) we are going to get radar vectors to the localizer three six.” At 1836:01, ZMP03 transmitted, “november three bravo sierra affirmative.” At 1904:49, ZMP03 transmitted, “a november three bravo sierra’s four south of dougy maintain three thousand five hundred til on a published portion of the approach cleared for the localizer three six approach arbor vitae.” At 1905:07, N193BS transmitted, “ah i got all that ah three thousand five hundred till on a published segment (unintelligible) cleared three six approach.” At 1905:13, ZMP03 transmitted, “November three bravo sierra roger and are you going to be able to shoot the approach from a couple south of the marker there.” At 1905:19, N193BS transmitted, “i’m sorry what.” At 1905:20, ZMP03 transmitted, “are you going to be able to make the approach from fifty two hundred from a couple south of the marker.” At 1905:29, the autopilot (AP) was selected OFF at a pressure altitude of 5,033 feet and a heading of 359 degrees magnetic."
- ERA09LA111: "Approach and Landing Guidance According to the FAA's Airplane Flying Handbook (FAA-H-8083-3A), the objective of a good final approach is to descend at an angle and airspeed that will permit the airplane to reach the desired touchdown point at an airspeed which will result in minimum floating just before touchdown; in essence, a semi-stalled condition."
- WPR14LA271: "Probable cause: The pilot’s execution of a traffic pattern that did not put the airplane in position for a normal final approach and the pilot’s decision to continue the landing attempt instead of initiating a go-around, which resulted in the airplane exceeding its critical angle-of-attack and experiencing an aerodynamic stall at an altitude too low to prevent ground impact."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B24 · Landing short of the runway

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent USOS Undershoot/Overshoot*

**Definition.** The aircraft touches down before the runway threshold, on the approach lights or in the undershoot area.

**Include when**
- The occurrence meets the CICTT USOS (Undershoot/Overshoot) definition.  `[parent:USOS]`
- Core definition: The aircraft touches down before the runway threshold, on the approach lights or in the undershoot area.  `[candidate:B24]`
- Matches 'Undershoot' (SKYbrary – Landing Short (Undershoot)): The aircraft touches down before the runway threshold, often after an unstable or low approach or a visual illusion.  `[definition:IND-37]`

**Exclude when**
- Coded RI (Runway Incursion) rather than USOS: similar wording, different occurrence category.  `[report:DCA18IA081]`  
  > The captain stated that shortly after crossing the initial approach fix, the airplane exited the clouds and that he observed what he believed was runway 06 and runway lights, though according to his interview he questioned whether the runway lights were on bright or dim.
- Coded CTOL (Collision with Obstacle(s) During Takeoff and Landing) rather than USOS: similar wording, different occurrence category.  `[report:ERA09CA038]`  
  > The final approach is initially over trees, then opens into a cleared area where approach lights are positioned.
- Coded RE (Runway Excursion) rather than USOS: similar wording, different occurrence category.  `[report:DCA19MA143]`  
  > (Precision approach radar is a fixed-base primary approach aid used by the US Navy during poor visibility conditions to provide vertical and lateral guidance, as well as range, to aircraft on final approach).
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not USOS.  `[definition:IND-04]`
- Not 'Pilot deviation (runway incursion)' — that definition is crosswalked to RI, not USOS.  `[definition:IND-40]`
- Not 'Runway incursion' — that definition is crosswalked to RI, not USOS.  `[definition:IND-01]`
- Events better described by CICTT RI (Runway Incursion) (runner-up parent, margin 0.03).  `[parent:RI]`

**Linked example reports**
- WPR10LA427: "This touchdown location was about 217 feet short of the runway's displaced threshold."
- ERA20MA001: "Witness statements and video indicated that the airplane struck the runway 6 approach lights in a right wing-down attitude about 1,000 ft before the runway."
- CEN21LA189: "Probable cause: The pilot's distraction and his failure to maintain a proper glidepath on the approach, which resulted in him landing short of the runway and impacting a snowbank."
- ERA10CA343: "The pilot's manual also advised, "consider flying a steeper approach to compensate for the 'burble' downdraft typically present at the end of the runway," and noted that the hills on either side and the runway's upslope "will combine to produce the optical illusion of being too steep an approach path." The manual further stated, "consider carefully the effects of density altitude on the performance of your aircraft," as well as, "many pilots will not consider landing with SSE winds, and will simply divert" to another airport."
- ERA25LA128: "Probable cause: The pilot’s failure to maintain an appropriate glide path during the landing approach, which resulted in in the airplane contacting a snowbank short of the runway."
- GAA19CA525: "The pilot reported that, while performing landings for night currency, he misjudged the approach and the airplane landed short on the engineered materials arrestor system prior to the runway threshold."
- WPR12LA087: "Because he failed to manage his glide profile in a manner that allowed him to extend the airplane's glide all the way to the approach end of the runway, and since he elected not to add engine power, the airplane touched down in a grassy area a little over 300 feet short of the runway threshold."
- ERA20CA210: "Probable cause: The pilot's failure to maintain proper glide path during final approach which resulted in a collision with airport equipment short of the runway."
- GAA19CA016: "He added that the precision approach path indicator (PAPI) lights were off, and he could not get the runway lights to turn on either."
- DCA25LA291: "The right main landing gear touched down approximately 52 feet short of the paved surface, which was about 430 feet short of the runway threshold (see figure 2)."
- ANC19LA045: "A video, recorded by a bystander, captured the accident sequence and revealed that the airplane, while on short final approach, was low on the glide path and dragging its landing gear through vegetation located near the approach end of the runway."
- CEN10CA106: "The pilot flew an instrument approach to runway 36 and decided to circle to land on runway 18 as the winds slightly favored runway 18, and because runway 36 contained a slight downhill slope."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 pass · G9 pass

### B25 · Airframe icing in flight

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent SCF-PP System/Component Failure – Powerplant*

**Definition.** Ice builds on the wings, tail or windshield in flight in icing conditions, degrading performance or handling.

**Include when**
- The occurrence meets the CICTT SCF-PP (System/Component Failure – Powerplant) definition.  `[parent:SCF-PP]`
- Core definition: Ice builds on the wings, tail or windshield in flight in icing conditions, degrading performance or handling.  `[candidate:B25]`
- Matches 'In-flight engine shutdown (IFSD)' (SKYbrary – In-Flight Shutdown): An engine is shut down in flight because of a failure or a precautionary indication such as low oil pressure, high vibration or fire.  `[definition:IND-28]`

**Exclude when**
- Belongs to sibling B13 'Engine shutdown after loss of oil pressure' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN14FA046]`  
  > Visual meteorological conditions prevailed for the flight, and an instrument flight plan had been filed.
- Coded ARC (Abnormal Runway Contact) rather than SCF-PP: similar wording, different occurrence category.  `[report:DCA14FA058]`  
  > When either of the ice detectors detect ice, an advisory message "ICE CONDITION" is shown on the EICAS display, a signal would be sent to the anti-ice system valves to activate them to open, and a signal would be sent to the full authority digital engine control to activate the automated engine icing thrust setting logic to limit the thrust to a minimum acceptable level.
- Coded FUEL (Fuel Related) rather than SCF-PP: similar wording, different occurrence category.  `[report:ERA22LA157]`  
  > This will result in the need to select ‘carb heat on’ in less severe icing conditions and for a longer duration while using Mogas.” Review of a carburetor icing probability chart indicated that meteorological conditions that existed at the time of the accident were conducive to carburetor icing at glide and cruise power.
- Not 'In-flight airframe icing' — that definition is crosswalked to ICE, not SCF-PP.  `[definition:IND-38]`
- Not 'Holdover time' — that definition is crosswalked to ICE, not SCF-PP.  `[definition:IND-17]`
- Not 'Unreliable airspeed' — that definition is crosswalked to LOC-I, SCF-NP, not SCF-PP.  `[definition:IND-09]`
- Events better described by CICTT FUEL (Fuel Related) (runner-up parent, margin 0.15).  `[parent:FUEL]`

**Linked example reports**
- ERA12LA575: "Utilizing those ambient temperature/dew point conditions, the FAA chart titled "Conditions Favoring Carb Ice Formation" indicated the probability of serious carburetor icing at glide power."
- CEN09MA117: "In the event of an in-flight engine fire indication, the affected engine's fire extinguisher T-handle will illuminate, and the flight crew is trained to pull the illuminated handle full aft."
- ERA21FA232: "Review of the icing probability chart contained withing the FAA Special Airworthiness Information Bulletin CE-09-35 revealed the atmospheric conditions at the time of the accident were “conducive to serious icing at glide power.” According to the Gulfstream American Model AA-5A Cheetah Pilot’s Operating Handbook, Normal Procedures: Page 4-11, DESCENT, (3) Carburetor Heat – As required by engine power setting and weather conditions page 4-19, NOTE – If engine runs rough during cruise with carburetor heat on, it may be due to an over-rich condition."
- GAA17CA306: "Probable cause: A partial loss of engine power due to the formation of carburetor icing, which resulted from the student pilot’s failure to apply carburetor heat and the flight instructor’s delayed response in applying carburetor heat while operating in conditions conducive to carburetor icing."
- ERA20LA335: "Review of the carburetor icing probability chart contained within FAA Special Airworthiness Information Bulletin CE-09-35 revealed the atmospheric conditions at the time of the accident were "conducive to serious icing at cruise power." According to FAA Advisory Circular 20-113, "To prevent accident due to induction system icing, the pilot should regularly use [carburetor] heat under conditions known to be conducive to atmospheric icing and be alert at all times for indications of icing in the fuel system." The AC recommended that when operating in conditions where the relative humidity is greater than 50 percent, "…apply carburetor heat briefly immediately before takeoff, particularly with float type carburetors, to remove any ice which may have been accumulated during taxi and runup." It also stated, "Remain alert for indications of induction system icing during takeoff and climb-out, especially when the relative humidity is above 50 percent, or when visible moisture is present in the atmosphere.""
- CEN11CA660: "Cause: Environmental issues-Conditions/weather/phenomena-Temp/humidity/pressure-Conducive to carburetor icing-Contributed to outcome."
- WPR21LA141: "The Federal Aviation Administration Special Airworthiness Information Bulletin CE-09-35, Carburetor Icing Prevention, stated the following: Pilots should be aware that carburetor icing doesn't just occur in freezing conditions, it can occur at temperatures well above freezing temperatures when there is visible moisture or high humidity."
- ERA21LA284: "FAA Special Airworthiness Information Bulletin (CE-09-35) – Carburetor Icing Prevention, stated that: …pilots should be aware that carburetor icing doesn't just occur in freezing conditions, it can occur at temperatures well above freezing temperatures when there is visible moisture or high humidity."
- WPR18LA102: "The Federal Aviation Administration Special Airworthiness Information Bulletin CE-09-35, Carburetor Icing Prevention, stated the following: Pilots should be aware that carburetor icing doesn't just occur in freezing conditions, it can occur at temperatures well above freezing temperatures when there is visible moisture or high humidity."
- ERA14FA112: "The anti-icing systems were designed to prevent ice accumulation and should be placed in operation prior to entering flight conditions conducive to the formation of ice."
- ANC16CA056: "This document discusses carburetor icing and states in part: Pilots should be aware that carburetor icing doesn't just occur in freezing conditions, it can occur at temperatures well above freezing temperatures when there is visible moisture or high humidity."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass

### B26 · Unreliable airspeed from blocked pitot probes

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent LOC-I Loss of Control – Inflight*

**Definition.** Pitot probes blocked by ice, insects or covers give wrong airspeed indications, leading to warnings and autopilot disconnection.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: Pitot probes blocked by ice, insects or covers give wrong airspeed indications, leading to warnings and autopilot disconnection.  `[candidate:B26]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`

**Exclude when**
- Belongs to sibling B05 'Stall warning or upset during a go-around' when it matches that bucket better (2 report(s) assigned there).  `[report:WPR24FA083]`  
  > According to Section 57-41-00 of the repair manual, “WINGS LEADING EDGE AND LEADING EDGE DEVICES WING LEADING EDGE GENERAL REPAIR,” “In accordance with the Flight Manual procedures the airplane must be test flown by a pilot familiar with the stall identification system and stall characteristics of the 750, 800, 800XP, 850XP, and 900XP series if: (1) The leading edge assembly was removed as a whole for any reason (2) Two or more TKS [de-icing] wing distribution panels on one side are removed or installed” This section of the SRM also refers the operator of the Series 900XP airplane to Section V of the Pilot’s Operating Manual for the procedure and technique to complete the stall test.The manual requires that, before taking the test flight, the operator verify that the Stall Warning and Identification System is functioning properly while on the ground.
- Belongs to sibling C4 'Upset or stall after unreliable airspeed' when it matches that bucket better (2 report(s) assigned there).  `[report:WPR13FA072]`  
  > A "CAUTION" in the PA-31 POH/AFM stated "Do not overpower Autopilot pitch axis for periods longer than 3 seconds because the Autotrim System will operate in a direction to oppose the pilot and will, thereby, cause an increase in the pitch overpower forces." In addition, Paragraph 3.15 (Rough Air Operation) of Section 3(Emergency Procedures) of the PA-31 POH/AFM stated that "when flying in extreme turbulence or strong vertical currents and using the autopilot, the altitude-hold mode should not be used." The airplane was approved for flight into light to moderate icing when equipped with wing and empennage deicing boots, electric propeller deicers, electrically heated windshield, and an ice detection light.
- Distinguish from sibling B23 'Windshear on final approach' under the same parent.  `[sibling:B23]`
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than LOC-I: similar wording, different occurrence category.  `[report:WPR23FA034]`  
  > Indicated airspeed recorded by the Pratt & Whitney engine monitoring system (FAST) measured 35 knots indicated airspeed (KIAS) at 1019:00 and 37 KIAS at 1019:03 before quickly rising to a maximum of 223 KIAS at 1019:21, then dropping to approximately 80 KIAS as the airplane descended.
- Not 'In-flight airframe icing' — that definition is crosswalked to ICE, not LOC-I.  `[definition:IND-38]`
- Not 'Holdover time' — that definition is crosswalked to ICE, not LOC-I.  `[definition:IND-17]`
- Not 'Low-level windshear' — that definition is crosswalked to WSTRW, not LOC-I.  `[definition:IND-36]`
- Events better described by CICTT SCF-NP (System/Component Failure – Non-Powerplant) (runner-up parent, margin 0.18).  `[parent:SCF-NP]`

**Linked example reports**
- DCA14FA058: "The first officer indicated that the airplane was covered in ice, and the captain indicated observing “a lot of ice” on the leading edge of the wings."
- CEN17FA168: "Installed "Modified" Autopilot Computer P/N 065-0064-15, S/N X1898 There was one additional log entry for an autopilot discrepancy reported by a Rico Aviation pilot on April 26, 2017: Autopilot disconnects on climb and cruise."
- ERA12FA385: "At 1232:26, the aircraft's central advisory and warning system (CAWS) recorded that the pusher system went into "ice mode" indicating the pilot had selected the propeller heat on and inertial separator open."
- ERA23LA135: "Flight Data Recorder and Non-Volatile Memory Information Takeoff and Climb According to data recovered from the airplane’s FDR, no significant difference in airspeed between the left and right PFD airspeed indicators was observed in the data following the SIC’s removal of the pitot probe cover."
- ERA19LA072: "He also discussed and trained what airspeed (130 to 140 knots) to maintain during climb and cruise when operating in icing conditions to avoid ice accumulating on the bottom of wing."
- WPR23FA080: "ICE SPEED RESET (down): reset the Stall Warning and Protection System (SWPS) to non-icing schedule and removed the SWPS ICE SPEED message."
- WPR23MA113: "There were seven means by which the pilot could manually disconnect the autopilot, including the autopilot mode pushbutton, the autopilot disconnect/trim interrupt switch, the manual electric trim switch, the go-around pushbutton, the autopilot circuit breaker, the autopilot power switch (if installed), and the avionics master switch."
- CEN12LA095: "Since the autopilot, when installed and operating, may mask tactile cues that indicate adverse changes in handling characteristics, use of the autopilot is prohibited when any of the visual cues specified above exist, or when unusual lateral trim requirements or autopilot trim warnings are encountered while the airplane is in icing conditions."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 FAIL · G9 pass

### B27 · Crew crossed a hold-short line without clearance

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent RI Runway Incursion*

**Definition.** The flight crew taxis past a runway hold-short line without a clearance to enter or cross the runway (pilot deviation).

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: The flight crew taxis past a runway hold-short line without a clearance to enter or cross the runway (pilot deviation).  `[candidate:B27]`
- Matches 'Pilot deviation (runway incursion)' (FAA Runway Safety programme – Pilot deviation): A runway incursion caused by a pilot, such as crossing a hold-short line or entering a runway without an ATC clearance.  `[definition:IND-40]`
- Matches 'Vehicle or pedestrian deviation' (FAA Runway Safety programme): A runway incursion caused by a ground vehicle or a person, such as a driver or pedestrian entering a runway without ATC authorization.  `[definition:IND-19]`
- Matches 'Runway incursion types' (FAA Runway Safety programme): Runway incursions are classified by cause as pilot deviations, operational incidents (controller actions) or vehicle and pedestrian deviations, and by severity from A to D.  `[definition:IND-02]`

**Exclude when**
- Belongs to sibling B01 'Vehicle or pedestrian on the runway without clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:DCA23LA133]`  
  > At 1610:21, the local controller instructed the KMK145 pilot to turn “right” onto taxiway E and cross “runway 4R.” The pilot questioned the instruction to turn right at the taxiway, and the controller then advised the pilot to turn left on taxiway E and hold-short of runway 8L, and the pilot acknowledged those instructions.
- Distinguish from sibling B02 'Landing on a taxiway or the wrong runway at night' under the same parent.  `[sibling:B02]`
- Coded RE (Runway Excursion) rather than RI: similar wording, different occurrence category.  `[report:DCA19MA143]`  
  > At 2140:15, the RF controller advised the flight crew that they were “well above” the 3º glidepath to runway 10; at 2140:25, the precision approach path indicator (PAPI) lights would have appeared to the flight crew as four white lights, indicating the airplane’s glidepath exceeded 3.5º.
- Coded ARC (Abnormal Runway Contact) rather than RI: similar wording, different occurrence category.  `[report:DCA14MA081]`  
  > As the captain taxied onto runway 27L, he noticed that runway 27R had been inserted into the FMC instead of runway 27L and requested that the first officer change the runway in the FMC, which was completed at 1823:10.
- Coded CFIT (Controlled Flight Into or Toward Terrain) rather than RI: similar wording, different occurrence category.  `[report:CEN14FA110]`  
  > Flight locating procedures required that the pilot-in-command of a flight give the dispatcher or a responsible person within Royal Air Freight, Inc.
- Not 'Resolution advisory (RA)' — that definition is crosswalked to MAC, not RI.  `[definition:IND-10]`
- Not 'Loss of separation' — that definition is crosswalked to MAC, ATM, not RI.  `[definition:IND-23]`
- Events better described by CICTT MED (Medical) (runner-up parent, margin 0.36).  `[parent:MED]`

**Linked example reports**
- OPS10IA001: "The crew was subsequently re-assigned to runway 27L and at about the outer marker for that runway approach, the ATL tower local controller offered runway 27R, which the crew accepted."
- DCA18IA081: "Probable cause: the flight crew's misidentification of the taxiway as the landing runway due to the failure of the runway lighting that caused only the taxiway lights to be illuminated."
- DCA26LA242/2: "Delta Air Lines Flight 2351 (DAL2351) Flight Crew Statements Postincident statements provided by the DAL2351 flight crew revealed the first officer (FO) was the pilot flying and the captain was the pilot monitoring."
- DCA22LA126: "The first officer reported that when the flight exited the clouds, he could not see the runway but did visually acquire the TUL airport beacon and said it “looked like a normal downwind.” The captain reported that after exiting the clouds he could see the lights for runway 8/26 and that they were “normal.” The flight crew extended the centerline for runway 18L in their flight management system, which displayed the extended centerline on their ND in the cockpit."
- OPS09IA005/2: "The flight crew waited the required brake cooling time and then taxied to the approach end of runway 18L and completed the flight to EWN without further incident."
- OPS17IA008: "After pushback the ground controller provided the crew with taxi instructions to taxi via "Alpha, Foxtrot, cross 1 left, 1 right to 28 left." During the taxi, while on "Alpha" the controller modified their instructions and issued the crew instructions to taxi via "Alpha, Delta, Bravo, Foxtrot to 28L." The crew briefed the modified clearance to each other and proceeded to taxi via the new instructions."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 pass · G8 pass · G9 pass

### B28 · Wrong route or waypoint loaded in the FMS

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** The flight management system is loaded with the wrong route, waypoint or departure, and the aircraft deviates from its cleared route.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: The flight management system is loaded with the wrong route, waypoint or departure, and the aircraft deviates from its cleared route.  `[candidate:B28]`
- Matches 'Level bust (altitude deviation)' (EUROCONTROL – Level bust): An unauthorised vertical deviation of more than 300 feet from the cleared flight level or altitude, a common cause of loss of separation and TCAS resolution advisories.  `[definition:IND-11]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`
- Matches 'Resolution advisory (RA)' (ICAO Annex 10 – Airborne Collision Avoidance System (ACAS)): An ACAS or TCAS indication to the flight crew recommending a vertical manoeuvre to increase separation from conflicting traffic.  `[definition:IND-10]`

**Exclude when**
- Belongs to sibling B07 'Loss of separation caused by an ATC clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:OPS10IA574]`  
  > CDT, an air traffic control operational error resulted in a near-midair-collision between US Airways flight 1848 (AWE 1848), an Airbus 320, operating as a scheduled 14 Code of Federal Regulations (CFR) part 121 passenger flight en route to Philadelphia, Pennsylvania, carrying five crewmembers and 90 passengers, and Bemidji Aviation Services flight 46 (BMJ46), a Beech 99 cargo flight with only the pilot aboard, operating as a 14 CFR part 135 cargo flight en route to LaCrosse, Wisconsin.
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (1 report(s) assigned there).  `[report:ERA15MA259]`  
  > (The Shaw General Briefing Guide is a local USAF document that F-16 pilots use to prepare for their missions.) Before departure, squadron personnel briefed the pilot on a range of subjects, including parking location, maintenance issues, aircraft configuration, notices to airmen, weather, and the mission timeline.
- Belongs to sibling B12 'GNSS interference or spoofing' when it matches that bucket better (2 report(s) assigned there).  `[report:WPR15MA243/2]`  
  > At the same time, Eagle1's CVR recorded the pilot asking, "you still got the guy on the right side?" At 1102:42, the LC instructed the Eagle1 flight crew to turn base and cleared the flight to land on runway 26R.
- Distinguish from sibling B11 'Terrain warning on a non-precision approach' under the same parent.  `[sibling:B11]`
- Distinguish from sibling B20 'Pushback or towing collision' under the same parent.  `[sibling:B20]`
- Distinguish from sibling C8 'Takeoff after de-icing holdover time exceeded' under the same parent.  `[sibling:C8]`
- Coded ATM (ATM/CNS) rather than MAC: similar wording, different occurrence category.  `[report:OPS12IA849]`  
  > He did not immediately recognize that the local controller had misunderstood his direction because both aircraft were Republic Airlines flights, he heard her instruct a Republic flight to turn, and he was uncertain about the flight numbers of each aircraft.
- Coded LOC-I (Loss of Control – Inflight) rather than MAC: similar wording, different occurrence category.  `[report:WPR13FA072]`  
  > According to FAA air traffic control (ATC) information, the flight's first ATC contact was with Albuquerque air route traffic control center (designated ZAB) about 1812, when the airplane was at an altitude of about 13,500 feet; the pilot requested a clearance to PHX.
- Coded UIMC (Unintended Flight in IMC) rather than MAC: similar wording, different occurrence category.  `[report:CEN24MA111]`  
  > Finding: Aircraft-Aircraft systems-Indicating/recording systems-Data recorders (flight/maint)-Not installed/available.
- Not 'Lateral navigation error' — that definition is crosswalked to NAV, not MAC.  `[definition:IND-41]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.01).  `[parent:LOC-I]`

**Linked example reports**
- ERA12LA401: "Contributing factor: Aircraft-Aircraft systems-Flight control system-TE flap control system-Not used/operated."
- DCA17IA202: "The incident helicopter was the lead aircraft of a flight of two, and was operating as a local orientation flight for the Hudson Class B Airspace Exclusion and the United Nations General Assembly Temporary Flight Restriction (TFR) operations."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### C1 · Landing or takeoff on an unintended surface

*Merged into B02 before grounding.*

### C2 · Runway entry or crossing without clearance

*Merged into B01 before grounding.*

### C3 · Overrun after a long or fast landing on a wet or contaminated runway

*Merged into B04 before grounding.*

### C4 · Upset or stall after unreliable airspeed

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent LOC-I Loss of Control – Inflight*

**Definition.** Disagreeing or erroneous airspeed indications, for example from icing or pitot failure, lead to a stall warning, overspeed or upset in flight.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: Disagreeing or erroneous airspeed indications, for example from icing or pitot failure, lead to a stall warning, overspeed or upset in flight.  `[candidate:C4]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`
- Matches 'Stall prevention and recovery' (FAA Advisory Circular 120-109A – Stall Prevention and Recovery Training): Training to recognise and recover from approaches to stall and full stalls, including during go-arounds with high thrust and pitch.  `[definition:IND-21]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Narrative describes 'adequate' (5 of 9 supporting reports).  `[report:ERA22LA394]`  
  > Probable cause: The pilot’s failure to maintain an adequate airspeed, which resulted in an aerodynamic stall.

**Exclude when**
- Belongs to sibling B05 'Stall warning or upset during a go-around' when it matches that bucket better (1 report(s) assigned there).  `[report:WPR24FA083]`  
  > According to Section 57-41-00 of the repair manual, “WINGS LEADING EDGE AND LEADING EDGE DEVICES WING LEADING EDGE GENERAL REPAIR,” “In accordance with the Flight Manual procedures the airplane must be test flown by a pilot familiar with the stall identification system and stall characteristics of the 750, 800, 800XP, 850XP, and 900XP series if: (1) The leading edge assembly was removed as a whole for any reason (2) Two or more TKS [de-icing] wing distribution panels on one side are removed or installed” This section of the SRM also refers the operator of the Series 900XP airplane to Section V of the Pilot’s Operating Manual for the procedure and technique to complete the stall test.The manual requires that, before taking the test flight, the operator verify that the Stall Warning and Identification System is functioning properly while on the ground.
- Belongs to sibling B23 'Windshear on final approach' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN14FA046]`  
  > MU-2B Stall Training In addition to MU-2B ground training, pilots are flight trained in stall recognition and recovery in accordance with flight profiles contained in SFAR No.
- Belongs to sibling B26 'Unreliable airspeed from blocked pitot probes' when it matches that bucket better (1 report(s) assigned there).  `[report:DCA14FA058]`  
  > When either of the ice detectors detect ice, an advisory message "ICE CONDITION" is shown on the EICAS display, a signal would be sent to the anti-ice system valves to activate them to open, and a signal would be sent to the full authority digital engine control to activate the automated engine icing thrust setting logic to limit the thrust to a minimum acceptable level.
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than LOC-I: similar wording, different occurrence category.  `[report:WPR23FA034]`  
  > The airplane's maneuvers and speeds leading up to the minimum airspeed recorded at 1019:01 suggests the performance of an intentional stall in a 30° left roll with the engine power above idle (at about 930 ft-lb of torque), consistent with the stated intent of the flight and the items remaining on the flight test card for that flight (including a power-on stall in a 30° bank).
- Not 'In-flight airframe icing' — that definition is crosswalked to ICE, not LOC-I.  `[definition:IND-38]`
- Not 'Holdover time' — that definition is crosswalked to ICE, not LOC-I.  `[definition:IND-17]`
- Not 'In-flight engine shutdown (IFSD)' — that definition is crosswalked to SCF-PP, not LOC-I.  `[definition:IND-28]`
- Events better described by CICTT ICE (Icing) (runner-up parent, margin 0.37).  `[parent:ICE]`

**Linked example reports**
- WPR13FA072: "Sierra, Tango, and Zulu AIRMETs issued between 1345 and 1419, and valid for the flight and accident region for the period of the flight, warned of IFR conditions with ceilings below 1,000 feet, and visibility below 3 miles in precipitation and mist, mountains obscured by precipitation and clouds, moderate turbulence below 14,000 feet, and moderate icing between 7,000 feet and FL250."
- DCA16FA199: "(100% is the full-up collective position, and 0% is the full-down collective position.) Data recorded on the helicopter's flight test recorder system, which was typically downloaded after each test flight and also transmitted via a telemetry stream to Bell's flight-test facility for real-time analysis and recording, indicate the build-up tests and recovery time required (see table 1)."
- CEN10MA088: "I don't think that spoileron thing is working for some reason." Post-accident performance studies indicated that the airplane's N1 and true airspeed decreased, and bank angle increased to greater than 50 degrees."
- ERA22LA394: "Probable cause: The pilot’s failure to maintain an adequate airspeed, which resulted in an aerodynamic stall."
- WPR22LA362: "Probable cause: The pilot’s failure to maintain adequate airspeed during the landing approach, which resulted in an aerodynamic stall."
- ERA22LA305: "Probable cause: The pilot’s failure to maintain adequate airspeed during landing leading to an aerodynamic stall and subsequent impact with the ground."
- CEN22LA015: "Probable cause: The pilot’s failure to adequately monitor airspeed during a low-level turn, which resulted in an aerodynamic stall and impact with the water."
- ERA23LA371: "Probable cause: The pilot’s failure to maintain adequate airspeed during the banner pickup, which resulted in a low altitude aerodynamic stall/spin."
- WPR23LA168: "Probable cause: The pilot’s failure to maintain adequate airspeed on takeoff that resulted in an aerodynamic stall and subsequent impact with trees."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### C5 · TCAS resolution advisory after an altitude deviation

*Merged into B08 before grounding.*

### C6 · Clear-air turbulence with cabin injuries

*Taxonomy version ntsb-draft-dadb5659b8 · status grounded · parent TURB Turbulence Encounter*

**Definition.** An unexpected encounter with turbulence in clear air injures passengers or cabin crew who are standing, unbelted or near unsecured carts.

**Include when**
- The occurrence meets the CICTT TURB (Turbulence Encounter) definition.  `[parent:TURB]`
- Core definition: An unexpected encounter with turbulence in clear air injures passengers or cabin crew who are standing, unbelted or near unsecured carts.  `[candidate:C6]`
- Matches 'Turbulence-related injuries' (FAA Advisory Circular 120-88A – Preventing Injuries Caused by Turbulence): Passengers and flight attendants are injured in turbulence mainly when standing or not wearing seat belts, and by unsecured carts and galley equipment.  `[definition:IND-14]`
- Matches 'Clear-air turbulence (CAT)' (SKYbrary – Clear Air Turbulence): Turbulence in cloud-free air, often near jet streams or over mountains, with no visual cue and often not shown on weather radar.  `[definition:IND-13]`
- Matches 'Wake turbulence' (FAA Advisory Circular 90-23G – Aircraft Wake Turbulence): Vortices from a preceding aircraft, strongest behind heavy aircraft at slow speed, can cause sudden rolls on approach or departure; spacing reduces the risk.  `[definition:IND-22]`
- Narrative describes 'encounter' (12 of 12 supporting reports).  `[report:DCA23LA096]`  
  > At 1013:43, the flight crew made a passenger announcement about the turbulence encounter.
- Narrative describes 'turbulence' (12 of 12 supporting reports).  `[report:DCA23LA096]`  
  > At 1013:43, the flight crew made a passenger announcement about the turbulence encounter.
- Narrative describes 'air' (10 of 12 supporting reports).  `[report:DCA22LA196]`  
  > Probable cause: An encounter with clear air turbulence, which resulted in a serious injury as a flight attendant was lowering her jumpseat.

**Exclude when**
- Distinguish from sibling B06 'Wake turbulence upset on approach' under the same parent.  `[sibling:B06]`
- Not 'Unruly or disruptive passenger' — that definition is crosswalked to CABIN, not TURB.  `[definition:IND-30]`
- Not 'Lithium battery fire' — that definition is crosswalked to F-NI, CABIN, not TURB.  `[definition:IND-31]`
- Not 'Resolution advisory (RA)' — that definition is crosswalked to MAC, not TURB.  `[definition:IND-10]`
- Events better described by CICTT CABIN (Cabin Safety Events) (runner-up parent, margin 0.79).  `[parent:CABIN]`

**Linked example reports**
- DCA23LA096: "At 1013:43, the flight crew made a passenger announcement about the turbulence encounter."
- ERA09LA488: "Meteorological Conditions in Vicinity of Turbulence Encounter The 1600 NWS radar composite reflectivity mosaic image depicted several defined echoes associated with thunderstorms north of the departure airport, including a short but intense line at the latitude and longitude of the turbulence encounter, but below the airplane's altitude."
- DCA22LA196: "Probable cause: An encounter with clear air turbulence, which resulted in a serious injury as a flight attendant was lowering her jumpseat."
- DCA14CA014: "While cruising at FL360 in smooth air conditions with no storms in the vicinity, the airplane experienced a 3 to 5 second encounter with clear air turbulence."
- DCA26LA167: "Probable cause: An unanticipated encounter with clear air turbulence while in cruise flight."
- DCA19CA088: "Probable cause: the airplanes encounter with clear air turbulence."
- DCA25LA091: "Probable cause: An encounter with an area of clear air turbulence during cruise, which resulted in a serious injury to a flight attendant."
- DCA23LA008: "Probable cause: An encounter with clear air turbulence during cruise flight."
- DCA25LA156: "Probable cause: An encounter with an area of moderate clear air turbulence associated with the jet stream during cruise."
- DCA20CA043: "Probable cause: an encounter with clear air turbulence during cruise flight."
- DCA21LA209: "Probable cause: An encounter with clear air turbulence."
- DCA23LA411: "Probable cause: An encounter with clear air turbulence."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C7 · Engine damage or shutdown after bird ingestion

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent BIRD Bird*

**Definition.** Birds ingested into an engine cause vibration, surge, loss of thrust, fire warning or shutdown.

**Include when**
- The occurrence meets the CICTT BIRD (Bird) definition.  `[parent:BIRD]`
- Core definition: Birds ingested into an engine cause vibration, surge, loss of thrust, fire warning or shutdown.  `[candidate:C7]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Matches 'Damaging bird strike' (FAA National Wildlife Strike Database – strike reporting): A collision with birds that damages the aircraft, such as a cracked windshield, dented radome or ingested engine, reported to the wildlife strike database.  `[definition:IND-39]`
- Matches 'Wildlife strike' (FAA National Wildlife Strike Database): A collision between an aircraft and a bird or other wildlife, including ingestion into an engine, reported with damage and phase of flight.  `[definition:IND-15]`
- Narrative describes 'bird' (7 of 7 supporting reports).  `[report:CEN09MA117]`  
  > Probable cause: (1) the sudden loss of power to both engines that resulted from impact with a bird (red-tailed hawk), which fractured the windshield and interfered with engine fuel controls, and (2) the subsequent disorientation of the flight crewmembers, which left them unable to recover from the loss of power.
- Narrative describes 'ingestion' (3 of 7 supporting reports).  `[report:ENG11IA051]`  
  > ADDITIONAL INFORMATION Bird Ingestion Requirements The PW2037 was certified under Part 33, Amendment 6 and the bird ingestion requirement at that time in Part 33.77 Foreign Object Ingestion was for a 4-pound bird.

**Exclude when**
- Belongs to sibling B16 'Bird strike damaging the windshield or nose on approach' when it matches that bucket better (5 report(s) assigned there).  `[report:CEN25LA070]`  
  > Probable cause: Bird strike.
- Distinguish from sibling B15 'Bird ingestion damaging an engine on takeoff or climb' under the same parent.  `[sibling:B15]`
- Coded SCF-PP (System/Component Failure – Powerplant) rather than BIRD: similar wording, different occurrence category.  `[report:ERA17MA316]`  
  > A decision for this option requires the pilot to continuously monitor engine parameters N1 (gas generator speed), TOT (turbine outlet temperature), TRQ (engine torque), oil pressure and temperature, and be prepared for immediate engine shutdown.
- Coded LOC-I (Loss of Control – Inflight) rather than BIRD: similar wording, different occurrence category.  `[report:CEN14FA046]`  
  > Probable cause: The pilot's loss of airplane control during a known one-engine-inoperative condition.
- Coded F-NI (Fire/Smoke (Non-Impact)) rather than BIRD: similar wording, different occurrence category.  `[report:DCA18LA163]`  
  > Contributing to the duration of the fire was the contamination of an engine fire isolation system component which resulted in hydraulic fluid leaking into the designated engine fire zone after the engine was shutdown and the fire button was pressed.
- Not 'In-flight engine shutdown (IFSD)' — that definition is crosswalked to SCF-PP, not BIRD.  `[definition:IND-28]`
- Not 'Lithium battery fire' — that definition is crosswalked to F-NI, CABIN, not BIRD.  `[definition:IND-31]`
- Not 'Low-level windshear' — that definition is crosswalked to WSTRW, not BIRD.  `[definition:IND-36]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.27).  `[parent:SCF-PP]`

**Linked example reports**
- CEN09MA117: "Probable cause: (1) the sudden loss of power to both engines that resulted from impact with a bird (red-tailed hawk), which fractured the windshield and interfered with engine fuel controls, and (2) the subsequent disorientation of the flight crewmembers, which left them unable to recover from the loss of power."
- ENG11IA051: "ADDITIONAL INFORMATION Bird Ingestion Requirements The PW2037 was certified under Part 33, Amendment 6 and the bird ingestion requirement at that time in Part 33.77 Foreign Object Ingestion was for a 4-pound bird."
- DCA24LA330: "DAMAGE TO AIRCRAFTPostincident examination of the airplane found damage to the left engine fan blades consistent with a bird ingestion (see figure 3)."
- CEN09IA481: "The requirements stated the engine is acceptable if it ingested the bird and “demonstrated freedom from explosion, disintegration, or uncontrollable fire.” AC-33-1B further stated that it would be acceptable if the engine required shutdown."
- CEN10CA202: "All observed damage was consistent with the airplane colliding with a bird while in flight."
- ENG14IA005: "The engine and airplane met the applicable bird and containment design standards since the engine did not catch on fire, no engine cases exhibited any penetrations, the engine was able to be shutdown normally, and the airplane damage did not impact the safe operation of the airplane or create a hazard to the persons on board."
- ENG22LA002: "Probable cause: The ingestion of a bird into the right engine during the takeoff roll caused a fan blade to fracture near the blade platform resulting in high fan blade off loads and engine vibrations sufficient to result in an eventual failure of a fuel tube in the right engine that sprayed fuel onto hot engine cases, igniting an undercowl engine fire and triggering a rejected takeoff."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 pass · G8 FAIL · G9 pass

### C8 · Takeoff after de-icing holdover time exceeded

*Taxonomy version ntsb-draft-dadb5659b8 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** The aircraft is delayed after ground de-icing and the fluid holdover time is exceeded before takeoff.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: The aircraft is delayed after ground de-icing and the fluid holdover time is exceeded before takeoff.  `[candidate:C8]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`
- Matches 'Loss of separation' (ICAO Doc 4444 – PANS-ATM (separation minima)): Two aircraft come closer than the prescribed separation minima, often after an ATC clearance or instruction puts them in conflict.  `[definition:IND-23]`

**Exclude when**
- Belongs to sibling B07 'Loss of separation caused by an ATC clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:OPS10IA574]`  
  > At that time the ground control positions were combined at Ground Control South.
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (1 report(s) assigned there).  `[report:ERA15MA259]`  
  > At that time, the Cessna reported an altitude of 1,400 ft and was established on an approximate ground track of 110º.
- Belongs to sibling B12 'GNSS interference or spoofing' when it matches that bucket better (2 report(s) assigned there).  `[report:WPR15MA243/2]`  
  > At 1100:23, the LC instructed, "stationair five eight uniform two six right cleared for I'm sorry two six left cleared for takeoff." At 1100:29, the pilot of N5058U stated, "uh I'm sorry was that for five eight uniform?" The LC then cleared the pilot of N5058U for takeoff from runway 26L.
- Belongs to sibling B28 'Wrong route or waypoint loaded in the FMS' when it matches that bucket better (1 report(s) assigned there).  `[report:DCA17IA202]`  
  > He had registered with the FAA as a model aircraft operator during the time period that the registration requirement was in effect.
- Distinguish from sibling B11 'Terrain warning on a non-precision approach' under the same parent.  `[sibling:B11]`
- Distinguish from sibling B20 'Pushback or towing collision' under the same parent.  `[sibling:B20]`
- Coded ARC (Abnormal Runway Contact) rather than MAC: similar wording, different occurrence category.  `[report:DCA14MA081]`  
  > She could not remember if she uplinked the takeoff data or manually entered the V-speeds and FLEX (a reduced takeoff thrust setting) temperature information into the multipurpose control display unit (MCDU).
- Coded ICE (Icing) rather than MAC: similar wording, different occurrence category.  `[report:WPR23FA080]`  
  > While deicing removes ice, anti-icing protects against additional icing for a certain period of time, called holdover time.
- Coded LOC-I (Loss of Control – Inflight) rather than MAC: similar wording, different occurrence category.  `[report:WPR12FA089]`  
  > Comparing the times of the pilot's radio transmissions (as recorded in the ATC transcript) to the times of events recorded in the EFIS data revealed that the ATC transcript time lags the EFIS time by about 23 seconds.
- Not 'Holdover time' — that definition is crosswalked to ICE, not MAC.  `[definition:IND-17]`
- Not 'Runway incursion' — that definition is crosswalked to RI, not MAC.  `[definition:IND-01]`
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not MAC.  `[definition:IND-04]`
- Events better described by CICTT ICE (Icing) (runner-up parent, margin 0.03).  `[parent:ICE]`

**Linked example reports**
- none

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 FAIL · G8 FAIL · G9 FAIL

### C9 · Hard landing or tail strike

*Taxonomy version ntsb-draft-dadb5659b8 · status needs review · parent ARC Abnormal Runway Contact*

**Definition.** A hard or bounced touchdown, or contact of the tail with the runway during rotation or flare.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: A hard or bounced touchdown, or contact of the tail with the runway during rotation or flare.  `[candidate:C9]`
- Matches 'Hard landing, tail strike' (SKYbrary – Hard Landing and Tail Strike): A touchdown with a vertical load above limits, a bounced landing, or contact of the tail with the runway during takeoff rotation or landing flare.  `[definition:IND-18]`
- Matches 'Tail strike' (SKYbrary – Tailstrike): The aft fuselage contacts the runway during takeoff rotation or landing, often after early rotation, wrong takeoff speeds or excessive pitch.  `[definition:IND-35]`
- Narrative describes 'bounced' (8 of 12 supporting reports).  `[report:CEN10CA336]`  
  > On the third landing the airplane landed hard and bounced, so the pilot performed a go-around.
- Narrative describes 'flare' (7 of 12 supporting reports).  `[report:ANC08CA054]`  
  > Probable cause: The pilot's misjudged flare and subsequent hard landing, and her inadequate recovery from a bounced landing.

**Exclude when**
- Distinguish from sibling B10 'Landing gear did not extend' under the same parent.  `[sibling:B10]`
- Coded RE (Runway Excursion) rather than ARC: similar wording, different occurrence category.  `[report:DCA19MA143]`  
  > Touchdown occurred at 2141:43.1, about 20 ft right of centerline, 1,580 ft past the displaced threshold and 394 ft beyond the runway’s short field arresting gear; according to the FCOM, the target touchdown point is 1,000 ft from the threshold and “should occur within -250 ft to +500 ft of the target touchdown point).
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not ARC.  `[definition:IND-03]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not ARC.  `[definition:IND-07]`
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not ARC.  `[definition:IND-04]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.59).  `[parent:RE]`

**Linked example reports**
- CEN10CA336: "On the third landing the airplane landed hard and bounced, so the pilot performed a go-around."
- CEN11CA018: "During touchdown the airplane impacted the runway hard and bounced back into the air before settling back on the runway."
- ANC08CA054: "Probable cause: The pilot's misjudged flare and subsequent hard landing, and her inadequate recovery from a bounced landing."
- CEN11CA497: "Probable cause: The pilot's improper flare which resulted in a hard landing."
- ERA11CA147: "The airplane impacted the runway hard and bounced."
- ERA19FA248: "In retrospect, he felt the initial touchdown was too hard, possibly from an inadequate landing flare between final approach and touchdown, which would have slowed the descent rate and created a softer touchdown."
- CEN20CA241: "Probable cause: The pilot's improper flare, which resulted in a hard, bounced landing."
- CEN26LA200: "Probable cause: The pilot’s improper engine power application during the landing flare, which resulted in a hard, bounced landing and nose over."
- CEN22LA379: "Probable cause: The pilot’s inadequate landing flare, which resulted in a hard, bounced landing."
- CEN13CA090: "He added that the airplane landed hard on the nose wheel, the airplane bounced, and then settled onto the runway."
- SEA08CA125: "Probable cause: The pilot's misjudged landing flare, which resulted in a hard landing."
- ERA21LA390: "Probable cause: The buckling of the tail boom as a result of a hard landing event of undetermined time and location."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass
