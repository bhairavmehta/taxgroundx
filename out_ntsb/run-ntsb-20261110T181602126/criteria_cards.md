# Criteria cards · taxonomy ntsb-draft-c94008cd21

Run run-ntsb-20261110T181602126 · selector rules · embedder local-lsa-128 · reports are synthetic.

### B01 · Vehicle or pedestrian on the runway without clearance

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent RI Runway Incursion*

**Definition.** A ground vehicle, tug or person enters an active runway or its protected area without an ATC clearance.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: A ground vehicle, tug or person enters an active runway or its protected area without an ATC clearance.  `[candidate:B01]`
- Matches 'Pilot deviation (runway incursion)' (FAA Runway Safety programme – Pilot deviation): A runway incursion caused by a pilot, such as crossing a hold-short line or entering a runway without an ATC clearance.  `[definition:IND-40]`
- Matches 'Vehicle or pedestrian deviation' (FAA Runway Safety programme): A runway incursion caused by a ground vehicle or a person, such as a driver or pedestrian entering a runway without ATC authorization.  `[definition:IND-19]`
- Matches 'Anomaly: Ground Incursion – Runway or Taxiway' (NASA ASRS coding taxonomy): An aircraft, vehicle or person entering a runway or taxiway without authorization, or an aircraft using a taxiway or the wrong runway for landing or takeoff.  `[definition:IND-04]`

**Exclude when**
- Belongs to sibling B02 'Landing on a taxiway or the wrong runway at night' when it matches that bucket better (1 report(s) assigned there).  `[report:DCA23LA133/2]`  
  > (As previously stated, the airplane was precluded by company procedures from landing on runway 4R and holding short of runway 8L.) The UAL384 airplane subsequently crossed runway 4L without stopping at the hold-short line on taxiway K.
- Belongs to sibling B27 'Crew crossed a hold-short line without clearance' when it matches that bucket better (1 report(s) assigned there).  `[report:OPS09IA009/2]`  
  > Probable cause: The local controller did not visually scan the runways and ensure that the E145 had crossed runway 24L prior to issuing a takeoff clearance to the DH8, did not ensure separation between the two airplanes, and did not cancel takeoff clearance for the DH8 in a timely manner.
- Belongs to sibling C1 'Landing or takeoff on an unintended surface' when it matches that bucket better (3 report(s) assigned there).  `[report:OPS09IA007]`  
  > The traditional taxi route for aircraft departing runway 6L was the ground controller directed aircraft to taxi via taxiway L, to taxiway N and then the local controller directed across runway 6R on taxiway N to a left turn on taxiway G to the approach end of runway 6L.
- Coded ADRM (Aerodrome) rather than RI: similar wording, different occurrence category.  `[report:OPS16IA008/2]`  
  > As AAL2408 began its takeoff roll the Runway Status Lights (RWSLs) on runway 35L activated illuminating the Runway Entrance Lights (RELs) at the hold short locations of the three aircraft that had just been instructed to cross runway 35L, as well as the Takeoff Hold Lights (THLs) at the approach end of the runway.
- Coded ATM (ATM/CNS) rather than RI: similar wording, different occurrence category.  `[report:OPS11IA673]`  
  > The ERJ145 taxied from the passenger terminal located to the west of runway 18/36 and east of runway 14/32 and was not required to cross any runways en route to the approach end of runway 14.
- Coded GCOL (Ground Collision) rather than RI: similar wording, different occurrence category.  `[report:WPR18LA118]`  
  > Both the student and instructor onboard the PA-12 stated that the tower controller issued a clearance to cross runway 12 while they were still holding short of runway 11.
- Not 'Clearance - wrong aircraft' — that definition is crosswalked to ATM, not RI.  `[definition:ECC-4010704]`
- Not 'Clearance - wrong heading' — that definition is crosswalked to ATM, not RI.  `[definition:ECC-4010702]`
- Not 'Clearance - wrong speed' — that definition is crosswalked to ATM, not RI.  `[definition:ECC-4010703]`
- Events better described by CICTT GCOL (Ground Collision) (runner-up parent, margin 0.41).  `[parent:GCOL]`

**Linked example reports**
- OPS09IA004: "HISTORY OF FLIGHT The Andrews Air Force Base (ADW) ground controller, working the ground control (GC), clearance delivery (CD), and flight data (FD) positions combined, authorized four vehicles to cross runway 19R without the local controller’s approval (LC) while VM206, a BE-20, was departing runway 19R."
- OPS16IA008: "As AAL2408 began its takeoff roll the Runway Status Lights (RWSLs) on runway 35L activated illuminating the Runway Entrance Lights (RELs) at the hold short locations of the three aircraft that had just been instructed to cross runway 35L, as well as the Takeoff Hold Lights (THLs) at the approach end of the runway."
- NYC08FA265: "Upon receipt of any clearance from ATC to cross a runway or taxiway, vehicle operators shall look both ways to ensure it is safe to cross.” On January 25, 2010, suggestions were provided to the FAA via the AAI-100 (Office of Accident Investigation) party representative to the investigation, to: 1) Revise both the FAA’s “Airport Ground Vehicle Operations, An FAA Guide” and FAA AC150/5210-20 publications to include ground vehicle operators’ requirement to visually confirm that an active runway was clear prior to crossing, even with ATCT clearance, 2) Review airport ACMs and airport-ATCT Letters of Agreement to ensure that appropriate language is included for vehicle operators’ runway vigilance, even with ATCT clearance, and 3) That FAA ensure that the increased vehicle operators’ vigilance requirements be incorporated into local airport ground vehicle training programs."
- DCA22LA126: "The captain stated during a post incident interview, that he applied the brakes and “came on them harder initially because he was confused.” After slowing the airplane, the captain asked the FO “are we on the correct runway?” and then stated, “we landed on the right [hand] runway.” After informing the controller that they had landed on runway 18R, the controller provided taxi instructions to the ramp."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### B02 · Landing on a taxiway or the wrong runway at night

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent RI Runway Incursion*

**Definition.** At night or in low light the crew lines up on and lands, or nearly lands, on a taxiway or a runway other than the one assigned.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: At night or in low light the crew lines up on and lands, or nearly lands, on a taxiway or a runway other than the one assigned.  `[candidate:B02]`
- Matches 'Wrong-surface event' (FAA Runway Safety programme): A landing, attempted landing, line-up or takeoff on a surface other than the one assigned: a wrong runway, a taxiway, a closed runway or the wrong airport.  `[definition:IND-03]`
- Matches 'Anomaly: Ground Incursion – Runway or Taxiway' (NASA ASRS coding taxonomy): An aircraft, vehicle or person entering a runway or taxiway without authorization, or an aircraft using a taxiway or the wrong runway for landing or takeoff.  `[definition:IND-04]`
- Matches 'Pilot deviation (runway incursion)' (FAA Runway Safety programme – Pilot deviation): A runway incursion caused by a pilot, such as crossing a hold-short line or entering a runway without an ATC clearance.  `[definition:IND-40]`

**Exclude when**
- Belongs to sibling B27 'Crew crossed a hold-short line without clearance' when it matches that bucket better (1 report(s) assigned there).  `[report:DCA24LA219]`  
  > The flight crew did not observe any equipment, markings, visual closed runway lighted “Xs” designations, or any other sign indicating that the runway was closed, and all equipment and people were clear of the runway.
- Belongs to sibling C1 'Landing or takeoff on an unintended surface' when it matches that bucket better (3 report(s) assigned there).  `[report:OPS09IA007]`  
  > The traditional taxi route for aircraft departing runway 6L was the ground controller directed aircraft to taxi via taxiway L, to taxiway N and then the local controller directed across runway 6R on taxiway N to a left turn on taxiway G to the approach end of runway 6L.
- Distinguish from sibling B01 'Vehicle or pedestrian on the runway without clearance' under the same parent.  `[sibling:B01]`
- Coded ADRM (Aerodrome) rather than RI: similar wording, different occurrence category.  `[report:OPS08IA007/2]`  
  > At the time of the incident, the taxiway F enhanced hold short line had both in-pavement and elevated runway guard lights, as well as taxiway centerline lights, which were operating on step one, the lowest setting.
- Coded ATM (ATM/CNS) rather than RI: similar wording, different occurrence category.  `[report:OPS25LA005/2]`  
  > The LC1 controller cleared N895AM to land on runway 30 and instructed the crew to hold short of runway 26 right for traffic.
- Not 'Undershoot' — that definition is crosswalked to USOS, not RI.  `[definition:ECC-2010800]`
- Not 'Aircraft collision with approach/runway/taxiway lights' — that definition is crosswalked to GCOL, not RI.  `[definition:ECC-2050403]`
- Events better described by CICTT ADRM (Aerodrome) (runner-up parent, margin 0.37).  `[parent:ADRM]`

**Linked example reports**
- DCA26MA161: "At 2336:51, the red runway entrance lights (RELs, discussed later) illuminated for the intersection of runway 4 and taxiway D."
- DCA18IA081: "Probable cause: the flight crew's misidentification of the taxiway as the landing runway due to the failure of the runway lighting that caused only the taxiway lights to be illuminated."
- OPS10IA001: "Contributing to the cause of the incident were (1) the flight crew’s decision to accept a late runway change, (2) the unavailability of the approach light system and the instrument landing system for the runway of intended landing, and (3) the combination of numerous taxiway signs and intermixing of light technologies on the taxiway."
- DCA23LA133/2: "Additionally, in case they were given runway 4R, they briefed the anticipated taxi plan which included possibly exiting at taxiway “K” or exiting at the end of the runway on taxiway “C.” Furthermore, in her postincident statement, the first officer indicated that she briefed the published hot spot, referred to as HS2, (see figure 2) located at taxiway “K” in case they were given runway 4R for landing."
- CEN21LA136: "Both pilots reported that the only runway lights that they saw during the approach were the lights on runway 32, and there were no visible indications that the runway they approached was closed."
- OPS17IA003: "HISTORY OF FLIGHTOn October 21, 2016, at about 0822 eastern daylight time, a runway incursion occurred at the Westfield-Barnes Regional Airport (BAF), Westfield/Springfield, Massachusetts, when a Douglas DC-9-83, registration N425NV, operating as Allegiant Air Flight 4203 (AAY4203) landed on runway 20 while Guard Sweeper 96 was conducting runway sweeping operations on the last 4000 feet of the same runway."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### B03 · Veer-off during landing in a strong or gusty crosswind

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent LOC-G Loss of Control – Ground*

**Definition.** In a strong or gusty crosswind the aircraft drifts and veers off the side of the runway during the landing roll.

**Include when**
- The occurrence meets the CICTT LOC-G (Loss of Control – Ground) definition.  `[parent:LOC-G]`
- Core definition: In a strong or gusty crosswind the aircraft drifts and veers off the side of the runway during the landing roll.  `[candidate:B03]`
- Matches 'Intentional ground loop/swerve' (ECCAIRS 1.3.0.12 · Events (390) · 2010501 · Aircraft operation general › Aircraft handling › Swerve-take-off/landing): An event involving an intentional ground loop or swerve of the aircraft on take-off or landing, e.g. to avoid obstacles in the runway overrun area.  `[definition:ECC-2010501]`
- Matches 'Ground loop/swerve on take-off or landing' (ECCAIRS 1.3.0.12 · Events (390) · 2010500 · Aircraft operation general › Aircraft handling): An event involving a ground loop/swerve of the aircraft on take-off or landing.  `[definition:ECC-2010500]`
- Matches 'Helicopter damage caused by ground resonance' (ECCAIRS 1.3.0.12 · Events (390) · 2060300 · Aircraft operation general › Damage to aircraft): An event involving ground resonance damage to the helicopter. Aircraft damage caused by lightning strike (Lightning strike damage)                                                   2060400   * An event involving lightning strike damage to the aircraft. Moved to weather encounters  `[definition:ECC-2060300]`
- Narrative describes 'directional' (5 of 12 supporting reports).  `[report:WPR10CA296]`  
  > Probable cause: The pilot's inadequate compensation for the crosswind condition and failure to maintain directional control during the landing roll in gusty crosswind conditions.

**Exclude when**
- Coded RE (Runway Excursion) rather than LOC-G: similar wording, different occurrence category.  `[report:ERA11LA390]`  
  > It was marked with nonprecision markings that were in good condition Usable length for landing on runway 24 was 3,471 feet due to a displaced threshold on the end of runway 06, marked as a taxiway aligned with a runway, and a chevroned runway safety area on the end of runway 24.
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than LOC-G: similar wording, different occurrence category.  `[report:ERA25LA090]`  
  > Probable cause: A landing gear collapse during landing in gusty crosswind conditions.
- Coded TURB (Turbulence Encounter) rather than LOC-G: similar wording, different occurrence category.  `[report:WPR24LA085]`  
  > This AC stated that, when landing behind a larger aircraft on a parallel runway closer than 2,500 feet apart, pilots need to consider the relationship between the runway threshold locations, the relative glideslope descent paths/locations and possible vortex drift onto your runway.
- Not 'Crosswind landing' — that definition is crosswalked to RE, not LOC-G.  `[definition:IND-20]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not LOC-G.  `[definition:IND-07]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not LOC-G.  `[definition:ECC-2180101]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.02).  `[parent:RE]`

**Linked example reports**
- GAA16CA476: "The pilot of a tailwheel-equipped airplane reported that during the landing roll in gusty crosswind conditions, the airplane abruptly veered to the left because his right foot had rolled off the right rudder pedal."
- WPR10CA296: "Probable cause: The pilot's inadequate compensation for the crosswind condition and failure to maintain directional control during the landing roll in gusty crosswind conditions."
- ANC09LA104: "In addition, a subheading titled “Slippery Runways,” in the Crosswind Landing section of the Operations Manual, recommends, in part, that the operators adjust the crosswind limit, reducing it by 25 to 75 percent, depending on slippery conditions."
- GAA16CA184: "The pilot reported that he was landing in gusty crosswind conditions following a parachute jump flight, and that the gusty conditions had persisted for the previous 10 skydiving flights that day."
- GAA16CA402: "The pilot reported that during the landing in gusty crosswind conditions, the airplane touched down "firm" with the landing gear side loaded."
- GAA17CA043: "Probable cause: The pilot's failure to maintain directional control during the landing roll in gusty crosswind conditions, which resulted in a runway excursion."
- GAA16CA183: "This handbook discusses operations in crosswind conditions and states in part: Takeoffs and landings in certain crosswind conditions are inadvisable or even dangerous."
- WPR25LA038: "The manual stated that, in strong crosswinds, landing with reduced flaps is recommended to reduce the crosswind component (as a percentage of airspeed) at touchdown."
- ERA13CA141: "Probable cause: The pilot's decision to land in gusty crosswind conditions, which resulted in a loss of airplane directional control during the landing roll."
- GAA16CA249: "Probable cause: The pilot's failure to maintain directional control during the landing roll in gusty crosswind conditions, which resulted in a runway excursion and nose over."
- ERA26LA099: "Probable cause: The pilot’s failure to compensate for gusty crosswind conditions during the landing roll, which resulted in a loss of control and subsequent runway excursion."
- CEN18CA176: "The pilot stated that upon landing, the aircraft encountered a strong gusty crosswind and he lost directional control."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 FAIL · G8 FAIL · G9 pass

### B04 · Overrun on a contaminated runway

*Taxonomy version ntsb-draft-c94008cd21 · status grounded · parent RE Runway Excursion*

**Definition.** On a wet, slushy, snowy or icy runway braking is poor and the aircraft overruns the end of the runway.

**Include when**
- The occurrence meets the CICTT RE (Runway Excursion) definition.  `[parent:RE]`
- Core definition: On a wet, slushy, snowy or icy runway braking is poor and the aircraft overruns the end of the runway.  `[candidate:B04]`
- Matches 'The aircraft ran off the end of the runway' (ECCAIRS 1.3.0.12 · Events (390) · 2070400 · Aircraft operation general › Aircraft off movement area): The aircraft ran off the end of the runway.  `[definition:ECC-2070400]`
- Matches 'Runway excursion (veer-off and overrun)' (SKYbrary – Runway Excursion): An aircraft leaves the runway surface during takeoff or landing, either by veering off the side or by overrunning the end.  `[definition:IND-05]`
- Matches 'Runway condition code (RWYCC)' (ICAO Global Reporting Format (GRF) for runway surface conditions): A runway condition code from 6 (dry) down to 0 reports braking performance on wet or contaminated runways (water, slush, snow, ice), so crews can recompute landing distance.  `[definition:IND-06]`
- Narrative describes 'runway' (12 of 12 supporting reports).  `[report:ERA12FA056]`  
  > There was concern, and a lack of data, for an EMAS at the departure end of runway 27 (approach end of runway 9).
- Narrative describes 'landing' (8 of 12 supporting reports).  `[report:ERA22LA150]`  
  > The performance calculations also indicated that even with the longer-than-nominal touchdown point and 3-knot fast touchdown airspeed, the accident airplane might have stopped before the end of the runway had it achieved the wet runway wheel braking friction coefficient implied by the airframe manufacturer’s AFM recommendation to increase dry runway landing distance by 30%.
- Narrative describes 'wet' (7 of 12 supporting reports).  `[report:ERA22LA150]`  
  > The performance calculations also indicated that even with the longer-than-nominal touchdown point and 3-knot fast touchdown airspeed, the accident airplane might have stopped before the end of the runway had it achieved the wet runway wheel braking friction coefficient implied by the airframe manufacturer’s AFM recommendation to increase dry runway landing distance by 30%.

**Exclude when**
- Distinguish from sibling B22 'Tail strike on takeoff' under the same parent.  `[sibling:B22]`
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not RE.  `[definition:IND-04]`
- Not 'Undershoot' — that definition is crosswalked to USOS, not RE.  `[definition:ECC-2010800]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not RE.  `[definition:ECC-2180101]`
- Events better described by CICTT SCF-NP (System/Component Failure – Non-Powerplant) (runner-up parent, margin 0.66).  `[parent:SCF-NP]`

**Linked example reports**
- ERA12FA056: "There was concern, and a lack of data, for an EMAS at the departure end of runway 27 (approach end of runway 9)."
- ERA22LA150: "The performance calculations also indicated that even with the longer-than-nominal touchdown point and 3-knot fast touchdown airspeed, the accident airplane might have stopped before the end of the runway had it achieved the wet runway wheel braking friction coefficient implied by the airframe manufacturer’s AFM recommendation to increase dry runway landing distance by 30%."
- CEN14FA505: "The pilots calculated the runway length required for a wet runway landing and then chose to land on runway 1, which was the longer runway."
- CEN09LA100: "Using the supplement, the anticipated landing distance on a wet runway was calculated to be about 3,400 feet, the anticipated landing distance on an uncontaminated runway was calculated to be approximately 2,800 feet, and the prescribed landing speed (Vref) was determined to be about 111 knots."
- ERA13IA294: "The PIC was noted as alarmed and applying maximum braking pressure and attempted to steer the aircraft to the right towards the taxiway at the end of the runway, but then straighten the aircraft out just prior to the end of the runway." DAMAGE TO THE AIRPLANE According to an FAA inspector, the airplane came to rest about 40 feet from the end of the paved portion of the runway."
- WPR11IA055: "" Subpart G states in part "...No correlation has been established between MU values and the descriptive terms "good," "fair," "poor," and "nil" used in braking action reports." Review of the company Flight Operations Manual (FOM) revealed that in section 2.4.10, Additional Requirements – Takeoff and/or Landing Operations, part 2, subpart B, states in part "… if current weather or runway surface conditions, the aircraft's status, or any other relevant factor, has worsened significantly from that used in landing distance planning (for release), and the worsened condition(s) would have a significant negative impact on the 'Actual Landing Distance' ...the Flightcrew shall calculate the 'Actual Landing Distance' for the current existing conditions, using AFM data."
- ERA23FA235: "If landing on a wet runway, it is recommended to increase the predicted landing field length by 30%.” The landing distances published in the AFM were based on several assumptions about touchdown speed and location."
- ERA09LA339: "The captain estimated the airplane touched down about halfway down the 4,677-foot-long runway, and she immediately applied "max reverse" thrust, and "more than average braking." The airplane initially began to slow, and then "started hydroplaning" on the wet runway."
- CEN15LA057: "Contributing to the pilot's decision to engage the emergency parking brake was the expectation of a faster rate of deceleration and considerably shorter wet runway landing distance provided by the airplane flight manual than that experienced by the crew upon touchdown and an actual wet runway friction level lower than the assumed runway fiction level used in the calculation of the stopping distances published in the airplane flight manual."
- CEN12CA355: "During the second landing attempt, the pilot touched the airplane down on the main landing gear about the mid-point of the runway, held the nose wheel up, and applied gentle braking."
- WPR25LA124: "The definition contained in the supplement for “wet runway” is then “water depth on the runway is less than 0.125 inch.” The VREF and landing distance required were calculated from the AFMS based on the temperature of 11°C, the self-reported weight of 9,000 lbs, a “wet” runway, negligible tail/head wind, a runway slope gradient of 0.05%, and an airport altitude of 16 ft."
- WPR16LA061: "1O3 features two runways, runway 8/26, a 3,735 foot-long and 42-foot wide asphalt runway, and runway 12/30, a 2,073-foot long and 26-foot wide asphalt runway."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B05 · Stall warning or upset during a go-around

*Taxonomy version ntsb-draft-c94008cd21 · status grounded · parent LOC-I Loss of Control – Inflight*

**Definition.** During a go-around or missed approach the aircraft pitches up with high thrust, energy is mismanaged, and a stall warning or upset follows.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: During a go-around or missed approach the aircraft pitches up with high thrust, energy is mismanaged, and a stall warning or upset follows.  `[candidate:B05]`
- Matches 'Stall prevention and recovery' (FAA Advisory Circular 120-109A – Stall Prevention and Recovery Training): Training to recognise and recover from approaches to stall and full stalls, including during go-arounds with high thrust and pitch.  `[definition:IND-21]`
- Matches 'Stall warning triggered' (ECCAIRS 1.3.0.12 · Events (390) · 2260500 · Aircraft operation general › Warning system triggered): Stall warning triggered  `[definition:ECC-2260500]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Narrative describes 'stall' (9 of 12 supporting reports).  `[report:ERA24FA001]`  
  > The airplane’s stall warning system sustained impact-related damage that precluded any postaccident functional testing.
- Narrative describes 'warning' (6 of 12 supporting reports).  `[report:ERA24FA001]`  
  > The airplane’s stall warning system sustained impact-related damage that precluded any postaccident functional testing.

**Exclude when**
- Distinguish from sibling B23 'Windshear on final approach' under the same parent.  `[sibling:B23]`
- Distinguish from sibling B24 'Landing short of the runway' under the same parent.  `[sibling:B24]`
- Distinguish from sibling B28 'Wrong route or waypoint loaded in the FMS' under the same parent.  `[sibling:B28]`
- Not 'Aircraft encountered vortex/wake turbulence' — that definition is crosswalked to TURB, not LOC-I.  `[definition:ECC-2220400]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not LOC-I.  `[definition:ECC-2180101]`
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not LOC-I.  `[definition:IND-22]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.54).  `[parent:SCF-PP]`

**Linked example reports**
- ERA24FA001: "The airplane’s stall warning system sustained impact-related damage that precluded any postaccident functional testing."
- NYC08MA090: "HISTORY OF FLIGHT On February 1, 2008, about 1128 eastern standard time, a Raytheon Aircraft Company C90A, N57WR, was substantially damaged when it impacted terrain during a missed approach following an instrument approach to the Mount Airy/Surry County Airport (MWK), Mount Airy, North Carolina."
- DCA08FA075: "If recovery action is not promptly initiated, a substantial loss of altitude may result… The Boeing MD-10 Flight Crew Operations Manual (FCOM) section titled Recovery from Approach to Stall reads in part: At first indication of approach to stall, simultaneously apply maximum available thrust, level wings and adjust pitch as required to minimize altitude loss."
- WPR22FA235: "This means that an aircraft with a normal unaccelerated stalling speed of 50 knots can be stalled at 100 knots by inducing a load factor of 4 Gs… A pilot should be aware of the following: • The danger of inadvertently stalling the aircraft by increasing the load factor, as in a steep turn or spiral; • When intentionally stalling an aircraft above its design maneuvering speed, a tremendous load factor is imposed …an aircraft greater than 72° in a steep turn produces a load factor of 3, and the stalling speed is increased significantly."
- ERA14FA417: "AIRCRAFT INFORMATIONThe accident aircraft was a four-place, strut braced, high wing airplane of conventional metal construction."
- WPR22FA196: "Finding: Aircraft-Aircraft oper/perf/capability-Performance/control parameters-Airspeed-Not attained/maintained."
- ERA17FA223: "Certification standards permit manufacturers to provide the required stall warning either through the inherent aerodynamic qualities of the airplane or through a stall warning device that gives a clear indication of the impending stall."
- ERA22FA004: "According to the operations manual, the stall warning system was designed to inform the pilot of a forthcoming stall by sounding an aural warning."
- CEN14FA046: "Pilots must perform approaches to stalls in takeoff, clean, and landing configurations with at least one approach-to-stall maneuver flown while in a 15-30 degree bank turn."
- WPR24FA083: "The POM also warned that there is no natural stall warning or aerodynamic buffet before the stall."
- CEN16FA214: "The airplane was also equipped with an electro-pneumatic stall warning system that provided audible warning of an approach to an aerodynamic stall."
- WPR21FA286: "According to the CVR data, the stick shaker engaged at 1318:04, then the captain asked, “What are you doing,” which was followed by a stall warning sound."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B06 · Wake turbulence upset on approach

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent TURB Turbulence Encounter*

**Definition.** Wake vortices from a preceding heavier aircraft cause a sudden roll or pitch upset on approach or departure.

**Include when**
- The occurrence meets the CICTT TURB (Turbulence Encounter) definition.  `[parent:TURB]`
- Core definition: Wake vortices from a preceding heavier aircraft cause a sudden roll or pitch upset on approach or departure.  `[candidate:B06]`
- Matches 'Wake turbulence' (FAA Advisory Circular 90-23G – Aircraft Wake Turbulence): Vortices from a preceding aircraft, strongest behind heavy aircraft at slow speed, can cause sudden rolls on approach or departure; spacing reduces the risk.  `[definition:IND-22]`
- Matches 'Aircraft encountered vortex/wake turbulence' (ECCAIRS 1.3.0.12 · Events (390) · 2220400 · Aircraft operation general › Weather encounters): Wake turbulence: Turbulent air behind an aircraft caused by any of the following: (a) wing-tip vortices; (b) rotor-tip vortices; (c) jet-engine thrust stream or jet blast; (d) rotor downwash; (e) prop wash. Wing tip vortex: A circular pattern of air current created by the movement of an airfoil through the air when the airfoil is generating lift. As an airfoil moves through the atmosphere in sustained flight, an area of high pressure is created beneath it and an area of low pressure is created above it. The air flowing from the high-pressure area to the low-pressure area around and about the tips of the airfoil tends to roll up into two rapidly rotating vortices, cylindrical in shape. These vortices are the predominant parts of aircraft wake turbulence and their rotational force is dependent upon the wing loading, gross weight, and speed of the generating aircraft. The vortices from medium to heavy aircraft can be of extremely high velocity and hazardous to smaller aircraft.  `[definition:ECC-2220400]`
- Matches 'Aircraft encounter with turbulence' (ECCAIRS 1.3.0.12 · Events (390) · 2220600 · Aircraft operation general › Weather encounters): Encounter with any or all of a) clear air turbulence (CAT) b) turbulence in cloud c) vortex / wake turbulence also to be used in events in which the aircraft was damaged by turbulence. CAT: Clear Air Turbulence (CAT) is the bumpiness experienced by aircraft at high altitudes (above 18,000 feet) in either cloud- free conditions or in stratiform clouds. CAT occurs when undulations (known as gravity waves) in the upper atmosphere become steep and unstable, then break down into chaotic motion. The scale of wave motion that normally affects jet aircraft is on the order of ~10 meters to ~1-2 kilometers. These unstable waves occur when vertical wind shear becomes locally excessive, allowing the waves to overcome the stability of environmental temperature conditions. This condition is known as Kelvin-Helmholtz instability. Most CAT occurs on the fringes of (not within the core of) the jet stream, in the vicinity of upper level frontal zones where temperature contrasts are strong. CAT may also occur when strong winds cross a mountain range in certain thermal conditions, allowing gravity waves to amplify and propagate vertically toward the stratosphere. These 'mountain waves' may be smooth undulations, resulting in updrafts and downdrafts (UDDF in pilot report code), or can break down into smaller scale turbulence. A third instance in which CAT occurs is when strong winds encounter the tops of thunderstorm clouds, resulting in strong shear waves that extend well downstream from the convective cloud.  `[definition:ECC-2220600]`
- Narrative describes 'turbulence' (7 of 12 supporting reports).  `[report:ERA18LA002]`  
  > Pilots operating lighter aircraft behind aircraft producing strong wake vortices should consider the following techniques to assist in avoiding wake turbulence and should be aware of the wind direction and speed along the final approach path: 1) If the pilot of the smaller following aircraft has visual contact with the preceding, larger aircraft and also with the runway, the pilot may further adjust the flightpath to avoid possible wake vortex turbulence by: (a) Flying slightly above the glidepath and maintain that glidepath to a touchdown point beyond the touchdown point of the larger preceding aircraft.

**Exclude when**
- Distinguish from sibling C6 'Clear-air turbulence with cabin injuries' under the same parent.  `[sibling:C6]`
- Coded MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) rather than TURB: similar wording, different occurrence category.  `[report:ANC16FA061]`  
  > Cause: Personnel issues-Psychological-Attention/monitoring-Monitoring other aircraft-Pilot of other aircraft.
- Coded ARC (Abnormal Runway Contact) rather than TURB: similar wording, different occurrence category.  `[report:DCA13FA131]`  
  > Finding: Aircraft-Aircraft oper/perf/capability-Performance/control parameters-Descent/approach/glide path-Not attained/maintained.
- Coded LOC-I (Loss of Control – Inflight) rather than TURB: similar wording, different occurrence category.  `[report:CHI08FA282]`  
  > At 1835:55, N193BS transmitted, and Minneapolis three bravo sierra so for planning purposes uh (unintelligible) we are going to get radar vectors to the localizer three six.” At 1836:01, ZMP03 transmitted, “november three bravo sierra affirmative.” At 1904:49, ZMP03 transmitted, “a november three bravo sierra’s four south of dougy maintain three thousand five hundred til on a published portion of the approach cleared for the localizer three six approach arbor vitae.” At 1905:07, N193BS transmitted, “ah i got all that ah three thousand five hundred till on a published segment (unintelligible) cleared three six approach.” At 1905:13, ZMP03 transmitted, “November three bravo sierra roger and are you going to be able to shoot the approach from a couple south of the marker there.” At 1905:19, N193BS transmitted, “i’m sorry what.” At 1905:20, ZMP03 transmitted, “are you going to be able to make the approach from fifty two hundred from a couple south of the marker.” At 1905:29, the autopilot (AP) was selected OFF at a pressure altitude of 5,033 feet and a heading of 359 degrees magnetic.
- Not 'Undershoot' — that definition is crosswalked to USOS, not TURB.  `[definition:IND-37]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not TURB.  `[definition:ECC-2180101]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.11).  `[parent:LOC-I]`

**Linked example reports**
- WPR12FA067: "Cause: Environmental issues-Conditions/weather/phenomena-Turbulence-Wake turbulence-Effect on equipment."
- ERA18LA002: "Pilots operating lighter aircraft behind aircraft producing strong wake vortices should consider the following techniques to assist in avoiding wake turbulence and should be aware of the wind direction and speed along the final approach path: 1) If the pilot of the smaller following aircraft has visual contact with the preceding, larger aircraft and also with the runway, the pilot may further adjust the flightpath to avoid possible wake vortex turbulence by: (a) Flying slightly above the glidepath and maintain that glidepath to a touchdown point beyond the touchdown point of the larger preceding aircraft."
- DCA16CA197: "The operators post-flight telemetry analysis showed that the aircraft experienced significant deviations in pitch, roll, and airspeed, consistent with turbulence during the final approach."
- WPR14LA169: "Cause: Aircraft-Aircraft oper/perf/capability-Performance/control parameters-Airspeed-Not attained/maintained."
- WPR16FA086: "Probable cause: The weight shift control aircraft encounter with a wake vortex from a preceding airplane, which resulted in a roll upset at an altitude too low for recovery."
- WPR16FA172: "Probable cause: The pilot's selection of a landing runway which, given the wind and traffic conditions, was susceptible to high crosswinds and the translation of wake turbulence across its approach path, and the controller's and pilot's failure to ensure separation from the B757 and its wake, which resulted in a low-altitude encounter with wake vortices that the pilot was unable to recover from."
- WPR10CA226: "Cause: Aircraft-Aircraft structures-Empennage structure-Spars/ribs (on vert stab)-Capability exceeded."
- DCA23FA428: "During the descent, at about 2231:15 UTC, as the aircraft passed through a pressure altitude of about 15,100 ft and computed airspeed of 312 kts, the aircraft experienced a period of severe turbulence."
- ERA22LA089: "The guidance required controllers to issue wake turbulence cautionary advisories "including the position, altitude if known, and direction of flight" to "VFR arriving aircraft that have previously been radar vectored and the vectoring has been discontinued." The guidance also stated, "Issue cautionary information to any aircraft if in your opinion, wake turbulence may have an adverse effect on it." FAA Advisory Circular 90-23G, Aircraft Wake Turbulence, states the following: “… if a pilot accepts a clearance to visually follow a preceding aircraft, the pilot accepts responsibility for both separation and wake turbulence avoidance."
- CEN13FA438: "Cause: Aircraft-Aircraft oper/perf/capability-Performance/control parameters-(general)-Capability exceeded."
- WPR17FA023: "The pilot was concerned that if the turbulence continued during the approach, he would be vulnerable to strong buffeting at normal approach speed, which might lead to a rough landing; as a countermeasure, he elected to land at a higher airspeed."
- LAX08LA105: "Probable cause: The pilot's encounter with severe turbulence during descent into the airport environment, which resulted in an exceedence of the aircraft's design stress limit and structural damage."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 pass · G9 pass

### B07 · Loss of separation caused by an ATC clearance

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** A controller clearance or instruction puts two aircraft into conflict, leading to loss of separation or a TCAS alert.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: A controller clearance or instruction puts two aircraft into conflict, leading to loss of separation or a TCAS alert.  `[candidate:B07]`
- Matches 'Loss of separation' (ICAO Doc 4444 – PANS-ATM (separation minima)): Two aircraft come closer than the prescribed separation minima, often after an ATC clearance or instruction puts them in conflict.  `[definition:IND-23]`
- Matches 'Loss of separation with aircraft - both airborne' (ECCAIRS 1.3.0.12 · Events (390) · 2180101 · Aircraft operation general › Aircraft - near collisions/loss of separation › Loss of separation between aircraft): This includes the AIRPROX defined as: A situation in which, in the opinion of a pilot or air traffic services personnel, the distance between aircraft as well as their relative positions and speed have been such that the safety of the aircraft involved may have been compromised. An aircraft proximity is classified as follows: Risk of collision. The risk classification of an aircraft proximity in which serious risk of collision has existed. Safety not assured. The risk classification of an aircraft proximity in which the safety of the aircraft may have been compromised. No risk of collision. The risk classification of an aircraft proximity in which no risk of collision has existed. Risk not determined. The risk classification of an aircraft proximity in which insufficient information was available to determine the risk involved, or inconclusive or conflicting evidence precluded such determination.  `[definition:ECC-2180101]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`

**Exclude when**
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (1 report(s) assigned there).  `[report:OPS16IA010]`  
  > Probable cause: The air traffic controller's decision to issue climb instruction to one aircraft without ensuring the required separation with another could be maintained.
- Distinguish from sibling B12 'GNSS interference or spoofing' under the same parent.  `[sibling:B12]`
- Distinguish from sibling B20 'Pushback or towing collision' under the same parent.  `[sibling:B20]`
- Coded CFIT (Controlled Flight Into or Toward Terrain) rather than MAC: similar wording, different occurrence category.  `[report:WPR16LA028]`  
  > Until a pilot acknowledges a controller's clearance or instruction, a controller cannot know if a pilot will comply with the clearance or remain as previously cleared."
- Coded ATM (ATM/CNS) rather than MAC: similar wording, different occurrence category.  `[report:OPS17IA010]`  
  > At 0124:03, the SCT Manhattan controller instructed EVA015 to "climb and maintain five thousand, and ah, are you, are you southbound now, I see you going northbound, climb and maintain six thousand." The pilot of EVA015 responded "roger, turning ah, we are turning south, and ah maintain five thousand, EVA015 heavy." The SCT Manhattan controller contacted LAX Air Traffic Control Tower (ATCT) and instructed them to stop departures.
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than MAC: similar wording, different occurrence category.  `[report:ERA18FA064]`  
  > The controller repeated the instruction, and at 1202:03, the pilot responded, "course one two zero stay at twenty-five hundred." The controller responded, "November two six two whiskey sierra I don't have time to talk to you four times per control instruction cause there's a lot going on please listen up…" At 1203, the pilot climbed the airplane to 2,900 ft and then was instructed to return to 2,500 ft; the pilot acknowledged without using the airplane's call sign.
- Not 'Clearance - wrong aircraft' — that definition is crosswalked to ATM, not MAC.  `[definition:ECC-4010704]`
- Not 'Clearance - not suitable for aircraft' — that definition is crosswalked to ATM, not MAC.  `[definition:ECC-99010092]`
- Not 'Clearance - wrong heading' — that definition is crosswalked to ATM, not MAC.  `[definition:ECC-4010702]`
- Events better described by CICTT CFIT (Controlled Flight Into or Toward Terrain) (runner-up parent, margin 0.26).  `[parent:CFIT]`

**Linked example reports**
- WPR15MA243/2: "Probable cause: The local controller's (LC) failure to properly identify the aircraft in the pattern and to ensure control instructions provided to the intended Cessna on downwind were being performed before turning Eagle1 into its path for landing."
- OPS11IA653/2: "In a TRSA, controllers are required to ensure that aircraft targets do not merge unless the aircraft have a minimum of 500 feet vertical separation or can maintain visual separation, although visual separation was not being applied in this incident."
- OPS11IA246: "At 2235:35, the R66 controller instructed AAL951 “…turn left at your discretion traffic now one o’clock four miles southwest heavy C17 flight level 220.” At 2235:49, the R86 controller transmitted “THUG11, you up?’ The pilot responded, “Level 220 in a right hand turn to 020.” At 2235:54, the R66 controller asked AAL951 “…do you have that traffic in sight?” The pilot transmitted “No, we do not.” At 2235:56, the R86 controller informed THUG11 “traffic right below you is a Boeing triple seven that should be leveling at flight level 210.” At 2235:58, the R66 controller informed AAL951 “… traffic is now at 12 o’clock less than one mile at flight level 220, C17.” At 2236:12, THUG11 transmitted to the R86 controller, “Yeah, THUG11 just came within approximately 2000 feet of that traffic.” At 2236:17, AAL951 transmitted to the R66 controller “that guy passed us now and that was not good.” At 2236:21, the R86 controller instructed THUG11 to “…continue right turn and then proceed to COYLE.” At 2236:24, the R66 controller responded to AAL951 statement “I understand that and I apologize, I am not working that other airplane.” The R66 controller then instructed AAL951 to climb to FL230."
- OPS10IA574/2: "At 0650:26, the LCS controller asked, "Bemidji 46 are you in the turn?" The pilot replied, "46 say again the turn?” The LCS controller transmitted, "Bemidji 46 heading 180." The pilot of BMJ 46 replied, "46 left to 180." At 0650:54, the LCS controller transmitted, "Bemidji 46 remain this frequency maintain 4000 heading 180." At 0651:00, the pilot of Bemidji 46 responded, "4000 180 and I've got traffic." At 0651:41, Bemidji 46 transmitted, "Bemidji 46 going to departure." At 0651:44, the LCS controller transmitted, "Bemidji 46 now contact departure." At 0651:47, Bemidji 46 transmitted, "46 has that traffic up ahead there I wasn't notified about that." The LCS controller replied, "okay why didn't you start the turn once you were airborne?”The pilot replied, "all right okay I'm going to departure sorry about that." At 0649:49, AWE1848 made a partial transmission to departure control, stating "1848 is..."."
- OPS15IA017: "Probable cause: The controller's issuance of a landing clearance to an arriving aircraft while another aircraft was in position on the same runway."
- OPS10IA163/2: "At closest point of approach, the aircraft were separated by approximately .77 nautical mile laterally and 100 feet vertically; as the controller did not issue any control instructions to establish and maintain separation, neither visual separation nor target resolution procedures were being applied before the incident occurred."
- OPS25LA052: "At about 1941 CDT, the Dakota RAPCON Minot radar sector controller (MIB sector controller) coordinated via shout line (a dedicated, direct voice communication link) with MOT ATCT LC (local control) controller requesting an opposite direction arrival for SKW3788 to runway 31, and an approach to runway 8 for another uninvolved aircraft, N717BL."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 pass · G8 pass · G9 pass

### B08 · TCAS resolution advisory after a level bust

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** The aircraft climbs or descends through its cleared altitude (level bust) and a TCAS resolution advisory follows.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: The aircraft climbs or descends through its cleared altitude (level bust) and a TCAS resolution advisory follows.  `[candidate:B08]`
- Matches 'Level bust (altitude deviation)' (EUROCONTROL – Level bust): An unauthorised vertical deviation of more than 300 feet from the cleared flight level or altitude, a common cause of loss of separation and TCAS resolution advisories.  `[definition:IND-11]`
- Matches 'Loss of separation with aircraft - both airborne' (ECCAIRS 1.3.0.12 · Events (390) · 2180101 · Aircraft operation general › Aircraft - near collisions/loss of separation › Loss of separation between aircraft): This includes the AIRPROX defined as: A situation in which, in the opinion of a pilot or air traffic services personnel, the distance between aircraft as well as their relative positions and speed have been such that the safety of the aircraft involved may have been compromised. An aircraft proximity is classified as follows: Risk of collision. The risk classification of an aircraft proximity in which serious risk of collision has existed. Safety not assured. The risk classification of an aircraft proximity in which the safety of the aircraft may have been compromised. No risk of collision. The risk classification of an aircraft proximity in which no risk of collision has existed. Risk not determined. The risk classification of an aircraft proximity in which insufficient information was available to determine the risk involved, or inconclusive or conflicting evidence precluded such determination.  `[definition:ECC-2180101]`
- Matches 'Aircraft not RVSM (Reduced Vertical Separation Minimum) equipped while being operated in' (ECCAIRS 1.3.0.12 · Events (390) · 7050300 · Regulatory issues / events › Aircraft related regulatory event/issue): RVSM airspace (Aircraft not RVSM equipped) Aircraft not RVSM equipped while being operated in RVSM airspace. RVSM: Reduced Vertical Separation Minimum of 1.000 ft (300 m.)  `[definition:ECC-7050300]`

**Exclude when**
- Belongs to sibling B07 'Loss of separation caused by an ATC clearance' when it matches that bucket better (1 report(s) assigned there).  `[report:WPR15MA243/2]`  
  > At 1100:23, the LC instructed, "stationair five eight uniform two six right cleared for I'm sorry two six left cleared for takeoff." At 1100:29, the pilot of N5058U stated, "uh I'm sorry was that for five eight uniform?" The LC then cleared the pilot of N5058U for takeoff from runway 26L.
- Distinguish from sibling B12 'GNSS interference or spoofing' under the same parent.  `[sibling:B12]`
- Distinguish from sibling B20 'Pushback or towing collision' under the same parent.  `[sibling:B20]`
- Coded ATM (ATM/CNS) rather than MAC: similar wording, different occurrence category.  `[report:OPS17IA021/2]`  
  > Separate an arriving aircraft from another aircraft using the same runway by ensuring that the arriving aircraft does not cross the landing threshold until one of the following conditions exists or unless authorized in para 3-10-10, Altitude Restricted Low Approach.
- Not 'Aircraft encountered vortex/wake turbulence' — that definition is crosswalked to TURB, not MAC.  `[definition:ECC-2220400]`
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.35).  `[parent:NAV]`

**Linked example reports**
- OPS11IA686: "Air Traffic Procedural Requirements Traffic advisories were provided to both pilots in accordance with Federal Aviation Administration Order 7110.65, paragraphs 2-1-21 "Traffic Advisories", and 5-1-8 "Merging Target Procedures", which state in part: 2-1-21 Unless an aircraft is operating within Class A airspace or omission is requested by the pilot, issue traffic advisories to all aircraft (IFR or VFR) on your frequency when, in your judgment, their proximity may diminish to less than the applicable separation minima."
- ERA15MA259: "At 1100:16, the CHS approach controller issued a traffic advisory advising the F-16 pilot of "traffic 12 o'clock, 2 miles, opposite direction, 1,200 [ft altitude] indicated, type unknown." At 1100:24, the F-16 pilot responded that he was "looking" for the traffic."
- ERA22FA318/2: "Air traffic control responsibility for the flight was transferred to the VGT air traffic control tower (ATCT) at 1158:26."
- ANC20LA085/2: "When a rule of this section gives another aircraft the right-of-way, the pilot shall give way to that aircraft and may not pass over, under, or ahead of it unless well clear."
- ERA11FA468/2: "His airplane was initially at an altitude of about 1,500 feet at the Expressway, but descended until it was about 1,200 to 1,000 feet, before turning onto the downwind leg."
- OPS16IA010: "At 0936:48, the pilot of N57GX contacted JAX approach control and advised that he "would like to go back on course and climb to 9,000." The approach controller responded, "Mooney 7GX you are radar contact eight miles west of the Ocala airport, say altitude." The pilot of N57GX replied, "yeah I see that 57GX, we would like to go back on course to go towards Fort Myers." The approach controller replied, "…roger that, ah, cleared direct Lakeland, climb and maintain 5,000." The pilot of N57GX correctly read back the route and altitude clearance, and the approach controller then climbed N57GX to 9,000 feet."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### B09 · Hydraulic system failure in flight

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent SCF-NP System/Component Failure – Non-Powerplant*

**Definition.** Loss of fluid or pressure in a hydraulic system in flight degrades flight controls, brakes or landing gear.

**Include when**
- The occurrence meets the CICTT SCF-NP (System/Component Failure – Non-Powerplant) definition.  `[parent:SCF-NP]`
- Core definition: Loss of fluid or pressure in a hydraulic system in flight degrades flight controls, brakes or landing gear.  `[candidate:B09]`
- Matches 'Hydraulic system failure' (SKYbrary – Hydraulic System Failure): Loss of hydraulic fluid or pressure that degrades flight controls, brakes, steering or landing gear, handled with non-normal checklists.  `[definition:IND-24]`
- Matches 'Smoke - Landing gear' (ECCAIRS 1.3.0.12 · Events (390) · 1990162 · Aircraft/system/component › Non-component specific events › Explosions / fire/ fumes / smoke › Smoke): Smoke emanating from the landing gear, e.g. from hydraulic liquid dripping onto hot brakes.  `[definition:ECC-1990162]`
- Matches 'Fire - Landing gear' (ECCAIRS 1.3.0.12 · Events (390) · 1990161 · Aircraft/system/component › Non-component specific events › Explosions / fire/ fumes / smoke › Fire): Fire - Landing gear: e.g. by fluids coming into contact with hot brakes.  `[definition:ECC-1990161]`

**Exclude when**
- Belongs to sibling B10 'Landing gear did not extend' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN11IA379]`  
  > Probable cause: The failure of the right main landing gear (MLG) to extend normally, which resulted from the combination of a slightly worn uplock pin, the operation of the hydraulic pumps below their specified operating pressures, and contamination within the landing gear hydraulic system.
- Coded ARC (Abnormal Runway Contact) rather than SCF-NP: similar wording, different occurrence category.  `[report:DCA24FA002]`  
  > The cause of the system failure was a broken wire, due to tensile overload, between the alternate gear extend switch and the alternate extension power pack (AEPP), preventing the AEPP from energizing and supplying hydraulic fluid to the door lock release actuators for the nose landing gear and main landing gear.
- Coded UNK (Unknown or Undetermined) rather than SCF-NP: similar wording, different occurrence category.  `[report:ERA12IA060]`  
  > Probable cause: The pilots’ failure to appropriately apply the landing gear wheel brakes after landing, to properly perform the hard brake pedal-no braking condition procedure following the reported brake failure and to apply the emergency brakes.
- Coded RE (Runway Excursion) rather than SCF-NP: similar wording, different occurrence category.  `[report:ERA11LA390]`  
  > Hydraulic pressure for operation of the landing gear was supplied by the hydraulic system through a selector valve which was electrically controlled by the landing gear lever.
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.13).  `[parent:RE]`

**Linked example reports**
- CEN11FA193: "Probable cause: The pilot flying's (PF) decision to land on a shorter-than-recommended runway with a known left hydraulic system failure rather than go around as suggested by the pilot-not-flying, his failure to immediately apply emergency brakes following the detection of the lack of normal brakes, and his attempt to go around late in the landing roll with insufficient runway remaining."
- ERA15LA140: "Cause: Aircraft-Aircraft systems-Landing gear system-Landing gear brakes system-Malfunction."
- WPR22LA341: "Refer to Emergency/Abnormal Procedures, LANDING WITH NO “A” HYDRAULIC SYSTEM PRESSURE; Tab P2 WARNING DO NOT USE SPED BRAKES IN FLIGHT UNLESS “A” HYDRAULIC SYSTEM PRESSURE IS ZERO."
- ERA23LA202: "The hydraulic landing gear system is designed so when the pilot places the landing gear handle in the UP position, the hydraulic power pack is energized, and hydraulic fluid is directed to the up port of each gear actuating cylinder to retract the gear."
- WPR12FA193: "The hydraulic fluid pressurizes and routes through the landing gear control valve to the retract side of the hydraulic system."
- SEA08LA147: "According to the Gulfstream Commander 690A/690B Maintenance Manual, Section VI, Landing Gear, Wheels and Brakes, Landing Gear Operation, when the landing gear control lever is in the down and locked position, hydraulic pressure is being applied to the inboard main landing gear actuating cylinder, as well as assisted by the outboard main landing gear (hydraulic-pneumatic) actuating cylinder to extend and lock the main gear."
- ERA14FA144: "The landing gear system's hydraulic power pack fluid reservoir was designed to hold approximately 3 quarts of hydraulic fluid."
- CEN21LA323: "During normal operation, the landing gear is retracted and held in the fully retracted position by hydraulic pressure and, as such, the hydraulic power pack will occasionally cycle on/off during flight to maintain sufficient hydraulic pressure to keep the landing gear retracted."
- ERA16LA042: "The airplane's landing gear was hydraulically controlled, and by design the nose landing gear extended aft while the main landing gears extended forward."
- ERA14LA022: "Lubricated landing gear system." ADDITIONAL INFORMATIONBrake System The airplane was equipped with a hydraulic fluid braking system that included two independent wheel brakes actuated by two separate brake master cylinders, one each for the left and right brake."
- ERA11IA316: "7 instructed that the emergency landing gear extension should be performed if the hydraulic pressure was "low." At 0908, the flightcrew switched duties due to the location of the emergency landing gear extension controls."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 pass · G9 pass

### B10 · Landing gear did not extend

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent SCF-NP System/Component Failure – Non-Powerplant*

**Definition.** One or more landing gear legs fail to extend or lock down, requiring alternate extension or a gear-up landing.

**Include when**
- The occurrence meets the CICTT SCF-NP (System/Component Failure – Non-Powerplant) definition.  `[parent:SCF-NP]`
- Core definition: One or more landing gear legs fail to extend or lock down, requiring alternate extension or a gear-up landing.  `[candidate:B10]`
- Matches 'Landing gear malfunction' (SKYbrary – Landing Gear Malfunction): Failure of a landing gear leg to extend, retract or lock, requiring alternate extension or a landing with gear not fully down.  `[definition:IND-25]`
- Matches 'Fire - Landing gear' (ECCAIRS 1.3.0.12 · Events (390) · 1990161 · Aircraft/system/component › Non-component specific events › Explosions / fire/ fumes / smoke › Fire): Fire - Landing gear: e.g. by fluids coming into contact with hot brakes.  `[definition:ECC-1990161]`
- Matches 'Smoke - Landing gear' (ECCAIRS 1.3.0.12 · Events (390) · 1990162 · Aircraft/system/component › Non-component specific events › Explosions / fire/ fumes / smoke › Smoke): Smoke emanating from the landing gear, e.g. from hydraulic liquid dripping onto hot brakes.  `[definition:ECC-1990162]`

**Exclude when**
- Belongs to sibling B09 'Hydraulic system failure in flight' when it matches that bucket better (1 report(s) assigned there).  `[report:WPR12FA193]`  
  > To extend the landing gear, the system works identical with the exception that the landing gear control valve routes fluid through the uplocks to release them before going to the extend side of the actuating cylinders.
- Coded ARC (Abnormal Runway Contact) rather than SCF-NP: similar wording, different occurrence category.  `[report:DCA12FA058]`  
  > Landing Gear Alternate Extension To isolate the normal landing gear selector valve during flight, a landing gear inhibit switch is installed in the flight compartment ceiling.
- Coded SCF-PP (System/Component Failure – Powerplant) rather than SCF-NP: similar wording, different occurrence category.  `[report:CEN13FA196]`  
  > Cause: Aircraft-Aircraft systems-Landing gear system-Gear extension and retract sys-Incorrect use/operation.
- Not 'Wheels-up landing - unintentional' — that definition is crosswalked to ARC, not SCF-NP.  `[definition:ECC-2011202]`
- Not 'Wheels-up landing,' — that definition is crosswalked to ARC, not SCF-NP.  `[definition:ECC-2011200]`
- Events better described by CICTT ARC (Abnormal Runway Contact) (runner-up parent, margin 0.02).  `[parent:ARC]`

**Linked example reports**
- WPR25LA122: "When the actuators fully extend the landing gear, an internal mechanical lock in the nose gear actuator and a mechanical lock on each main landing gear drag brace (called downlock hooks) will hold the landing gear in the down position."
- ERA11CA396: "He reset the CB, raised then lowered the landing gear; however, the landing gear failed to fully extend and the landing gear CB tripped again."
- DCA10IA021: "Contributing to this incident was a circular reference in the company Flight Manual in which the Landing Gear Gravity Extension checklist referred back to the Landing Gear Unsafe Indication After Extension checklist rather than the Landing Gear - Partial Gear or Gear Up Landing checklist."
- WPR22LA228: "Additionally, during the gear extension the nose gear was observed to lock into place first, and the main landing gear would extend, pivot, and then lock into place."
- GAA16CA074: "The tests revealed that the landing gear extension process could not be completed, and the manual landing gear pump did not have sufficient fluid remaining to extend all three landing gear."
- CEN11IA379: "Probable cause: The failure of the right main landing gear (MLG) to extend normally, which resulted from the combination of a slightly worn uplock pin, the operation of the hydraulic pumps below their specified operating pressures, and contamination within the landing gear hydraulic system."
- WPR16LA058: "Landing gear position switches located on the aft bell crank of each gear transmit signals to the instrument panel position indicators to indicate when the landing gear is down and locked."
- WPR10LA347: "The nose landing gear was folded up into the wheel well, and the nose landing gear extend rod was separated from the landing gear actuator nose landing gear extend/retract arm, which is located at the base of the landing gear actuator."
- CEN16LA336: "Probable cause: The failure of the landing gear assembly snap ring, which prevented the pilot from being able to extend the landing gear and resulted in a gear-up landing."
- CEN22LA378: "The pilot reported that the landing gear retracted normally during takeoff; however, when he attempted to extend the landing gear in preparation for the landing, the nosewheel extended and locked into place but the main landing gear did not fully extend."
- WPR17LA061: "Probable cause: Failure of the landing gear to extend as a result of excessive wear within the landing gear gearbox and motor, which resulted in a gear-up landing."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 FAIL · G8 pass · G9 pass

### B11 · Terrain warning on a non-precision approach

*Taxonomy version ntsb-draft-c94008cd21 · status grounded · parent CFIT Controlled Flight Into or Toward Terrain*

**Definition.** During a non-precision or visual approach the aircraft descends too low and the terrain awareness system warns of terrain or obstacles.

**Include when**
- The occurrence meets the CICTT CFIT (Controlled Flight Into or Toward Terrain) definition.  `[parent:CFIT]`
- Core definition: During a non-precision or visual approach the aircraft descends too low and the terrain awareness system warns of terrain or obstacles.  `[candidate:B11]`
- Matches 'Terrain awareness and warning system (TAWS)' (14 CFR 121.354 – Terrain awareness and warning system): Airliners must carry a system that warns the crew of terrain, obstacles and excessive descent so they can climb away before impact.  `[definition:IND-26]`
- Matches 'Ground proximity warning system nuisance alarm' (ECCAIRS 1.3.0.12 · Events (390) · 1344401 · Aircraft/system/component › 3400 Navigation systems › 3440 Independent position system › 3444 Ground proximity warning): An event involving nuisance warnings by the aircraft's ground proximity warning system.  `[definition:ECC-1344401]`
- Matches 'Other ground proximity warning system related event' (ECCAIRS 1.3.0.12 · Events (390) · 1344402 · Aircraft/system/component › 3400 Navigation systems › 3440 Independent position system › 3444 Ground proximity warning): An event involving the aircraft's ground proximity warning system other than a nuisance warning.  `[definition:ECC-1344402]`

**Exclude when**
- Coded RI (Runway Incursion) rather than CFIT: similar wording, different occurrence category.  `[report:DCA16IA200]`  
  > At 2029:29, the airplane was descending through flight level 235 (about 23,500 feet above sea level) descending to 17,000 feet, and the flight crew made initial contact with Ellsworth Radar Approach Control (EA) The approach controller acknowledged and cleared the flight to descend to 5,300 feet and to expect a visual approach to runway 14.
- Coded ATM (ATM/CNS) rather than CFIT: similar wording, different occurrence category.  `[report:OPS21LA003/2]`  
  > The alert stated that data indicate a potential for “unstable approaches” and “GPWS Terrain/Obstacle Warnings.” It further provided conditions that may result in an unstabilized approach with those conditions being “a steeper glidepath,” “Parking garage approximately 0.4 NM from RWY 27 threshold” and “high gross weight and tailwinds may require vertical speeds in excess of 1000 fpm during final approach segment.” Southwest Airlines General Approach Policies The Southwest Airlines B737NG Operating Manual, Section 11.1.3.1 provided, in part, the following general approach guidance: If available, follow glidepath guidance on final.
- Coded LOC-G (Loss of Control – Ground) rather than CFIT: similar wording, different occurrence category.  `[report:ERA21LA353]`  
  > Because of mountainous terrain, the visual approach to runway 12 was not straight-in; pilots were required to fly through a valley and then make a left turn while on short final approach to align with the runway.
- Not 'Undershoot' — that definition is crosswalked to USOS, not CFIT.  `[definition:IND-37]`
- Not 'Genuine airborne collision avoidance system/traffic alert and collision avoidance system warning' — that definition is crosswalked to MAC, not CFIT.  `[definition:ECC-2260100]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not CFIT.  `[definition:ECC-2180101]`
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.23).  `[parent:NAV]`

**Linked example reports**
- ANC15FA049: "Probable cause: The pilot's decision to initiate and continue visual flight into instrument meteorological conditions, which resulted in a loss of situational awareness and controlled flight into terrain."
- ANC17MA001: "Contributing to the accident were (1) Hageland's allowance of routine use of the terrain inhibit switch for inhibiting the terrain awareness and warning system alerts and inadequate guidance for uninhibiting the alerts, which reduced the margin of safety, particularly in deteriorating visibility; (2) Hageland's inadequate crew resource management (CRM) training; (3) the Federal Aviation Administration's failure to ensure that Hageland's approved CRM training contained all the required elements of Title 14 Code of Federal Regulations 135.330; and (4) Hageland's CFIT avoidance ground training, which was not tailored to the company's operations and did not address current CFIT-avoidance technologies."
- WPR09FA320: "The TAWS provides the following visual warnings on the Terrain Awareness Control Unit: red annunciator light for terrain warnings, amber annunciator light for terrain cautions, and white annunciator light for terrain inhibit."
- ERA19FA070: "No visual approach slope indicator (VASI) or precision approach path indicator (PAPI) system was installed."
- ERA11FA219: "According to the Garmin 500 W Series Pilot's Guide and Reference, the unit featured a non-certified terrain awareness system, or an optional certified Terrain Awareness and Warning System (TAWS)."
- CEN14FA110: "HISTORY OF FLIGHTOn January 10, 2014, about 1948 eastern standard time, a Cessna 310R, N3829G, impacted trees and terrain about 1,500 feet west of the approach end of runway 9R (6,521 feet by 150 feet, asphalt) at Oakland County International Airport (PTK), Pontiac, Michigan, during a straight-in instrument landing system (ILS) approach to runway 9R."
- ANC14MA008: "The airplane was equipped with a Honeywell KGP-560 Terrain Awareness and Warning System (TAWS), and a Midcontinent Avionics MD41 Terrain Awareness Annunciator Control Unit."
- ERA24FA136: "Probable cause: The PIC’s continuation of an unstabilized approach in gusting wind conditions and his failure to monitor the airplane’s altitude during the approach, which led to a descent into terrain short of the runway."
- OPS18IA003: "At 1810:04, the pilot of SKW3567 transmitted "approach SkyWest thirty five sixty seven we received a ah G-P-S or a excuse me a G-P-W-S which is one of our terrain warnings ah that ah comes up when ah we are too low and we just wanted to let you when we called you we wanted to let you know that we thought were ah too low for this sector and we wanted to confirm with you the altitude on the approach"."
- WPR23FA257: "Except as provided in 91.176 of this chapter, where a DA/DH or MDA is applicable, no pilot may operate an aircraft, except a military aircraft of the United States, below the authorized MDA or continue an approach below the authorized DA/DH unless— (1) The aircraft is continuously in a position from which a descent to a landing on the intended runway can be made at a normal rate of descent using normal maneuvers, … (2) The flight visibility is not less than the visibility prescribed in the standard instrument approach being used; and (3) Except for a Category II or Category III approach where any necessary visual reference requirements are specified by the Administrator, at least one of the following visual references for the intended runway is distinctly visible and identifiable to the pilot: (i) The approach light system, except that the pilot may not descend below 100 feet above the touchdown zone elevation using the approach lights as a reference unless the red terminating bars or the red side row bars are also distinctly visible and identifiable."
- CEN09MA019: "Although the GNS 430 could display terrain and obstacles, the software for that function had never been installed."
- NYC08MA090: "HISTORY OF FLIGHT On February 1, 2008, about 1128 eastern standard time, a Raytheon Aircraft Company C90A, N57WR, was substantially damaged when it impacted terrain during a missed approach following an instrument approach to the Mount Airy/Surry County Airport (MWK), Mount Airy, North Carolina."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B12 · GNSS interference or spoofing

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** Satellite navigation signals are jammed or spoofed, giving false position, lost RNP capability or incorrect time, often near conflict zones.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: Satellite navigation signals are jammed or spoofed, giving false position, lost RNP capability or incorrect time, often near conflict zones.  `[candidate:B12]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`
- Matches 'Near collision with tall structure/object' (ECCAIRS 1.3.0.12 · Events (390) · 2180402 · Aircraft operation general › Aircraft - near collisions/loss of separation › Near collision with object on ground): An event involving a near collision by an aircraft with tall structure or other object on the ground. Near collision with parachutist on the ground (Near collision - parachutist)                                  2180404    * An event involving a near collision by an aircraft with a parachutist on the ground.  `[definition:ECC-2180402]`
- Matches 'Genuine airborne collision avoidance system/traffic alert and collision avoidance system warning' (ECCAIRS 1.3.0.12 · Events (390) · 2260100 · Aircraft operation general › Warning system triggered): triggered (ACAS/TCAS warning triggered) An event involving a genuine airborne collision avoidance system/traffic alert and collision avoidance system warning. ACAS: An aircraft system based on secondary surveillance radar (SSR) transponder signals which operates independently of ground-based equipment to provide advice to the pilot on potential conflicting aircraft that are equipped with SSR transponders. Note: In this context the term 'independently' means that ACAS operates independently of other systems used by air traffic services except for communications with Mode S ground stations. TCAS: TCAS is the terminology used in the United States for its traffic alert and collision avoidance system. In ICAO the system is known as ACAS.  `[definition:ECC-2260100]`

**Exclude when**
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (1 report(s) assigned there).  `[report:ERA15MA259]`  
  > His additional duties at the time of the accident included the position of 55th Fighter Squadron Chief of Mobility.
- Belongs to sibling B20 'Pushback or towing collision' when it matches that bucket better (1 report(s) assigned there).  `[report:LAX08FA265]`  
  > According to L-3 Avionics personnel, the upgrade provided an extended audio callout capability.
- Distinguish from sibling B07 'Loss of separation caused by an ATC clearance' under the same parent.  `[sibling:B07]`
- Coded GCOL (Ground Collision) rather than MAC: similar wording, different occurrence category.  `[report:WPR14LA025/2]`  
  > At the time of the accident, the ATCT cab was staffed by four persons serving three positions, including two positions of operation.
- Coded LOC-I (Loss of Control – Inflight) rather than MAC: similar wording, different occurrence category.  `[report:ERA19LA026]`  
  > The ELT signal was captured only on the recording of the "R52" controller position at the Jacksonville air route traffic control center, which was the 2nd controller position at Jacksonville to talk to N555PM.
- Coded OTHR (Other) rather than MAC: similar wording, different occurrence category.  `[report:CEN10FA115/3]`  
  > Radar data, provided by Denver Air Route Traffic Control Center (ZDV) in National Track Analysis Program (NTAP) format, identified and depicted the Cirrus flight from the time of departure from KEIK to the time of the accident.
- Not 'GNSS jamming and spoofing' — that definition is crosswalked to NAV, not MAC.  `[definition:IND-27]`
- Not 'Lateral navigation error' — that definition is crosswalked to NAV, not MAC.  `[definition:IND-41]`
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.04).  `[parent:NAV]`

**Linked example reports**
- CEN10FA115/2: "Radar data, provided by Denver Air Route Traffic Control Center (ZDV) in National Track Analysis Program (NTAP) format, identified and depicted the Cirrus flight from the time of departure from KEIK to the time of the accident."
- OPS10IA014/2: "She reported that developmental controllers (controllers in training) are allocated 120 to 140 hours of training time for each radar position."
- OPS25LA032/5: "The CIC acknowledged and stated that they were waiting for a “stop the departures time.” The PCT TRACON OS stated that the Time on Target (TOT) would be at 1521 EDT and the stop time would be 17."
- OPS08IA014: "The R4 and R6 positions were combined at one position adjacent to the D4/A4/D6/A6/O10 combined position."
- ERA22FA318: "Contributing to the accident was the controller’s failure to provide timely and adequate traffic information to either airplane and his failure to recognize the developing conflict and to act in a timely manner."
- OPS10IA020/2: "With the training in progress and other activity in the cab, she stated that, "...it was pretty loud up there." When the radar coordinator took over the position, she did receive a recorded position relief briefing that included information on the Cessna, but she did not recall exactly what was said."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B13 · Engine shutdown after loss of oil pressure

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent SCF-PP System/Component Failure – Powerplant*

**Definition.** Low oil pressure or oil loss in flight leads the crew to shut an engine down as a precaution.

**Include when**
- The occurrence meets the CICTT SCF-PP (System/Component Failure – Powerplant) definition.  `[parent:SCF-PP]`
- Core definition: Low oil pressure or oil loss in flight leads the crew to shut an engine down as a precaution.  `[candidate:B13]`
- Matches 'In-flight engine shutdown (IFSD)' (SKYbrary – In-Flight Shutdown): An engine is shut down in flight because of a failure or a precautionary indication such as low oil pressure, high vibration or fire.  `[definition:IND-28]`
- Matches 'Engine oil system related event (ATA Code:7900)' (ECCAIRS 1.3.0.12 · Events (390) · 1790000 · Aircraft/system/component): (ATA Code:7900) An event involving the system units external to the engine which store and deliver engine lubricating oil to and from either turbine or reciprocating engines.  `[definition:ECC-1790000]`
- Matches 'Reciprocating engine - vibration' (ECCAIRS 1.3.0.12 · Events (390) · 1850110 · Aircraft/system/component › 8500 Reciprocating engine › 8501 Reciprocating engine general): Reciprocating engine - Vibration  `[definition:ECC-1850110]`

**Exclude when**
- Distinguish from sibling B17 'Lithium battery fire from a passenger device' under the same parent.  `[sibling:B17]`
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than SCF-PP: similar wording, different occurrence category.  `[report:WPR18LA269]`  
  > Manual manipulation of the twist grip is not typically required except during start up, shut down, autorotation practice, and emergencies." In addition, the emergency procedure for an illuminated oil light states, in part, that the oil light "…indicates loss of engine power or oil pressure.
- Not 'Aircraft encountered vortex/wake turbulence' — that definition is crosswalked to TURB, not SCF-PP.  `[definition:ECC-2220400]`
- Not 'Loss of control in-flight' — that definition is crosswalked to LOC-I, not SCF-PP.  `[definition:IND-08]`
- Not 'Explosion - Powerplant' — that definition is crosswalked to SCF-NP, not SCF-PP.  `[definition:ECC-1990108]`
- Events better described by CICTT LOC-G (Loss of Control – Ground) (runner-up parent, margin 0.60).  `[parent:LOC-G]`

**Linked example reports**
- ERA13FA184: "Engine parameters graphed included engine rpm, exhaust gas temperature, cylinder head temperature, fuel flow, and engine oil pressure."
- ERA13IA313: "Probable cause: The improper maintenance decision to adjust the engine oil pressure regulator valve in response to high oil pressure indications rather than to properly troubleshoot the anomaly, which then allowed an existing oil supply path blockage to increase and led to the eventual insufficient lubrication of the compressor section No."
- ERA20LA327: "Figure 3 Engine Oil Pressure - Data from Flight Prior to Accident Flight During the accident flight, the oil pressure was generally more consistent with a typical flight, with a decrease (about 7-8 psi) over the 3 minutes prior to the loss of engine power."
- ERA12LA343: "The oil system which fed lubricating oil to the engine consisted of a 5-gallon cylindrical oil supply tank, oil shut off valve oil strainer, pressure oil pump, scavenger oil pump, oil cooler, oil pressure gauge, and oil temperature gauge."
- CEN19LA320: "According to an oil analysis report dated May 29, 2019, the sample indicated the best “wear-rate” results from the engine; the amount of iron detected was a “bit” more than average for the type of engine, but “not far enough out of line to call a problem.” According to the engine manufacturer’s maintenance manual directions current at the time of the accident, the minimum requirement is to change the oil and filter every 50 hours and/or 4 months on engines with full flow oil filters and on engines with a large or small replaceable oil filter cartridge."
- ERA23LA058: "Examination of the oil system revealed the presence of metal contamination inside the main engine oil filter, oil pump filter, and two other oil strainers."
- ERA15LA062: "About 3 minutes after last checking the engine parameters, noting all engine parameters (specifically, oil temperature, oil pressure, and CHT) were in the green, or at 1153:02, the oil pressure indication first began to decrease from the steady state reading."
- CEN18LA031: "When the oil pressure decreased below 30 psi, the oil temperature began to increase steadily until the total loss of engine power."
- ERA11FA414: "The analog oil pressure indicator receives a pressure signal from an oil pressure sensor mounted at the aft end of the engine below the oil cooler."
- CEN17LA065: "The engine oil level then rose, and its quantity was at the base of the oil filler neck, which was above the maximum oil capacity for the engine."
- CEN23LA246: "An engine logbook entry dated June 16, 2023, stated that in addition to replacing the turbocharger, the mechanic drained the engine oil, opened the oil filter, and cleaned the oil pickup screen, where a small amount of metal was observed."
- CEN24LA140: "The engine’s manifold pressure, fuel pressure, and fuel flow values remained unremarkable until about 1 hour 7 minutes into the flight, when the oil pressure decreased briefly to 22 psi."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass

### B14 · Takeoff with frost or ice not removed

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent ICE Icing*

**Definition.** The aircraft departs or begins to depart with frost, snow or ice on its wings because it was not removed or the fluid failed.

**Include when**
- The occurrence meets the CICTT ICE (Icing) definition.  `[parent:ICE]`
- Core definition: The aircraft departs or begins to depart with frost, snow or ice on its wings because it was not removed or the fluid failed.  `[candidate:B14]`
- Matches 'Clean aircraft concept' (FAA Advisory Circular 120-60B – Ground Deicing and Anti-icing Program): No takeoff may be made with frost, ice or snow adhering to wings or control surfaces; contamination must be removed before departure.  `[definition:IND-29]`
- Matches 'Holdover time' (FAA holdover time guidelines (ground de-icing and anti-icing)): The estimated time a de-icing or anti-icing fluid protects aircraft surfaces from frost or ice; if it is exceeded before takeoff, the aircraft must be checked or de-iced again.  `[definition:IND-17]`
- Matches 'Aircraft encountered icing conditions' (ECCAIRS 1.3.0.12 · Events (390) · 2220100 · Aircraft operation general › Weather encounters): Icing conditions: Weather conditions conducive to the formation of ice on an aircraft in flight. These conditions are usually characterized by visible moisture in the air and temperatures around the freezing level. Pilots encountering icing conditions are urged to issue a pilot weather report (PIREP) immediately.  `[definition:ECC-2220100]`

**Exclude when**
- Belongs to sibling B25 'Airframe icing in flight' when it matches that bucket better (4 report(s) assigned there).  `[report:DCA14FA058]`  
  > When either of the ice detectors detect ice, an advisory message "ICE CONDITION" is shown on the EICAS display, a signal would be sent to the anti-ice system valves to activate them to open, and a signal would be sent to the full authority digital engine control to activate the automated engine icing thrust setting logic to limit the thrust to a minimum acceptable level.
- Belongs to sibling B26 'Unreliable airspeed from blocked pitot probes' when it matches that bucket better (1 report(s) assigned there).  `[report:ERA14FA112]`  
  > The anti-icing system included heated stall warning, rudder horn anti-ice, rudder tab anti-ice, generator inlet anti-ice, electrically heated wind shield, and pitot-static heaters.
- Coded CTOL (Collision with Obstacle(s) During Takeoff and Landing) rather than ICE: similar wording, different occurrence category.  `[report:ERA10TA142]`  
  > Notices to Airmen (NOTAMs) obtained by the pilot prior to the flight included citations of snow banks at several local airports, but did not include warnings about snow banks at 1MD4.
- Coded LOC-G (Loss of Control – Ground) rather than ICE: similar wording, different occurrence category.  `[report:WPR10LA092]`  
  > The ACM further states that the "Runway will be closed for aircraft use if it has more than 1/2-inch of slush or 2 inches of dry snow." Additionally, "The Airport Manager or Airport Technicians will check snow depth accumulation during stormy weather," and "Upon determination that snow removal is required, Operations will post a Notice To Airmen (NOTAM) through the Cedar City Flight Service Station." The manual added that "During after hour’s snow events, Airport Technicians will report to the airport early to verify conditions and notify the County Road Maintenance Department of needed snow removal." The airport manager stated that snow removal equipment at the airport is limited, not to availability, but in its size and capacity.
- Coded OTHR (Other) rather than ICE: similar wording, different occurrence category.  `[report:CEN12IA123]`  
  > The snowplow, operated by Aero Snow Removal Corporation (Aero Snow), was conducting snow removal operations.
- Not 'Runway condition code (RWYCC)' — that definition is crosswalked to RE, not ICE.  `[definition:IND-06]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not ICE.  `[definition:ECC-2180101]`
- Not 'Aircraft encountered vortex/wake turbulence' — that definition is crosswalked to TURB, not ICE.  `[definition:ECC-2220400]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.22).  `[parent:LOC-I]`

**Linked example reports**
- CEN24FA046: "AIRCRAFT INFORMATIONAccording to the airplane manufacturer’s pilot operating handbook (POH), during the preflight inspection, all snow, frost, and ice must be removed from all wing and control surfaces; the POH also states that on snow covered or icy runways the airplane must be sprayed with anti-icing fluid."
- ERA24LA094: "Whenever ground icing conditions are in effect, a pre-takeoff contamination check must be accomplished to ensure the aircraft is free of frost, ice or snow on the following surfaces: 1."
- WPR23FA080: "Additionally, the airplane’s BEFORE TAKEOFF checklist includes an ice accumulation check and includes the following specific guidance: Aerodynamic surfaces must be confirmed free of all forms of frost, ice, snow and slush prior to entering the takeoff runway or initiating takeoff."
- ANC10LA019: "The limitations section of the Cessna 208B flight manual supplement "Known Icing Equipment," states, in part: "Takeoff is prohibited with any frost, ice, snow, or slush adhering to the wings, horizontal stabilizer, vertical stabilizer, control surfaces, proper blades, or engine inlets." The limitations section also includes the following: "WARNING, EVEN SMALL AMOUNTS OF FROST, ICE, SNOW OR SLUSH ON THE WING MAY ADVERSELY CHANGE LIFT AND DRAG."
- CEN18LA077: "National Weather Service Forecast Icing Potential (FIP) and Current Icing Potential (CIP) products are intended to be supplemental to other icing advisories (AIRMET and SIGMET) that have been issued."
- WPR13FA041: "Cause: Aircraft-Aircraft oper/perf/capability-Performance/control parameters-Altitude-Not attained/maintained."
- ANC17TA015: "Probable cause: The pilot's continued flight into known icing conditions, which resulted in structural icing and a forced landing on icy, snow-covered terrain."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 pass · G8 pass · G9 pass

### B15 · Bird ingestion damaging an engine on takeoff or climb

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent BIRD Bird*

**Definition.** One or more birds are ingested into an engine during takeoff or initial climb, causing vibration, surging or loss of thrust.

**Include when**
- The occurrence meets the CICTT BIRD (Bird) definition.  `[parent:BIRD]`
- Core definition: One or more birds are ingested into an engine during takeoff or initial climb, causing vibration, surging or loss of thrust.  `[candidate:B15]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Matches 'Damaging bird strike' (FAA National Wildlife Strike Database – strike reporting): A collision with birds that damages the aircraft, such as a cracked windshield, dented radome or ingested engine, reported to the wildlife strike database.  `[definition:IND-39]`
- Matches 'Turbine engine ingestion - bird' (ECCAIRS 1.3.0.12 · Events (390) · 2140100 · Aircraft operation general › Object ingestion by engine): An event involving the ingestion of a bird by a turbine engine.  `[definition:ECC-2140100]`
- Narrative describes 'bird' (6 of 7 supporting reports).  `[report:DEN08FA072]`  
  > Probable cause: the impact with a bird during initial takeoff climb.
- Narrative describes 'collision' (3 of 7 supporting reports).  `[report:GAA19CA268]`  
  > Probable cause: The airplane’s collision with a bird during the initial climb, which resulted in the engine cowling separating and impacting the empennage.

**Exclude when**
- Belongs to sibling B16 'Bird strike damaging the windshield or nose on approach' when it matches that bucket better (1 report(s) assigned there).  `[report:DCA12CA043]`  
  > Photo of bird strike to radome Photo of Bird strike damage to right engine Photo of bird strike damage to E and E bay Photo of bird recovered from E and E bay
- Belongs to sibling C7 'Engine damage or shutdown after bird ingestion' when it matches that bucket better (4 report(s) assigned there).  `[report:ENG14IA005]`  
  > Probable cause: The initial damage to the fan blades was caused by the ingestion of two mallard ducks that caused one or more fan blades to fracture, striking the fan shroud, as well as other passing fan blades, producing various sized blades fragments that created a cascading effect of collateral impact damage to the other fan blades, the fan case, and the inlet cowl.
- Coded SCF-PP (System/Component Failure – Powerplant) rather than BIRD: similar wording, different occurrence category.  `[report:ERA13FA131]`  
  > The front engine was a Continental Motors TSIO-360A3B, 210-hp engine and the rear engine was a Continental Motors TSIO-360 AcAB, 210-hp engine.
- Coded CTOL (Collision with Obstacle(s) During Takeoff and Landing) rather than BIRD: similar wording, different occurrence category.  `[report:DEN08IA143]`  
  > Probable cause: The impact with a bird during initial takeoff climb.
- Coded ARC (Abnormal Runway Contact) rather than BIRD: similar wording, different occurrence category.  `[report:DCA14MA081]`  
  > In response, the first officer stated "engine thrust levers not set." FDR data indicate the thrust levers were briefly reduced to the climb detent then returned to the FLEX detent about 1 second later.
- Not 'Climb above the towing aircraft' — that definition is crosswalked to RAMP, not BIRD.  `[definition:ECC-2240202]`
- Not 'Tail strike' — that definition is crosswalked to ARC, not BIRD.  `[definition:IND-35]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.01).  `[parent:SCF-PP]`

**Linked example reports**
- CEN17LA136: "The 2,500-pound takeoff thrust JT15D-4 engine is similar in design and structure to the previously built 2,200-pound takeoff thrust JT15D-1 engine."
- DEN08FA072: "Probable cause: the impact with a bird during initial takeoff climb."
- GAA19CA268: "Probable cause: The airplane’s collision with a bird during the initial climb, which resulted in the engine cowling separating and impacting the empennage."
- ERA20CA058: "Probable cause: The airplane's impact by a bird during the initial climb."
- ERA24LA065: "Probable cause: An inflight collision with a bird during initial climb."
- GAA18CA345: "According to the flight instructor, a bird struck the airplane during takeoff, initial climb."
- CEN23LA203: "Probable cause: An inflight collision with a bird while on initial climb."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 FAIL · G8 pass · G9 pass

### B16 · Bird strike damaging the windshield or nose on approach

*Taxonomy version ntsb-draft-c94008cd21 · status grounded · parent BIRD Bird*

**Definition.** A large bird or flock strikes the windshield, radome or nose on approach or descent and causes visible damage.

**Include when**
- The occurrence meets the CICTT BIRD (Bird) definition.  `[parent:BIRD]`
- Core definition: A large bird or flock strikes the windshield, radome or nose on approach or descent and causes visible damage.  `[candidate:B16]`
- Matches 'Damaging bird strike' (FAA National Wildlife Strike Database – strike reporting): A collision with birds that damages the aircraft, such as a cracked windshield, dented radome or ingested engine, reported to the wildlife strike database.  `[definition:IND-39]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Matches 'Bird control' (ECCAIRS 1.3.0.12 · Events (390) · 5030500 · Aerodrome & ground aids › Aerodrome services / operations › Wildlife control): Bird control: an event related to the bird control at the aerodrome.  `[definition:ECC-5030500]`

**Exclude when**
- Belongs to sibling B15 'Bird ingestion damaging an engine on takeoff or climb' when it matches that bucket better (1 report(s) assigned there).  `[report:DEN08FA072]`  
  > The bird remains were identified as American White Pelican (Pelecanus erythrorhynchos), and the average mass for the bird is approximately 7,000 grams (15.4 pounds).
- Distinguish from sibling C7 'Engine damage or shutdown after bird ingestion' under the same parent.  `[sibling:C7]`
- Coded CTOL (Collision with Obstacle(s) During Takeoff and Landing) rather than BIRD: similar wording, different occurrence category.  `[report:CEN23FA160]`  
  > Inflight Bird Strike Damage Assessment Guidance The Department of the Air Force Instruction 91-212 Bird/Wildlife Aircraft Strike Hazard (BASH) Management Program provides guidance on inflight bird strike damage assessments and states in part: Aircrews experiencing enroute bird strikes should abort the mission when practicable.
- Not 'Helicopter damage caused by ground resonance' — that definition is crosswalked to LOC-G, not BIRD.  `[definition:ECC-2060300]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.57).  `[parent:LOC-I]`

**Linked example reports**
- CEN09MA117: "Probable cause: (1) the sudden loss of power to both engines that resulted from impact with a bird (red-tailed hawk), which fractured the windshield and interfered with engine fuel controls, and (2) the subsequent disorientation of the flight crewmembers, which left them unable to recover from the loss of power."
- CEN24FA094: "A review of data provided by AHAS showed that at the time of the accident the probability of bird strike in that area was deemed to be “low.” In addition, historic migration data used in the Bird Avoidance Model found the historical probability of bird strike at the time of the accident would have been “low.” In addition, another bird avoidance resource, BirdCast, uses a collaboration of radar and spotter information to provide near-real-time models of bird activity."
- DCA12CA043: "Photo of bird strike to radome Photo of Bird strike damage to right engine Photo of bird strike damage to E and E bay Photo of bird recovered from E and E bay"
- DCA13CA066: "On December 5, 2012, at approximately 1800 eastern standard time, a Bombardier CRJ200 operated by Air Wisconsin as USAirways Express flight 3852, experienced a bird strike while descending through 7,000 feet on approach to the New York LaGuardia Airport, New York."
- CEN14LA262: "Probable cause: An in-flight collision with a bird during the descent to land, which resulted in substantial damage to the airplane."
- ANC16LA034: "Bird Strike Avoidance The Aircraft Owners and Pilots Association (AOPA) Air Safety Institute has published Heard About The Bird?"
- ERA19FA170: "There was no requirement for bird strike resistance; therefore, bird penetration testing was not performed.."
- CEN13CA215: "Probable cause: A bird strike during a practice instrument approach in visual conditions."
- CEN25LA070: "Probable cause: Bird strike."
- GAA19CA180: "Probable cause: An in-flight collision with a bird during the approach, which resulted in damage to the vertical stabilizer."
- DCA21LA120: "Probable cause: a bird strike."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B17 · Lithium battery fire from a passenger device

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent SCF-PP System/Component Failure – Powerplant*

**Definition.** A phone, laptop, power bank or other lithium battery device overheats, smokes or catches fire in the cabin.

**Include when**
- The occurrence meets the CICTT SCF-PP (System/Component Failure – Powerplant) definition.  `[parent:SCF-PP]`
- Core definition: A phone, laptop, power bank or other lithium battery device overheats, smokes or catches fire in the cabin.  `[candidate:B17]`
- Matches 'Power loss in a reciprocating engine due to non-mechanical failure' (ECCAIRS 1.3.0.12 · Events (390) · 1850104 · Aircraft/system/component › 8500 Reciprocating engine › 8501 Reciprocating engine general): An event involving a power loss in a reciprocating engine due to non-mechanical failure.  `[definition:ECC-1850104]`
- Matches 'Turbine engine related event (ATA Code:7200)' (ECCAIRS 1.3.0.12 · Events (390) · 1720000 · Aircraft/system/component): (ATA Code:7200) An event involving the units and components which are used to induce and convert fuel-air mixture into power, and transmit power to the propeller shaft (if any) and accessory drives. Includes reports pertaining to bird strikes to engines/cowling.  `[definition:ECC-1720000]`
- Matches 'In-flight engine shutdown (IFSD)' (SKYbrary – In-Flight Shutdown): An engine is shut down in flight because of a failure or a precautionary indication such as low oil pressure, high vibration or fire.  `[definition:IND-28]`

**Exclude when**
- Distinguish from sibling B13 'Engine shutdown after loss of oil pressure' under the same parent.  `[sibling:B13]`
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than SCF-PP: similar wording, different occurrence category.  `[report:CEN18LA349]`  
  > The inflight emergency checklists for fire were: Engine Fire, Fuselage Fire, Wing Fire, and Electrical Fire.
- Coded LOC-I (Loss of Control – Inflight) rather than SCF-PP: similar wording, different occurrence category.  `[report:WPR18FA247]`  
  > The stall recovery technique while flying straight ahead or in a bank called for “firmly easing the control stick forward and, if necessary, applying opposite rudder and aileron.” The manual-provided instructions for spin recovery stated that with a rearward center of gravity, a steady spinning motion is possible that will stop within about ¼ and ½ rotation once the appropriate recovery technique has been applied.
- Coded OTHR (Other) rather than SCF-PP: similar wording, different occurrence category.  `[report:GAA19CA372]`  
  > The pilot suggested the passenger switch seats, and the passenger moved to the left rear passenger seat and fastened his seat belt.
- Not 'Smell - Passenger cabin - the presence of an unusual (not electrical) smell in the' — that definition is crosswalked to SCF-NP, not SCF-PP.  `[definition:ECC-1990143]`
- Not 'Lithium battery fire' — that definition is crosswalked to F-NI, CABIN, not SCF-PP.  `[definition:IND-31]`
- Not 'Smoke - Passenger cabin' — that definition is crosswalked to F-NI, SCF-NP, not SCF-PP.  `[definition:ECC-1990133]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.12).  `[parent:LOC-I]`

**Linked example reports**
- CEN13FA196: "At 1614:14, the pilot told the pilot-rated-passenger "we gotta get -- just pull -- just pull the power out." At 1614:18, the pilot-rated-passenger asked, "just pull it on down?" The pilot replied, "yeah, let's -- let's get back to two hundred (knots)." At 1614:21, the cockpit area microphone recorded another sound consistent with a decrease in engine speed."
- WPR14FA068: "Review of the video, recorded by passenger 8, indicated that the fatally injured passenger, passenger 3, exited the airplane under her own power while wearing an inflated life vest."
- DCA21FA085: "An engine fire warning would be accompanied by several indications, including an aural fire bell, the illumination of master WARNING lights, an EICAS warning message (FIRE ENG [L or R]), the illumination of the affected engine fire switch, unlocking of the engine fire switch, and the illumination of the engine FUEL CONTROL (L or R) switch fire warning light."
- CEN14LA441: "Subsequently, a dual battery design incorporated a simpler wiring harness where one battery would provide power to the engine components and a second battery served as a backup."
- ERA24FA110: "After the airplane came to rest, the cabin and emergency exits were blocked by fire and the cabin attendant coordinated the successful egress of her passengers and herself through the baggage compartment door in the tail section of the airplane."
- WPR18LA021: "He also installed two EARTHX-brand lithium-ion batteries as part of the modifications."
- ERA12LA085: "He then moved to the back of the cabin and he and the passenger pushed the raft out the main cabin door."
- ERA17FA195: "The third passenger did not egress, and the front seat passenger tried to go back toward the airplane, but the fire was too intense, and he was badly burned."
- DCA26FA274: "Other passengers were assisting and managed to pull the injured passenger back into the cabin."
- ERA20MA001: "The commercial pilot, airline transport pilot, and five passengers were fatally injured; the crew chief/flight engineer and four passengers were seriously injured; and one passenger and one person on the ground sustained minor injuries."
- ERA17TA233: "Since he was attempting to charge the battery with an incompatible charger, he thought that he probably started the flight with "low battery charge." Then, when the alternator was trying to recharge the battery, it overheated, and the battery subsequently shut down, resulting in a loss of electrical power to the airplane."
- ERA19LA253: "Probable cause: The pilot’s failure to properly secure the airplane electrical system’s positive/negative leads to the 24v battery, which resulted in a total loss of electrical and engine power in flight."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 FAIL · G9 pass

### B18 · Electrical smoke or burning smell in the flight deck

*Taxonomy version ntsb-draft-c94008cd21 · status grounded · parent F-NI Fire/Smoke (Non-Impact)*

**Definition.** Smoke, fumes or a burning electrical smell appears in the flight deck, often traced to wiring, a display or a window heater.

**Include when**
- The occurrence meets the CICTT F-NI (Fire/Smoke (Non-Impact)) definition.  `[parent:F-NI]`
- Core definition: Smoke, fumes or a burning electrical smell appears in the flight deck, often traced to wiring, a display or a window heater.  `[candidate:B18]`
- Matches 'Smoke or fumes in flight' (SKYbrary – Smoke and Fumes): Smoke, fumes or burning smells in the flight deck or cabin, often electrical in origin, handled with oxygen masks and the smoke checklist.  `[definition:IND-32]`
- Matches 'Fumes - APU' (ECCAIRS 1.3.0.12 · Events (390) · 1990129 · Aircraft/system/component › Non-component specific events › Explosions / fire/ fumes / smoke › Fumes): Fumes - APU  `[definition:ECC-1990129]`
- Matches 'Fumes - Avionics bay' (ECCAIRS 1.3.0.12 · Events (390) · 1990127 · Aircraft/system/component › Non-component specific events › Explosions / fire/ fumes / smoke › Fumes): Fumes - Avionics bay  `[definition:ECC-1990127]`

**Exclude when**
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than F-NI: similar wording, different occurrence category.  `[report:ERA18LA010]`  
  > The majority of insulation of the electrical wire from the bus bar to the avionics switch was melted or completely missing, while portions of insulation of the electrical wire from the "COM 2" circuit breaker to the avionics switch exhibited melting where it was located in proximity to the other electrical wire.
- Coded BIRD (Bird) rather than F-NI: similar wording, different occurrence category.  `[report:DCA24LA330]`  
  > The brief indicated that section 5.5.4 Engine Failure or Shutdown in the aircraft operating manual would be updated to indicate that if smoke enters the flight deck or cabin, flight crews should accomplish the Engine Fire or Engine Severe Damage or Separation steps of the QRC.
- Coded LOC-I (Loss of Control – Inflight) rather than F-NI: similar wording, different occurrence category.  `[report:CEN14LA441]`  
  > Cause: Aircraft-Aircraft systems-Electrical power system-Electrical pwr sys wiring-Failure.
- Not 'Electrical smell: to be used when the location of the electrical smell was not provided or' — that definition is crosswalked to SCF-NP, not F-NI.  `[definition:ECC-1990151]`
- Not 'Smell - Lavatory - the presence of an unusual (not electrical) smell in the lavatory' — that definition is crosswalked to SCF-NP, not F-NI.  `[definition:ECC-1990146]`
- Not 'Smell - Cockpit - the presence of an unusual (not electrical) smell in the cockpit' — that definition is crosswalked to SCF-NP, not F-NI.  `[definition:ECC-1990142]`
- Events better described by CICTT SCF-NP (System/Component Failure – Non-Powerplant) (runner-up parent, margin 0.14).  `[parent:SCF-NP]`

**Linked example reports**
- CEN22LA430: "Contributing to the accident were the incorrectly manufactured wiring support strip assembly that misrouted electrical wires near the collective control torque tube, the ambiguity of the support strip assembly drawing that allowed for its incorrect manufacturing, the inadequate quality control processes to identify the incorrectly manufactured support strip assembly, and the helicopter manufacturer’s inadequate assembly instructions that allowed the misrouting of the electrical wiring, due to the incorrectly manufactured strip assembly, on the helicopter production line."
- ERA24FA338: "About 1006, while the airplane was climbing to cruise altitude, the copilot stated that he could smell “something burning” and that it was “electrical,” then stated that it had “dissipated.” About one minute later, the copilot stated, “I definitely smell fire.” Immediately thereafter, audible alarms from various crew alerting system (CAS) messages could be heard, and the crew decided to divert to Jamestown Airport (JHW), Jamestown, New York."
- CEN12FA290: "The pilot told the passengers that the smell was normal for some heaters."
- CEN18LA349: "However, if circuit breaker protection does not prevent an electrical fire, and if electrical power is essential (as during instrument flight), try to identify and isolate the defective circuit as follows: 1."
- ERA19FA039: "We are issuing this AD to detect and correct a hazardous condition caused by deterioration of the combustion heater, which could lead to ignition of components and result in smoke and fumes in the cabin." The AD was required to be complied with within the next 10 hours of service of the combustion heater after May 5, 2017, or at the next scheduled annual inspection, which for the accident airplane would have occurred on July 14, 2017."
- ERA11FA312: "He went onto his deck, and saw smoke."
- WPR12LA402: "All wires appeared firmly attached to their respective posts on each electrically driven instrument, and no indication of smoke or thermal damage was observed."
- DCA11IA040: "The captain stated that the first item on the avionics smoke ECAM procedure was to don oxygen masks, but that he and the FO agreed not to don the masks because there was no smell of smoke."
- ENG10IA029: "Two thin electrical conductors, called bus bars, are installed on the upper and lower edges of the window to transmit electrical current from the power wires to the conductive heating film."
- DCA09IA018: "According to the first officer, after donning oxygen masks, he noted that “smoke was pouring out from the glare shield in front of my position and also appeared to be coming from below the glare shield between my legs.” After completing the Smoke and Fumes/Fire Electrical checklist, the first officer became “alarmed” when smoke did not cease from entering the cockpit after the left and right generators were turned off."
- WPR13LA122: "No electrical wiring diagram was recovered for the airplane, however, the configuration of the primary electrical system components appeared to match the manufacturer's “Basic Wiring Diagram” schematic."
- DCA25FA159: "Soon after arriving at the gate, flight attendants heard passengers yelling “fire” and “smoke” and saw smoke start to the fill the cabin."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B19 · Low fuel after holding or a diversion

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent NAV Navigation Error*

**Definition.** Extended holding, a missed approach or a diversion leaves the aircraft close to or below final reserve fuel, and the crew declares minimum fuel or a fuel emergency.

**Include when**
- The occurrence meets the CICTT NAV (Navigation Error) definition.  `[parent:NAV]`
- Core definition: Extended holding, a missed approach or a diversion leaves the aircraft close to or below final reserve fuel, and the crew declares minimum fuel or a fuel emergency.  `[candidate:B19]`
- Matches 'Lateral navigation error' (SKYbrary – Lateral Navigation Error): The aircraft leaves its cleared route because of a wrong route, waypoint or procedure loaded in the flight management system.  `[definition:IND-41]`
- Matches 'Aircraft navigation related event' (ECCAIRS 1.3.0.12 · Events (390) · 2170000 · Aircraft operation general): An event involving navigation of the aircraft.  `[definition:ECC-2170000]`

**Exclude when**
- Coded ATM (ATM/CNS) rather than NAV: similar wording, different occurrence category.  `[report:OPS12IA849]`  
  > At 1412:13, after being transferred back to PCT to be set up for another approach to DCA, the pilot of RPA3329 advised the PCT Final controller, "We really don't have the fuel for this...we gotta get on the ground here pretty quick." Information later provided by Republic Airlines stated that their company policy is for crews to advise ATC of "minimum fuel" when the aircraft's fuel state reached 3000 pounds, and "emergency fuel" at 2000 pounds.
- Coded LOC-I (Loss of Control – Inflight) rather than NAV: similar wording, different occurrence category.  `[report:CHI08FA282]`  
  > At 1835:55, N193BS transmitted, and Minneapolis three bravo sierra so for planning purposes uh (unintelligible) we are going to get radar vectors to the localizer three six.” At 1836:01, ZMP03 transmitted, “november three bravo sierra affirmative.” At 1904:49, ZMP03 transmitted, “a november three bravo sierra’s four south of dougy maintain three thousand five hundred til on a published portion of the approach cleared for the localizer three six approach arbor vitae.” At 1905:07, N193BS transmitted, “ah i got all that ah three thousand five hundred till on a published segment (unintelligible) cleared three six approach.” At 1905:13, ZMP03 transmitted, “November three bravo sierra roger and are you going to be able to shoot the approach from a couple south of the marker there.” At 1905:19, N193BS transmitted, “i’m sorry what.” At 1905:20, ZMP03 transmitted, “are you going to be able to make the approach from fifty two hundred from a couple south of the marker.” At 1905:29, the autopilot (AP) was selected OFF at a pressure altitude of 5,033 feet and a heading of 359 degrees magnetic.
- Coded MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) rather than NAV: similar wording, different occurrence category.  `[report:ANC16FA061]`  
  > Cause: Personnel issues-Psychological-Attention/monitoring-Monitoring other aircraft-Pilot of other aircraft.
- Not 'Minimum fuel and fuel emergency' — that definition is crosswalked to FUEL, not NAV.  `[definition:IND-33]`
- Not 'Undershoot' — that definition is crosswalked to USOS, not NAV.  `[definition:IND-37]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not NAV.  `[definition:ECC-2180101]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.04).  `[parent:SCF-PP]`

**Linked example reports**
- NYC08MA090: "HISTORY OF FLIGHT On February 1, 2008, about 1128 eastern standard time, a Raytheon Aircraft Company C90A, N57WR, was substantially damaged when it impacted terrain during a missed approach following an instrument approach to the Mount Airy/Surry County Airport (MWK), Mount Airy, North Carolina."
- OPS25LA048: "Audio recording provided by the FAA indicated that when the flight crew contacted NORCAL on the missed approach and explained the reason for the missed approach, the air traffic controller stated, “… news to me.” The NORCAL controller subsequently stated, “This is a big surprise to what you are saying, and we are trying to figure out on our side what is going on.” The flight crew confirmed they had adequate fuel to attempt another approach and, if necessary, be able to divert to the flight’s filed alternate airport."
- OPS18IA003: "Minimum Vectoring Altitude The FAA defines the MVA as "The lowest msl altitude at which an Instrument Flight Rules (IFR) aircraft may be vectored by a radar controller, except as otherwise authorized for radar approaches, departures, and missed approaches."
- ERA24FA136: "The CVR did not contain any cross check or verification of the altimeter setting from either member of the flight crew, nor did the crew conduct an approach briefing before beginning the approach."
- DCA14IA037: "FAA order 7110.65, "Air Traffic Control", stated, in part, that Air Route Traffic Control Centers (ARTCC) and approach controls may clear aircraft for visual approaches using the following procedures: "In those instances where airports are located in close proximity, also provide the location of the airport that may cause the confusion." When ATC communicated the airport location and provided an approach clearance to the flight crew, the approach controller did not provide the location of other airports in the area."
- DCA26FA194: "He stated that he expected to fly the final portion of the approach at 3 red and 1 white on the Precision Approach Path Indicator (PAPI)."
- OPS21LA003: "The alert stated that data indicate a potential for “unstable approaches” and “GPWS Terrain/Obstacle Warnings.” It further provided conditions that may result in an unstabilized approach with those conditions being “a steeper glidepath,” “Parking garage approximately 0.4 NM from RWY 27 threshold” and “high gross weight and tailwinds may require vertical speeds in excess of 1000 fpm during final approach segment.” Southwest Airlines General Approach Policies The Southwest Airlines B737NG Operating Manual, Section 11.1.3.1 provided, in part, the following general approach guidance: If available, follow glidepath guidance on final."
- ERA22FA004: "At 0539:28, as the flight was nearing the final approach fix and attempting to activate the pilot-controlled lighting, the captain stated in a frustrated tone, “would you fly the airplane- man-uhh man- I’ve been doing everything else.” A few seconds later, the captain stated, “here it is right over.” The captain subsequently stated, “fly the ILS approach.” The captain also noted that air brakes were stowed, flaps were set to 40°, and the before landing checklist was complete."
- CEN16LA076: "Power setting is appropriate for the aircraft configuration and is not below the minimum power for approach as defined by the aircraft operating manual; 7."
- WPR16FA059: "The airplane crossed Scaggs Island VOR, an initial approach fix on the runway 32 ILS approach, at 1837 and then turned to the LUSEE intersection, an intermediate fix on the approach located 12.2 nm from STS."
- GAA16LA128: "Missed Approaches FAA-H-8083-15B Instrument Flying Handbook also discusses missed approaches and states in part: A missed approach point is formulated for each published instrument approach and allows the pilot to return to the airway structure while remaining clear of obstacles."
- CEN19LA007: "He selected the left fuel tank while he maneuvered to land, but the airplane had a total loss of engine power while on final approach."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B20 · Pushback or towing collision

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** During pushback or towing the tug, towbar or aircraft strikes another aircraft, a vehicle or a fixed object.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: During pushback or towing the tug, towbar or aircraft strikes another aircraft, a vehicle or a fixed object.  `[candidate:B20]`
- Matches 'Loss of separation with aircraft - both airborne' (ECCAIRS 1.3.0.12 · Events (390) · 2180101 · Aircraft operation general › Aircraft - near collisions/loss of separation › Loss of separation between aircraft): This includes the AIRPROX defined as: A situation in which, in the opinion of a pilot or air traffic services personnel, the distance between aircraft as well as their relative positions and speed have been such that the safety of the aircraft involved may have been compromised. An aircraft proximity is classified as follows: Risk of collision. The risk classification of an aircraft proximity in which serious risk of collision has existed. Safety not assured. The risk classification of an aircraft proximity in which the safety of the aircraft may have been compromised. No risk of collision. The risk classification of an aircraft proximity in which no risk of collision has existed. Risk not determined. The risk classification of an aircraft proximity in which insufficient information was available to determine the risk involved, or inconclusive or conflicting evidence precluded such determination.  `[definition:ECC-2180101]`
- Matches 'Near collision with vehicle' (ECCAIRS 1.3.0.12 · Events (390) · 2180405 · Aircraft operation general › Aircraft - near collisions/loss of separation › Near collision with object on ground): An event a near collision by an aircraft with a vehicle.  `[definition:ECC-2180405]`
- Matches 'Loss of separation with no risk of collision' (ECCAIRS 1.3.0.12 · Events (390) · 2180105 · Aircraft operation general › Aircraft - near collisions/loss of separation › Loss of separation between aircraft): No risk of collision. The risk classification of an aircraft proximity in which no risk of collision has existed. Doc 4444.  `[definition:ECC-2180105]`

**Exclude when**
- Distinguish from sibling B07 'Loss of separation caused by an ATC clearance' under the same parent.  `[sibling:B07]`
- Distinguish from sibling B08 'TCAS resolution advisory after a level bust' under the same parent.  `[sibling:B08]`
- Distinguish from sibling B12 'GNSS interference or spoofing' under the same parent.  `[sibling:B12]`
- Coded GCOL (Ground Collision) rather than MAC: similar wording, different occurrence category.  `[report:SEA08LA061]`  
  > The UAL tug operator reported to SFO Airport Authority shortly after the collision that during the pushback process, he was looking over his shoulder and didn't see the other aircraft pushback from Gate 79.
- Not 'A standing or parked aircraft was struck/damaged by a vehicle/equipment' — that definition is crosswalked to ADRM, not MAC.  `[definition:ECC-5030704]`
- Not 'Collision of towed aircraft with object/obstacles' — that definition is crosswalked to RAMP, ADRM, not MAC.  `[definition:ECC-99010060]`
- Not 'Collision of a vehicle with an another vehicle or moveable equipment' — that definition is crosswalked to GCOL, ADRM, not MAC.  `[definition:ECC-5030701]`
- Events better described by CICTT GCOL (Ground Collision) (runner-up parent, margin 0.22).  `[parent:GCOL]`

**Linked example reports**
- DCA20IA081/2: "(b) No person may operate a small unmanned aircraft so close to another aircraft as to create a collision hazard."
- ANC16FA052: "When a rule of this section gives another aircraft the right-of-way, the pilot shall give way to that aircraft and may not pass over, under, or ahead of it unless well clear."
- ANC20LA074: "Therefore, it is likely the pilots of both aircraft could have maneuvered to avoid the collision if their aircraft were equipped with ATAS-capable devices conforming to DO 371B standards, and these devices were operational."
- ERA17FA143/2: "Cause: Personnel issues-Psychological-Attention/monitoring-Monitoring environment-Pilot of other aircraft."
- LAX08FA265: "According to the supplemental flight manual for the Skywatch, the purpose of the system was "to advise the pilot of transponder equipped aircraft that may pose a collision threat." The supplemental flight manual stated that the SkyWatch monitors a radius of approximately 6 nautical miles around the aircraft by interrogating transponders in the monitored area and determining if a collision threat exists."
- CEN22FA081: "Additionally, no person shall operate an ultralight vehicle in a manner that creates a collision hazard with respect to any aircraft."
- ANC16FA061: "Cause: Personnel issues-Psychological-Attention/monitoring-Monitoring other aircraft-Pilot of other aircraft."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 FAIL · G9 pass

### B21 · Disruptive or unruly passenger

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent CABIN Cabin Safety Events*

**Definition.** A passenger is aggressive, intoxicated or refuses crew instructions, interfering with the crew or other passengers.

**Include when**
- The occurrence meets the CICTT CABIN (Cabin Safety Events) definition.  `[parent:CABIN]`
- Core definition: A passenger is aggressive, intoxicated or refuses crew instructions, interfering with the crew or other passengers.  `[candidate:B21]`
- Matches 'Unruly or disruptive passenger' (ICAO Doc 10117 – Manual on the Legal Aspects of Unruly and Disruptive Passengers): A passenger who fails to respect rules of conduct or to follow crew instructions, disturbing good order and discipline on board.  `[definition:IND-30]`
- Matches 'Difficult / unruly passenger' (ECCAIRS 1.3.0.12 · Events (390) · 2230500 · Aircraft operation general › Security generally): Difficult / unruly passenger: includes aggressive behaviour, smoking, not following instructions, significant intoxication, indecent actions etc.  `[definition:ECC-2230500]`
- Matches 'Cabin crew - injuries sustained' (ECCAIRS 1.3.0.12 · Events (390) · 2030500 · Aircraft operation general › Cabin safety): Cabin crew sustained injuries that impacted on the ability to carry out the related duties.  `[definition:ECC-2030500]`

**Exclude when**
- Coded EVAC (Evacuation) rather than CABIN: similar wording, different occurrence category.  `[report:DCA15CA129]`  
  > The crew stated that they believed the delay in receiving response to their radio calls indicated ARFF personnel were busy addressing a safety concern and after hearing no further transmissions, the crew completed the evacuation checklist and advised passengers and cabin crew to proceed with evacuation.
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than CABIN: similar wording, different occurrence category.  `[report:ERA15IA198]`  
  > The crew evacuated the passengers and fire personnel double checked the airplane for any signs of continued fire or hot spots.
- Coded SCF-PP (System/Component Failure – Powerplant) rather than CABIN: similar wording, different occurrence category.  `[report:WPR14FA068]`  
  > One passenger was fatally injured, the airline transport pilot and two passengers were seriously injured, and five passengers received minor injuries.
- Not 'Fire - crew rest compartment' — that definition is crosswalked to F-NI, SCF-NP, not CABIN.  `[definition:ECC-99010083]`
- Not 'Fumes - Crew rest compartment' — that definition is crosswalked to F-NI, SCF-NP, not CABIN.  `[definition:ECC-99010088]`
- Not 'Smoke - Crew rest compartment' — that definition is crosswalked to F-NI, SCF-NP, not CABIN.  `[definition:ECC-99010087]`
- Events better described by CICTT EVAC (Evacuation) (runner-up parent, margin 0.10).  `[parent:EVAC]`

**Linked example reports**
- CEN11LA092: "According to crew statements, the injured passenger was designated as a wheelchair passenger and had boarded the airplane wearing an ankle brace."
- ERA09LA488: "According to the operator, the airplane was configured for 2 flight crew, 4 cabin crew, and 117 passengers."
- DCA16CA193: "There were 6 crew and 172 passengers on board."
- CEN09LA256: "The first officer made a similar announcement to the crew and passengers stressing the need to remain seated for their safety."
- ANC09IA015: "Upon arrival at Juneau the flight crew and one passenger, an off-duty airline employee, were taken to the local hospital to be tested for carbon monoxide (CO)."
- ERA23FA256: "An oxygen control valve switch could be used to direct the flow of oxygen to flight crew only or to both flight crew and passengers; this switch could also be used to manually drop the passenger oxygen masks if they did not drop automatically."
- DCA18CA219: "Of the 292 passengers and crew onboard, one flight attendant received minor injuries and one flight attendant received serious injuries."
- DCA18CA049: "Of the 57 passengers and crew onboard, one flight attendant was seriously injured."
- DCA15CA152: "According to flight crew statements, the seatbelt sign was illuminated and a public address announcement had been made to remain seated prior beginning the initial descent."
- DCA14CA090: "On March 4, 2014, about 2300 Pacific standard time, a flight attendant (FA) on Delta Air Lines flight 1248, a Boeing 737-900ER, N809DN, tripped over a passenger's bag while the passengers were boarding at San Diego International Airport (SAN), San Diego, California."
- ERA23LA135: "At 1544:26, after control of the airplane had been regained, the SIC stated, “we shouldn’t have had the autopilot on” and the PIC responded with, “yeah.” Moments after the in-flight upset, the flight crew were alerted by one of the passengers that another passenger had been seriously injured."
- DCA17CA096: "The remaining 114 passengers and crew were not injured."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 pass · G9 pass

### B22 · Tail strike on takeoff

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent RE Runway Excursion*

**Definition.** The tail strikes the runway during takeoff rotation, often after early or fast rotation or a wrong takeoff speed or weight.

**Include when**
- The occurrence meets the CICTT RE (Runway Excursion) definition.  `[parent:RE]`
- Core definition: The tail strikes the runway during takeoff rotation, often after early or fast rotation or a wrong takeoff speed or weight.  `[candidate:B22]`
- Matches 'Anomaly: Ground Excursion – Runway' (NASA ASRS coding taxonomy): An aircraft departs the runway surface during the takeoff or landing roll, including overruns after a long or fast landing.  `[definition:IND-07]`
- Matches 'Runway excursion (veer-off and overrun)' (SKYbrary – Runway Excursion): An aircraft leaves the runway surface during takeoff or landing, either by veering off the side or by overrunning the end.  `[definition:IND-05]`
- Matches 'Runway condition code (RWYCC)' (ICAO Global Reporting Format (GRF) for runway surface conditions): A runway condition code from 6 (dry) down to 0 reports braking performance on wet or contaminated runways (water, slush, snow, ice), so crews can recompute landing distance.  `[definition:IND-06]`

**Exclude when**
- Distinguish from sibling B04 'Overrun on a contaminated runway' under the same parent.  `[sibling:B04]`
- Coded OTHR (Other) rather than RE: similar wording, different occurrence category.  `[report:DCA10IA022]`  
  > The ACARS performance data included the following: takeoff weight 44,400 pounds, takeoff flap setting 20, FLEX 33 takeoff thrust setting (reduced thrust takeoff), V1 (takeoff decision speed) of 127 knots, and Vr (rotation speed) of 128 knots.
- Coded CTOL (Collision with Obstacle(s) During Takeoff and Landing) rather than RE: similar wording, different occurrence category.  `[report:ERA16FA257]`  
  > With a flap setting of 25°, the rotation speed for a short-field takeoff was between 50 and 60 KIAS.
- Coded ARC (Abnormal Runway Contact) rather than RE: similar wording, different occurrence category.  `[report:DCA14MA081]`  
  > As the captain taxied onto runway 27L, he noticed that runway 27R had been inserted into the FMC instead of runway 27L and requested that the first officer change the runway in the FMC, which was completed at 1823:10.
- Not 'Tail strike' — that definition is crosswalked to ARC, not RE.  `[definition:IND-35]`
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not RE.  `[definition:IND-03]`
- Not 'Hard landing, tail strike' — that definition is crosswalked to ARC, not RE.  `[definition:IND-18]`
- Events better described by CICTT CTOL (Collision with Obstacle(s) During Takeoff and Landing) (runner-up parent, margin 0.01).  `[parent:CTOL]`

**Linked example reports**
- DCA22MA009: "The captain briefed the rejected takeoff procedures, during which he stated that they would reject the takeoff after V1 “only if the airplane won’t fly.” (V1, also known as the decision speed, is defined, in part, as the maximum speed by which a rejected takeoff must be initiated to ensure that the airplane can be stopped on the remaining runway.) The captain and the first officer subsequently started the engines, and, at 0952:33, the TME air traffic controller provided their clearance to taxi to runway 36."
- WPR15FA125: "The pilot stated that once cleared for takeoff, he applied engine thrust and the engine spool-up, takeoff roll, and acceleration check speeds were as expected."
- WPR18LA179: "Ramp fuel weight = 966 lbs Takeoff fuel weight = 936 lbs The pilot provided both maximum allowable and calculated ramp and takeoff weights for the flight."
- CEN20TA031: "Regarding takeoff weight, it contains the following information: "…the effect of gross weight on takeoff distance is significant, and proper consideration of this item must be made in predicting the aircraft's takeoff distance."
- CEN10CA301: "After receiving a takeoff clearance he taxied the airplane onto the runway, aligning with the runway centerline with 3,300 feet of runway remaining."
- CEN20CA052: "Probable cause: The pilot's improper decision to take off with the airplane at a high gross weight from a short, turf runway, which degraded its climb performance and led to a delayed aborted takeoff, a runway excursion, and impact with terrain."
- CEN15LA149: "The passenger reported that although the airplane slowed considerably during the aborted takeoff, there was insufficient runway remaining for the airplane to come to a stop before the end of the runway."
- WPR18LA166: "At that weight, the airplane's takeoff distance was about 1,673 ft and the accelerate-stop-distance was about 3,040 ft; therefore, about 910 ft of runway should have remained during the aborted takeoff."
- WPR21LA110: "According to the airplane manufacturer, it is possible for the pilots to change FMS-suggested runway length or takeoff weight for the computation of takeoff speeds."
- CEN17LA029: "Probable cause: The pilot’s inadequate preflight planning, his decision to take off knowing the airplane was over its gross takeoff weight, and his failure to abort the takeoff after he realized that the airplane was not accelerating as expected, which resulted in a runway excursion."
- ANC16LA071: "He reported he calculated his takeoff weight at 3400 pounds with a "middle center of gravity location." The pilot stated that after conducting a pre-takeoff contamination check of the airplane, the flaps were set to 30 degrees, the trim set for takeoff, and the before takeoff checklist was completed."
- WPR19FA230: "The airplane operating manual stated, in part: On the ground, the amber no takeoff annunciator will illuminate steadily if one or more of the following conditions exist: Flaps not within takeoff range (less than 7° or more than 15°), elevator out of trim for takeoff, horizontal stabilizer is out of takeoff position, or speed brakes are out of takeoff position."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B23 · Windshear on final approach

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent LOC-I Loss of Control – Inflight*

**Definition.** A sudden change in wind speed or direction on approach, often near a thunderstorm or microburst, causes loss of airspeed and a windshear warning.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: A sudden change in wind speed or direction on approach, often near a thunderstorm or microburst, causes loss of airspeed and a windshear warning.  `[candidate:B23]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Matches 'Stall warning triggered' (ECCAIRS 1.3.0.12 · Events (390) · 2260500 · Aircraft operation general › Warning system triggered): Stall warning triggered  `[definition:ECC-2260500]`

**Exclude when**
- Belongs to sibling B05 'Stall warning or upset during a go-around' when it matches that bucket better (2 report(s) assigned there).  `[report:NYC08MA090]`  
  > At 11:17:37, the pilot was cleared for the “GPS runway three six approach, Mount Airy.” At 11:17:57, a conversation between the two pilots began regarding the approach and what altitudes they could descend to as they reached each designated navigational fix on the approach.
- Distinguish from sibling B24 'Landing short of the runway' under the same parent.  `[sibling:B24]`
- Distinguish from sibling B28 'Wrong route or waypoint loaded in the FMS' under the same parent.  `[sibling:B28]`
- Distinguish from sibling C4 'Upset or stall after unreliable airspeed' under the same parent.  `[sibling:C4]`
- Coded WSTRW (Windshear or Thunderstorm) rather than LOC-I: similar wording, different occurrence category.  `[report:WPR22LA251]`  
  > This document defined windshear as – “any rapid change in wind direction or velocity.” Severe windshear was defined as “a rapid change in wind direction or velocity causing airspeed changes greater than 15 knots or vertical speed changes greater than 500 feet per minute.” Text that followed these definitions stated the following: The primary focus of the Pilot Windshear Guide is directed toward windshear associated with convective weather conditions: thunderstorms, and in particular the most hazardous form of wind shear, the microburst.
- Coded ARC (Abnormal Runway Contact) rather than LOC-I: similar wording, different occurrence category.  `[report:DCA13FA131]`  
  > The first officer said that when they reached the final approach fix, the airplane was configured with the gear down and the flaps set at 30º.
- Coded RE (Runway Excursion) rather than LOC-I: similar wording, different occurrence category.  `[report:ERA16LA131]`  
  > The PF stated that he overshot the final approach and had to turn back toward the final runway centerline as the airplane was “pushed by the winds.” Additionally, the PF described the presence of moderate turbulence during the final approach.
- Not 'Low-level windshear' — that definition is crosswalked to WSTRW, not LOC-I.  `[definition:IND-36]`
- Not 'Aircraft encountered windshear' — that definition is crosswalked to WSTRW, not LOC-I.  `[definition:ECC-2220200]`
- Not 'Wake turbulence' — that definition is crosswalked to TURB, not LOC-I.  `[definition:IND-22]`
- Events better described by CICTT WSTRW (Windshear or Thunderstorm) (runner-up parent, margin 0.16).  `[parent:WSTRW]`

**Linked example reports**
- CHI08FA282: "At 1835:55, N193BS transmitted, and Minneapolis three bravo sierra so for planning purposes uh (unintelligible) we are going to get radar vectors to the localizer three six.” At 1836:01, ZMP03 transmitted, “november three bravo sierra affirmative.” At 1904:49, ZMP03 transmitted, “a november three bravo sierra’s four south of dougy maintain three thousand five hundred til on a published portion of the approach cleared for the localizer three six approach arbor vitae.” At 1905:07, N193BS transmitted, “ah i got all that ah three thousand five hundred till on a published segment (unintelligible) cleared three six approach.” At 1905:13, ZMP03 transmitted, “November three bravo sierra roger and are you going to be able to shoot the approach from a couple south of the marker there.” At 1905:19, N193BS transmitted, “i’m sorry what.” At 1905:20, ZMP03 transmitted, “are you going to be able to make the approach from fifty two hundred from a couple south of the marker.” At 1905:29, the autopilot (AP) was selected OFF at a pressure altitude of 5,033 feet and a heading of 359 degrees magnetic."
- CEN12LA345: ""Low-level wind shear is a sudden, drastic change in wind speed and/or direction over a very small area."
- WPR22FA068: "About 1 second later the copilot stated, “speed speed speed, more more, more more, faster, faster.” Soon after, the CVR indicated that the airplane impacted the terrain."
- WPR17FA023: "Additionally, the POH recommends "a slightly higher approach speed under turbulent air conditions." This is to compensate for any sudden loss in the headwind component, which would result in a momentary loss of airspeed and could lead to an aerodynamic stall above the published stall speed."
- DCA17FA109: "Most recently, during the ATP certificate checkride, on July 22, 2016, the captain received a notice of disapproval due to excessive deflection of both the glideslope and localizer for an instrument landing system approach, repeated glideslope and sink rate warnings from the ground proximity warning system, and his subsequent failure to initiate a go-around."
- CEN24FA064: "At 12:16:40, the controller issued a heading of 270°, and at 12:17:17 instructed the pilot to “turn right heading 030° maintain 4,300 until established on the final approach course, cleared RNAV runway 36 approach.” The KSJT RNAV runway 36 final approach course heading is 002° magnetic, or 6.7° true."
- OPS21LA003: "The alert stated that data indicate a potential for “unstable approaches” and “GPWS Terrain/Obstacle Warnings.” It further provided conditions that may result in an unstabilized approach with those conditions being “a steeper glidepath,” “Parking garage approximately 0.4 NM from RWY 27 threshold” and “high gross weight and tailwinds may require vertical speeds in excess of 1000 fpm during final approach segment.” Southwest Airlines General Approach Policies The Southwest Airlines B737NG Operating Manual, Section 11.1.3.1 provided, in part, the following general approach guidance: If available, follow glidepath guidance on final."
- CEN14FA438: "METEOROLOGICAL INFORMATIONAt 1535 the Automated Surface Observation System (AWOS) at 0F2 reported wind from 150 degrees at 9 knots gusting to 14 knots, wind direction 100 degrees variable 170 degrees, visibility 10 miles, sky clear, temperature 35 degrees Celsius (C), dew point temperature 17 degrees C, with an altimeter setting of 29.92 inches of mercury."
- ERA12FA007: "He noted the airplane was in a nose low descending turn (consistent with a turn onto final approach), and when it was on short final approach, the airplane was about 75 to 80 feet above ground level (agl) and east of a barn located south of the approach end of runway 36."
- CEN21FA209: "ADDITIONAL INFORMATIONStandard LNAV/VNAV Approach FAA Advisory Circular (AC) 91-89, Mitsubishi MU-2B Training Program, states that before the final approach fix, the airplane should be configured with 5° flaps and a minimum airspeed of 140 kts."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 FAIL · G9 pass

### B24 · Landing short of the runway

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent LOC-I Loss of Control – Inflight*

**Definition.** The aircraft touches down before the runway threshold, on the approach lights or in the undershoot area.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: The aircraft touches down before the runway threshold, on the approach lights or in the undershoot area.  `[candidate:B24]`
- Matches 'Aeroplane - spin' (ECCAIRS 1.3.0.12 · Events (390) · 2080400 · Aircraft operation general › Aeroplane flight path deviation): An event involving a spin by a fixed wing aircraft.  `[definition:ECC-2080400]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Matches 'Aeroplane - mush/stall' (ECCAIRS 1.3.0.12 · Events (390) · 2080300 · Aircraft operation general › Aeroplane flight path deviation): An event involving a mush/stall by a fixed wing aircraft.  `[definition:ECC-2080300]`

**Exclude when**
- Belongs to sibling B05 'Stall warning or upset during a go-around' when it matches that bucket better (1 report(s) assigned there).  `[report:NYC08MA090]`  
  > It was equipped with runway end identifier lights, medium intensity runway edge lights, and a 2-light precision approach path indicator.
- Belongs to sibling B23 'Windshear on final approach' when it matches that bucket better (2 report(s) assigned there).  `[report:CHI08FA282]`  
  > At 1835:55, N193BS transmitted, and Minneapolis three bravo sierra so for planning purposes uh (unintelligible) we are going to get radar vectors to the localizer three six.” At 1836:01, ZMP03 transmitted, “november three bravo sierra affirmative.” At 1904:49, ZMP03 transmitted, “a november three bravo sierra’s four south of dougy maintain three thousand five hundred til on a published portion of the approach cleared for the localizer three six approach arbor vitae.” At 1905:07, N193BS transmitted, “ah i got all that ah three thousand five hundred till on a published segment (unintelligible) cleared three six approach.” At 1905:13, ZMP03 transmitted, “November three bravo sierra roger and are you going to be able to shoot the approach from a couple south of the marker there.” At 1905:19, N193BS transmitted, “i’m sorry what.” At 1905:20, ZMP03 transmitted, “are you going to be able to make the approach from fifty two hundred from a couple south of the marker.” At 1905:29, the autopilot (AP) was selected OFF at a pressure altitude of 5,033 feet and a heading of 359 degrees magnetic.
- Distinguish from sibling B28 'Wrong route or waypoint loaded in the FMS' under the same parent.  `[sibling:B28]`
- Distinguish from sibling C4 'Upset or stall after unreliable airspeed' under the same parent.  `[sibling:C4]`
- Distinguish from sibling C8 'Takeoff after de-icing holdover time exceeded' under the same parent.  `[sibling:C8]`
- Coded LOC-G (Loss of Control – Ground) rather than LOC-I: similar wording, different occurrence category.  `[report:ERA21LA353]`  
  > In addition, due to the higher terrain at the approach end of the runway, the initial heading for the approach should be approximately 140 degrees until the aircraft is aligned with the runway on short final.
- Coded RI (Runway Incursion) rather than LOC-I: similar wording, different occurrence category.  `[report:DCA18IA081]`  
  > The captain stated that shortly after crossing the initial approach fix, the airplane exited the clouds and that he observed what he believed was runway 06 and runway lights, though according to his interview he questioned whether the runway lights were on bright or dim.
- Coded CFIT (Controlled Flight Into or Toward Terrain) rather than LOC-I: similar wording, different occurrence category.  `[report:ERA19FA070]`  
  > During the approach, the pilot described to the passenger that he needed to hit "markers" on the GPS he was using for navigation as the airplane approached the runway.
- Not 'Undershoot' — that definition is crosswalked to USOS, not LOC-I.  `[definition:IND-37]`
- Not 'Aircraft collision with approach/runway/taxiway lights' — that definition is crosswalked to GCOL, not LOC-I.  `[definition:ECC-2050403]`
- Not 'Undershoot' — that definition is crosswalked to USOS, not LOC-I.  `[definition:ECC-2010800]`
- Events better described by CICTT RI (Runway Incursion) (runner-up parent, margin 0.05).  `[parent:RI]`

**Linked example reports**
- GAA16LA128: "At least one of the following visual references for the intended runway is visible and identifiable to the pilot: Approach light system, threshold, threshold markings, threshold lights, runway end identifier lights, visual approach slope indicator, touchdown zone or touchdown zone markings, touchdown zone lights, runway or runway markings, and runway lights."
- ERA11FA412: "At 2148, the airplane reached a point about 1 nm southwest of the runway 05 threshold at HRJ, and was displaced about 0.3 nm from, and parallel to, the runway final approach course."
- CEN11FA195: "The runway has no lights or approach path light systems."
- CEN10FA027: "The missed approach point is the runway 23 runway threshold."
- CEN12FA097: "Area to be re-examined stated “Non-precision instrument approach” and “Loss of gyro attitude and heading indicators.” February 17, 2008 Flight instructor certificate issued with airplane single-engine land and instrument ratings."
- ERA17FA074: "The controller gave the pilot vectors to the final approach course, provided missed approach instructions (fly heading 070° and climb to 2,000 ft), and cleared the flight for the approach."
- CEN10FA557: "The controller told the pilot that the final approach course was not depicted on his radar display, to which the pilot replied, "Alright, well thank you very much." At 2007:14, the controller reissued the approach clearance and asked the pilot if he wanted to proceed to MIGPY intersection to complete the procedure turn to the final approach course."
- ERA18TA255: "A witness located on the airport's ramp reported that he "heard a high revving engine noise and turned towards the approach end of the runway and saw [a] small plane strike the [approach] lights." According to a Federal Aviation Administration (FAA) inspector who examined the airplane at the accident site, damage to the approach lighting system began with the elevated approach lights about 900 ft from runway 23 and continued to where the airplane came to rest about 400 ft short of the runway threshold."
- CEN10FA101: "The runway is equipped with high intensity runway lights (HIRL), and both runway ends have runway end identification lights (REIL)."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B25 · Airframe icing in flight

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent ICE Icing*

**Definition.** Ice builds on the wings, tail or windshield in flight in icing conditions, degrading performance or handling.

**Include when**
- The occurrence meets the CICTT ICE (Icing) definition.  `[parent:ICE]`
- Core definition: Ice builds on the wings, tail or windshield in flight in icing conditions, degrading performance or handling.  `[candidate:B25]`
- Matches 'Aircraft encountered icing conditions' (ECCAIRS 1.3.0.12 · Events (390) · 2220100 · Aircraft operation general › Weather encounters): Icing conditions: Weather conditions conducive to the formation of ice on an aircraft in flight. These conditions are usually characterized by visible moisture in the air and temperatures around the freezing level. Pilots encountering icing conditions are urged to issue a pilot weather report (PIREP) immediately.  `[definition:ECC-2220100]`
- Matches 'In-flight airframe icing' (FAA Advisory Circular 91-74B – Pilot Guide: Flight in Icing Conditions): Ice accumulates on wings, tail and windshield in supercooled cloud or freezing drizzle, increasing drag and stall speed.  `[definition:IND-38]`
- Matches 'Holdover time' (FAA holdover time guidelines (ground de-icing and anti-icing)): The estimated time a de-icing or anti-icing fluid protects aircraft surfaces from frost or ice; if it is exceeded before takeoff, the aircraft must be checked or de-iced again.  `[definition:IND-17]`

**Exclude when**
- Belongs to sibling B26 'Unreliable airspeed from blocked pitot probes' when it matches that bucket better (3 report(s) assigned there).  `[report:ERA14FA112]`  
  > The operating letter stated in part, that engine inlet anti-ice should be used during all flight in potential icing conditions and icing conditions should be considered to exist when flying in precipitation or visible moisture (including clouds or fog) with an outside air temperature 10 degrees Celsius or 50 degrees Fahrenheit (F), or colder.
- Distinguish from sibling B14 'Takeoff with frost or ice not removed' under the same parent.  `[sibling:B14]`
- Coded LOC-I (Loss of Control – Inflight) rather than ICE: similar wording, different occurrence category.  `[report:CEN12LA095]`  
  > Flight in freezing rain, freezing drizzle, or mixed icing conditions (supercooled liquid water and ice crystals) may result in ice build-up on protected surfaces exceeding the capability of the ice protection system, or may result in ice forming aft of the protected surfaces.
- Coded UIMC (Unintended Flight in IMC) rather than ICE: similar wording, different occurrence category.  `[report:ANC16FA023]`  
  > The base manager asked the pilot what kind of precipitation he was experiencing, and the pilot reported "wet snow." The base manager told the pilot "to do what he thought was best." The pilot responded that he would evaluate the icing conditions as he flew on the subsequent flights.
- Not 'Unreliable airspeed' — that definition is crosswalked to LOC-I, SCF-NP, not ICE.  `[definition:IND-09]`
- Not '5610 Flight compartment window' — that definition is crosswalked to SCF-NP, not ICE.  `[definition:ECC-1561000]`
- Not 'Aircraft wing structure related event (ATA Code:5700)' — that definition is crosswalked to SCF-NP, not ICE.  `[definition:ECC-1570000]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.11).  `[parent:LOC-I]`

**Linked example reports**
- CEN13FA130: "Cause: Environmental issues-Conditions/weather/phenomena-Temp/humidity/pressure-Conducive to structural icing-Ability to respond/compensate."
- CEN21FA238: "If an aircraft is not certificated for flight in icing conditions, each flight should be planned carefully so that icing conditions are avoided."
- ERA12FA115: "One of the flight crewmembers reported that the icing was the worst he had seen in 38 years of flying experience and that he had never seen ice accumulate so quickly."
- DCA14FA058: "When either of the ice detectors detect ice, an advisory message "ICE CONDITION" is shown on the EICAS display, a signal would be sent to the anti-ice system valves to activate them to open, and a signal would be sent to the full authority digital engine control to activate the automated engine icing thrust setting logic to limit the thrust to a minimum acceptable level."
- CEN21FA198: "Flight in freezing rain, freezing drizzle, or mixed icing conditions (supercooled liquid water and ice crystals) may result in ice build-up on protected surfaces exceeding the capability of the ice protection system, or may result in ice forming aft of the protected surfaces."
- CEN18FA144: "The airplane was not equipped with an anti-icing or deicing system, thus it was not equipped for flight in icing conditions."
- ANC23LA065: "FAA Advisory Circular AC 91-74B “Pilots Guide: Flight in Icing Conditions” provides pilots with a general reference on the principal factors related to flight in icing conditions and the location of additional information in related publications."
- WPR13FA072: "A "CAUTION" in the PA-31 POH/AFM stated "Do not overpower Autopilot pitch axis for periods longer than 3 seconds because the Autotrim System will operate in a direction to oppose the pilot and will, thereby, cause an increase in the pitch overpower forces." In addition, Paragraph 3.15 (Rough Air Operation) of Section 3(Emergency Procedures) of the PA-31 POH/AFM stated that "when flying in extreme turbulence or strong vertical currents and using the autopilot, the altitude-hold mode should not be used." The airplane was approved for flight into light to moderate icing when equipped with wing and empennage deicing boots, electric propeller deicers, electrically heated windshield, and an ice detection light."
- CEN19FA008: "The POH indicates that carburetor heat should be used to avoid a loss of engine power due to air filter icing and/or carburetor icing while the airplane is operating in inadvertent icing conditions, and that “an unexplained loss in manifold pressure could be caused by carburetor ice or air intake filter ice.” According to the Before Takeoff checklist, pilots are to verify the proper function of the carburetor heat before each flight."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### B26 · Unreliable airspeed from blocked pitot probes

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent ICE Icing*

**Definition.** Pitot probes blocked by ice, insects or covers give wrong airspeed indications, leading to warnings and autopilot disconnection.

**Include when**
- The occurrence meets the CICTT ICE (Icing) definition.  `[parent:ICE]`
- Core definition: Pitot probes blocked by ice, insects or covers give wrong airspeed indications, leading to warnings and autopilot disconnection.  `[candidate:B26]`
- Matches 'Aircraft encountered icing conditions' (ECCAIRS 1.3.0.12 · Events (390) · 2220100 · Aircraft operation general › Weather encounters): Icing conditions: Weather conditions conducive to the formation of ice on an aircraft in flight. These conditions are usually characterized by visible moisture in the air and temperatures around the freezing level. Pilots encountering icing conditions are urged to issue a pilot weather report (PIREP) immediately.  `[definition:ECC-2220100]`
- Matches 'Holdover time' (FAA holdover time guidelines (ground de-icing and anti-icing)): The estimated time a de-icing or anti-icing fluid protects aircraft surfaces from frost or ice; if it is exceeded before takeoff, the aircraft must be checked or de-iced again.  `[definition:IND-17]`
- Matches 'In-flight airframe icing' (FAA Advisory Circular 91-74B – Pilot Guide: Flight in Icing Conditions): Ice accumulates on wings, tail and windshield in supercooled cloud or freezing drizzle, increasing drag and stall speed.  `[definition:IND-38]`

**Exclude when**
- Belongs to sibling B14 'Takeoff with frost or ice not removed' when it matches that bucket better (1 report(s) assigned there).  `[report:ERA24LA094]`  
  > The POH stall speed table showed the indicated airspeed for a stall at the incident weight and flaps up was 63 kts.
- Belongs to sibling B25 'Airframe icing in flight' when it matches that bucket better (4 report(s) assigned there).  `[report:DCA14FA058]`  
  > The first officer indicated that the airplane was covered in ice, and the captain indicated observing “a lot of ice” on the leading edge of the wings.
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than ICE: similar wording, different occurrence category.  `[report:ERA10LA128]`  
  > The POH also stated that in the event of an airspeed indicator anomaly, if only the airspeed indicator was affected, it was reasonable to assume that a pitot tube blockage had occurred.
- Coded LOC-I (Loss of Control – Inflight) rather than ICE: similar wording, different occurrence category.  `[report:CEN12LA095]`  
  > Since the autopilot, when installed and operating, may mask tactile cues that indicate adverse changes in handling characteristics, use of the autopilot is prohibited when any of the visual cues specified above exist, or when unusual lateral trim requirements or autopilot trim warnings are encountered while the airplane is in icing conditions.
- Not 'Unreliable airspeed' — that definition is crosswalked to LOC-I, SCF-NP, not ICE.  `[definition:IND-09]`
- Not 'Stall warning triggered' — that definition is crosswalked to LOC-I, not ICE.  `[definition:ECC-2260500]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.01).  `[parent:LOC-I]`

**Linked example reports**
- ERA14FA112: "The anti-icing system included heated stall warning, rudder horn anti-ice, rudder tab anti-ice, generator inlet anti-ice, electrically heated wind shield, and pitot-static heaters."
- ERA24FA209: "Also, the use of autopilot was prohibited when certain icing indications were observed by the pilot, including an unusually extensive ice accumulation on the airframe and windshield in areas not normally observed to collect ice; accumulation of ice on the lower surface of the wing aft of the are protected by the de-icing system; or an accumulation of ice on the engine nacelles and propeller spinners farther aft than normally observed."
- CEN16LA076: "However, a warning in the airplane flight manual, in part, stated: Due to distortion of the wing airfoil, ice accumulations on the leading edges can cause a significant loss in rate of climb and in speed performance, as well as increases in stall speed."
- ANC21LA073: "The POH further stated, “the autopilot must be disconnected once every 10 minutes in icing conditions to check for any out-of-trim conditions caused by ice buildup.” Data obtained from the Garmin GFC 600 autopilot revealed that the autopilot was not disconnected every 10 minutes through the course of the flight as required."
- CEN16LA093: "Flight in freezing rain, freezing drizzle, or mixed icing conditions (supercooled liquid water and ice crystals) may result in ice build-up on protected surfaces exceeding the capability of the ice protection system, or may result in ice forming aft of the protected surfaces."
- ERA19FA039: "Review of the publicly-available National Weather Service Forecast Icing Potential (FIP) charts issued before the pilot's departure indicated a 30 to 70% probability of icing at 6,000 ft to 8,000 ft above the accident site at 1500."
- WPR24FA124: "This ice may not be shed using the ice protection systems, and may seriously degrade the performance and controllability of the airplane.” The POH further states, “Since the autopilot, when installed and operating, may mask tactile cues that indicate adverse changes in handling characteristics, use of the autopilot is prohibited when unusual lateral trim requirements or autopilot trim warnings are encountered while the airplane is in icing conditions.” The section “Procedures for Exiting the Severe Icing Environment” includes the following: - Immediately request priority handling from Air Traffic Control to facilitate a route or an altitude change to exit the severe icing conditions, in order to avoid extended exposure to flight conditions more severe than those for which the airplane has been certificated."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B27 · Crew crossed a hold-short line without clearance

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent RI Runway Incursion*

**Definition.** The flight crew taxis past a runway hold-short line without a clearance to enter or cross the runway (pilot deviation).

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: The flight crew taxis past a runway hold-short line without a clearance to enter or cross the runway (pilot deviation).  `[candidate:B27]`
- Matches 'Pilot deviation (runway incursion)' (FAA Runway Safety programme – Pilot deviation): A runway incursion caused by a pilot, such as crossing a hold-short line or entering a runway without an ATC clearance.  `[definition:IND-40]`
- Matches 'Vehicle or pedestrian deviation' (FAA Runway Safety programme): A runway incursion caused by a ground vehicle or a person, such as a driver or pedestrian entering a runway without ATC authorization.  `[definition:IND-19]`
- Matches 'Runway incursion types' (FAA Runway Safety programme): Runway incursions are classified by cause as pilot deviations, operational incidents (controller actions) or vehicle and pedestrian deviations, and by severity from A to D.  `[definition:IND-02]`

**Exclude when**
- Belongs to sibling B01 'Vehicle or pedestrian on the runway without clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:OPS09IA004]`  
  > HISTORY OF FLIGHT The Andrews Air Force Base (ADW) ground controller, working the ground control (GC), clearance delivery (CD), and flight data (FD) positions combined, authorized four vehicles to cross runway 19R without the local controller’s approval (LC) while VM206, a BE-20, was departing runway 19R.
- Belongs to sibling C1 'Landing or takeoff on an unintended surface' when it matches that bucket better (1 report(s) assigned there).  `[report:OPS09IA007]`  
  > The traditional taxi route for aircraft departing runway 6L was the ground controller directed aircraft to taxi via taxiway L, to taxiway N and then the local controller directed across runway 6R on taxiway N to a left turn on taxiway G to the approach end of runway 6L.
- Distinguish from sibling B02 'Landing on a taxiway or the wrong runway at night' under the same parent.  `[sibling:B02]`
- Coded GCOL (Ground Collision) rather than RI: similar wording, different occurrence category.  `[report:DCA26FA001]`  
  > Flight 5155 started its taxi, and while taxiing on taxiway A, the flight crew accomplished the taxi checklist, with the first officer calling out the checklist step and the captain verifying the step.
- Coded CFIT (Controlled Flight Into or Toward Terrain) rather than RI: similar wording, different occurrence category.  `[report:WPR26FA067]`  
  > At 2054:28, the controller instructed the flight crew to fly heading 310 descend and maintain 2,000, to which the flight crew responded with, “descend and maintain two three thousand, heading three one zero.” At 2054:42, the controller advised the flight crew, their assigned altitude is 2,000 and the heading was correct, which the flight crew acknowledged.
- Coded LOC-I (Loss of Control – Inflight) rather than RI: similar wording, different occurrence category.  `[report:WPR22FA068]`  
  > The controller asked the pilot if they wanted to cancel their IFR flight plan, to which the pilot replied, “yes sir.” The controller acknowledged that the IFR cancellation was received and instructed the pilot to overfly the field and enter left traffic for runway 27R and cleared them to land on runway 27R.
- Not 'Clearance - wrong aircraft' — that definition is crosswalked to ATM, not RI.  `[definition:ECC-4010704]`
- Not 'Clearance - wrong heading' — that definition is crosswalked to ATM, not RI.  `[definition:ECC-4010702]`
- Not 'Clearance - wrong speed' — that definition is crosswalked to ATM, not RI.  `[definition:ECC-4010703]`
- Events better described by CICTT GCOL (Ground Collision) (runner-up parent, margin 0.05).  `[parent:GCOL]`

**Linked example reports**
- DCA24FA164: "Local Controller Two instructed the flight crew of SWR17K to exit runway 4L on runway 31L with a good read back."
- OPS09IA009/2: "Probable cause: The local controller did not visually scan the runways and ensure that the E145 had crossed runway 24L prior to issuing a takeoff clearance to the DH8, did not ensure separation between the two airplanes, and did not cancel takeoff clearance for the DH8 in a timely manner."
- DCA24LA219: "The flight crew did not observe any equipment, markings, visual closed runway lighted “Xs” designations, or any other sign indicating that the runway was closed, and all equipment and people were clear of the runway."
- OPS25LA054: "The flight crew reported they made the appropriate advisory transmissions on the MBS common traffic advisory frequency (CTAF) as they taxied to runway 14 via taxiway “C” and taxiway “A.” During the taxi out to runway 14 the crew reported there “were no visible cues indicating a closure of the taxiways or runways.” As the flight was holding short of runway 14, the first officer contacted Great Lakes approach control and informed the controller that they were number one at runway 14 and ready for departure."
- DCA26LA242/2: "Delta Air Lines Flight 2351 (DAL2351) Flight Crew Statements Postincident statements provided by the DAL2351 flight crew revealed the first officer (FO) was the pilot flying and the captain was the pilot monitoring."
- OPS21LA003: "At 1746:02 The ATC tower controller stated, “do not overfly the aircraft on the runway.” According to the Southwest pilots’ interviews, the pilot monitoring unknowingly keyed the transmit button and stated, “how are we going to do that.” According to written statements from the SkyWest flight crew, the captain, after receiving clearance from the controller to line up and wait on runway 27 and that there was traffic on a 5-mile final, taxied into position for departure."
- DCA23LA125/2: "Contributing to the incident was the air traffic control tower team’s nondetection of the AAL106 crew’s deviation from taxi instructions while performing concurrent operational tasks; the timing of the runway status light system, which activated too late to prevent the AAL106 crew from crossing the runway hold short line; and American Airlines’ lack of adequate risk controls to prevent concurrent flight crew tasks from leading to distraction, loss of situational awareness, and deviation from an authorized taxi clearance."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 FAIL · G8 pass · G9 pass

### B28 · Wrong route or waypoint loaded in the FMS

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent LOC-I Loss of Control – Inflight*

**Definition.** The flight management system is loaded with the wrong route, waypoint or departure, and the aircraft deviates from its cleared route.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: The flight management system is loaded with the wrong route, waypoint or departure, and the aircraft deviates from its cleared route.  `[candidate:B28]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Matches 'Aeroplane - spin' (ECCAIRS 1.3.0.12 · Events (390) · 2080400 · Aircraft operation general › Aeroplane flight path deviation): An event involving a spin by a fixed wing aircraft.  `[definition:ECC-2080400]`
- Matches 'Aeroplane - mush/stall' (ECCAIRS 1.3.0.12 · Events (390) · 2080300 · Aircraft operation general › Aeroplane flight path deviation): An event involving a mush/stall by a fixed wing aircraft.  `[definition:ECC-2080300]`

**Exclude when**
- Distinguish from sibling B05 'Stall warning or upset during a go-around' under the same parent.  `[sibling:B05]`
- Distinguish from sibling B23 'Windshear on final approach' under the same parent.  `[sibling:B23]`
- Distinguish from sibling B24 'Landing short of the runway' under the same parent.  `[sibling:B24]`
- Coded UIMC (Unintended Flight in IMC) rather than LOC-I: similar wording, different occurrence category.  `[report:ANC17MA001]`  
  > Finding: Aircraft-Aircraft systems-Navigation system-Ground proximity system-Capability exceeded.
- Coded MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) rather than LOC-I: similar wording, different occurrence category.  `[report:ERA13LA022/2]`  
  > The flight lead's responsibilities include navigation, en route communication (between flight members, ATC, and supported units), obstacle and threat avoidance, wingmen position awareness, and the energy states of all aircraft.
- Coded CFIT (Controlled Flight Into or Toward Terrain) rather than LOC-I: similar wording, different occurrence category.  `[report:ANC23FA056]`  
  > In the event a company aircraft operating on a company flight plan is more than 60 minutes overdue from the latest ETA, or if an emergency signal is indicated by the aircraft flight following system.
- Not 'Lateral navigation error' — that definition is crosswalked to NAV, not LOC-I.  `[definition:IND-41]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not LOC-I.  `[definition:ECC-2180101]`
- Not 'Genuine airborne collision avoidance system/traffic alert and collision avoidance system warning' — that definition is crosswalked to MAC, not LOC-I.  `[definition:ECC-2260100]`
- Events better described by CICTT CFIT (Controlled Flight Into or Toward Terrain) (runner-up parent, margin 0.04).  `[parent:CFIT]`

**Linked example reports**
- ERA25FA082: "Finding: Aircraft-Aircraft systems-Flight control system-Aileron control system-Capability exceeded."
- CEN13FA196: "The pilot then explained how to promote KNUTE as the next active waypoint within the flight management system, and how to plan for the descent to the waypoint."
- CEN12FA670: "Over the intercom, the Flight Nurse heard the Flight Paramedic state that, "I'm not comfortable with this." At that time, the Flight Nurse turned to the right to look forward into the cockpit and the helicopter was in the clouds – totally "Whited Out." The Flight Nurse replied to the Paramedic, "Oh, I'm not either." She said that prior to the aircraft entering into the clouds the flight was normal, doing just fine and no issues."
- WPR17FA089: "Cause: Aircraft-Aircraft systems-Flight control system-Elevator control system-Incorrect service/maintenance."
- DCA11MA076: "Probable cause: The National Transportation Safety Board determines the probable cause(s) of this accident as follows: an aerodynamic stall and subsequent uncommanded roll during a one engine-inoperative takeoff flight test, which were the result of (1) Gulfstream’s failure to properly develop and validate takeoff speeds for the flight tests and recognize and correct the takeoff safety speed (V2) error during previous G650 flight tests, (2) the G650 flight test team’s persistent and increasingly aggressive attempts to achieve V2 speeds that were erroneously low, and (3) Gulfstream’s inadequate investigation of previous G650 uncommanded roll events, which indicated that the company’s estimated stall angle of attack while the airplane was in ground effect was too high."
- CEN21LA030: "Finding: Aircraft-Aircraft systems-Air conditioning system-Heating system-Damaged/degraded."
- ERA24FA371: "Finding: Aircraft-Aircraft systems-Flight control system-TE flap control system-Incorrect use/operation."
- ERA22LA120: "The pilot spent the next 3 minutes attempting to program the route of flight into the flight management system, and mentioned, “I can’t get [nothing] on this thing that I want.” On one occasion, the pilot asked the controller to clarify the name of the fix that they had been cleared to fly to in order to begin the approach (CIGOR or CIBAG), and on another occasion he asked the same question of the passenger."
- CEN10FA119: "After departure, the flight was cleared to SCHMD intersection before resuming the OZARK 3 departure procedure."
- ERA17FA190: "The briefings included weather observations, forecasts, and NOTAMs for the departure, destination, and selected en route stations; PIREPs (pilot reports); and in-flight weather advisories for the planned flight."
- CEN16LA230: "Contributing factor: Aircraft-Aircraft systems-Flight control system-Elevator control system-Malfunction."
- WPR24FA257: "The Primus APEX is composed of multiple subsystems including, but not limited to, the electronic display system, automatic flight control system, crew alerting system, flight management system, traffic alert and collision avoidance system, terrain awareness and warning system, and weather radar system."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### C1 · Landing or takeoff on an unintended surface

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent RI Runway Incursion*

**Definition.** The aircraft lands, lines up to land, or starts a takeoff on a surface other than the assigned runway: a taxiway, a closed or wrong runway, or the wrong airport.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: The aircraft lands, lines up to land, or starts a takeoff on a surface other than the assigned runway: a taxiway, a closed or wrong runway, or the wrong airport.  `[candidate:C1]`
- Matches 'Wrong-surface event' (FAA Runway Safety programme): A landing, attempted landing, line-up or takeoff on a surface other than the one assigned: a wrong runway, a taxiway, a closed runway or the wrong airport.  `[definition:IND-03]`
- Matches 'Anomaly: Ground Incursion – Runway or Taxiway' (NASA ASRS coding taxonomy): An aircraft, vehicle or person entering a runway or taxiway without authorization, or an aircraft using a taxiway or the wrong runway for landing or takeoff.  `[definition:IND-04]`
- Matches 'Runway incursion' (ICAO Doc 9870, Manual on the Prevention of Runway Incursions): Any occurrence at an aerodrome involving the incorrect presence of an aircraft, vehicle or person on the protected area of a surface designated for the landing and takeoff of aircraft.  `[definition:IND-01]`
- Narrative describes 'enter' (3 of 7 supporting reports).  `[report:OPS16IA004]`  
  > Airport Runway Status Lights System FLL runway 28R was equipped with RWSLs, a "fully automated system that provides runway status information to pilots and surface vehicle operators to clearly indicate when it is unsafe to enter, cross, takeoff from, or land on a runway." When operational, RWSLs have two states; ON (lights are illuminated red) and OFF (lights are off), and are switched automatically based on input from the ASDE-X system and independent of air traffic controllers.

**Exclude when**
- Belongs to sibling B01 'Vehicle or pedestrian on the runway without clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:OPS16IA008]`  
  > As AAL2408 began its takeoff roll the Runway Status Lights (RWSLs) on runway 35L activated illuminating the Runway Entrance Lights (RELs) at the hold short locations of the three aircraft that had just been instructed to cross runway 35L, as well as the Takeoff Hold Lights (THLs) at the approach end of the runway.
- Belongs to sibling B02 'Landing on a taxiway or the wrong runway at night' when it matches that bucket better (2 report(s) assigned there).  `[report:DCA26MA161]`  
  > R35 entered taxiway BB, another airplane that had landed on runway 4 crossed taxiway D, and Jazz flight 646 was about 3.7 nautical miles from taxiway D and at 1,180 ft altitude.
- Distinguish from sibling B27 'Crew crossed a hold-short line without clearance' under the same parent.  `[sibling:B27]`
- Coded ADRM (Aerodrome) rather than RI: similar wording, different occurrence category.  `[report:OPS08IA007/2]`  
  > About 18 seconds later, the local controller received an aural and visual alert from the ASDE-X stating, "Warning, Runway 3-4-Right, Occupied" was generated on the controller's display and the corresponding alert text "RWY 34R | NWA106 TRS227 | RWY OCCUPIED" was displayed when TRS227 crossed the taxiway hold short lines, and proceeded across the runway edge line onto runway 34R.
- Coded ATM (ATM/CNS) rather than RI: similar wording, different occurrence category.  `[report:OPS11IA673/2]`  
  > Probable cause: the Gulfport control tower local controller cleared two aircraft for takeoff from runways with intersecting departure flight paths without ensuring the first aircraft had passed the flight path intersection prior to clearing the second aircraft for takeoff.
- Not 'Undershoot' — that definition is crosswalked to USOS, not RI.  `[definition:ECC-2010800]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not RI.  `[definition:IND-07]`
- Not 'Runway excursion (veer-off and overrun)' — that definition is crosswalked to RE, not RI.  `[definition:IND-05]`
- Events better described by CICTT ADRM (Aerodrome) (runner-up parent, margin 0.49).  `[parent:ADRM]`

**Linked example reports**
- OPS09IA007: "The traditional taxi route for aircraft departing runway 6L was the ground controller directed aircraft to taxi via taxiway L, to taxiway N and then the local controller directed across runway 6R on taxiway N to a left turn on taxiway G to the approach end of runway 6L."
- OPS18IA014: "During the conversation, the chief pilot reported the pilot of ENY3660 had reported that as the aircraft was abeam taxiway U, the vehicle was off the runway surface but between the runway edge marking and the hold short lines on taxiway U and that there was no overflight."
- OPS09IA008: "BOS has six asphalt runways: runway 4L/22R is 7,861 ft in length by 150 ft in width; runway 4R/22L is 10,005 ft in length by 150 ft in width; runway 9/27 is 7,000 ft in length by 150 ft in width; runway 14/32 is 5,000 ft in length by 100 ft in width; runway 15L/33R is 2,557 in length by 100 ft in width; and runway 15R/33L is 10,083 ft in length by 150 ft in width."
- OPS16IA004: "Airport Runway Status Lights System FLL runway 28R was equipped with RWSLs, a "fully automated system that provides runway status information to pilots and surface vehicle operators to clearly indicate when it is unsafe to enter, cross, takeoff from, or land on a runway." When operational, RWSLs have two states; ON (lights are illuminated red) and OFF (lights are off), and are switched automatically based on input from the ASDE-X system and independent of air traffic controllers."
- DCA23LA185: "At 1855:50, SKW5326 began its take-off roll, and then at 1855:53, the LC responded to the crew of ASH5826, “… affirmative, runway 33 cleared to land.” According to FAA Order 7110.65Z, the controller was required to apply a 6,000 feet separation between a departing aircraft on its takeoff roll and an arriving aircraft on final approach."
- OPS11IA273: "According to the DEN ASDE-X playback, OPS6 entered runway 34R at taxiway WC at approximately 1333:40 and proceed down runway 34R while ACA1072 was in takeoff position on the runway."
- OPS17IA008: "• Runway Entrance Lights (RELs) provide signal to aircraft crossing entering runway from intersecting taxiway • Takeoff Hold Lights (THLs) provide signal to aircraft in position for takeoff" RELs The FAA website stated the following, in part: Runway Entrance Lights are a string of lights located around the center of taxiways/runway crossings and illuminate red when there is high-speed traffic on or approaching the runway to signal that it is unsafe to enter the runway."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### C2 · Runway entry or crossing without clearance

*Merged into B01 before grounding.*

### C3 · Overrun after a long or fast landing on a wet or contaminated runway

*Merged into B04 before grounding.*

### C4 · Upset or stall after unreliable airspeed

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent LOC-I Loss of Control – Inflight*

**Definition.** Disagreeing or erroneous airspeed indications, for example from icing or pitot failure, lead to a stall warning, overspeed or upset in flight.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: Disagreeing or erroneous airspeed indications, for example from icing or pitot failure, lead to a stall warning, overspeed or upset in flight.  `[candidate:C4]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`
- Matches 'Stall warning triggered' (ECCAIRS 1.3.0.12 · Events (390) · 2260500 · Aircraft operation general › Warning system triggered): Stall warning triggered  `[definition:ECC-2260500]`
- Matches 'Stall prevention and recovery' (FAA Advisory Circular 120-109A – Stall Prevention and Recovery Training): Training to recognise and recover from approaches to stall and full stalls, including during go-arounds with high thrust and pitch.  `[definition:IND-21]`

**Exclude when**
- Belongs to sibling B05 'Stall warning or upset during a go-around' when it matches that bucket better (5 report(s) assigned there).  `[report:ERA24FA001]`  
  > The airplane’s stall warning system sustained impact-related damage that precluded any postaccident functional testing.
- Distinguish from sibling B23 'Windshear on final approach' under the same parent.  `[sibling:B23]`
- Distinguish from sibling B24 'Landing short of the runway' under the same parent.  `[sibling:B24]`
- Distinguish from sibling B28 'Wrong route or waypoint loaded in the FMS' under the same parent.  `[sibling:B28]`
- Coded ARC (Abnormal Runway Contact) rather than LOC-I: similar wording, different occurrence category.  `[report:CEN16LA076]`  
  > However, a warning in the airplane flight manual, in part, stated: Due to distortion of the wing airfoil, ice accumulations on the leading edges can cause a significant loss in rate of climb and in speed performance, as well as increases in stall speed.
- Not 'In-flight airframe icing' — that definition is crosswalked to ICE, not LOC-I.  `[definition:IND-38]`
- Not 'Aircraft encountered icing conditions' — that definition is crosswalked to ICE, not LOC-I.  `[definition:ECC-2220100]`
- Not 'Holdover time' — that definition is crosswalked to ICE, not LOC-I.  `[definition:IND-17]`
- Events better described by CICTT ICE (Icing) (runner-up parent, margin 0.47).  `[parent:ICE]`

**Linked example reports**
- CEN12LA095: "Minimum Airspeed for Sustained Icing Flight...140 knots Sustained flight in icing conditions with flaps extended is prohibited except for approach and landings."
- ERA11FA493: "This low pressure would create a differential pressure in the stall warning system, which would draw air through the warning horn, and would result in an audible warning between 5 to 10 miles per hour above the stall in all configurations."
- WPR10LA059: "Coping with the hazards of icing begins with preflight planning to determine where icing may occur during a flight and ensuring the aircraft is free of ice and frost prior to takeoff.” “Because of their small size and shape, antennas that do not lay flush with the aircraft’s skin tend to accumulate ice rapidly."
- ERA19LA072: "Also causal was the pilot’s failure to maintain an appropriate airspeed for flight in icing conditions."
- CEN10MA088: "I don't think that spoileron thing is working for some reason." Post-accident performance studies indicated that the airplane's N1 and true airspeed decreased, and bank angle increased to greater than 50 degrees."
- WPR12FA059: "Review of the pilot's flight logbook indicated a total flight experience of about 713 hours."
- WPR16FA067: "115 km/h (62 kts) should be maintained." Aviation Circular 23-8C Flight Test Guide states that the following formula can be used to calculate the stall airspeed when the airplane's weight is different than the specified weight, Vs=Vstv(Ws/Wt) where Vs= new stall airspeed, Vst= standard stall airspeed, Ws= new weight, Wt = standard weight."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### C5 · TCAS resolution advisory after an altitude deviation

*Merged into B08 before grounding.*

### C6 · Clear-air turbulence with cabin injuries

*Taxonomy version ntsb-draft-c94008cd21 · status grounded · parent TURB Turbulence Encounter*

**Definition.** An unexpected encounter with turbulence in clear air injures passengers or cabin crew who are standing, unbelted or near unsecured carts.

**Include when**
- The occurrence meets the CICTT TURB (Turbulence Encounter) definition.  `[parent:TURB]`
- Core definition: An unexpected encounter with turbulence in clear air injures passengers or cabin crew who are standing, unbelted or near unsecured carts.  `[candidate:C6]`
- Matches 'Aircraft encounter with turbulence' (ECCAIRS 1.3.0.12 · Events (390) · 2220600 · Aircraft operation general › Weather encounters): Encounter with any or all of a) clear air turbulence (CAT) b) turbulence in cloud c) vortex / wake turbulence also to be used in events in which the aircraft was damaged by turbulence. CAT: Clear Air Turbulence (CAT) is the bumpiness experienced by aircraft at high altitudes (above 18,000 feet) in either cloud- free conditions or in stratiform clouds. CAT occurs when undulations (known as gravity waves) in the upper atmosphere become steep and unstable, then break down into chaotic motion. The scale of wave motion that normally affects jet aircraft is on the order of ~10 meters to ~1-2 kilometers. These unstable waves occur when vertical wind shear becomes locally excessive, allowing the waves to overcome the stability of environmental temperature conditions. This condition is known as Kelvin-Helmholtz instability. Most CAT occurs on the fringes of (not within the core of) the jet stream, in the vicinity of upper level frontal zones where temperature contrasts are strong. CAT may also occur when strong winds cross a mountain range in certain thermal conditions, allowing gravity waves to amplify and propagate vertically toward the stratosphere. These 'mountain waves' may be smooth undulations, resulting in updrafts and downdrafts (UDDF in pilot report code), or can break down into smaller scale turbulence. A third instance in which CAT occurs is when strong winds encounter the tops of thunderstorm clouds, resulting in strong shear waves that extend well downstream from the convective cloud.  `[definition:ECC-2220600]`
- Matches 'Clear-air turbulence (CAT)' (SKYbrary – Clear Air Turbulence): Turbulence in cloud-free air, often near jet streams or over mountains, with no visual cue and often not shown on weather radar.  `[definition:IND-13]`
- Matches 'Turbulence-related injuries' (FAA Advisory Circular 120-88A – Preventing Injuries Caused by Turbulence): Passengers and flight attendants are injured in turbulence mainly when standing or not wearing seat belts, and by unsecured carts and galley equipment.  `[definition:IND-14]`
- Narrative describes 'encounter' (12 of 12 supporting reports).  `[report:ERA09LA488]`  
  > Meteorological Conditions in Vicinity of Turbulence Encounter The 1600 NWS radar composite reflectivity mosaic image depicted several defined echoes associated with thunderstorms north of the departure airport, including a short but intense line at the latitude and longitude of the turbulence encounter, but below the airplane's altitude.
- Narrative describes 'turbulence' (11 of 12 supporting reports).  `[report:ERA09LA488]`  
  > Meteorological Conditions in Vicinity of Turbulence Encounter The 1600 NWS radar composite reflectivity mosaic image depicted several defined echoes associated with thunderstorms north of the departure airport, including a short but intense line at the latitude and longitude of the turbulence encounter, but below the airplane's altitude.
- Narrative describes 'air' (6 of 12 supporting reports).  `[report:DCA16CA209]`  
  > On August 3, 2016 at 7:45 pm eastern daylight time, American Airlines flight 1007, an Airbus A319, N9010R, encountered clear air turbulence on descent to the Owen Roberts International Airport (GCM), George Town, Cayman Islands.

**Exclude when**
- Distinguish from sibling B06 'Wake turbulence upset on approach' under the same parent.  `[sibling:B06]`
- Not 'Cabin crew - injuries sustained' — that definition is crosswalked to CABIN, not TURB.  `[definition:ECC-2030500]`
- Not 'Cabin crew unable to perform duties - medical (non-injury) reasons' — that definition is crosswalked to CABIN, MED, not TURB.  `[definition:ECC-2030400]`
- Events better described by CICTT CABIN (Cabin Safety Events) (runner-up parent, margin 0.74).  `[parent:CABIN]`

**Linked example reports**
- ERA09LA488: "Meteorological Conditions in Vicinity of Turbulence Encounter The 1600 NWS radar composite reflectivity mosaic image depicted several defined echoes associated with thunderstorms north of the departure airport, including a short but intense line at the latitude and longitude of the turbulence encounter, but below the airplane's altitude."
- DCA16CA209: "On August 3, 2016 at 7:45 pm eastern daylight time, American Airlines flight 1007, an Airbus A319, N9010R, encountered clear air turbulence on descent to the Owen Roberts International Airport (GCM), George Town, Cayman Islands."
- DCA23LA096: "At 1013:43, the flight crew made a passenger announcement about the turbulence encounter."
- DCA24FA143: "After the turbulence encounter, the A FA walked through the cabin to inspect for damage and check for injuries."
- DCA10CA032: "After encountering the turbulence, the crew assessed airplane damage and checked the number and severity of injuries to passengers and crew."
- CEN14CA455: "While cruising in smooth air conditions with no clouds in the area and with the autopilot on and the seat belt sign off the airplane had a brief encounter with what the flight crew described as wake turbulence."
- DCA12FA069: "COMMUNICATIONS Following the turbulence encounter, the flight crew was unable to establish communications with company dispatch or station personnel to alert emergency crews."
- CEN09LA388: "On June 15, 2009, about 1652 mountain daylight time (mdt), a Beech B100 (King Air) airplane, N4490M, operated by Air Methods Corporation, encountered clear-air-turbulence while descending through 7,000 feet mean sea level (msl) en route to Rapid City Regional Airport (KRAP), Rapid City, South Dakota."
- DCA14CA014: "While cruising at FL360 in smooth air conditions with no storms in the vicinity, the airplane experienced a 3 to 5 second encounter with clear air turbulence."
- DCA23LA421: "Probable cause: An inadvertent encounter with clear air turbulence during cruise flight."
- CEN22LA166: "Probable cause: The airplane’s encounter with severe clear air turbulence that was not forecasted, which resulted in a serious injury to an unrestrained passenger."
- CEN10LA189: "Probable cause: A clear air turbulence encounter during cruise flight, during which an unrestrained cabin flight attendant sustained a hip fracture."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C7 · Engine damage or shutdown after bird ingestion

*Taxonomy version ntsb-draft-c94008cd21 · status not grounded · parent BIRD Bird*

**Definition.** Birds ingested into an engine cause vibration, surge, loss of thrust, fire warning or shutdown.

**Include when**
- The occurrence meets the CICTT BIRD (Bird) definition.  `[parent:BIRD]`
- Core definition: Birds ingested into an engine cause vibration, surge, loss of thrust, fire warning or shutdown.  `[candidate:C7]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Matches 'Damaging bird strike' (FAA National Wildlife Strike Database – strike reporting): A collision with birds that damages the aircraft, such as a cracked windshield, dented radome or ingested engine, reported to the wildlife strike database.  `[definition:IND-39]`
- Matches 'Turbine engine ingestion - bird' (ECCAIRS 1.3.0.12 · Events (390) · 2140100 · Aircraft operation general › Object ingestion by engine): An event involving the ingestion of a bird by a turbine engine.  `[definition:ECC-2140100]`

**Exclude when**
- Belongs to sibling B15 'Bird ingestion damaging an engine on takeoff or climb' when it matches that bucket better (2 report(s) assigned there).  `[report:CEN17LA136]`  
  > Probable cause: An in-flight collision with multiple birds, which resulted in separation of the right engine's fan rotor and subsequent total loss of power of the right engine.
- Belongs to sibling B16 'Bird strike damaging the windshield or nose on approach' when it matches that bucket better (2 report(s) assigned there).  `[report:DCA12CA043]`  
  > Photo of bird strike to radome Photo of Bird strike damage to right engine Photo of bird strike damage to E and E bay Photo of bird recovered from E and E bay
- Coded CTOL (Collision with Obstacle(s) During Takeoff and Landing) rather than BIRD: similar wording, different occurrence category.  `[report:CEN23FA160]`  
  > Inflight Bird Strike Damage Assessment Guidance The Department of the Air Force Instruction 91-212 Bird/Wildlife Aircraft Strike Hazard (BASH) Management Program provides guidance on inflight bird strike damage assessments and states in part: Aircrews experiencing enroute bird strikes should abort the mission when practicable.
- Coded SCF-PP (System/Component Failure – Powerplant) rather than BIRD: similar wording, different occurrence category.  `[report:DCA21FA085]`  
  > An engine fire warning would be accompanied by several indications, including an aural fire bell, the illumination of master WARNING lights, an EICAS warning message (FIRE ENG [L or R]), the illumination of the affected engine fire switch, unlocking of the engine fire switch, and the illumination of the engine FUEL CONTROL (L or R) switch fire warning light.
- Not 'Turbine engine - vibration' — that definition is crosswalked to SCF-PP, not BIRD.  `[definition:ECC-1720109]`
- Not 'Turbine engine chip warning' — that definition is crosswalked to SCF-PP, not BIRD.  `[definition:ECC-1720113]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.37).  `[parent:SCF-PP]`

**Linked example reports**
- ENG14IA005: "The engine and airplane met the applicable bird and containment design standards since the engine did not catch on fire, no engine cases exhibited any penetrations, the engine was able to be shutdown normally, and the airplane damage did not impact the safe operation of the airplane or create a hazard to the persons on board."
- CEN09IA481: "The requirements stated the engine is acceptable if it ingested the bird and “demonstrated freedom from explosion, disintegration, or uncontrollable fire.” AC-33-1B further stated that it would be acceptable if the engine required shutdown."
- ENG11IA051: "ADDITIONAL INFORMATION Bird Ingestion Requirements The PW2037 was certified under Part 33, Amendment 6 and the bird ingestion requirement at that time in Part 33.77 Foreign Object Ingestion was for a 4-pound bird."
- ENG22LA002: "Probable cause: The ingestion of a bird into the right engine during the takeoff roll caused a fan blade to fracture near the blade platform resulting in high fan blade off loads and engine vibrations sufficient to result in an eventual failure of a fuel tube in the right engine that sprayed fuel onto hot engine cases, igniting an undercowl engine fire and triggering a rejected takeoff."
- CEN10IA053: "Inspection disclosed damage to both engine inlet cowlings, but boroscope examination revealed only the right engine, a General Electric CFM56-5B5P, had sustained internal damage."
- DCA26LA106: "The right engine had damage to the inlet cowl acoustic liner and bird remnants were found on the spinner and the exhaust nozzle."
- ENG14IA013: "2 engine fire following a bird strike during takeoff roll at Sugar Land Regional Airport (SGR), Sugar Land, Texas."
- ENG14IA011: "2 engine inlet that was consistent with bird remains."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 FAIL · G9 pass

### C8 · Takeoff after de-icing holdover time exceeded

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent LOC-I Loss of Control – Inflight*

**Definition.** The aircraft is delayed after ground de-icing and the fluid holdover time is exceeded before takeoff.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: The aircraft is delayed after ground de-icing and the fluid holdover time is exceeded before takeoff.  `[candidate:C8]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Matches 'Aeroplane - mush/stall' (ECCAIRS 1.3.0.12 · Events (390) · 2080300 · Aircraft operation general › Aeroplane flight path deviation): An event involving a mush/stall by a fixed wing aircraft.  `[definition:ECC-2080300]`
- Matches 'Aeroplane - spin' (ECCAIRS 1.3.0.12 · Events (390) · 2080400 · Aircraft operation general › Aeroplane flight path deviation): An event involving a spin by a fixed wing aircraft.  `[definition:ECC-2080400]`

**Exclude when**
- Distinguish from sibling B05 'Stall warning or upset during a go-around' under the same parent.  `[sibling:B05]`
- Distinguish from sibling B23 'Windshear on final approach' under the same parent.  `[sibling:B23]`
- Distinguish from sibling B24 'Landing short of the runway' under the same parent.  `[sibling:B24]`
- Coded OTHR (Other) rather than LOC-I: similar wording, different occurrence category.  `[report:WPR16FA095]`  
  > Takeoff Performance Information The excerpts below from the airplane flight manual (AFM) show the procedures for a normal takeoff and an obstacle takeoff.
- Coded FUEL (Fuel Related) rather than LOC-I: similar wording, different occurrence category.  `[report:ERA20LA126]`  
  > Finding: Aircraft-Aircraft systems-Ice/rain protection system-Ice detection-Not used/operated.
- Coded CTOL (Collision with Obstacle(s) During Takeoff and Landing) rather than LOC-I: similar wording, different occurrence category.  `[report:CEN26FA098]`  
  > Holdover time is the estimated period for which deicing or anti-icing fluid will prevent the accumulation of ice, snow or frost on an aircraft.
- Not 'Holdover time' — that definition is crosswalked to ICE, not LOC-I.  `[definition:IND-17]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not LOC-I.  `[definition:ECC-2180101]`
- Not 'Interference with aircraft from the ground' — that definition is crosswalked to SEC, not LOC-I.  `[definition:ECC-2270000]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.09).  `[parent:SCF-PP]`

**Linked example reports**
- WPR23FA080: "While deicing removes ice, anti-icing protects against additional icing for a certain period of time, called holdover time."
- CEN14LA202: "Contributing factor: Aircraft-Aircraft systems-Ice/rain protection system-Intake anti-ice, deice-Incorrect use/operation."
- GAA16CA477: "Cause: Aircraft-Aircraft oper/perf/capability-Aircraft capability-Takeoff distance-Not attained/maintained."
- CEN19FA124: "Cause: Aircraft-Fluids/misc hardware-Fluids-Fuel-Fluid level."
- WPR23LA334: "Review of the carburetor icing probability chart contained within FAA Special Airworthiness Information Bulletin CE-09-35 revealed the atmospheric conditions at the time of the accident were “conducive to serious icing at glide [idle] power.” ADDITIONAL INFORMATION FAA Advisory Circular 20-113, “Pilot Precautions and Procedures to be Taken in Preventing Aircraft Reciprocating Engine Induction System and Fuel System Icing Problems,” stated that, “to prevent accidents due to induction system icing, the pilot should regularly use [carburetor] heat under conditions known to be conducive to atmospheric icing and be alert at all times for indications of icing in the fuel system." The advisory circular recommended that, when operating in conditions where the relative humidity is greater than 50%, “…apply carburetor heat briefly immediately before takeoff, particularly with float type carburetors, to remove any ice which may have been accumulated during taxi and runup.” It also stated, “remain alert for indications of induction system icing during takeoff and climb-out, especially when the relative humidity is above 50%, or when visible moisture is present in the atmosphere.” According to 14 CFR 91.3, the PIC of an aircraft “is directly responsible for, and the final authority as to, the operation of that aircraft.” Title 14 CFR 61.89 stated that a student pilot may not act as PIC of an aircraft that is carrying passengers."
- CHI08FA150: "Corrections to theses values include: Reduce total distances of 10 percent every 10 knots of headwind Increase total distances of 30 percent every 10 knots of rear wind Increase by: 7 percent on hard sod, 10 percent on short grass, 15 percent on wet runway, 25 percent on high grass, 30 percent on slippery runway At a takeoff weight of 5,512 lbs, the takeoff ground roll and distance to clear 50 feet above ground level (D50) at an international standard atmosphere and pressure altitude of 0 and 2000 feet are listed as: Pressure altitude - 0 feet, ground roll - 1,017 feet, D50 - 1,591 feet Pressure altitude - 2000 feet, ground roll - 1,132 feet, D50 - 1,772 feet At a takeoff weight of 6,579 lbs, the takeoff ground roll and distance to clear 50 feet above ground level (D50) at an international standard atmosphere and pressure altitude of 0 and 2000 feet are listed as: Pressure altitude - 0 feet, ground roll – 1,378 feet, D50 – 2,133 feet Pressure altitude - 2000 feet, ground roll – 1,542 feet, D50 – 2,362 feet At a takeoff weight of 7,394 lbs, the takeoff ground roll and distance to clear 50 feet above ground level (D50) at an international standard atmosphere and pressure altitude of 0 and 2000 feet are listed as: Pressure altitude - 0 feet, ground roll – 2,035 feet, D50 – 2,840 feet Pressure altitude - 2000 feet, ground roll – 2,280 feet, D50 – 3,150 feet Section 4 of the POH, Before Starting checklist, states that the oxygen supply is to be available for the planned flight and the ‘OXYGEN’ switch is to be in the "ON" position."
- WPR17LA064: "He reported that the engine sounded normal, which he elaborated as both "strong and loud" and "ear piercing loud." The airplane just broke ground as it passed abeam of him, and he then mentioned to a person who was with him to watch the airplane, because its takeoff appeared to be unusual."
- WPR17FA117: "Cause: Aircraft-Aircraft oper/perf/capability-Aircraft capability-Climb capability-Capability exceeded."
- CEN10LA002: "Cause: Aircraft-Aircraft power plant-Engine controls-(general)-Incorrect use/operation."
- WPR20LA122: "Review of the meteorological conditions that existed around the time of the accident and the carburetor icing chart from FAA Special Airworthiness Information Bulletin CE-09-35 “Carburetor Icing Prevention” indicated a potential for serious icing at cruise power at the temperature and dew point that existed around the time of the accident."
- CEN19FA191: "To prevent carburetor icing, the pilot should: • Assure the proper functionality of the carburetor heat during the ground (Before Takeoff) check."
- WPR19MA177: "Finding: Aircraft-Aircraft oper/perf/capability-Aircraft capability-CG/weight distribution-Capability exceeded."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### C9 · Hard landing or tail strike

*Taxonomy version ntsb-draft-c94008cd21 · status needs review · parent ARC Abnormal Runway Contact*

**Definition.** A hard or bounced touchdown, or contact of the tail with the runway during rotation or flare.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: A hard or bounced touchdown, or contact of the tail with the runway during rotation or flare.  `[candidate:C9]`
- Matches 'Hard landing, tail strike' (SKYbrary – Hard Landing and Tail Strike): A touchdown with a vertical load above limits, a bounced landing, or contact of the tail with the runway during takeoff rotation or landing flare.  `[definition:IND-18]`
- Matches 'Hard landing' (ECCAIRS 1.3.0.12 · Events (390) · 2010600 · Aircraft operation general › Aircraft handling): An event involving a hard landing. Hard landing: A landing in which the vertical deceleration encountered required a hard landing check.  `[definition:ECC-2010600]`
- Matches 'Tail strike' (SKYbrary – Tailstrike): The aft fuselage contacts the runway during takeoff rotation or landing, often after early rotation, wrong takeoff speeds or excessive pitch.  `[definition:IND-35]`
- Narrative describes 'hard' (11 of 12 supporting reports).  `[report:ERA09LA538]`  
  > The approach was stable, "all the way down to the flare;" however, when airplane was about 15 feet above the runway, "the aircraft suddenly lost airspeed and landed hard." The airplane bounced approximately 15 to 20 feet back into the air, before it contacted the ground, and bounced about 5 to 10 feet.
- Narrative describes 'bounced' (10 of 12 supporting reports).  `[report:ERA09LA538]`  
  > The approach was stable, "all the way down to the flare;" however, when airplane was about 15 feet above the runway, "the aircraft suddenly lost airspeed and landed hard." The airplane bounced approximately 15 to 20 feet back into the air, before it contacted the ground, and bounced about 5 to 10 feet.
- Narrative describes 'landed' (10 of 12 supporting reports).  `[report:ERA09LA538]`  
  > The approach was stable, "all the way down to the flare;" however, when airplane was about 15 feet above the runway, "the aircraft suddenly lost airspeed and landed hard." The airplane bounced approximately 15 to 20 feet back into the air, before it contacted the ground, and bounced about 5 to 10 feet.

**Exclude when**
- Not 'Undershoot' — that definition is crosswalked to USOS, not ARC.  `[definition:ECC-2010800]`
- Not 'Wrong-surface event' — that definition is crosswalked to RI, not ARC.  `[definition:IND-03]`
- Not 'External load - contact with aircraft structure or component' — that definition is crosswalked to EXTL, not ARC.  `[definition:ECC-99010042]`
- Events better described by CICTT SCF-NP (System/Component Failure – Non-Powerplant) (runner-up parent, margin 0.69).  `[parent:SCF-NP]`

**Linked example reports**
- ERA09LA538: "The approach was stable, "all the way down to the flare;" however, when airplane was about 15 feet above the runway, "the aircraft suddenly lost airspeed and landed hard." The airplane bounced approximately 15 to 20 feet back into the air, before it contacted the ground, and bounced about 5 to 10 feet."
- ERA10CA305: "The airplane landed hard once again, and again bounced several times down the runway."
- CEN11CA018: "During touchdown the airplane impacted the runway hard and bounced back into the air before settling back on the runway."
- WPR15CA093: "The pilot reported that he was on a straight-in approach for landing during touchdown; the airplane landed hard and bounced."
- ERA15LA218: "During the hard landing, the tail rotor contacted the ground and the main rotor contact the tail boom."
- CEN13CA144: "The airplane was not aligned with the runway when it “hit the ground hard and bounced”."
- MIA08CA056: "The airplane bounced again and thereafter had a hard nose-low landing onto the runway."
- ERA10CA198: "He flared late and the airplane landed hard and bounced back into the air."
- CEN12LA676: "Probable cause: The pilot’s misjudged landing flare, which resulted in a hard landing."
- WPR09LA445: "The airspeed was 60 knots, and as he reduced the power to flare, the airplane was "caught in a downdraft." The airplane landed hard, bounced back up into the air in an "erratically unusual attitude," landed, and bounced a second time."
- WPR09LA480: "Probable cause: The pilot's improper landing flare and inadequate recovery from a bounced landing."
- WPR10CA422: "Probable cause: The pilot’s inadequate flare and bounced landing recovery technique that resulted in a hard landing."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass
