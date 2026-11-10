# Criteria cards · taxonomy ntsb-draft-45231e0fc8

Run run-ntsb-20261110T185650894 · selector rules · embedder local-lsa-128 · reports are synthetic.

### B01 · Vehicle or pedestrian on the runway without clearance

*Taxonomy version ntsb-draft-45231e0fc8 · status not grounded · parent RI Runway Incursion*

**Definition.** A ground vehicle, tug or person enters an active runway or its protected area without an ATC clearance.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: A ground vehicle, tug or person enters an active runway or its protected area without an ATC clearance.  `[candidate:B01]`
- Matches 'Pilot deviation (runway incursion)' (FAA Runway Safety programme – Pilot deviation): A runway incursion caused by a pilot, such as crossing a hold-short line or entering a runway without an ATC clearance.  `[definition:IND-40]`
- Matches 'Vehicle or pedestrian deviation' (FAA Runway Safety programme): A runway incursion caused by a ground vehicle or a person, such as a driver or pedestrian entering a runway without ATC authorization.  `[definition:IND-19]`
- Matches 'Anomaly: Ground Incursion – Runway or Taxiway' (NASA ASRS coding taxonomy): An aircraft, vehicle or person entering a runway or taxiway without authorization, or an aircraft using a taxiway or the wrong runway for landing or takeoff.  `[definition:IND-04]`
- Narrative describes 'vehicle' (2 of 5 supporting reports).  `[report:NYC08FA265]`  
  > Upon receipt of any clearance from ATC to cross a runway or taxiway, vehicle operators shall look both ways to ensure it is safe to cross.” On January 25, 2010, suggestions were provided to the FAA via the AAI-100 (Office of Accident Investigation) party representative to the investigation, to: 1) Revise both the FAA’s “Airport Ground Vehicle Operations, An FAA Guide” and FAA AC150/5210-20 publications to include ground vehicle operators’ requirement to visually confirm that an active runway was clear prior to crossing, even with ATCT clearance, 2) Review airport ACMs and airport-ATCT Letters of Agreement to ensure that appropriate language is included for vehicle operators’ runway vigilance, even with ATCT clearance, and 3) That FAA ensure that the increased vehicle operators’ vigilance requirements be incorporated into local airport ground vehicle training programs.

**Exclude when**
- Belongs to sibling B02 'Landing on a taxiway or the wrong runway at night' when it matches that bucket better (1 report(s) assigned there).  `[report:DCA23LA133/2]`  
  > (As previously stated, the airplane was precluded by company procedures from landing on runway 4R and holding short of runway 8L.) The UAL384 airplane subsequently crossed runway 4L without stopping at the hold-short line on taxiway K.
- Belongs to sibling B27 'Crew crossed a hold-short line without clearance' when it matches that bucket better (4 report(s) assigned there).  `[report:OPS09IA009/2]`  
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
- Not 'Clearance - not suitable for aircraft' — that definition is crosswalked to ATM, not RI.  `[definition:ECC-99010092]`
- Events better described by CICTT GCOL (Ground Collision) (runner-up parent, margin 0.41).  `[parent:GCOL]`

**Linked example reports**
- OPS09IA004: "HISTORY OF FLIGHT The Andrews Air Force Base (ADW) ground controller, working the ground control (GC), clearance delivery (CD), and flight data (FD) positions combined, authorized four vehicles to cross runway 19R without the local controller’s approval (LC) while VM206, a BE-20, was departing runway 19R."
- OPS16IA008: "As AAL2408 began its takeoff roll the Runway Status Lights (RWSLs) on runway 35L activated illuminating the Runway Entrance Lights (RELs) at the hold short locations of the three aircraft that had just been instructed to cross runway 35L, as well as the Takeoff Hold Lights (THLs) at the approach end of the runway."
- NYC08FA265: "Upon receipt of any clearance from ATC to cross a runway or taxiway, vehicle operators shall look both ways to ensure it is safe to cross.” On January 25, 2010, suggestions were provided to the FAA via the AAI-100 (Office of Accident Investigation) party representative to the investigation, to: 1) Revise both the FAA’s “Airport Ground Vehicle Operations, An FAA Guide” and FAA AC150/5210-20 publications to include ground vehicle operators’ requirement to visually confirm that an active runway was clear prior to crossing, even with ATCT clearance, 2) Review airport ACMs and airport-ATCT Letters of Agreement to ensure that appropriate language is included for vehicle operators’ runway vigilance, even with ATCT clearance, and 3) That FAA ensure that the increased vehicle operators’ vigilance requirements be incorporated into local airport ground vehicle training programs."
- OPS15IA017/2: "MIA ATCT procedures required controllers to use memory aids to indicate that an aircraft had been directed to LUAW, when an aircraft was issued a departure clearance, and to indicate that a runway was occupied by an airport vehicle."
- ERA16CA057/2: "The pilot of the biplane entered the left 45 degree entry for downwind to runway 16 because winds appeared to favor that runway."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### B02 · Landing on a taxiway or the wrong runway at night

*Taxonomy version ntsb-draft-45231e0fc8 · status not grounded · parent RI Runway Incursion*

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
- Belongs to sibling C1 'Landing or takeoff on an unintended surface' when it matches that bucket better (5 report(s) assigned there).  `[report:OPS09IA007]`  
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
- DCA18IA265: "The captain stated that all the lights, including the taxiway lights, runway lights, and lights on the sides of runways 35 and 27R blended together."
- DCA16IA036: "Probable cause: the flight crew's misidentification of the taxiway as the landing runway."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 pass · G7 pass · G8 pass · G9 pass

### B03 · Veer-off during landing in a strong or gusty crosswind

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent RE Runway Excursion*

**Definition.** In a strong or gusty crosswind the aircraft drifts and veers off the side of the runway during the landing roll.

**Include when**
- The occurrence meets the CICTT RE (Runway Excursion) definition.  `[parent:RE]`
- Core definition: In a strong or gusty crosswind the aircraft drifts and veers off the side of the runway during the landing roll.  `[candidate:B03]`
- Matches 'Crosswind landing' (SKYbrary – Crosswind Landings): Landing with a wind component across the runway; strong or gusty crosswinds near the aircraft limit increase the risk of lateral runway excursion (veer-off).  `[definition:IND-20]`
- Matches 'Anomaly: Ground Excursion – Runway' (NASA ASRS coding taxonomy): An aircraft departs the runway surface during the takeoff or landing roll, including overruns after a long or fast landing.  `[definition:IND-07]`
- Matches 'Runway excursion (veer-off and overrun)' (SKYbrary – Runway Excursion): An aircraft leaves the runway surface during takeoff or landing, either by veering off the side or by overrunning the end.  `[definition:IND-05]`
- Narrative describes 'failure' (7 of 12 supporting reports).  `[report:WPR10CA296]`  
  > Probable cause: The pilot's inadequate compensation for the crosswind condition and failure to maintain directional control during the landing roll in gusty crosswind conditions.
- Narrative describes 'directional' (6 of 12 supporting reports).  `[report:WPR10CA296]`  
  > Probable cause: The pilot's inadequate compensation for the crosswind condition and failure to maintain directional control during the landing roll in gusty crosswind conditions.
- Narrative describes 'maintain' (6 of 12 supporting reports).  `[report:WPR10CA296]`  
  > Probable cause: The pilot's inadequate compensation for the crosswind condition and failure to maintain directional control during the landing roll in gusty crosswind conditions.

**Exclude when**
- Belongs to sibling B04 'Overrun on a contaminated runway' when it matches that bucket better (1 report(s) assigned there).  `[report:ERA11LA390]`  
  > It was marked with nonprecision markings that were in good condition Usable length for landing on runway 24 was 3,471 feet due to a displaced threshold on the end of runway 06, marked as a taxiway aligned with a runway, and a chevroned runway safety area on the end of runway 24.
- Distinguish from sibling B22 'Tail strike on takeoff' under the same parent.  `[sibling:B22]`
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than RE: similar wording, different occurrence category.  `[report:ERA25LA090]`  
  > Probable cause: A landing gear collapse during landing in gusty crosswind conditions.
- Coded TURB (Turbulence Encounter) rather than RE: similar wording, different occurrence category.  `[report:WPR24LA085]`  
  > This AC stated that, when landing behind a larger aircraft on a parallel runway closer than 2,500 feet apart, pilots need to consider the relationship between the runway threshold locations, the relative glideslope descent paths/locations and possible vortex drift onto your runway.
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not RE.  `[definition:ECC-2180101]`
- Not 'Aircraft encounter with turbulence' — that definition is crosswalked to TURB, not RE.  `[definition:ECC-2220600]`
- Not 'Aircraft encountered vortex/wake turbulence' — that definition is crosswalked to TURB, not RE.  `[definition:ECC-2220400]`
- Events better described by CICTT LOC-G (Loss of Control – Ground) (runner-up parent, margin 0.05).  `[parent:LOC-G]`

**Linked example reports**
- GAA16CA476: "The pilot of a tailwheel-equipped airplane reported that during the landing roll in gusty crosswind conditions, the airplane abruptly veered to the left because his right foot had rolled off the right rudder pedal."
- WPR10CA296: "Probable cause: The pilot's inadequate compensation for the crosswind condition and failure to maintain directional control during the landing roll in gusty crosswind conditions."
- ANC09LA104: "In addition, a subheading titled “Slippery Runways,” in the Crosswind Landing section of the Operations Manual, recommends, in part, that the operators adjust the crosswind limit, reducing it by 25 to 75 percent, depending on slippery conditions."
- GAA16CA402: "The pilot reported that during the landing in gusty crosswind conditions, the airplane touched down "firm" with the landing gear side loaded."
- GAA16CA184: "The pilot reported that he was landing in gusty crosswind conditions following a parachute jump flight, and that the gusty conditions had persisted for the previous 10 skydiving flights that day."
- GAA17CA043: "Probable cause: The pilot's failure to maintain directional control during the landing roll in gusty crosswind conditions, which resulted in a runway excursion."
- GAA16CA183: "This handbook discusses operations in crosswind conditions and states in part: Takeoffs and landings in certain crosswind conditions are inadvisable or even dangerous."
- GAA16CA249: "Probable cause: The pilot's failure to maintain directional control during the landing roll in gusty crosswind conditions, which resulted in a runway excursion and nose over."
- ERA26LA099: "Probable cause: The pilot’s failure to compensate for gusty crosswind conditions during the landing roll, which resulted in a loss of control and subsequent runway excursion."
- GAA16CA311: "Probable cause: The pilot's failure to maintain directional control during the landing roll in gusty crosswind conditions, which resulted in a runway excursion and a collision with a concrete barrier wall."
- CEN23LA286: "Probable cause: The pilot’s failure to maintain directional control during the landing roll with gusty wind which exceeded the maximum crosswind of the airplane."
- WPR11CA178: "Probable cause: The pilot’s failure to maintain directional control during landing in gusty crosswind conditions."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 FAIL · G8 pass · G9 pass

### B04 · Overrun on a contaminated runway

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent RE Runway Excursion*

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
- Distinguish from sibling B03 'Veer-off during landing in a strong or gusty crosswind' under the same parent.  `[sibling:B03]`
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

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent LOC-I Loss of Control – Inflight*

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

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent TURB Turbulence Encounter*

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
- WPR17FA023: "The pilot was concerned that if the turbulence continued during the approach, he would be vulnerable to strong buffeting at normal approach speed, which might lead to a rough landing; as a countermeasure, he elected to land at a higher airspeed."
- CEN13FA438: "Cause: Aircraft-Aircraft oper/perf/capability-Performance/control parameters-(general)-Capability exceeded."
- LAX08LA105: "Probable cause: The pilot's encounter with severe turbulence during descent into the airport environment, which resulted in an exceedence of the aircraft's design stress limit and structural damage."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 pass · G9 pass

### B07 · Loss of separation caused by an ATC clearance

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** A controller clearance or instruction puts two aircraft into conflict, leading to loss of separation or a TCAS alert.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: A controller clearance or instruction puts two aircraft into conflict, leading to loss of separation or a TCAS alert.  `[candidate:B07]`
- Matches 'Loss of separation' (ICAO Doc 4444 – PANS-ATM (separation minima)): Two aircraft come closer than the prescribed separation minima, often after an ATC clearance or instruction puts them in conflict.  `[definition:IND-23]`
- Matches 'Loss of separation with aircraft - both airborne' (ECCAIRS 1.3.0.12 · Events (390) · 2180101 · Aircraft operation general › Aircraft - near collisions/loss of separation › Loss of separation between aircraft): This includes the AIRPROX defined as: A situation in which, in the opinion of a pilot or air traffic services personnel, the distance between aircraft as well as their relative positions and speed have been such that the safety of the aircraft involved may have been compromised. An aircraft proximity is classified as follows: Risk of collision. The risk classification of an aircraft proximity in which serious risk of collision has existed. Safety not assured. The risk classification of an aircraft proximity in which the safety of the aircraft may have been compromised. No risk of collision. The risk classification of an aircraft proximity in which no risk of collision has existed. Risk not determined. The risk classification of an aircraft proximity in which insufficient information was available to determine the risk involved, or inconclusive or conflicting evidence precluded such determination.  `[definition:ECC-2180101]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`

**Exclude when**
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (5 report(s) assigned there).  `[report:OPS16IA010]`  
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
- OPS25LA052: "At about 1941 CDT, the Dakota RAPCON Minot radar sector controller (MIB sector controller) coordinated via shout line (a dedicated, direct voice communication link) with MOT ATCT LC (local control) controller requesting an opposite direction arrival for SKW3788 to runway 31, and an approach to runway 8 for another uninvolved aircraft, N717BL."
- LAX08FA265: "When the unit detects an intruder aircraft within 0.55 nautical mile horizontal distance and plus or minus 800 feet relative altitude or detects an intruder aircraft is on a course that will intercept the Skywatch airplane's course within 20 seconds (non-altitude reporting intruder aircraft) or 30 seconds (altitude reporting intruder aircraft), the unit will issue a Traffic Advisory (TA)."
- OPS14IA011: "Probable cause: The air traffic controller’s failure to identify a conflict between two aircraft and to issue an adequate clearance, which resulted in a loss of required separation."
- OPS10IA020/2: "At 1812:50, the local controller transmitted, "70 echo traffic off the departure end climbing out of 500 heavy triple 7." The pilot of N9870E responded, "70E in sight." The controller then continued, "70E maintain visual separation pass behind that aircraft." The pilot responded, "70E pass behind 'em." At 1813:03, the controller transmitted, "United 889 heavy traffic's uh just ahead and to your right has you in sight Cessna 1,500 they're maintaining visual separation." At 1813:13, the controller continued, "United 889 heavy traffic's no factor contact Norcal departure." The pilot of UAL889 responded, "OK, that set off the TCAS...that was...that...we need to talk." At 1813:47, UAL889 transmitted, "All right, trip...889's going to uh departure," and the controller acknowledged."
- OPS11IA101/2: "Probable cause: The air traffic controllers’ failure to maintain required awareness of available flight data and aircraft positions, resulting in issuance of an incorrect altitude clearance that caused a loss of standard instrument flight rules separation between the two aircraft."
- WPR12LA109/2: "About 1842, the controller asked N7508Y how much further east she would be flying, and the pilot responded, "We'll be over Antioch Bridge but be turning [.]bound soon, zero eight yankee." The radar controller responded "roger traffic one o'clock 6 miles northbound altitude indicates two thousand six hundred appears level," and the pilot replied, "zero eight yankee." Fifty seconds later, the controller advised the pilot that the target was now turning northwest bound at a range of 4 miles, and the pilot replied that she was turning northbound."
- OPS09IA001: "Of the two ATCS on position, one controller was working local control (LC) and one controller was working ground control (GC) combined with the controller-in-charge (CIC) position."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 pass · G9 pass

### B08 · TCAS resolution advisory after a level bust

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** The aircraft climbs or descends through its cleared altitude (level bust) and a TCAS resolution advisory follows.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: The aircraft climbs or descends through its cleared altitude (level bust) and a TCAS resolution advisory follows.  `[candidate:B08]`
- Matches 'Level bust (altitude deviation)' (EUROCONTROL – Level bust): An unauthorised vertical deviation of more than 300 feet from the cleared flight level or altitude, a common cause of loss of separation and TCAS resolution advisories.  `[definition:IND-11]`
- Matches 'Loss of separation with aircraft - both airborne' (ECCAIRS 1.3.0.12 · Events (390) · 2180101 · Aircraft operation general › Aircraft - near collisions/loss of separation › Loss of separation between aircraft): This includes the AIRPROX defined as: A situation in which, in the opinion of a pilot or air traffic services personnel, the distance between aircraft as well as their relative positions and speed have been such that the safety of the aircraft involved may have been compromised. An aircraft proximity is classified as follows: Risk of collision. The risk classification of an aircraft proximity in which serious risk of collision has existed. Safety not assured. The risk classification of an aircraft proximity in which the safety of the aircraft may have been compromised. No risk of collision. The risk classification of an aircraft proximity in which no risk of collision has existed. Risk not determined. The risk classification of an aircraft proximity in which insufficient information was available to determine the risk involved, or inconclusive or conflicting evidence precluded such determination.  `[definition:ECC-2180101]`
- Matches 'Aircraft not RVSM (Reduced Vertical Separation Minimum) equipped while being operated in' (ECCAIRS 1.3.0.12 · Events (390) · 7050300 · Regulatory issues / events › Aircraft related regulatory event/issue): RVSM airspace (Aircraft not RVSM equipped) Aircraft not RVSM equipped while being operated in RVSM airspace. RVSM: Reduced Vertical Separation Minimum of 1.000 ft (300 m.)  `[definition:ECC-7050300]`

**Exclude when**
- Belongs to sibling B07 'Loss of separation caused by an ATC clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:WPR15MA243/2]`  
  > At 1100:23, the LC instructed, "stationair five eight uniform two six right cleared for I'm sorry two six left cleared for takeoff." At 1100:29, the pilot of N5058U stated, "uh I'm sorry was that for five eight uniform?" The LC then cleared the pilot of N5058U for takeoff from runway 26L.
- Distinguish from sibling B12 'GNSS interference or spoofing' under the same parent.  `[sibling:B12]`
- Distinguish from sibling B20 'Pushback or towing collision' under the same parent.  `[sibling:B20]`
- Coded ATM (ATM/CNS) rather than MAC: similar wording, different occurrence category.  `[report:OPS17IA021/2]`  
  > Separate an arriving aircraft from another aircraft using the same runway by ensuring that the arriving aircraft does not cross the landing threshold until one of the following conditions exists or unless authorized in para 3-10-10, Altitude Restricted Low Approach.
- Coded CFIT (Controlled Flight Into or Toward Terrain) rather than MAC: similar wording, different occurrence category.  `[report:WPR16LA028]`  
  > Immediately issue/initiate an alert to an aircraft if you are aware the aircraft is at an altitude that, in your judgment, places it in unsafe proximity to terrain and/or obstructions.
- Not 'Aircraft encountered vortex/wake turbulence' — that definition is crosswalked to TURB, not MAC.  `[definition:ECC-2220400]`
- Not 'Climb above the towing aircraft' — that definition is crosswalked to RAMP, not MAC.  `[definition:ECC-2240202]`
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.35).  `[parent:NAV]`

**Linked example reports**
- OPS11IA686: "Air Traffic Procedural Requirements Traffic advisories were provided to both pilots in accordance with Federal Aviation Administration Order 7110.65, paragraphs 2-1-21 "Traffic Advisories", and 5-1-8 "Merging Target Procedures", which state in part: 2-1-21 Unless an aircraft is operating within Class A airspace or omission is requested by the pilot, issue traffic advisories to all aircraft (IFR or VFR) on your frequency when, in your judgment, their proximity may diminish to less than the applicable separation minima."
- ERA15MA259: "At 1100:16, the CHS approach controller issued a traffic advisory advising the F-16 pilot of "traffic 12 o'clock, 2 miles, opposite direction, 1,200 [ft altitude] indicated, type unknown." At 1100:24, the F-16 pilot responded that he was "looking" for the traffic."
- ERA22FA318/2: "Air traffic control responsibility for the flight was transferred to the VGT air traffic control tower (ATCT) at 1158:26."
- ANC20LA085/2: "When a rule of this section gives another aircraft the right-of-way, the pilot shall give way to that aircraft and may not pass over, under, or ahead of it unless well clear."
- ERA11FA468/2: "His airplane was initially at an altitude of about 1,500 feet at the Expressway, but descended until it was about 1,200 to 1,000 feet, before turning onto the downwind leg."
- OPS16IA010: "At 0936:48, the pilot of N57GX contacted JAX approach control and advised that he "would like to go back on course and climb to 9,000." The approach controller responded, "Mooney 7GX you are radar contact eight miles west of the Ocala airport, say altitude." The pilot of N57GX replied, "yeah I see that 57GX, we would like to go back on course to go towards Fort Myers." The approach controller replied, "…roger that, ah, cleared direct Lakeland, climb and maintain 5,000." The pilot of N57GX correctly read back the route and altitude clearance, and the approach controller then climbed N57GX to 9,000 feet."
- OPS10IA163/2: "At approximately 1942, when SKW5943 was descending through 1,500 feet, the local controller advised the pilot of helicopter traffic off to his left side, “…low level at 1,400 feet.” The pilot responded that he had received a TCAS alert on that traffic and would have to go around because he had to climb in response a resolution advisory."
- DCA10LA083: "During FAST13's ascent to FL286, TCF7630 received a Traffic Alert and Collision Avoidance System (TCAS) warning resolution advisory (RA), directing the pilot to climb."
- OPS08IA014: "On initial contact with San Juan ATC, DAL485 advised that they had just maneuvered in response to a TCAS resolution advisory and climbed to a higher altitude to avoid a 747 passing by on the right side of the aircraft."
- ANC20LA074: "When it detects a traffic conflict, ATAS sounds an audio alert or “traffic callout.” Conflicting aircraft are also highlighted on cockpit displays when such displays are available in an aircraft."
- OPS25LA032/5: "1516:23 The DEALE controller instructed DRAGO61 to maintain visual separation with the traffic, instructed them to climb to 5,000 feet and fly heading 270° when able."
- ANC16FA052: "Pilots should clearly communicate on the CTAF and coordinate maneuvering for and execution of the landing with other traffic so as not to disrupt the flow of other aircraft."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B09 · Hydraulic system failure in flight

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent SCF-NP System/Component Failure – Non-Powerplant*

**Definition.** Loss of fluid or pressure in a hydraulic system in flight degrades flight controls, brakes or landing gear.

**Include when**
- The occurrence meets the CICTT SCF-NP (System/Component Failure – Non-Powerplant) definition.  `[parent:SCF-NP]`
- Core definition: Loss of fluid or pressure in a hydraulic system in flight degrades flight controls, brakes or landing gear.  `[candidate:B09]`
- Matches 'Hydraulic system failure' (SKYbrary – Hydraulic System Failure): Loss of hydraulic fluid or pressure that degrades flight controls, brakes, steering or landing gear, handled with non-normal checklists.  `[definition:IND-24]`
- Matches 'Smoke - Landing gear' (ECCAIRS 1.3.0.12 · Events (390) · 1990162 · Aircraft/system/component › Non-component specific events › Explosions / fire/ fumes / smoke › Smoke): Smoke emanating from the landing gear, e.g. from hydraulic liquid dripping onto hot brakes.  `[definition:ECC-1990162]`
- Matches 'Fire - Landing gear' (ECCAIRS 1.3.0.12 · Events (390) · 1990161 · Aircraft/system/component › Non-component specific events › Explosions / fire/ fumes / smoke › Fire): Fire - Landing gear: e.g. by fluids coming into contact with hot brakes.  `[definition:ECC-1990161]`

**Exclude when**
- Belongs to sibling B10 'Landing gear did not extend' when it matches that bucket better (3 report(s) assigned there).  `[report:CEN11IA379]`  
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
- ERA14LA022: "Lubricated landing gear system." ADDITIONAL INFORMATIONBrake System The airplane was equipped with a hydraulic fluid braking system that included two independent wheel brakes actuated by two separate brake master cylinders, one each for the left and right brake."
- CEN16LA153: "Landing gear extension begins when the pilot moves the cockpit landing gear handle to the down position, which directs hydraulic fluid to the extension side of the actuators."
- CEN14FA505: "Brake System The airplane's hydraulic brake system delivered hydraulic pressure to the brakes via input from the brake pedals."
- DCA13FA148: "Two red in transit lights are provided on the landing gear control selector handle which illuminate when the landing gear control has been selected and any of the landing gear are not either fully extended or fully retracted."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 pass · G9 pass

### B10 · Landing gear did not extend

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent SCF-NP System/Component Failure – Non-Powerplant*

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
- Events better described by CICTT ARC (Abnormal Runway Contact) (runner-up parent, margin 0.15).  `[parent:ARC]`

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
- CEN11IA341: "The MLG actuators retract for gear extension and extend for gear retraction while the NLG actuator extends for gear extension and retracts for gear retraction."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B11 · Terrain warning on a non-precision approach

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent CFIT Controlled Flight Into or Toward Terrain*

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
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.22).  `[parent:NAV]`

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

*Taxonomy version ntsb-draft-45231e0fc8 · status not grounded · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** Satellite navigation signals are jammed or spoofed, giving false position, lost RNP capability or incorrect time, often near conflict zones.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: Satellite navigation signals are jammed or spoofed, giving false position, lost RNP capability or incorrect time, often near conflict zones.  `[candidate:B12]`
- Matches 'Conflict: Airborne Conflict / NMAC' (NASA ASRS coding taxonomy): Two aircraft in flight come into conflict or lose separation, including near midair collisions and TCAS events.  `[definition:IND-12]`
- Matches 'Near collision with tall structure/object' (ECCAIRS 1.3.0.12 · Events (390) · 2180402 · Aircraft operation general › Aircraft - near collisions/loss of separation › Near collision with object on ground): An event involving a near collision by an aircraft with tall structure or other object on the ground. Near collision with parachutist on the ground (Near collision - parachutist)                                  2180404    * An event involving a near collision by an aircraft with a parachutist on the ground.  `[definition:ECC-2180402]`
- Matches 'Genuine airborne collision avoidance system/traffic alert and collision avoidance system warning' (ECCAIRS 1.3.0.12 · Events (390) · 2260100 · Aircraft operation general › Warning system triggered): triggered (ACAS/TCAS warning triggered) An event involving a genuine airborne collision avoidance system/traffic alert and collision avoidance system warning. ACAS: An aircraft system based on secondary surveillance radar (SSR) transponder signals which operates independently of ground-based equipment to provide advice to the pilot on potential conflicting aircraft that are equipped with SSR transponders. Note: In this context the term 'independently' means that ACAS operates independently of other systems used by air traffic services except for communications with Mode S ground stations. TCAS: TCAS is the terminology used in the United States for its traffic alert and collision avoidance system. In ICAO the system is known as ACAS.  `[definition:ECC-2260100]`

**Exclude when**
- Belongs to sibling B07 'Loss of separation caused by an ATC clearance' when it matches that bucket better (5 report(s) assigned there).  `[report:LAX08FA265]`  
  > According to L-3 Avionics personnel, the upgrade provided an extended audio callout capability.
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (6 report(s) assigned there).  `[report:OPS25LA032/5]`  
  > The CIC acknowledged and stated that they were waiting for a “stop the departures time.” The PCT TRACON OS stated that the Time on Target (TOT) would be at 1521 EDT and the stop time would be 17.
- Distinguish from sibling B20 'Pushback or towing collision' under the same parent.  `[sibling:B20]`
- Coded GCOL (Ground Collision) rather than MAC: similar wording, different occurrence category.  `[report:WPR14LA025/2]`  
  > At the time of the accident, the ATCT cab was staffed by four persons serving three positions, including two positions of operation.
- Coded LOC-I (Loss of Control – Inflight) rather than MAC: similar wording, different occurrence category.  `[report:ERA19LA026]`  
  > The ELT signal was captured only on the recording of the "R52" controller position at the Jacksonville air route traffic control center, which was the 2nd controller position at Jacksonville to talk to N555PM.
- Coded OTHR (Other) rather than MAC: similar wording, different occurrence category.  `[report:CEN10FA115/3]`  
  > Radar data, provided by Denver Air Route Traffic Control Center (ZDV) in National Track Analysis Program (NTAP) format, identified and depicted the Cirrus flight from the time of departure from KEIK to the time of the accident.
- Not 'GNSS jamming and spoofing' — that definition is crosswalked to NAV, not MAC.  `[definition:IND-27]`
- Not 'Lateral navigation error' — that definition is crosswalked to NAV, not MAC.  `[definition:IND-41]`
- Not 'Failure to provide navigation' — that definition is crosswalked to ATM, not MAC.  `[definition:ECC-4050600]`
- Events better described by CICTT NAV (Navigation Error) (runner-up parent, margin 0.03).  `[parent:NAV]`

**Linked example reports**
- CEN10FA115/2: "Radar data, provided by Denver Air Route Traffic Control Center (ZDV) in National Track Analysis Program (NTAP) format, identified and depicted the Cirrus flight from the time of departure from KEIK to the time of the accident."
- OPS11IA476: "Personnel Interviews MAF Local Control Trainee At the time of the incident, training was in progress at the MAF Local Control (LC) position."
- ERA17FA027: "HISTORY OF FLIGHT On October 21, 2016, about 1430 eastern daylight time, an experimental Nanchang CJ-6A airplane, N10EB, impacted terrain near Blackshear, Georgia, after a midair collision while maneuvering in formation with another experimental Nanchang CJ-6A airplane, N33CY."
- CEN23FA084: "HISTORY OF FLIGHTOn January 17, 2023, about 1036 central standard time, a Piper PA-46-350P JetProp DLX airplane, N963MA, sustained substantial damage when it was involved in an accident near Yoakum, Texas."
- ANC09LA011/2: "The tower cab is equipped with a digital bright radar indicator tower equipment (D-BRITE) radar repeater display at the local control position."
- WPR18LA144/2: "The white Navion was in the #3 position and the last airplane was in the #4 position."
- ERA12LA401: "The National Transportation Safety Board (NTSB) radar study indicated that at that time, the Cessna was at 1,800 feet msl and was nearly due east of the position of the Beech 400A, which was at 2,400 feet msl."
- CEN17FA072: "Spatial Disorientation The FAA Civil Aeromedical Institute's publication, "Introduction to Aviation Physiology," defines spatial disorientation as a loss of proper bearings or a state of mental confusion as to position, location, or movement relative to the position of the earth."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 FAIL · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B13 · Engine shutdown after loss of oil pressure

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent SCF-PP System/Component Failure – Powerplant*

**Definition.** Low oil pressure or oil loss in flight leads the crew to shut an engine down as a precaution.

**Include when**
- The occurrence meets the CICTT SCF-PP (System/Component Failure – Powerplant) definition.  `[parent:SCF-PP]`
- Core definition: Low oil pressure or oil loss in flight leads the crew to shut an engine down as a precaution.  `[candidate:B13]`
- Matches 'In-flight engine shutdown (IFSD)' (SKYbrary – In-Flight Shutdown): An engine is shut down in flight because of a failure or a precautionary indication such as low oil pressure, high vibration or fire.  `[definition:IND-28]`
- Matches 'Engine oil system related event (ATA Code:7900)' (ECCAIRS 1.3.0.12 · Events (390) · 1790000 · Aircraft/system/component): (ATA Code:7900) An event involving the system units external to the engine which store and deliver engine lubricating oil to and from either turbine or reciprocating engines.  `[definition:ECC-1790000]`
- Matches 'Reciprocating engine - vibration' (ECCAIRS 1.3.0.12 · Events (390) · 1850110 · Aircraft/system/component › 8500 Reciprocating engine › 8501 Reciprocating engine general): Reciprocating engine - Vibration  `[definition:ECC-1850110]`

**Exclude when**
- Belongs to sibling D12 'Reciprocating engine failure from a connecting rod or crankshaft fracture' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN19LA320]`  
  > According to an oil analysis report dated May 29, 2019, the sample indicated the best “wear-rate” results from the engine; the amount of iron detected was a “bit” more than average for the type of engine, but “not far enough out of line to call a problem.” According to the engine manufacturer’s maintenance manual directions current at the time of the accident, the minimum requirement is to change the oil and filter every 50 hours and/or 4 months on engines with full flow oil filters and on engines with a large or small replaceable oil filter cartridge.
- Distinguish from sibling B17 'Lithium battery fire from a passenger device' under the same parent.  `[sibling:B17]`
- Distinguish from sibling D01 'Carburetor icing leading to loss of engine power' under the same parent.  `[sibling:D01]`
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
- ERA23LA058: "Examination of the oil system revealed the presence of metal contamination inside the main engine oil filter, oil pump filter, and two other oil strainers."
- ERA15LA062: "About 3 minutes after last checking the engine parameters, noting all engine parameters (specifically, oil temperature, oil pressure, and CHT) were in the green, or at 1153:02, the oil pressure indication first began to decrease from the steady state reading."
- CEN18LA031: "When the oil pressure decreased below 30 psi, the oil temperature began to increase steadily until the total loss of engine power."
- ERA11FA414: "The analog oil pressure indicator receives a pressure signal from an oil pressure sensor mounted at the aft end of the engine below the oil cooler."
- CEN17LA065: "The engine oil level then rose, and its quantity was at the base of the oil filler neck, which was above the maximum oil capacity for the engine."
- CEN23LA246: "An engine logbook entry dated June 16, 2023, stated that in addition to replacing the turbocharger, the mechanic drained the engine oil, opened the oil filter, and cleaned the oil pickup screen, where a small amount of metal was observed."
- CEN24LA140: "The engine’s manifold pressure, fuel pressure, and fuel flow values remained unremarkable until about 1 hour 7 minutes into the flight, when the oil pressure decreased briefly to 22 psi."
- CEN21FA130: "Contributing to the accident was the damaged wiring harness of the left engine oil pressure sending unit, which gave a false indication of an engine malfunction that resulted in the precautionary shutdown of the left engine."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass

### B14 · Takeoff with frost or ice not removed

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent ICE Icing*

**Definition.** The aircraft departs or begins to depart with frost, snow or ice on its wings because it was not removed or the fluid failed.

**Include when**
- The occurrence meets the CICTT ICE (Icing) definition.  `[parent:ICE]`
- Core definition: The aircraft departs or begins to depart with frost, snow or ice on its wings because it was not removed or the fluid failed.  `[candidate:B14]`
- Matches 'Clean aircraft concept' (FAA Advisory Circular 120-60B – Ground Deicing and Anti-icing Program): No takeoff may be made with frost, ice or snow adhering to wings or control surfaces; contamination must be removed before departure.  `[definition:IND-29]`
- Matches 'Holdover time' (FAA holdover time guidelines (ground de-icing and anti-icing)): The estimated time a de-icing or anti-icing fluid protects aircraft surfaces from frost or ice; if it is exceeded before takeoff, the aircraft must be checked or de-iced again.  `[definition:IND-17]`
- Matches 'Aircraft encountered icing conditions' (ECCAIRS 1.3.0.12 · Events (390) · 2220100 · Aircraft operation general › Weather encounters): Icing conditions: Weather conditions conducive to the formation of ice on an aircraft in flight. These conditions are usually characterized by visible moisture in the air and temperatures around the freezing level. Pilots encountering icing conditions are urged to issue a pilot weather report (PIREP) immediately.  `[definition:ECC-2220100]`

**Exclude when**
- Belongs to sibling B25 'Airframe icing in flight' when it matches that bucket better (5 report(s) assigned there).  `[report:DCA14FA058]`  
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
- WPR13FA041: "Cause: Aircraft-Aircraft oper/perf/capability-Performance/control parameters-Altitude-Not attained/maintained."
- ANC17TA015: "Probable cause: The pilot's continued flight into known icing conditions, which resulted in structural icing and a forced landing on icy, snow-covered terrain."
- CEN09LA122: "The pilot was informed that the heavier band of snow had moved through the Three Rivers area with isolated snow showers still in the area."
- ANC12CA115: "Probable cause: The pilot's decision to take off with ice- and snow-contaminated wings."
- GAA20CA075: "The Federal Aviation Administration's Pilot's Handbook of Aeronautical Knowledge, FAA-H-8083-25B, provides information and guidance in a section titled "Stalls" which stated in part: As little as 0.8 millimeter of ice on the upper wing surface increases drag and reduces aircraft lift by 25 percent."
- CEN21LA030: "Finding: Aircraft-Aircraft systems-Ice/rain protection system-Airfoil anti-ice, deice-Not installed/available."
- CEN12FA161: "The airplane’s electric anti-ice and propeller anti-ice were found in the “off” position."
- ANC12IA024: "Remarks; station with a precipitation discriminator, freezing drizzle began at 2253 and snow began at 2203 and snow ended at 2253."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 pass · G9 pass

### B15 · Bird ingestion damaging an engine on takeoff or climb

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent BIRD Bird*

**Definition.** One or more birds are ingested into an engine during takeoff or initial climb, causing vibration, surging or loss of thrust.

**Include when**
- The occurrence meets the CICTT BIRD (Bird) definition.  `[parent:BIRD]`
- Core definition: One or more birds are ingested into an engine during takeoff or initial climb, causing vibration, surging or loss of thrust.  `[candidate:B15]`
- Matches 'Engine bird ingestion' (14 CFR 33.76 – Bird ingestion (engine certification)): Engines must be shown to withstand the ingestion of birds of defined sizes; large or multiple bird ingestion can damage fan blades and cause surge, loss of thrust, shutdown or fire.  `[definition:IND-16]`
- Matches 'Damaging bird strike' (FAA National Wildlife Strike Database – strike reporting): A collision with birds that damages the aircraft, such as a cracked windshield, dented radome or ingested engine, reported to the wildlife strike database.  `[definition:IND-39]`
- Matches 'Turbine engine ingestion - bird' (ECCAIRS 1.3.0.12 · Events (390) · 2140100 · Aircraft operation general › Object ingestion by engine): An event involving the ingestion of a bird by a turbine engine.  `[definition:ECC-2140100]`
- Narrative describes 'bird' (11 of 12 supporting reports).  `[report:DEN08FA072]`  
  > Probable cause: the impact with a bird during initial takeoff climb.
- Narrative describes 'collision' (6 of 12 supporting reports).  `[report:GAA19CA268]`  
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
- CEN09CA418: "The pilot stated that a large bird struck the nose of the airplane during initial climb after takeoff."
- DCA20CA010: "Probable cause: a bird strike during climb out."
- ERA21LA047: "Probable cause: The airplane’s collision with a bird during initial climb, which resulted in a forced landing."
- ERA24LA061: "Probable cause: An in-flight collision with a bird during initial climb."
- CEN24LA153: "Probable cause: An in-flight collision with a bird during the initial climb."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 pass · G9 pass

### B16 · Bird strike damaging the windshield or nose on approach

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent BIRD Bird*

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
- GAA19CA467: "Probable cause: The airplane’s impact with a bird during approach."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B17 · Lithium battery fire from a passenger device

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent SCF-PP System/Component Failure – Powerplant*

**Definition.** A phone, laptop, power bank or other lithium battery device overheats, smokes or catches fire in the cabin.

**Include when**
- The occurrence meets the CICTT SCF-PP (System/Component Failure – Powerplant) definition.  `[parent:SCF-PP]`
- Core definition: A phone, laptop, power bank or other lithium battery device overheats, smokes or catches fire in the cabin.  `[candidate:B17]`
- Matches 'Power loss in a reciprocating engine due to non-mechanical failure' (ECCAIRS 1.3.0.12 · Events (390) · 1850104 · Aircraft/system/component › 8500 Reciprocating engine › 8501 Reciprocating engine general): An event involving a power loss in a reciprocating engine due to non-mechanical failure.  `[definition:ECC-1850104]`
- Matches 'Turbine engine related event (ATA Code:7200)' (ECCAIRS 1.3.0.12 · Events (390) · 1720000 · Aircraft/system/component): (ATA Code:7200) An event involving the units and components which are used to induce and convert fuel-air mixture into power, and transmit power to the propeller shaft (if any) and accessory drives. Includes reports pertaining to bird strikes to engines/cowling.  `[definition:ECC-1720000]`
- Matches 'In-flight engine shutdown (IFSD)' (SKYbrary – In-Flight Shutdown): An engine is shut down in flight because of a failure or a precautionary indication such as low oil pressure, high vibration or fire.  `[definition:IND-28]`

**Exclude when**
- Distinguish from sibling B13 'Engine shutdown after loss of oil pressure' under the same parent.  `[sibling:B13]`
- Distinguish from sibling D01 'Carburetor icing leading to loss of engine power' under the same parent.  `[sibling:D01]`
- Distinguish from sibling D12 'Reciprocating engine failure from a connecting rod or crankshaft fracture' under the same parent.  `[sibling:D12]`
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

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent F-NI Fire/Smoke (Non-Impact)*

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
- Events better described by CICTT SCF-NP (System/Component Failure – Non-Powerplant) (runner-up parent, margin 0.13).  `[parent:SCF-NP]`

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

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent NAV Navigation Error*

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
- OPS18IA003: "Minimum Vectoring Altitude The FAA defines the MVA as "The lowest msl altitude at which an Instrument Flight Rules (IFR) aircraft may be vectored by a radar controller, except as otherwise authorized for radar approaches, departures, and missed approaches."
- OPS25LA048: "Audio recording provided by the FAA indicated that when the flight crew contacted NORCAL on the missed approach and explained the reason for the missed approach, the air traffic controller stated, “… news to me.” The NORCAL controller subsequently stated, “This is a big surprise to what you are saying, and we are trying to figure out on our side what is going on.” The flight crew confirmed they had adequate fuel to attempt another approach and, if necessary, be able to divert to the flight’s filed alternate airport."
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

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent MAC Airprox / ACAS alert / loss of separation / near midair / midair collision*

**Definition.** During pushback or towing the tug, towbar or aircraft strikes another aircraft, a vehicle or a fixed object.

**Include when**
- The occurrence meets the CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) definition.  `[parent:MAC]`
- Core definition: During pushback or towing the tug, towbar or aircraft strikes another aircraft, a vehicle or a fixed object.  `[candidate:B20]`
- Matches 'Loss of separation with aircraft - both airborne' (ECCAIRS 1.3.0.12 · Events (390) · 2180101 · Aircraft operation general › Aircraft - near collisions/loss of separation › Loss of separation between aircraft): This includes the AIRPROX defined as: A situation in which, in the opinion of a pilot or air traffic services personnel, the distance between aircraft as well as their relative positions and speed have been such that the safety of the aircraft involved may have been compromised. An aircraft proximity is classified as follows: Risk of collision. The risk classification of an aircraft proximity in which serious risk of collision has existed. Safety not assured. The risk classification of an aircraft proximity in which the safety of the aircraft may have been compromised. No risk of collision. The risk classification of an aircraft proximity in which no risk of collision has existed. Risk not determined. The risk classification of an aircraft proximity in which insufficient information was available to determine the risk involved, or inconclusive or conflicting evidence precluded such determination.  `[definition:ECC-2180101]`
- Matches 'Near collision with vehicle' (ECCAIRS 1.3.0.12 · Events (390) · 2180405 · Aircraft operation general › Aircraft - near collisions/loss of separation › Near collision with object on ground): An event a near collision by an aircraft with a vehicle.  `[definition:ECC-2180405]`
- Matches 'Loss of separation with no risk of collision' (ECCAIRS 1.3.0.12 · Events (390) · 2180105 · Aircraft operation general › Aircraft - near collisions/loss of separation › Loss of separation between aircraft): No risk of collision. The risk classification of an aircraft proximity in which no risk of collision has existed. Doc 4444.  `[definition:ECC-2180105]`

**Exclude when**
- Belongs to sibling B07 'Loss of separation caused by an ATC clearance' when it matches that bucket better (1 report(s) assigned there).  `[report:LAX08FA265]`  
  > According to the supplemental flight manual for the Skywatch, the purpose of the system was "to advise the pilot of transponder equipped aircraft that may pose a collision threat." The supplemental flight manual stated that the SkyWatch monitors a radius of approximately 6 nautical miles around the aircraft by interrogating transponders in the monitored area and determining if a collision threat exists.
- Belongs to sibling B08 'TCAS resolution advisory after a level bust' when it matches that bucket better (3 report(s) assigned there).  `[report:ANC16FA052]`  
  > When a rule of this section gives another aircraft the right-of-way, the pilot shall give way to that aircraft and may not pass over, under, or ahead of it unless well clear.
- Distinguish from sibling B12 'GNSS interference or spoofing' under the same parent.  `[sibling:B12]`
- Coded GCOL (Ground Collision) rather than MAC: similar wording, different occurrence category.  `[report:SEA08LA061]`  
  > The UAL tug operator reported to SFO Airport Authority shortly after the collision that during the pushback process, he was looking over his shoulder and didn't see the other aircraft pushback from Gate 79.
- Not 'A standing or parked aircraft was struck/damaged by a vehicle/equipment' — that definition is crosswalked to ADRM, not MAC.  `[definition:ECC-5030704]`
- Not 'Collision of towed aircraft with object/obstacles' — that definition is crosswalked to RAMP, ADRM, not MAC.  `[definition:ECC-99010060]`
- Not 'Collision of a vehicle with an another vehicle or moveable equipment' — that definition is crosswalked to GCOL, ADRM, not MAC.  `[definition:ECC-5030701]`
- Events better described by CICTT GCOL (Ground Collision) (runner-up parent, margin 0.21).  `[parent:GCOL]`

**Linked example reports**
- DCA20IA081/2: "(b) No person may operate a small unmanned aircraft so close to another aircraft as to create a collision hazard."
- ERA17FA143/2: "Cause: Personnel issues-Psychological-Attention/monitoring-Monitoring environment-Pilot of other aircraft."
- CEN22FA081: "Additionally, no person shall operate an ultralight vehicle in a manner that creates a collision hazard with respect to any aircraft."
- ERA10LA041: "Each TCAS-equipped aircraft interrogates all other aircraft in a determined range about their position, and all other aircraft reply to other interrogations."
- CEN22FA424/2: "HISTORY OF FLIGHTOn September 17, 2022, about 0853 mountain daylight time, a Cessna 172S, N2117Y, and a Sonex Aircraft Xenos, N255BF, were destroyed when they were involved in a mid-air collision near Longmont, Colorado."
- CEN14LA036: "The bottom of the 185 and the top of the 182 met." After the collision, the skydivers jumped free of the C-185 as it went inverted."
- ERA18FA194: "Cause: Personnel issues-Psychological-Attention/monitoring-Monitoring other aircraft-Pilot of other aircraft."
- DEN08MA116: "The witness stated, "I saw both aircraft on what appeared to be a collision course."
- DCA17IA202: "AIRCRAFT INFORMATIONThe UH-60M is a four-bladed, twin-engine, medium utility helicopter manufactured by Sikorsky Aircraft."
- WPR16FA065/2: "Cause: Personnel issues-Psychological-Attention/monitoring-Monitoring other aircraft-Pilot of other aircraft."
- WPR16LA146/2: "The FAA Airplane Flying Handbook states, "Collision Avoidance All pilots must be alert to the potential for midair collision and near midair collisions… This concept requires that vigilance shall be maintained at all times, by each person operating an aircraft regardless of whether the operation is conducted under instrument flight rules (IFR) or visual flight rules (VFR)…Most midair collision accidents and reported near midair collision incidents occur in good VFR weather conditions and during the hours of daylight."
- WPR15FA010: "Federal Aviation Administration (FAA) regulations [14 CFR 91.113(b)] required that each person operating an aircraft maintain vigilance so as to "see and avoid other aircraft." When aircraft of the same certification category are converging, "the aircraft to the other's right has the right-of-way." However, the FAA Pilot's Handbook of Aeronautical Knowledge (FAA-H-8083-25B) noted that even if entitled to the right-of-way, a pilot should yield if another aircraft seemed too close."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass

### B21 · Disruptive or unruly passenger

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent CABIN Cabin Safety Events*

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

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent RE Runway Excursion*

**Definition.** The tail strikes the runway during takeoff rotation, often after early or fast rotation or a wrong takeoff speed or weight.

**Include when**
- The occurrence meets the CICTT RE (Runway Excursion) definition.  `[parent:RE]`
- Core definition: The tail strikes the runway during takeoff rotation, often after early or fast rotation or a wrong takeoff speed or weight.  `[candidate:B22]`
- Matches 'Anomaly: Ground Excursion – Runway' (NASA ASRS coding taxonomy): An aircraft departs the runway surface during the takeoff or landing roll, including overruns after a long or fast landing.  `[definition:IND-07]`
- Matches 'Runway excursion (veer-off and overrun)' (SKYbrary – Runway Excursion): An aircraft leaves the runway surface during takeoff or landing, either by veering off the side or by overrunning the end.  `[definition:IND-05]`
- Matches 'Runway condition code (RWYCC)' (ICAO Global Reporting Format (GRF) for runway surface conditions): A runway condition code from 6 (dry) down to 0 reports braking performance on wet or contaminated runways (water, slush, snow, ice), so crews can recompute landing distance.  `[definition:IND-06]`

**Exclude when**
- Distinguish from sibling B03 'Veer-off during landing in a strong or gusty crosswind' under the same parent.  `[sibling:B03]`
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

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent LOC-I Loss of Control – Inflight*

**Definition.** A sudden change in wind speed or direction on approach, often near a thunderstorm or microburst, causes loss of airspeed and a windshear warning.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: A sudden change in wind speed or direction on approach, often near a thunderstorm or microburst, causes loss of airspeed and a windshear warning.  `[candidate:B23]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Matches 'Stall warning triggered' (ECCAIRS 1.3.0.12 · Events (390) · 2260500 · Aircraft operation general › Warning system triggered): Stall warning triggered  `[definition:ECC-2260500]`

**Exclude when**
- Belongs to sibling B05 'Stall warning or upset during a go-around' when it matches that bucket better (4 report(s) assigned there).  `[report:NYC08MA090]`  
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
- Events better described by CICTT WSTRW (Windshear or Thunderstorm) (runner-up parent, margin 0.17).  `[parent:WSTRW]`

**Linked example reports**
- CHI08FA282: "At 1835:55, N193BS transmitted, and Minneapolis three bravo sierra so for planning purposes uh (unintelligible) we are going to get radar vectors to the localizer three six.” At 1836:01, ZMP03 transmitted, “november three bravo sierra affirmative.” At 1904:49, ZMP03 transmitted, “a november three bravo sierra’s four south of dougy maintain three thousand five hundred til on a published portion of the approach cleared for the localizer three six approach arbor vitae.” At 1905:07, N193BS transmitted, “ah i got all that ah three thousand five hundred till on a published segment (unintelligible) cleared three six approach.” At 1905:13, ZMP03 transmitted, “November three bravo sierra roger and are you going to be able to shoot the approach from a couple south of the marker there.” At 1905:19, N193BS transmitted, “i’m sorry what.” At 1905:20, ZMP03 transmitted, “are you going to be able to make the approach from fifty two hundred from a couple south of the marker.” At 1905:29, the autopilot (AP) was selected OFF at a pressure altitude of 5,033 feet and a heading of 359 degrees magnetic."
- CEN12LA345: ""Low-level wind shear is a sudden, drastic change in wind speed and/or direction over a very small area."
- WPR22FA068: "About 1 second later the copilot stated, “speed speed speed, more more, more more, faster, faster.” Soon after, the CVR indicated that the airplane impacted the terrain."
- WPR17FA023: "Additionally, the POH recommends "a slightly higher approach speed under turbulent air conditions." This is to compensate for any sudden loss in the headwind component, which would result in a momentary loss of airspeed and could lead to an aerodynamic stall above the published stall speed."
- DCA17FA109: "Most recently, during the ATP certificate checkride, on July 22, 2016, the captain received a notice of disapproval due to excessive deflection of both the glideslope and localizer for an instrument landing system approach, repeated glideslope and sink rate warnings from the ground proximity warning system, and his subsequent failure to initiate a go-around."
- CEN24FA064: "At 12:16:40, the controller issued a heading of 270°, and at 12:17:17 instructed the pilot to “turn right heading 030° maintain 4,300 until established on the final approach course, cleared RNAV runway 36 approach.” The KSJT RNAV runway 36 final approach course heading is 002° magnetic, or 6.7° true."
- CEN14FA438: "METEOROLOGICAL INFORMATIONAt 1535 the Automated Surface Observation System (AWOS) at 0F2 reported wind from 150 degrees at 9 knots gusting to 14 knots, wind direction 100 degrees variable 170 degrees, visibility 10 miles, sky clear, temperature 35 degrees Celsius (C), dew point temperature 17 degrees C, with an altimeter setting of 29.92 inches of mercury."
- ERA12FA007: "He noted the airplane was in a nose low descending turn (consistent with a turn onto final approach), and when it was on short final approach, the airplane was about 75 to 80 feet above ground level (agl) and east of a barn located south of the approach end of runway 36."
- CEN21FA209: "ADDITIONAL INFORMATIONStandard LNAV/VNAV Approach FAA Advisory Circular (AC) 91-89, Mitsubishi MU-2B Training Program, states that before the final approach fix, the airplane should be configured with 5° flaps and a minimum airspeed of 140 kts."
- ERA09LA111: "Approach and Landing Guidance According to the FAA's Airplane Flying Handbook (FAA-H-8083-3A), the objective of a good final approach is to descend at an angle and airspeed that will permit the airplane to reach the desired touchdown point at an airspeed which will result in minimum floating just before touchdown; in essence, a semi-stalled condition."
- GAA16CA002: "According to the airport manager, when the airplane was on final approach he announced on the common traffic advisory frequency, "wind 250 at 11 and use caution for down drafts and turbulence on short final." The accident pilot acknowledged the transmission."
- ERA13FA088: "The airplane was observed on radar turning to the northwest and intercepting the final approach course, then turned again and flew east of the final approach course."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 FAIL · G9 pass

### B24 · Landing short of the runway

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent LOC-I Loss of Control – Inflight*

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
- ERA18TA255: "A witness located on the airport's ramp reported that he "heard a high revving engine noise and turned towards the approach end of the runway and saw [a] small plane strike the [approach] lights." According to a Federal Aviation Administration (FAA) inspector who examined the airplane at the accident site, damage to the approach lighting system began with the elevated approach lights about 900 ft from runway 23 and continued to where the airplane came to rest about 400 ft short of the runway threshold."
- CEN10FA557: "The controller told the pilot that the final approach course was not depicted on his radar display, to which the pilot replied, "Alright, well thank you very much." At 2007:14, the controller reissued the approach clearance and asked the pilot if he wanted to proceed to MIGPY intersection to complete the procedure turn to the final approach course."
- CEN10FA101: "The runway is equipped with high intensity runway lights (HIRL), and both runway ends have runway end identification lights (REIL)."
- CEN11FA144: "A review of the cockpit voice recorder (CVR) transcript revealed that the flight was cleared for the ILS runway 22 approach at 1055:51 (hhmm:ss)."
- ERA16LA085: "The pilot asked if that was for the ILS approach to runway 20, and the controller advised that it was for the GPS approach to runway 2 at JQF."
- CEN10FA119: "At 1306, the controller approved the pilot's request to fly direct SCHUM intersection, which was an initial approach fix (IAF) for the area navigation (RNAV)/GPS Runway 33 instrument approach into FXY."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B25 · Airframe icing in flight

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent ICE Icing*

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
- CEN09LA206: "The service bulletin noted that the affected airplanes may have been "originally equipped with anti-ice and/or deice equipment that could make the airplane appear to be certified for flight in known icing conditions when in actuality it is not." The service bulletin further states that failure to avoid flight in known icing conditions can result in adverse performance/flight characteristics of the airplane that could result in serious injury and/or death to the pilot, crew, and/or passengers."
- NYC08FA139: "In those cases, the pilots chose to continue their flights without implementing an icing exit strategy or an alternate course of action…." The FAA letter also stated that "area forecasts alone are generally too broad to adequately inform a pilot of known icing conditions," and "may cover a large geographic area or represent too long a span of time to be particularly useful to a pilot." The letter further noted that, "pilots should not expose themselves or others to the risk associated with flying into conditions in which ice is likely to adhere to an aircraft."
- CEN15LA091: "Minimum speed in icing conditions Minimum airspeed in icing conditions, for all flight phases including approach, except takeoff and landing."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### B26 · Unreliable airspeed from blocked pitot probes

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent ICE Icing*

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
- CEN20LA028: "The outboard ends of the horizontal stabilizer had ice formation on about the outer 9 inches of both horizontals." AIRCRAFT INFORMATIONThe airplane’s ice detection system was equipped with a rotary-cutter type ice detector, two warning annunciators and a left-wing inspection spotlight."
- CEN11FA144: "Probable cause: The pilot’s decision to conduct an instrument approach in icing conditions without the anti-ice system activated, contrary to the airplane flight manual guidance, which resulted in an inadvertent aerodynamic stall due to an in-flight accumulation of airframe icing."
- ANC19FA038: "The forecast indicated moderate icing and marginal visual flight rules (MVFR) to instrument flight rules (IFR) conditions, with precipitation in the form of snow and fog."
- CEN14FA009: "One report of moderate icing came from a large Boeing KC-135E as it was taking off from IAB, and this report along with the ice pellet and snow reports indicate that more severe icing was possible at the flight altitude of the accident flight around the accident time."
- ERA22LA191: "The FIPs indicated that the icing intensity would range from “light” to “heavy.” An AIRMET for icing conditions valid from 1700 through 2000 indicated moderate icing between the freezing level and 17,000 ft msl."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### B27 · Crew crossed a hold-short line without clearance

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent RI Runway Incursion*

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
- Events better described by CICTT GCOL (Ground Collision) (runner-up parent, margin 0.12).  `[parent:GCOL]`

**Linked example reports**
- DCA24FA164: "Local Controller Two instructed the flight crew of SWR17K to exit runway 4L on runway 31L with a good read back."
- OPS09IA009/2: "Probable cause: The local controller did not visually scan the runways and ensure that the E145 had crossed runway 24L prior to issuing a takeoff clearance to the DH8, did not ensure separation between the two airplanes, and did not cancel takeoff clearance for the DH8 in a timely manner."
- DCA24LA219: "The flight crew did not observe any equipment, markings, visual closed runway lighted “Xs” designations, or any other sign indicating that the runway was closed, and all equipment and people were clear of the runway."
- OPS25LA054: "The flight crew reported they made the appropriate advisory transmissions on the MBS common traffic advisory frequency (CTAF) as they taxied to runway 14 via taxiway “C” and taxiway “A.” During the taxi out to runway 14 the crew reported there “were no visible cues indicating a closure of the taxiways or runways.” As the flight was holding short of runway 14, the first officer contacted Great Lakes approach control and informed the controller that they were number one at runway 14 and ready for departure."
- DCA26LA242/2: "Delta Air Lines Flight 2351 (DAL2351) Flight Crew Statements Postincident statements provided by the DAL2351 flight crew revealed the first officer (FO) was the pilot flying and the captain was the pilot monitoring."
- OPS21LA003: "At 1746:02 The ATC tower controller stated, “do not overfly the aircraft on the runway.” According to the Southwest pilots’ interviews, the pilot monitoring unknowingly keyed the transmit button and stated, “how are we going to do that.” According to written statements from the SkyWest flight crew, the captain, after receiving clearance from the controller to line up and wait on runway 27 and that there was traffic on a 5-mile final, taxied into position for departure."
- OPS09IA007/2: "The traditional taxi route for aircraft departing runway 6L was the ground controller directed aircraft to taxi via taxiway L, to taxiway N and then the local controller directed across runway 6R on taxiway N to a left turn on taxiway G to the approach end of runway 6L."
- DCA23LA125/2: "Contributing to the incident was the air traffic control tower team’s nondetection of the AAL106 crew’s deviation from taxi instructions while performing concurrent operational tasks; the timing of the runway status light system, which activated too late to prevent the AAL106 crew from crossing the runway hold short line; and American Airlines’ lack of adequate risk controls to prevent concurrent flight crew tasks from leading to distraction, loss of situational awareness, and deviation from an authorized taxi clearance."
- DCA23LA179/2: "The LC controller instructed the crew to taxi to runway 14 via taxiway A, and cross runway 22."
- DCA22LA126: "The first officer reported that when the flight exited the clouds, he could not see the runway but did visually acquire the TUL airport beacon and said it “looked like a normal downwind.” The captain reported that after exiting the clouds he could see the lights for runway 8/26 and that they were “normal.” The flight crew extended the centerline for runway 18L in their flight management system, which displayed the extended centerline on their ND in the cockpit."
- DCA23LA133: "At 1610:21, the local controller instructed the KMK145 pilot to turn “right” onto taxiway E and cross “runway 4R.” The pilot questioned the instruction to turn right at the taxiway, and the controller then advised the pilot to turn left on taxiway E and hold-short of runway 8L, and the pilot acknowledged those instructions."
- DCA24FA017/2: "A review of certified air traffic control voice recordings provided by the Federal Aviation Administration (FAA) revealed that at 1514:09, before N269AA began its taxi, the flight crew contacted ground control (GC) to request clearance to taxi for departure, which they received."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 pass · G8 pass · G9 pass

### B28 · Wrong route or waypoint loaded in the FMS

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent LOC-I Loss of Control – Inflight*

**Definition.** The flight management system is loaded with the wrong route, waypoint or departure, and the aircraft deviates from its cleared route.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: The flight management system is loaded with the wrong route, waypoint or departure, and the aircraft deviates from its cleared route.  `[candidate:B28]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Matches 'Aeroplane - spin' (ECCAIRS 1.3.0.12 · Events (390) · 2080400 · Aircraft operation general › Aeroplane flight path deviation): An event involving a spin by a fixed wing aircraft.  `[definition:ECC-2080400]`
- Matches 'Aeroplane - mush/stall' (ECCAIRS 1.3.0.12 · Events (390) · 2080300 · Aircraft operation general › Aeroplane flight path deviation): An event involving a mush/stall by a fixed wing aircraft.  `[definition:ECC-2080300]`

**Exclude when**
- Belongs to sibling B05 'Stall warning or upset during a go-around' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN16LA230]`  
  > Contributing factor: Aircraft-Aircraft systems-Flight control system-Elevator control system-Malfunction.
- Belongs to sibling B24 'Landing short of the runway' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN10FA119]`  
  > After departure, the flight was cleared to SCHMD intersection before resuming the OZARK 3 departure procedure.
- Distinguish from sibling B23 'Windshear on final approach' under the same parent.  `[sibling:B23]`
- Distinguish from sibling C4 'Upset or stall after unreliable airspeed' under the same parent.  `[sibling:C4]`
- Distinguish from sibling C8 'Takeoff after de-icing holdover time exceeded' under the same parent.  `[sibling:C8]`
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
- WPR17FA089: "Cause: Aircraft-Aircraft systems-Flight control system-Elevator control system-Incorrect service/maintenance."
- CEN12FA670: "Over the intercom, the Flight Nurse heard the Flight Paramedic state that, "I'm not comfortable with this." At that time, the Flight Nurse turned to the right to look forward into the cockpit and the helicopter was in the clouds – totally "Whited Out." The Flight Nurse replied to the Paramedic, "Oh, I'm not either." She said that prior to the aircraft entering into the clouds the flight was normal, doing just fine and no issues."
- DCA11MA076: "Probable cause: The National Transportation Safety Board determines the probable cause(s) of this accident as follows: an aerodynamic stall and subsequent uncommanded roll during a one engine-inoperative takeoff flight test, which were the result of (1) Gulfstream’s failure to properly develop and validate takeoff speeds for the flight tests and recognize and correct the takeoff safety speed (V2) error during previous G650 flight tests, (2) the G650 flight test team’s persistent and increasingly aggressive attempts to achieve V2 speeds that were erroneously low, and (3) Gulfstream’s inadequate investigation of previous G650 uncommanded roll events, which indicated that the company’s estimated stall angle of attack while the airplane was in ground effect was too high."
- CEN21LA030: "Finding: Aircraft-Aircraft systems-Air conditioning system-Heating system-Damaged/degraded."
- ERA24FA371: "Finding: Aircraft-Aircraft systems-Flight control system-TE flap control system-Incorrect use/operation."
- ERA22LA120: "The pilot spent the next 3 minutes attempting to program the route of flight into the flight management system, and mentioned, “I can’t get [nothing] on this thing that I want.” On one occasion, the pilot asked the controller to clarify the name of the fix that they had been cleared to fly to in order to begin the approach (CIGOR or CIBAG), and on another occasion he asked the same question of the passenger."
- ERA17FA190: "The briefings included weather observations, forecasts, and NOTAMs for the departure, destination, and selected en route stations; PIREPs (pilot reports); and in-flight weather advisories for the planned flight."
- WPR24FA257: "The Primus APEX is composed of multiple subsystems including, but not limited to, the electronic display system, automatic flight control system, crew alerting system, flight management system, traffic alert and collision avoidance system, terrain awareness and warning system, and weather radar system."
- CEN24MA111: "According to Orbic Air’s flight operations employee, during the broker discussions, he mentioned to the broker the addition of a second pilot for the nighttime flights, which was a standard company precaution for flights to Las Vegas, Nevada, due to the route and timing considerations."
- WPR16FA037: "As shown in figure 2, the system comprised a Garmin GDU 620 primary flight display and multifunction display, a Garmin GRS 77 attitude heading reference system (AHRS), and a Garmin GDC 74 air data computer."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### C1 · Landing or takeoff on an unintended surface

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent RI Runway Incursion*

**Definition.** The aircraft lands, lines up to land, or starts a takeoff on a surface other than the assigned runway: a taxiway, a closed or wrong runway, or the wrong airport.

**Include when**
- The occurrence meets the CICTT RI (Runway Incursion) definition.  `[parent:RI]`
- Core definition: The aircraft lands, lines up to land, or starts a takeoff on a surface other than the assigned runway: a taxiway, a closed or wrong runway, or the wrong airport.  `[candidate:C1]`
- Matches 'Wrong-surface event' (FAA Runway Safety programme): A landing, attempted landing, line-up or takeoff on a surface other than the one assigned: a wrong runway, a taxiway, a closed runway or the wrong airport.  `[definition:IND-03]`
- Matches 'Anomaly: Ground Incursion – Runway or Taxiway' (NASA ASRS coding taxonomy): An aircraft, vehicle or person entering a runway or taxiway without authorization, or an aircraft using a taxiway or the wrong runway for landing or takeoff.  `[definition:IND-04]`
- Matches 'Runway incursion' (ICAO Doc 9870, Manual on the Prevention of Runway Incursions): Any occurrence at an aerodrome involving the incorrect presence of an aircraft, vehicle or person on the protected area of a surface designated for the landing and takeoff of aircraft.  `[definition:IND-01]`

**Exclude when**
- Belongs to sibling B01 'Vehicle or pedestrian on the runway without clearance' when it matches that bucket better (2 report(s) assigned there).  `[report:OPS16IA008]`  
  > As AAL2408 began its takeoff roll the Runway Status Lights (RWSLs) on runway 35L activated illuminating the Runway Entrance Lights (RELs) at the hold short locations of the three aircraft that had just been instructed to cross runway 35L, as well as the Takeoff Hold Lights (THLs) at the approach end of the runway.
- Belongs to sibling B02 'Landing on a taxiway or the wrong runway at night' when it matches that bucket better (2 report(s) assigned there).  `[report:DCA26MA161]`  
  > R35 entered taxiway BB, another airplane that had landed on runway 4 crossed taxiway D, and Jazz flight 646 was about 3.7 nautical miles from taxiway D and at 1,180 ft altitude.
- Belongs to sibling B27 'Crew crossed a hold-short line without clearance' when it matches that bucket better (1 report(s) assigned there).  `[report:DCA22LA126]`  
  > The captain stated during a post incident interview, that he applied the brakes and “came on them harder initially because he was confused.” After slowing the airplane, the captain asked the FO “are we on the correct runway?” and then stated, “we landed on the right [hand] runway.” After informing the controller that they had landed on runway 18R, the controller provided taxi instructions to the ramp.
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
- OPS15IA011: "Airport Surface Detection Equipment Model X The air traffic control front-line manager on duty in the tower stated that the airport surface detection equipment, model X (ASDE-X) alarmed; however, there was insufficient time to cancel ENY3084's takeoff clearance."
- OPS09IA005: "At 1015:11, LC east directed JIA390 to taxi into position and hold at the approach end of runway 18L and advised that there was traffic landing on runway 23, which intersected runway 18L."
- OPS08IA015/2: "Runway 13/31 crossed runway 6 at 2,700 feet from the threshold, and taxiway B intersected runway 6 at 3,100 feet from the threshold."
- OPS08IA013/2: "Both aircraft were landing on runway 29R at the Fresno-Yosemite International Airport (FAT), Fresno, California, and were under control of the FAT airport traffic control tower."
- ANC11LA008: "After landing on the closed portion of the old runway, the airport manager said the airplane struck a ditch/berm where a portion of the old runway became an elevated taxiway for the new runway."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C2 · Runway entry or crossing without clearance

*Merged into B01 before grounding.*

### C3 · Overrun after a long or fast landing on a wet or contaminated runway

*Merged into B04 before grounding.*

### C4 · Upset or stall after unreliable airspeed

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent LOC-I Loss of Control – Inflight*

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
- WPR10LA059: "Coping with the hazards of icing begins with preflight planning to determine where icing may occur during a flight and ensuring the aircraft is free of ice and frost prior to takeoff.” “Because of their small size and shape, antennas that do not lay flush with the aircraft’s skin tend to accumulate ice rapidly."
- ERA11FA493: "This low pressure would create a differential pressure in the stall warning system, which would draw air through the warning horn, and would result in an audible warning between 5 to 10 miles per hour above the stall in all configurations."
- ERA19LA072: "Also causal was the pilot’s failure to maintain an appropriate airspeed for flight in icing conditions."
- CEN10MA088: "I don't think that spoileron thing is working for some reason." Post-accident performance studies indicated that the airplane's N1 and true airspeed decreased, and bank angle increased to greater than 50 degrees."
- WPR12FA059: "Review of the pilot's flight logbook indicated a total flight experience of about 713 hours."
- WPR16FA067: "115 km/h (62 kts) should be maintained." Aviation Circular 23-8C Flight Test Guide states that the following formula can be used to calculate the stall airspeed when the airplane's weight is different than the specified weight, Vs=Vstv(Ws/Wt) where Vs= new stall airspeed, Vst= standard stall airspeed, Ws= new weight, Wt = standard weight."
- ERA14FA112: "The anti-icing system included heated stall warning, rudder horn anti-ice, rudder tab anti-ice, generator inlet anti-ice, electrically heated wind shield, and pitot-static heaters."
- ERA10FA178: "Probable cause: The pilot’s failure to maintain adequate airspeed during takeoff, which resulted in an aerodynamic stall."
- DCA12IA141: "Probable cause: an in-flight loss of control due to the flight crew's inattention to airspeed, pitch attitude, and engine power during the climb leading to an aerodynamic stall."
- ERA24FA088: "The windshield anti-ice switch was in the “off” position, and the propeller anti-ice, pitot heat, and ice detect light switches were impact damaged."
- CEN16LA093: "Flight in freezing rain, freezing drizzle, or mixed icing conditions (supercooled liquid water and ice crystals) may result in ice build-up on protected surfaces exceeding the capability of the ice protection system, or may result in ice forming aft of the protected surfaces."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C5 · TCAS resolution advisory after an altitude deviation

*Merged into B08 before grounding.*

### C6 · Clear-air turbulence with cabin injuries

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent TURB Turbulence Encounter*

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
- Events better described by CICTT CABIN (Cabin Safety Events) (runner-up parent, margin 0.73).  `[parent:CABIN]`

**Linked example reports**
- ERA09LA488: "Meteorological Conditions in Vicinity of Turbulence Encounter The 1600 NWS radar composite reflectivity mosaic image depicted several defined echoes associated with thunderstorms north of the departure airport, including a short but intense line at the latitude and longitude of the turbulence encounter, but below the airplane's altitude."
- DCA24FA143: "After the turbulence encounter, the A FA walked through the cabin to inspect for damage and check for injuries."
- DCA16CA209: "On August 3, 2016 at 7:45 pm eastern daylight time, American Airlines flight 1007, an Airbus A319, N9010R, encountered clear air turbulence on descent to the Owen Roberts International Airport (GCM), George Town, Cayman Islands."
- DCA10CA032: "After encountering the turbulence, the crew assessed airplane damage and checked the number and severity of injuries to passengers and crew."
- CEN14CA455: "While cruising in smooth air conditions with no clouds in the area and with the autopilot on and the seat belt sign off the airplane had a brief encounter with what the flight crew described as wake turbulence."
- DCA23LA096: "At 1013:43, the flight crew made a passenger announcement about the turbulence encounter."
- DCA12FA069: "COMMUNICATIONS Following the turbulence encounter, the flight crew was unable to establish communications with company dispatch or station personnel to alert emergency crews."
- CEN09LA388: "On June 15, 2009, about 1652 mountain daylight time (mdt), a Beech B100 (King Air) airplane, N4490M, operated by Air Methods Corporation, encountered clear-air-turbulence while descending through 7,000 feet mean sea level (msl) en route to Rapid City Regional Airport (KRAP), Rapid City, South Dakota."
- DCA14CA014: "While cruising at FL360 in smooth air conditions with no storms in the vicinity, the airplane experienced a 3 to 5 second encounter with clear air turbulence."
- DCA23LA421: "Probable cause: An inadvertent encounter with clear air turbulence during cruise flight."
- CEN22LA166: "Probable cause: The airplane’s encounter with severe clear air turbulence that was not forecasted, which resulted in a serious injury to an unrestrained passenger."
- DCA16IA215: "Additionally, there were no pilot reports (PIREPs) to indicate that other aircraft were encountering severe turbulence nor any advisories of turbulence from air traffic control."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### C7 · Engine damage or shutdown after bird ingestion

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent BIRD Bird*

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
- DCA25FA148: "The captain checked the engine indications “which soon displayed right engine damage including fire indications (fire bell, warning lights, discrete fire light on the right fuel control) and an R ENGINE FIRE message on the Engine Indicating and Crew Alerting System (EICAS) display”."
- DCA24LA330: "DAMAGE TO AIRCRAFTPostincident examination of the airplane found damage to the left engine fan blades consistent with a bird ingestion (see figure 3)."
- GAA19CA168: "Probable cause: The helicopter’s collision with a bird during cruise flight."
- GAA20CA038: "Probable cause: An in-flight collision with a bird."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass

### C8 · Takeoff after de-icing holdover time exceeded

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent LOC-I Loss of Control – Inflight*

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

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent ARC Abnormal Runway Contact*

**Definition.** A hard or bounced touchdown, or contact of the tail with the runway during rotation or flare.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: A hard or bounced touchdown, or contact of the tail with the runway during rotation or flare.  `[candidate:C9]`
- Matches 'Hard landing, tail strike' (SKYbrary – Hard Landing and Tail Strike): A touchdown with a vertical load above limits, a bounced landing, or contact of the tail with the runway during takeoff rotation or landing flare.  `[definition:IND-18]`
- Matches 'Hard landing' (ECCAIRS 1.3.0.12 · Events (390) · 2010600 · Aircraft operation general › Aircraft handling): An event involving a hard landing. Hard landing: A landing in which the vertical deceleration encountered required a hard landing check.  `[definition:ECC-2010600]`
- Matches 'Tail strike' (SKYbrary – Tailstrike): The aft fuselage contacts the runway during takeoff rotation or landing, often after early rotation, wrong takeoff speeds or excessive pitch.  `[definition:IND-35]`
- Narrative describes 'hard' (12 of 12 supporting reports).  `[report:ERA09LA538]`  
  > The approach was stable, "all the way down to the flare;" however, when airplane was about 15 feet above the runway, "the aircraft suddenly lost airspeed and landed hard." The airplane bounced approximately 15 to 20 feet back into the air, before it contacted the ground, and bounced about 5 to 10 feet.
- Narrative describes 'bounced' (10 of 12 supporting reports).  `[report:ERA09LA538]`  
  > The approach was stable, "all the way down to the flare;" however, when airplane was about 15 feet above the runway, "the aircraft suddenly lost airspeed and landed hard." The airplane bounced approximately 15 to 20 feet back into the air, before it contacted the ground, and bounced about 5 to 10 feet.
- Narrative describes 'landed' (10 of 12 supporting reports).  `[report:ERA09LA538]`  
  > The approach was stable, "all the way down to the flare;" however, when airplane was about 15 feet above the runway, "the aircraft suddenly lost airspeed and landed hard." The airplane bounced approximately 15 to 20 feet back into the air, before it contacted the ground, and bounced about 5 to 10 feet.

**Exclude when**
- Belongs to sibling D06 'Bounced landing and improper recovery' when it matches that bucket better (1 report(s) assigned there).  `[report:WPR09LA480]`  
  > Probable cause: The pilot's improper landing flare and inadequate recovery from a bounced landing.
- Distinguish from sibling D07 'Gear-up landing with the landing gear not extended' under the same parent.  `[sibling:D07]`
- Distinguish from sibling D14 'Low rotor RPM in a helicopter' under the same parent.  `[sibling:D14]`
- Distinguish from sibling D15 'Balloon hard landing in high wind' under the same parent.  `[sibling:D15]`
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
- WPR10CA422: "Probable cause: The pilot’s inadequate flare and bounced landing recovery technique that resulted in a hard landing."
- WPR10CA453: "The pilot reported that during an off-field landing on a dry lake bed in a tail-wheel equipped airplane, he "rounded out too high, dropped hard," and the airplane bounced two times."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 FAIL · G9 pass

### D01 · Carburetor icing leading to loss of engine power

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent SCF-PP System/Component Failure – Powerplant*

**Definition.** Ice forms in the carburetor in conditions conducive to carburetor icing, often at reduced power, and the engine loses partial or total power because carburetor heat was not applied or was applied too late.

**Include when**
- The occurrence meets the CICTT SCF-PP (System/Component Failure – Powerplant) definition.  `[parent:SCF-PP]`
- Core definition: Ice forms in the carburetor in conditions conducive to carburetor icing, often at reduced power, and the engine loses partial or total power because carburetor heat was not applied or was applied too late.  `[candidate:D01]`
- Matches 'Power loss in a reciprocating engine due to non-mechanical failure' (ECCAIRS 1.3.0.12 · Events (390) · 1850104 · Aircraft/system/component › 8500 Reciprocating engine › 8501 Reciprocating engine general): An event involving a power loss in a reciprocating engine due to non-mechanical failure.  `[definition:ECC-1850104]`
- Matches 'Engine air system related event (ATA Code:7500)' (ECCAIRS 1.3.0.12 · Events (390) · 1750000 · Aircraft/system/component): (ATA Code:7500) An event involving the turbine engine compressor bleed air systems used to control the flow of air through the engine, cooling air systems, and heated air for engine anti-icing.  `[definition:ECC-1750000]`
- Matches 'Reciprocating engine - simulated failure' (ECCAIRS 1.3.0.12 · Events (390) · 1850105 · Aircraft/system/component › 8500 Reciprocating engine › 8501 Reciprocating engine general): An event involving a simulated power loss in a reciprocating engine.  `[definition:ECC-1850105]`

**Exclude when**
- Distinguish from sibling B13 'Engine shutdown after loss of oil pressure' under the same parent.  `[sibling:B13]`
- Distinguish from sibling B17 'Lithium battery fire from a passenger device' under the same parent.  `[sibling:B17]`
- Distinguish from sibling D12 'Reciprocating engine failure from a connecting rod or crankshaft fracture' under the same parent.  `[sibling:D12]`
- Coded FUEL (Fuel Related) rather than SCF-PP: similar wording, different occurrence category.  `[report:ERA16LA270]`  
  > According to a statement provided by the flight instructor, the carburetor heat was not used during takeoff, "as recommended in the pilot manual," and "carburetor heat was applied at the first sign of vibration and power reduction." After applying carburetor heat and noting the loss of RPM, the instructor turned the carburetor heat off to get as much power from the engine as possible to extend their glide range.
- Not 'Aircraft encountered icing conditions' — that definition is crosswalked to ICE, not SCF-PP.  `[definition:ECC-2220100]`
- Not 'Reciprocating engine - carburetor icing' — that definition is crosswalked to ICE, not SCF-PP.  `[definition:ECC-1850107]`
- Not 'De-icing' — that definition is crosswalked to ICE, RAMP, ADRM, not SCF-PP.  `[definition:ECC-5050200]`
- Events better described by CICTT FUEL (Fuel Related) (runner-up parent, margin 0.28).  `[parent:FUEL]`

**Linked example reports**
- ERA12LA575: "(3) If the airplane is equipped with a carburetor air temperature gauge, it can be used as a reference in maintaining carburetor air temperature at or slightly above the top of the yellow arc by application of carburetor heat." For "Rough Engine Operation or Loss of Power, Carburetor Icing," the POH states, "An unexplained drop in manifold pressure and eventual engine roughness may result from the formation of carburetor ice."
- ERA12FA143: "Probable cause: A partial loss of engine power due to the formation of carburetor ice and the flight instructor's improper application of carburetor heat."
- CEN18LA151: "The charted data showed that the weather was conducive to moderate icing at cruise power and serious icing at descent power about the time of the engine power loss."
- ERA21FA232: "Review of the icing probability chart contained withing the FAA Special Airworthiness Information Bulletin CE-09-35 revealed the atmospheric conditions at the time of the accident were “conducive to serious icing at glide power.” According to the Gulfstream American Model AA-5A Cheetah Pilot’s Operating Handbook, Normal Procedures: Page 4-11, DESCENT, (3) Carburetor Heat – As required by engine power setting and weather conditions page 4-19, NOTE – If engine runs rough during cruise with carburetor heat on, it may be due to an over-rich condition."
- ERA13LA269: "According to a carburetor icing probability chart published by the Federal Aviation Administration (FAA), the temperature and dew point conditions were conducive to the formation of serious carburetor icing at glide engine power settings."
- ERA18LA162: "An FAA carburetor icing probability chart indicated the temperature and dew point conditions were conducive to the formation of serious icing at glide power, and icing at glide and cruise power."
- CEN14LA161: "Probable cause: The flight instructor's failure to ensure that carburetor heat was used while performing maneuvers at reduced power settings in conditions conducive to the formation of carburetor ice, which resulted in a partial loss of engine power due to carburetor ice."
- WPR12LA329: "Additionally, it states that when conditions are conductive to carburetor icing that carburetor heat should be applied immediately and should be left ON until the pilot is certain all the ice has been removed."
- CEN17FA332: "Probable cause: The pilot's failure to use carburetor heat while operating in weather conditions that were conducive to carburetor ice formation, which resulted in a total loss of engine power due to carburetor ice accumulation."
- CEN19LA232: "In extreme cases of carburetor icing, even after the ice has been removed, full carburetor heat should be used to prevent further ice formation."
- CEN13LA398: "Probable cause: The pilot’s failure to recognize the formation of carburetor ice during cruise descent and apply carburetor heat, which resulted in the total loss of engine power."
- ERA21LA313: "Carburetor Heat According to the Aviation Maintenance Technician Handbook – Powerplant (FAA-H-8083-32B), carburetor heat is used in aircraft to prevent the formation of ice in the carburetor and carburetor normal flow air is admitted at the lower front nose cowling below the propeller spinner and is passed through an air filter into air ducts leading to the carburetor."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D02 · Fuel exhaustion from inadequate fuel planning

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent FUEL Fuel Related*

**Definition.** The engine stops because all usable fuel on board was used up: the pilot did not plan enough fuel for the flight, did not verify the quantity before departure, or continued past the point where a fuel stop was needed.

**Include when**
- The occurrence meets the CICTT FUEL (Fuel Related) definition.  `[parent:FUEL]`
- Core definition: The engine stops because all usable fuel on board was used up: the pilot did not plan enough fuel for the flight, did not verify the quantity before departure, or continued past the point where a fuel stop was needed.  `[candidate:D02]`
- Matches 'Minimum fuel and fuel emergency' (ICAO Annex 6 – Fuel planning and in-flight fuel management): The crew declares MINIMUM FUEL when any change may land them below final reserve, and MAYDAY FUEL when the landing fuel is expected to be below final reserve.  `[definition:IND-33]`
- Matches 'Turbine Engine fuel starvation' (ECCAIRS 1.3.0.12 · Events (390) · 1720106 · Aircraft/system/component › 7200 Turbine engine › 7201 Turbine engine - generally): An event involving a loss of power from a turbine engine due to fuel starvation. Fuel Starvation: Deprivation or insufficient supply of fuel to the engine.  `[definition:ECC-1720106]`
- Matches 'Reciprocating engine - fuel starvation' (ECCAIRS 1.3.0.12 · Events (390) · 1850106 · Aircraft/system/component › 8500 Reciprocating engine › 8501 Reciprocating engine general): An event involving a power loss in a reciprocating engine due to fuel starvation.  `[definition:ECC-1850106]`
- Narrative describes 'exhaustion' (9 of 12 supporting reports).  `[report:CEN19FA124]`  
  > Probable cause: The pilot's inadequate preflight fuel planning and fuel management, which resulted in a loss of engine power due to fuel exhaustion.
- Narrative describes 'inadequate' (7 of 12 supporting reports).  `[report:CEN19FA124]`  
  > Probable cause: The pilot's inadequate preflight fuel planning and fuel management, which resulted in a loss of engine power due to fuel exhaustion.
- Narrative describes 'preflight' (6 of 12 supporting reports).  `[report:CEN19FA124]`  
  > Probable cause: The pilot's inadequate preflight fuel planning and fuel management, which resulted in a loss of engine power due to fuel exhaustion.

**Exclude when**
- Distinguish from sibling D03 'Fuel starvation from fuel selector or tank mismanagement' under the same parent.  `[sibling:D03]`
- Coded SCF-PP (System/Component Failure – Powerplant) rather than FUEL: similar wording, different occurrence category.  `[report:WPR14LA185]`  
  > BPE did not change the engine designations (M14P or M14PF) and did not independently develop or provide power or fuel flow charts for the engines it modified, in part because there were multiple permutations of BPE engine modifications.
- Not 'Fuel system related event (ATA Code:2800)' — that definition is crosswalked to SCF-NP, not FUEL.  `[definition:ECC-1280000]`
- Not 'Closure of an aerodrome' — that definition is crosswalked to ATM, not FUEL.  `[definition:ECC-4070200]`
- Not 'Engine fuel system and control related event (ATA Code:7300)' — that definition is crosswalked to SCF-PP, not FUEL.  `[definition:ECC-1730000]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.39).  `[parent:SCF-PP]`

**Linked example reports**
- CEN19FA124: "Probable cause: The pilot's inadequate preflight fuel planning and fuel management, which resulted in a loss of engine power due to fuel exhaustion."
- CEN22LA189: "Using the information provided by the pilot, postaccident flight planning showed the engine would have consumed 21.9 gallons total for the flight."
- CEN18LA300: "Probable cause: The pilot's inadequate preflight and in-flight fuel planning, during which he did not visually check the fuel quantity in the fuel tanks and instead relied on the fuel gauges that were showing erroneous fuel quantity indications, which resulted in fuel exhaustion and the subsequent loss of engine power during cruise flight."
- CEN19FA236: "Probable cause: The pilot's failure to ensure adequate fuel was on board before departing and his in-flight fuel management, which resulted in a total loss of engine power due to fuel exhaustion."
- CEN15LA296: "Contributing to the accident was the unsnapped fuel bladder, which resulted in an inaccurate fuel quantity indication, and the pilot's inadequate preflight fuel planning, during which he relied solely on the fuel gauges to determine the amount of fuel on board."
- ERA20LA297: "Contributing to the fuel exhaustion was the fatigue fracture of an electrical wire in the tank unit or fuel transmitter, which likely resulted in an inaccurate fuel quantity indication."
- WPR13LA383: "Probable cause: The pilots' inadequate fuel planning, which resulted in the airplane departing with insufficient fuel to complete the planned flight, and their failure to recognize that discrepancy en route, which resulted in a total loss of engine power due to fuel exhaustion."
- ERA09CA297: "Probable cause: A total loss of engine power due to fuel exhaustion as a result of the pilot’s inadequate preflight planning."
- CEN14FA035: "Also causal were the pilot’s reliance on the fuel totalizer rather than the fuel quantity gauges to determine the fuel on board and his improper fuel planning."
- CEN16LA134: "Probable cause: The loss of engine power during cruise flight due to fuel exhaustion, which resulted from the pilot's inadequate preflight fuel planning and in-flight fuel management."
- WPR13LA416: "Probable cause: The pilot's inadequate preflight fuel planning, which resulted in departure with insufficient fuel to complete the flight, and consequent inflight power loss due to fuel exhaustion."
- ERA13CA107: "Contributing to the fuel exhaustion was the pilot’s lack of knowledge about the airplane’s total fuel capacity and fuel quantity instrumentation."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D03 · Fuel starvation from fuel selector or tank mismanagement

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent FUEL Fuel Related*

**Definition.** Fuel remains on board but does not reach the engine because the pilot selected an empty tank, positioned the fuel selector incorrectly, or did not switch tanks, and the engine loses power.

**Include when**
- The occurrence meets the CICTT FUEL (Fuel Related) definition.  `[parent:FUEL]`
- Core definition: Fuel remains on board but does not reach the engine because the pilot selected an empty tank, positioned the fuel selector incorrectly, or did not switch tanks, and the engine loses power.  `[candidate:D03]`
- Matches 'Turbine Engine fuel starvation' (ECCAIRS 1.3.0.12 · Events (390) · 1720106 · Aircraft/system/component › 7200 Turbine engine › 7201 Turbine engine - generally): An event involving a loss of power from a turbine engine due to fuel starvation. Fuel Starvation: Deprivation or insufficient supply of fuel to the engine.  `[definition:ECC-1720106]`
- Matches 'Reciprocating engine - fuel starvation' (ECCAIRS 1.3.0.12 · Events (390) · 1850106 · Aircraft/system/component › 8500 Reciprocating engine › 8501 Reciprocating engine general): An event involving a power loss in a reciprocating engine due to fuel starvation.  `[definition:ECC-1850106]`
- Matches 'Minimum fuel and fuel emergency' (ICAO Annex 6 – Fuel planning and in-flight fuel management): The crew declares MINIMUM FUEL when any change may land them below final reserve, and MAYDAY FUEL when the landing fuel is expected to be below final reserve.  `[definition:IND-33]`

**Exclude when**
- Distinguish from sibling D02 'Fuel exhaustion from inadequate fuel planning' under the same parent.  `[sibling:D02]`
- Coded SCF-PP (System/Component Failure – Powerplant) rather than FUEL: similar wording, different occurrence category.  `[report:CEN11LA148]`  
  > When FAA inspectors moved the fuel selector to the left main or auxiliary tank positions, fuel flowed to the fuel line at the engine.
- Not 'Fuel system related event (ATA Code:2800)' — that definition is crosswalked to SCF-NP, not FUEL.  `[definition:ECC-1280000]`
- Not 'Landing gear position and warning system related event (ATA Code:3260)' — that definition is crosswalked to SCF-NP, not FUEL.  `[definition:ECC-1326000]`
- Not 'Fuel leak (ATA Code:2801)' — that definition is crosswalked to SCF-NP, not FUEL.  `[definition:ECC-1280100]`
- Events better described by CICTT SCF-PP (System/Component Failure – Powerplant) (runner-up parent, margin 0.23).  `[parent:SCF-PP]`

**Linked example reports**
- ANC17LA028: "Fuel Selector Valves The FAA Pilot's Handbook of Aeronautical Knowledge (FAA-H-8083-25B) discusses how a fuel selector valve works and states: The fuel selector valve allows selection of fuel from various tanks."
- ERA25LA226: "The data shows one final fuel selector switch after the loss of engine power to the right fuel tank and fuel flow climbed slightly, but the engine did not regain power."
- CEN17FA085: "Probable cause: The pilot's negligent maintenance of the airplane, which resulted in improper fuel management, fuel starvation, and a loss of engine power during takeoff due to a missing securing pin in the fuel selector handle, and a subsequent forced landing on unsuitable terrain."
- CEN12LA110: "Shortly after takeoff, the pilot selected the auxiliary (AUX) fuel tanks "to burn from them first." Approximately 30 minutes later, the left engine started to vibrate like it wasn't getting enough fuel, so the pilot selected the left fuel tank from AUX to MAIN."
- LAX08LA073: "Fuel may be cross fed from the left main tank to the right engine or from the right main tank to the left engine by positioning both selector valves to the desired fuel tank."
- ERA21LA087: "During examination of the fuel system, the fuel selector was observed in the RIGHT fuel tank position and was confirmed to be in the right fuel tank position with low pressure air."
- CEN11FA625: "Documentation of the various cockpit controls and switches was performed with the following findings: Power Lever – forward Propeller lever – forward Condition lever – Forward Manual Override – Aft Flap Lever – Forward (up) Fuel Selector – Left tank Landing Gear – Up Engine Starter – Off Engine Ignition – Auto Auxiliary Boost Pump – Auto Fuel Selector – Manual Electrical Power Crash lever – Down After the on-scene examination, the airplane was transported to an enclosed facility for further examination."
- CEN19LA076: "Probable cause: The pilot's fuel mismanagement and his improper use and placement of the fuel selector, contrary to operating procedures, which resulted in a partial loss of engine power due to fuel starvation."
- CEN22FA298: "Upon return to IL48, the pilot’s son stated that he exited the airplane and at that time the right fuel tank gauge indicated just under a ¼ tank, and the left fuel tank gauge indicated just under ½ tank; he estimated there was about 12 gallons of fuel remaining."
- WPR24LA296: "The first calculation assumed the pilot departed with the fuel tank selector positioned to BOTH, had selected the RIGHT tank when cruise flight was reached, and then switched fuel tanks every 30 minutes until the LEFT tank was selected 45 minutes before a total loss of power."
- ERA09LA412: "The selector was positioned left to select wing fuel, up to select fuselage fuel, and right to select shutoff."
- CEN13FA432: "The left side fuel system main fuel sump was drained."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D04 · Loss of directional control in a crosswind on landing

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent LOC-G Loss of Control – Ground*

**Definition.** During the landing roll in a crosswind or gusting wind the pilot does not maintain directional control and the airplane veers off the runway, ground loops or strikes objects beside the runway.

**Include when**
- The occurrence meets the CICTT LOC-G (Loss of Control – Ground) definition.  `[parent:LOC-G]`
- Core definition: During the landing roll in a crosswind or gusting wind the pilot does not maintain directional control and the airplane veers off the runway, ground loops or strikes objects beside the runway.  `[candidate:D04]`
- Matches 'Intentional ground loop/swerve' (ECCAIRS 1.3.0.12 · Events (390) · 2010501 · Aircraft operation general › Aircraft handling › Swerve-take-off/landing): An event involving an intentional ground loop or swerve of the aircraft on take-off or landing, e.g. to avoid obstacles in the runway overrun area.  `[definition:ECC-2010501]`
- Matches 'Helicopter damage caused by ground resonance' (ECCAIRS 1.3.0.12 · Events (390) · 2060300 · Aircraft operation general › Damage to aircraft): An event involving ground resonance damage to the helicopter. Aircraft damage caused by lightning strike (Lightning strike damage)                                                   2060400   * An event involving lightning strike damage to the aircraft. Moved to weather encounters  `[definition:ECC-2060300]`
- Matches 'Ground loop/swerve on take-off or landing' (ECCAIRS 1.3.0.12 · Events (390) · 2010500 · Aircraft operation general › Aircraft handling): An event involving a ground loop/swerve of the aircraft on take-off or landing.  `[definition:ECC-2010500]`
- Narrative describes 'control' (11 of 12 supporting reports).  `[report:SEA08CA112]`  
  > Although the flare and touchdown were uneventful, during the landing roll, the airplane encountered a gusting crosswind, and the pilot was unable to maintain directional control.
- Narrative describes 'pilot' (10 of 12 supporting reports).  `[report:SEA08CA112]`  
  > Although the flare and touchdown were uneventful, during the landing roll, the airplane encountered a gusting crosswind, and the pilot was unable to maintain directional control.
- Narrative describes 'airplane' (9 of 12 supporting reports).  `[report:SEA08CA112]`  
  > Although the flare and touchdown were uneventful, during the landing roll, the airplane encountered a gusting crosswind, and the pilot was unable to maintain directional control.

**Exclude when**
- Belongs to sibling D05 'Ground loop in a tailwheel airplane' when it matches that bucket better (2 report(s) assigned there).  `[report:CEN14CA157]`  
  > Probable cause: The pilot's failure to maintain directional control of the airplane during the landing roll which resulted in the airplane ground looping.
- Not 'Crosswind landing' — that definition is crosswalked to RE, not LOC-G.  `[definition:IND-20]`
- Not 'Anomaly: Ground Excursion – Runway' — that definition is crosswalked to RE, not LOC-G.  `[definition:IND-07]`
- Not 'Aircraft encountered windshear' — that definition is crosswalked to WSTRW, not LOC-G.  `[definition:ECC-2220200]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.50).  `[parent:RE]`

**Linked example reports**
- SEA08CA112: "Although the flare and touchdown were uneventful, during the landing roll, the airplane encountered a gusting crosswind, and the pilot was unable to maintain directional control."
- ERA14FA327: "The NTSB determined that the probable cause of the accident was the failure of the pilot to maintain directional control of the airplane, while landing."
- WPR12CA077: "During the landing roll, the variable wind changed to a crosswind from the right and the pilot did not adequately compensate for the change in the wind direction."
- WPR10CA290: "The landing was uneventful; however, during the landing roll, a gust of wind lifted the right wing and despite the pilot’s control inputs, the left wing scraped the ground as the airplane turned to the right."
- WPR25LA038: "Probable cause: A loss of directional control during the landing roll in gusting crosswind conditions."
- GAA17CA346: "The pilot lost directional control of the airplane and airplane faced southeast when another gust of wind lifted the left wing and the right wing struck the ground."
- ERA24LA100: "Probable cause: The failure of the pilot flying to maintain directional control after touchdown with wind gusts that exceeded the airplane’s crosswind limitation."
- CEN15CA188: "Probable cause: The pilot's failure to maintain directional control during a crosswind landing in gusting crosswind conditions."
- CEN12CA641: "The wind gust knocked the tail wheel out of its detent and the pilot was unable to maintain directional control of the airplane."
- WPR13CA172: "The airplane settled back onto the runway and the pilot noted that he was able to maintain directional control as the airplane slowed down; however, shortly after, the airplane suddenly veered sharply to the right."
- ANC25LA107: "Probable cause: The pilot’s failure to maintain directional control of the airplane during the landing roll, in gusting crosswind conditions."
- WPR11CA109: "Probable cause: The certified flight instructor's loss of airplane control during the landing roll in a gusting crosswind."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D05 · Ground loop in a tailwheel airplane

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent LOC-G Loss of Control – Ground*

**Definition.** A tailwheel (conventional gear) airplane swerves and ground loops during takeoff or landing because the pilot does not maintain directional control with rudder and brakes.

**Include when**
- The occurrence meets the CICTT LOC-G (Loss of Control – Ground) definition.  `[parent:LOC-G]`
- Core definition: A tailwheel (conventional gear) airplane swerves and ground loops during takeoff or landing because the pilot does not maintain directional control with rudder and brakes.  `[candidate:D05]`
- Matches 'Intentional ground loop/swerve' (ECCAIRS 1.3.0.12 · Events (390) · 2010501 · Aircraft operation general › Aircraft handling › Swerve-take-off/landing): An event involving an intentional ground loop or swerve of the aircraft on take-off or landing, e.g. to avoid obstacles in the runway overrun area.  `[definition:ECC-2010501]`
- Matches 'Ground loop/swerve on take-off or landing' (ECCAIRS 1.3.0.12 · Events (390) · 2010500 · Aircraft operation general › Aircraft handling): An event involving a ground loop/swerve of the aircraft on take-off or landing.  `[definition:ECC-2010500]`
- Narrative describes 'control' (10 of 12 supporting reports).  `[report:ERA22LA175]`  
  > Loss of directional control may lead to an aggravated, uncontrolled, tight turn on the ground, or a ground loop.
- Narrative describes 'directional' (10 of 12 supporting reports).  `[report:ERA22LA175]`  
  > Loss of directional control may lead to an aggravated, uncontrolled, tight turn on the ground, or a ground loop.
- Narrative describes 'ground' (9 of 12 supporting reports).  `[report:ERA22LA175]`  
  > Loss of directional control may lead to an aggravated, uncontrolled, tight turn on the ground, or a ground loop.

**Exclude when**
- Distinguish from sibling D04 'Loss of directional control in a crosswind on landing' under the same parent.  `[sibling:D04]`
- Not 'Auxiliary landing gear related event (ATA Code:3270)' — that definition is crosswalked to SCF-NP, not LOC-G.  `[definition:ECC-1327000]`
- Not 'Landing gear steering related event (ATA Code:3250)' — that definition is crosswalked to SCF-NP, not LOC-G.  `[definition:ECC-1325000]`
- Not 'Ground handling services' — that definition is crosswalked to RAMP, ADRM, not LOC-G.  `[definition:ECC-5050000]`
- Events better described by CICTT RE (Runway Excursion) (runner-up parent, margin 0.49).  `[parent:RE]`

**Linked example reports**
- ERA22LA175: "Loss of directional control may lead to an aggravated, uncontrolled, tight turn on the ground, or a ground loop."
- CEN14CA157: "The airplane then swerved to the left and the pilot was not able to regain directional control which resulted in a ground loop."
- ANC18LA030: "Ground Loop The Airplane Flying Handbook (FAA-H-8083-3B) discusses a ground loop with a tailwheel airplane and states in part: A ground loop is an uncontrolled turn during ground operations that may occur during taxi, takeoff, or during the after-landing roll."
- CEN20CA192: "The pilot attempted to maintain directional control by pulling full aft on the control stick and applying maximum braking; however, his excessive brake input while the airplane was in a level pitch attitude caused the airplane to pitch down and the propeller to impact the runway before the airplane pivoted back onto the tailwheel."
- CEN20CA103: "Probable cause: The pilot's failure to lock the tailwheel before landing, which resulted in his loss of directional control during the landing roll, a runway excursion onto soft ground, and a subsequent ground loop."
- ANC14CA053: "Probable cause: The pilot's failure to maintain directional control during landing and attempted go-around, resulting in contact with terrain and a ground loop."
- CEN12CA614: "Probable cause: The pilot's failure to maintain directional control during the landing roll, which resulted in a ground loop."
- ANC12CA039: "Probable cause: The pilot's failure to maintain directional control of the tailwheel-equipped airplane during landing, which resulted in a ground loop."
- WPR14CA200: "Probable cause: The pilot's failure to maintain directional control during landing which resulted in a ground-loop and nose over."
- WPR20CA142: "Probable cause: The front seat pilot's failure to maintain directional control during the landing roll, and the rear seat pilot's delayed remedial control inputs that subsequently resulted in a ground loop."
- ERA23LA318: "Probable cause: The pilot’s failure to maintain directional control of the tailwheel-equipped airplane, which resulted in a ground-loop."
- CEN09CA215: "During the ground loop the left main landing gear encountered soft terrain located off the right side of the runway and the left wing tip then impacted the ground."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D06 · Bounced landing and improper recovery

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent ARC Abnormal Runway Contact*

**Definition.** The airplane touches down hard or at the wrong pitch attitude, bounces, and the pilot's recovery from the bounce or improper flare leads to a hard landing, porpoising, or damage to the nose gear, firewall or propeller.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: The airplane touches down hard or at the wrong pitch attitude, bounces, and the pilot's recovery from the bounce or improper flare leads to a hard landing, porpoising, or damage to the nose gear, firewall or propeller.  `[candidate:D06]`
- Matches 'Hard landing, tail strike' (SKYbrary – Hard Landing and Tail Strike): A touchdown with a vertical load above limits, a bounced landing, or contact of the tail with the runway during takeoff rotation or landing flare.  `[definition:IND-18]`
- Matches 'Hard landing' (ECCAIRS 1.3.0.12 · Events (390) · 2010600 · Aircraft operation general › Aircraft handling): An event involving a hard landing. Hard landing: A landing in which the vertical deceleration encountered required a hard landing check.  `[definition:ECC-2010600]`
- Narrative describes 'landing' (10 of 12 supporting reports).  `[report:CEN20TA025]`  
  > Figure 1 – Airplane with nose gear strut through the fuselage and windscreen A postaccident examination of the damage to the nose landing gear revealed that the lower truss of the nose gear mounting structure was fractured.
- Narrative describes 'pilot' (9 of 12 supporting reports).  `[report:GAA15CA176]`  
  > A factor contributing to the accident was the pilot's improper recovery from a bounced landing.
- Narrative describes 'bounced' (8 of 12 supporting reports).  `[report:GAA15CA176]`  
  > A factor contributing to the accident was the pilot's improper recovery from a bounced landing.

**Exclude when**
- Belongs to sibling C9 'Hard landing or tail strike' when it matches that bucket better (1 report(s) assigned there).  `[report:WPR15CA093]`  
  > The pilot reported that he was on a straight-in approach for landing during touchdown; the airplane landed hard and bounced.
- Distinguish from sibling D07 'Gear-up landing with the landing gear not extended' under the same parent.  `[sibling:D07]`
- Distinguish from sibling D14 'Low rotor RPM in a helicopter' under the same parent.  `[sibling:D14]`
- Distinguish from sibling D15 'Balloon hard landing in high wind' under the same parent.  `[sibling:D15]`
- Not 'Auxiliary landing gear related event (ATA Code:3270)' — that definition is crosswalked to SCF-NP, not ARC.  `[definition:ECC-1327000]`
- Not 'Landing gear malfunction' — that definition is crosswalked to SCF-NP, not ARC.  `[definition:IND-25]`
- Not 'Nose gear collapsed/retracted' — that definition is crosswalked to SCF-NP, not ARC.  `[definition:ECC-1322001]`
- Events better described by CICTT LOC-G (Loss of Control – Ground) (runner-up parent, margin 0.63).  `[parent:LOC-G]`

**Linked example reports**
- CEN20TA025: "Figure 1 – Airplane with nose gear strut through the fuselage and windscreen A postaccident examination of the damage to the nose landing gear revealed that the lower truss of the nose gear mounting structure was fractured."
- GAA15CA176: "A factor contributing to the accident was the pilot's improper recovery from a bounced landing."
- WPR16FA157: "During landing attempts, the pilot would either touch the airplane down early and bounce the airplane or hold the airplane in a nose-high attitude to bleed off airspeed then let the nose drop aggressively."
- DEN08CA117: "Prior to the flare, "the nose wheel touched the runway and the airplane bounced." The pilot "held the yoke steady and the airplane settled" unto the runway a second time resulting in another "bounce" that was higher than the first."
- DFW08CA162: "After the third bounce the airplane landed nose gear first, the propeller struck the runway, and the nose gear collapsed."
- CEN26LA063: "Probable cause: The pilot’s improper pitch control that resulted in a hard landing, and his improper recovery from multiple bounced landings."
- GAA16CA379: "During a postaccident examination, the pilot reported that the nose landing gear "support bungee" had failed and the nose landing gear strut jammed upward during the hard landing."
- WPR09CA185: "Thereafter, the airplane impacted the runway in a nose low attitude and bounced."
- WPR11CA445: "The airplane bounced, and while airborne again, the pilot applied power to prevent a second hard landing, but the airplane began to weather vane to the left."
- CEN09CA048: "While performing a full-stop landing, the solo student pilot's improper flare resulted in a "bounced landing." During the recovery, the airplane began to porpoise."
- ERA09CA016: "Probable cause: The pilot's improper recovery from a bounced landing."
- CEN10CA289: "Probable cause: The pilot's improper landing flare and recovery from a bounced landing."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D07 · Gear-up landing with the landing gear not extended

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent ARC Abnormal Runway Contact*

**Definition.** The pilot lands a retractable-gear airplane with the landing gear retracted because gear extension was forgotten, the before-landing checklist was not completed, or the gear warning was missed.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: The pilot lands a retractable-gear airplane with the landing gear retracted because gear extension was forgotten, the before-landing checklist was not completed, or the gear warning was missed.  `[candidate:D07]`
- Matches 'Wheels-up landing - unintentional' (ECCAIRS 1.3.0.12 · Events (390) · 2011202 · Aircraft operation general › Aircraft handling › Wheels-up landings): An event involving an unintentional wheels-up landing, e.g. the crew forgot to lower the landing gear.  `[definition:ECC-2011202]`
- Matches 'Wheels-up landing,' (ECCAIRS 1.3.0.12 · Events (390) · 2011200 · Aircraft operation general › Aircraft handling): An event involving a wheels-up landing generally. Use this when the intent is not known. To be used when the gear is not lowered or locked before contact with the runway/ground during a landing.  `[definition:ECC-2011200]`
- Matches 'Hard landing' (ECCAIRS 1.3.0.12 · Events (390) · 2010600 · Aircraft operation general › Aircraft handling): An event involving a hard landing. Hard landing: A landing in which the vertical deceleration encountered required a hard landing check.  `[definition:ECC-2010600]`

**Exclude when**
- Distinguish from sibling C9 'Hard landing or tail strike' under the same parent.  `[sibling:C9]`
- Distinguish from sibling D06 'Bounced landing and improper recovery' under the same parent.  `[sibling:D06]`
- Distinguish from sibling D14 'Low rotor RPM in a helicopter' under the same parent.  `[sibling:D14]`
- Coded SCF-NP (System/Component Failure – Non-Powerplant) rather than ARC: similar wording, different occurrence category.  `[report:WPR12FA193]`  
  > In summary, if the pilot wants to retract the landing gear: with weight off of the left landing gear squat switch, the landing gear handle solenoid unlocks, and the pilot can move the handle to the up (retract) position.
- Not 'Landing gear malfunction' — that definition is crosswalked to SCF-NP, not ARC.  `[definition:IND-25]`
- Not 'Smoke - Landing gear' — that definition is crosswalked to F-NI, SCF-NP, not ARC.  `[definition:ECC-1990162]`
- Not 'Fire - Landing gear' — that definition is crosswalked to F-NI, SCF-NP, not ARC.  `[definition:ECC-1990161]`
- Events better described by CICTT SCF-NP (System/Component Failure – Non-Powerplant) (runner-up parent, margin 0.22).  `[parent:SCF-NP]`

**Linked example reports**
- CEN12LA387: "In addition to the four normal landing gear cycles, the landing gear extended from the fully retracted position into the down-and-locked position via the emergency landing gear extension system."
- WPR24LA086: "The landing gear switch was placed in the down position, and all three landing gear extended fully."
- GAA19CA398: "Probable cause: The pilot's failure to verify that the main landing gear were extended, which resulted in landing with partially extended landing gear."
- ERA16FA188: "Landing Gear System When retracted, the airplane's landing gear was fully enclosed by the landing gear doors."
- CEN14LA065: "Photos provided by the Federal Aviation Administration show the airplane on the runway with the left main landing gear extended and parallel to the vertical axis of the airplane, the right main landing gear extended and in the aft direction and parallel to the longitudinal axis of the airplane, and the nose landing gear retracted."
- ERA16LA092: "According to the Piper PA-30 Owners Handbook, before extending the landing gear for landing, both throttle controls should be retarded to check that the landing gear warning horn is operating, and it is especially important to check that the landing gear is down when there is any distraction in the landing situation."
- DCA13FA094: "The FO stated that, during the approach, the landing gear warning horn sounded when the airplane slowed below 130 kts, and the captain maintained a speed above 130 kts to prevent the horn from sounding until the airplane was "close to the runway." After the captain called for the flaps to be selected to 35, the landing gear warning horn continued to sound until after landing."
- WPR22LA180: "The circuit breaker was reset, and the landing gear was subsequently cycled multiple times, with the landing gear being raised and lowered using the airplane’s electrical power and the landing gear switch."
- CEN12CA036: "He further noted that he failed to recognize the lack of sound and feel of the landing gear extending, the lack of an illuminated green landing gear position light, and the lack of visual confirmation that the main landing gear had not extended."
- DCA12FA058: "Landing Gear Alternate Extension To isolate the normal landing gear selector valve during flight, a landing gear inhibit switch is installed in the flight compartment ceiling."
- ERA13CA028: "Both pilots reported that they did not hear the landing gear warning horn prior to landing without the landing gear extended."
- DCA10IA021: "Contributing to this incident was a circular reference in the company Flight Manual in which the Landing Gear Gravity Extension checklist referred back to the Landing Gear Unsafe Indication After Extension checklist rather than the Landing Gear - Partial Gear or Gear Up Landing checklist."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D08 · Aerodynamic stall in the traffic pattern or on approach

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent LOC-I Loss of Control – Inflight*

**Definition.** While maneuvering at low altitude in the traffic pattern, on the turn to final or on approach, the pilot lets the airspeed decay or the angle of attack exceed the critical value, and the airplane stalls and loses height before recovery is possible.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: While maneuvering at low altitude in the traffic pattern, on the turn to final or on approach, the pilot lets the airspeed decay or the angle of attack exceed the critical value, and the airplane stalls and loses height before recovery is possible.  `[candidate:D08]`
- Matches 'Stall prevention and recovery' (FAA Advisory Circular 120-109A – Stall Prevention and Recovery Training): Training to recognise and recover from approaches to stall and full stalls, including during go-arounds with high thrust and pitch.  `[definition:IND-21]`
- Matches 'Stall warning triggered' (ECCAIRS 1.3.0.12 · Events (390) · 2260500 · Aircraft operation general › Warning system triggered): Stall warning triggered  `[definition:ECC-2260500]`
- Narrative describes 'airplane' (8 of 12 supporting reports).  `[report:CEN13FA051]`  
  > Overshooting finals An excerpt from the FAA’s “Airplane Flying Handbook,” 2004 (FAA-H-8083-3A): Normally, it is recommended that the angle of bank not exceed a medium bank because the steeper the angle of bank, the higher the airspeed at which the airplane stalls.
- Narrative describes 'stalls' (8 of 12 supporting reports).  `[report:CEN13FA051]`  
  > Overshooting finals An excerpt from the FAA’s “Airplane Flying Handbook,” 2004 (FAA-H-8083-3A): Normally, it is recommended that the angle of bank not exceed a medium bank because the steeper the angle of bank, the higher the airspeed at which the airplane stalls.
- Narrative describes 'turn' (7 of 12 supporting reports).  `[report:ERA13FA227]`  
  > The first airplane landed uneventfully, but as the accident airplane approached the runway, it entered an aerodynamic stall during the turn from the base leg of the traffic pattern to the final leg of the traffic pattern.

**Exclude when**
- Belongs to sibling B05 'Stall warning or upset during a go-around' when it matches that bucket better (1 report(s) assigned there).  `[report:CEN14FA046]`  
  > Pilots must perform approaches to stalls in takeoff, clean, and landing configurations with at least one approach-to-stall maneuver flown while in a 15-30 degree bank turn.
- Distinguish from sibling B23 'Windshear on final approach' under the same parent.  `[sibling:B23]`
- Distinguish from sibling B24 'Landing short of the runway' under the same parent.  `[sibling:B24]`
- Distinguish from sibling B28 'Wrong route or waypoint loaded in the FMS' under the same parent.  `[sibling:B28]`
- Not 'Undershoot' — that definition is crosswalked to USOS, not LOC-I.  `[definition:IND-37]`
- Not 'Vehicle traffic violation' — that definition is crosswalked to ADRM, not LOC-I.  `[definition:ECC-99010049]`
- Not 'Provision of ANS traffic information' — that definition is crosswalked to ATM, not LOC-I.  `[definition:ECC-4010204]`
- Events better described by CICTT SEC (Security Related) (runner-up parent, margin 0.62).  `[parent:SEC]`

**Linked example reports**
- CEN13FA051: "Overshooting finals An excerpt from the FAA’s “Airplane Flying Handbook,” 2004 (FAA-H-8083-3A): Normally, it is recommended that the angle of bank not exceed a medium bank because the steeper the angle of bank, the higher the airspeed at which the airplane stalls."
- ERA13FA227: "The first airplane landed uneventfully, but as the accident airplane approached the runway, it entered an aerodynamic stall during the turn from the base leg of the traffic pattern to the final leg of the traffic pattern."
- WPR10LA297: "The witness stated that it appeared as if the airplane continued beyond the normal point for the turn to the final leg, and was north of the final approach for landing; the airplane was low."
- ERA15FA096: "According to a pilot of a low-wing airplane that was approaching the airport, about 3 to 4 miles on a straight-in approach to runway 9, with the helicopter number two to land."
- CEN15FA083: "Probable cause: The pilot’s failure to maintain adequate airspeed while maneuvering at an excessive bank angle at a low altitude, which resulted in an accelerated stall and spin with insufficient altitude for a recovery."
- CEN22FA211: "Stalls encountered any time the G-load exceeds +1G are called “accelerated maneuver stalls.” The accelerated stall would most frequently occur inadvertently during improperly executed turns, stall and spin recoveries, pullouts from steep dives, or when overshooting a base to final turn."
- CEN19FA323: "Probable cause: The pilot’s exceedance of the airplane’s critical angle of attack while maneuvering toward the final leg of the traffic pattern and facing the rising sun, which resulted in a subsequent aerodynamic stall at too low an altitude to recover."
- ERA20FA101: "Probable cause: The pilot’s exceedance of the airplane's critical angle of attack and subsequent aerodynamic stall and spin at low altitude due to a possible distraction in the cockpit for which the reason was undetermined."
- ANC18FA007: "We said during our discussion of turn performance that 60-75 KIAS [knots indicated airspeed] was the sweet spot for maneuvering the A5, and this holds true at low altitude as well."
- DFW08FA060: "Another witness was in his backyard when he heard the airplane's engine "wind up hard." He said, "I turned to look at the plane, and it looked like it fell to the ground in a 45 degree angle - The plane disappeared behind a row of trees - then I saw a ball of smoke - then I heard it hit the ground." The witness also stated that he heard an airplane making "circles" around the airport before the crash but he was not sure it was the accident airplane."
- WPR17LA195: "I judged we had enough distance ahead to climb over the ridge." Once he recognized that the airplane would not outclimb the terrain, the pilot executed a right turn to reverse course, but then stalled the airplane during that turn."
- WPR11FA316: "Probable cause: The pilot's decision to take off toward a nearby low cloud layer and the subsequent turn, stall, and spin during the pilot’s attempt to avoid the cloud layer."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D09 · Stall after takeoff at high density altitude

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent CTOL Collision with Obstacle(s) During Takeoff and Landing*

**Definition.** The airplane cannot climb as expected after takeoff because of high density altitude, heavy weight or a short or rising field, and the pilot pulls the nose up until the airplane stalls or settles into terrain.

**Include when**
- The occurrence meets the CICTT CTOL (Collision with Obstacle(s) During Takeoff and Landing) definition.  `[parent:CTOL]`
- Core definition: The airplane cannot climb as expected after takeoff because of high density altitude, heavy weight or a short or rising field, and the pilot pulls the nose up until the airplane stalls or settles into terrain.  `[candidate:D09]`
- Matches 'Near collision with terrain generally' (ECCAIRS 1.3.0.12 · Events (390) · 2180200 · Aircraft operation general › Aircraft - near collisions/loss of separation): An event involving a near collision by an aircraft with terrain.  `[definition:ECC-2180200]`
- Matches 'Aircraft collision with tree/tall vegetation' (ECCAIRS 1.3.0.12 · Events (390) · 2050414 · Aircraft operation general › Aircraft - collisions with obstacle/terrain/aircraft › Collision aircraft - object ground): (Collision aircraft-tree / tall vegetation) An event involving an aircraft collision with tree(s)/tall vegetation.  `[definition:ECC-2050414]`

**Exclude when**
- Coded LOC-I (Loss of Control – Inflight) rather than CTOL: similar wording, different occurrence category.  `[report:ERA15LA238]`  
  > Consequently, the airplane may not be able to clear obstructions, or may settle back on the runway…" Density Altitude FAA Pamphlet FAA-P-8740-2 "Density Altitude" defines density altitude as "pressure altitude corrected for non-standard temperature variations." Density altitude can affect aircraft performance.
- Coded LALT (Low Altitude Operations) rather than CTOL: similar wording, different occurrence category.  `[report:CEN14FA414]`  
  > Probable cause: The pilot’s inability to maintain a climb while attempting to cross over a mountain pass in high-density altitude conditions that degraded the airplane’s climb performance.
- Not 'Aircraft encountered vortex/wake turbulence' — that definition is crosswalked to TURB, not CTOL.  `[definition:ECC-2220400]`
- Not '3410 Flight Environment Data systems realeted event' — that definition is crosswalked to SCF-NP, not CTOL.  `[definition:ECC-99010018]`
- Not 'Stall prevention and recovery' — that definition is crosswalked to LOC-I, not CTOL.  `[definition:IND-21]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.01).  `[parent:LOC-I]`

**Linked example reports**
- CEN16LA228: "Contributing to the accident was the operation of the airplane above its maximum takeoff weight at a high density altitude at the time of the accident."
- GAA16CA390: "Under conditions of high-density altitude, high temperature, and/or maximum gross weight, the airplane may be able to become airborne at an insufficient airspeed, but unable to climb out of ground effect."
- WPR23LA329: "Utilizing the performance instructions noted within the airplane flight manual, the assumed altitude and density altitude conditions, and an airplane loaded at maximum gross weight, the calculated climb performance would have been about 380 fpm."
- ERA21LA313: "A decrease in air density means a high-density altitude; an increase in air density means a lower density altitude."
- CEN22LA412: "At the airplane’s maximum gross weight, 3,000 ft density altitude, and equipped with a 100-horsepower engine, the POH listed the takeoff roll from a turf runway as 552 ft and the distance to clear a 50 ft obstacle as 960 ft."
- CEN11CA608: "The pilot reported that he loaded the airplane for a fire suppression mission with 450 gallons of water and calculated that the airplane's takeoff weight was 435 pounds below the maximum takeoff gross weight of 11,500 pounds."
- ANC21LA056: "This document stated that “Density altitude is formally defined as ’pressure altitude corrected for nonstandard temperature variations’.” The document also stated in part the following: The formal definition of density altitude is certainly correct, but the important thing to understand is that density altitude is an indicator of aircraft performance."
- CEN12LA569: "The witness questioned the pilot prior to the accident takeoff whether he should attempt to depart from the airport given the density altitude, grass runway, and airplane weight."
- CEN20LA305: "ADDITIONAL INFORMATIONAirplane Owner’s Handbook Performance Charts Using the performance charts listed in the handbook for the airplane, at gross weight and a density altitude of 2,300 ft, the takeoff distance was about 1,125 ft, and the airplane was capable of a 550 ft per minute climb rate."
- GAA19CA387: "The manufacturer's Pilot Operating Handbook (POH) stated that, short field takeoff's that require obstacle clearance will, after breaking ground accelerate to best angle of climb speed, 95 MPH and climb past obstacles."
- WPR13FA244: "Probable cause: The pilot's inability to maintain a climb after departure in high-density altitude conditions, which resulted in a collision with trees and terrain."
- WPR09CA393: "The pilot reported that the airplane did not climb after takeoff and was very sluggish."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### D10 · Wire strike during low-altitude flight

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent LALT Low Altitude Operations*

**Definition.** During low-altitude flight, such as agricultural application, maneuvering or a low pass, the aircraft collides with power lines or other wires the pilot did not see or did not keep clear of.

**Include when**
- The occurrence meets the CICTT LALT (Low Altitude Operations) definition.  `[parent:LALT]`
- Core definition: During low-altitude flight, such as agricultural application, maneuvering or a low pass, the aircraft collides with power lines or other wires the pilot did not see or did not keep clear of.  `[candidate:D10]`
- Matches 'Aircraft collision with power line conductor, cable or wire' (ECCAIRS 1.3.0.12 · Events (390) · 2050411 · Aircraft operation general › Aircraft - collisions with obstacle/terrain/aircraft › Collision aircraft - object ground): An event involving an aircraft collision with power line conductor, cable or wire.  `[definition:ECC-2050411]`
- Narrative describes 'wire' (5 of 12 supporting reports).  `[report:ERA21LA269]`  
  > Because this environment has an inherent risk of wire strikes, flight crews must be properly trained to assess the environment and verify the presence of wires without relying solely on “see and avoid.” The FAA Safety Briefing article presented the following tips for wire hazard mitigation: o Avoid low-level flight whenever it is not essential to the operation.

**Exclude when**
- Coded LOC-I (Loss of Control – Inflight) rather than LALT: similar wording, different occurrence category.  `[report:ERA15FA352]`  
  > He also indicated that he knew that the pilot had a habit of "making low passes" and, being a former DPE, he had numerous talks with the pilot about the hazards of performing low passes.
- Not 'Aircraft encountered vortex/wake turbulence' — that definition is crosswalked to TURB, not LALT.  `[definition:ECC-2220400]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not LALT.  `[definition:ECC-2180101]`
- Not 'Collision of towed aircraft with object/obstacles' — that definition is crosswalked to RAMP, ADRM, not LALT.  `[definition:ECC-99010060]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.48).  `[parent:LOC-I]`

**Linked example reports**
- ERA21LA269: "Because this environment has an inherent risk of wire strikes, flight crews must be properly trained to assess the environment and verify the presence of wires without relying solely on “see and avoid.” The FAA Safety Briefing article presented the following tips for wire hazard mitigation: o Avoid low-level flight whenever it is not essential to the operation."
- CEN19FA003: "The pilot was focused on some electrical power lines while maneuvering at low altitude during an agricultural application flight."
- CEN14LA211: "The operator said there was a stand of trees on the opposite side of the street where the power lines were located and it was really difficult to see the top ground wires as you approached the field because "they would get lost in the trees." The operator also thought that the pilot was most likely setting up his "A and B" lines along the haystack via the onboard GPS when he struck the power lines."
- ERA16FA182: "After this crossing maneuver, the MX2 pilot called out "ready-pull-now," and both pilots initiated a half Cuban-8, with the intention of simultaneously positioning the airplanes on 45º down angles toward show center, which was to be followed by another low altitude pass."
- WPR13GA128: "Probable cause: The pilot’s failure to maintain clearance from a wire while maneuvering during low-altitude operations."
- CHI08CA252: "Factors associated with the accident were the low altitude operations being conducted and the power lines."
- CEN15CA095: "Probable cause: The pilot's decision to maneuver the airplane at low altitude resulting in the airplane impacting power lines."
- NYC08CA279: "After flying along the power lines, he determined that he had enough clearance to "fit under the wire." He thought that it looked "good," and began his spray run on the east side of a field passing under the power lines without incident."
- CEN18FA011: "Probable cause: The pilot's decision to fly along the river at a low altitude contrary to applicable regulations and safety of flight considerations which resulted in the impact with the power lines."
- WPR09CA220: "In anticipation of a second wire strike, he closed the throttle and began an autorotation prior to the helicopter striking the east-west power lines."
- CEN19FA117: "Probable cause: The pilot’s failure to maintain clearance from power transmission lines during low altitude flight operations."
- WPR15FA161: "Probable cause: The pilot's failure to see and avoid power lines while intentionally maneuvering at low altitude for the aerial observation flight."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D11 · Spatial disorientation after VFR flight into instrument conditions

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent UIMC Unintended Flight in IMC*

**Definition.** A pilot flying under visual flight rules continues into clouds, darkness or low visibility, becomes spatially disoriented, and loses control of the aircraft or flies into terrain.

**Include when**
- The occurrence meets the CICTT UIMC (Unintended Flight in IMC) definition.  `[parent:UIMC]`
- Core definition: A pilot flying under visual flight rules continues into clouds, darkness or low visibility, becomes spatially disoriented, and loses control of the aircraft or flies into terrain.  `[candidate:D11]`
- Matches 'Aircraft encounter with instrument meteorological conditions' (ECCAIRS 1.3.0.12 · Events (390) · 2220500 · Aircraft operation general › Weather encounters): An event involving an aircraft encounter with instrument meteorological conditions. IMC is visibility, distance from clouds, and ceiling less than the minima specified for visual meteorological conditions.  `[definition:ECC-2220500]`
- Matches 'Loss of visual reference' (ECCAIRS 1.3.0.12 · Events (390) · 2221000 · Aircraft operation general › Weather encounters): Loss of visual reference  `[definition:ECC-2221000]`

**Exclude when**
- Coded LOC-I (Loss of Control – Inflight) rather than UIMC: similar wording, different occurrence category.  `[report:WPR22FA026]`  
  > If a pilot does not reference the aircraft flight instruments and there are no outside visual references, the pilot might experience spatial disorientation.
- Not 'Aircraft encounter with turbulence' — that definition is crosswalked to TURB, not UIMC.  `[definition:ECC-2220600]`
- Not 'Aircraft encountered icing conditions' — that definition is crosswalked to ICE, not UIMC.  `[definition:ECC-2220100]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not UIMC.  `[definition:ECC-2180101]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.15).  `[parent:LOC-I]`

**Linked example reports**
- ERA10FA091: "Probable cause: The pilot's decision to depart under special VFR flight at night when instrument meteorological conditions prevailed at the departure airport and along the route of flight and his continued VFR flight into instrument meteorological conditions, which resulted in his spatial disorientation and subsequent loss of aircraft control."
- CEN19FA140: "Probable cause: The non-instrument-rated pilot's decision to fly into instrument meteorological conditions, which resulted in spatial disorientation, a loss of control, and a subsequent impact with terrain."
- CEN14LA376: "Other weather observations in the area indicated that there were instrument flight rules (IFR) ceilings at the time of the accident from central Kansas westward, with visual flight rules (VFR) ceilings from central Kansas eastward into Missouri."
- CEN19FA078: "Scud running, or continued VFR flight into instrument flight rules (IFR) conditions, pushes the pilot and aircraft capabilities to the limit when the pilot tries to make visual contact with the terrain."
- ERA12FA012: "Probable cause: The non-instrument rated pilot's improper decision to continue visual flight into instrument meteorological conditions, which resulted in spatial disorientation and subsequent in-flight collision with mountainous terrain."
- CEN23FA125: "The FAA Helicopter Flying Handbook FAA-H-8083-21B discusses visual flight rules flight into IMC and states in part: Helicopter pilots that encounter inadvertent flight into instrument meteorological conditions (IIMC) may experience physiological illusions which can lead to spatial disorientation and loss of aircraft control."
- ERA15FA066: "Probable cause: The noninstrument-rated pilot's improper decision to attempt visual flight in instrument meteorological conditions, which resulted in an in-flight loss of airplane control due to spatial disorientation."
- ERA15FA299: "Without visual references outside the airplane, there are many situations where combinations of normal motions and forces can create convincing illusions that are difficult to overcome." The Handbook also advised, "unless a pilot has many hours of training in instrument flight, flight in reduced visibility or at night when the horizon is not visible should be avoided." The FAA Airplane Flying Handbook (FAA-H-8083-3) described some hazards associated with flying when visual references, such as the ground or horizon, are obscured."
- ANC20LA004: "The Federal Aviation Administration Civil Aerospace Medical Institute's publication, "Introduction to Aviation Physiology," defines spatial disorientation as a "loss of proper bearings; state of mental confusion as to position, location, or movement relative to the position of the earth." This document lists factors contributing to spatial disorientation, including changes in angular acceleration, flight in instrument flight rules conditions, frequent transfer from visual flight rules to instrument flight rules conditions, and unperceived changes in aircraft attitude."
- CEN23FA239: "The Graphical Forecasts for Aviation (GFA) applicable to the accident site and that were valid when the flight departed indicated low instrument flight rules (LIFR) to IFR conditions and a north wind of 5 knots."
- ERA16FA031: "Without visual references outside the airplane, there are many situations where combinations of normal motions and forces can create convincing illusions that are difficult to overcome." The Handbook also advised, "unless a pilot has many hours of training in instrument flight, flight in reduced visibility or at night when the horizon is not visible should be avoided." FAA Publication "Spatial Disorientation Visual Illusions" (OK-11-1550) , stated, in part, that "false visual reference illusions may cause you to orient your aircraft in relation to a false horizon; these illusions are caused by flying over a banked cloud, night flying over featureless terrain with ground lights that are indistinguishable from a dark sky with stars, or night flying over a featureless terrain with a clearly defined pattern of ground lights and a dark starless sky." The publication provided guidance on the prevention of spatial disorientation."
- NYC08FA231: "Probable cause: The pilot's intentional visual flight into known instrument meteorological conditions, resulting in spatial disorientation and a subsequent loss of control in flight."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D12 · Reciprocating engine failure from a connecting rod or crankshaft fracture

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent SCF-PP System/Component Failure – Powerplant*

**Definition.** A piston engine fails in flight because a connecting rod, rod bearing, crankshaft or cylinder fractures, often after oil starvation or a maintenance error, and the engine loses all power.

**Include when**
- The occurrence meets the CICTT SCF-PP (System/Component Failure – Powerplant) definition.  `[parent:SCF-PP]`
- Core definition: A piston engine fails in flight because a connecting rod, rod bearing, crankshaft or cylinder fractures, often after oil starvation or a maintenance error, and the engine loses all power.  `[candidate:D12]`
- Matches 'In-flight engine shutdown (IFSD)' (SKYbrary – In-Flight Shutdown): An engine is shut down in flight because of a failure or a precautionary indication such as low oil pressure, high vibration or fire.  `[definition:IND-28]`
- Matches 'Turbine engine - non mechanical failure' (ECCAIRS 1.3.0.12 · Events (390) · 1720104 · Aircraft/system/component › 7200 Turbine engine › 7201 Turbine engine - generally): An event involving a non-mechanical failure of a turbine engine, the engine failed even though the mechanics of the engine were intact.  `[definition:ECC-1720104]`
- Matches 'Turbine engine - uncontained failure' (ECCAIRS 1.3.0.12 · Events (390) · 1720102 · Aircraft/system/component › 7200 Turbine engine › 7201 Turbine engine - generally): An event involving the failure of a turbine engine's containment system, an engine failure in which parts of the engine exited the nacelle.  `[definition:ECC-1720102]`
- Narrative describes 'rod' (10 of 12 supporting reports).  `[report:CEN22LA117]`  
  > 5 piston connecting rod was not connected to its crankpin, and the connecting rod end was hammered into a rounded shape.
- Narrative describes 'connecting' (9 of 12 supporting reports).  `[report:CEN22LA117]`  
  > 5 piston connecting rod was not connected to its crankpin, and the connecting rod end was hammered into a rounded shape.
- Narrative describes 'oil' (6 of 12 supporting reports).  `[report:CEN17LA110]`  
  > The portions of rod bearing material found within the oil pan were consistent with bearing failure and extrusion.

**Exclude when**
- Distinguish from sibling B13 'Engine shutdown after loss of oil pressure' under the same parent.  `[sibling:B13]`
- Distinguish from sibling B17 'Lithium battery fire from a passenger device' under the same parent.  `[sibling:B17]`
- Distinguish from sibling D01 'Carburetor icing leading to loss of engine power' under the same parent.  `[sibling:D01]`
- Not 'Turbine Engine fuel starvation' — that definition is crosswalked to FUEL, not SCF-PP.  `[definition:ECC-1720106]`
- Not 'Data recording related event (ATA Code:3130)' — that definition is crosswalked to SCF-NP, not SCF-PP.  `[definition:ECC-1313000]`
- Not 'Reciprocating engine - fuel starvation' — that definition is crosswalked to FUEL, not SCF-PP.  `[definition:ECC-1850106]`
- Events better described by CICTT LOC-G (Loss of Control – Ground) (runner-up parent, margin 0.63).  `[parent:LOC-G]`

**Linked example reports**
- CEN22LA117: "5 piston connecting rod was not connected to its crankpin, and the connecting rod end was hammered into a rounded shape."
- CEN17LA110: "The portions of rod bearing material found within the oil pan were consistent with bearing failure and extrusion."
- CEN10LA037: "The connecting rod bolts for the #3 connecting rod and rod cap were found sheared in half, but the nuts were still attached to the connecting rod bolts."
- ERA24LA095: "The connecting rod remained installed to the piston pin and crankshaft in cylinder No."
- ERA23LA086: "There was no maintenance entry made in the engine logbook for the oil and oil filter change after the diminished oil pressure."
- WPR15LA032: "The number 5 connecting rod bearing was liberated along with the fractured connecting rod; however, the two bearing halves were located (one in the sump and one found outside the engine)."
- CEN12LA326: "Examination of the engine after the accident revealed that no oil was present in the engine and the aft connecting rod was protruding from a hole in the top of the engine crankcase."
- ERA13LA382: "6 cylinder connecting rod remained connected to the piston via the piston pin; however, the connecting rod was separated from the crankpin journal."
- WPR13FA169: "Probable cause: The manufacture and installation of a nonstandard part by unknown maintenance personnel to compensate for a bent, misaligned crankshaft propeller flange, which resulted in the improper clearance of the bearings on the crankshaft journal, a loss of oil pressure, overheating of the bearings, and the failure of a connecting rod during cruise flight."
- ERA15LA014: "1 and 2 main bearings, loss of lubrication, failure of the crankshaft, and a subsequent total loss of engine power."
- ERA14LA076: "A significant quantity of metallic debris, consistent with connecting rod, connecting rod bearing, piston, and piston ring material, was observed within the oil sump."
- CEN15FA424: "6 connecting rod due to oil starvation from the shifting of the crankshaft's No."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D13 · Loss of tail rotor effectiveness in a helicopter

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent LOC-I Loss of Control – Inflight*

**Definition.** A helicopter experiences an uncommanded yaw, such as loss of tail rotor effectiveness in a crosswind or tailwind at low airspeed, or a tail rotor drive failure, and the pilot cannot regain yaw control.

**Include when**
- The occurrence meets the CICTT LOC-I (Loss of Control – Inflight) definition.  `[parent:LOC-I]`
- Core definition: A helicopter experiences an uncommanded yaw, such as loss of tail rotor effectiveness in a crosswind or tailwind at low airspeed, or a tail rotor drive failure, and the pilot cannot regain yaw control.  `[candidate:D13]`
- Matches 'Loss of control in-flight' (IATA – Loss of Control In-flight (LOC-I)): A significant, unintended departure of the aircraft from controlled flight, such as a stall, spin or upset, often following a system malfunction or crew response to erroneous indications.  `[definition:IND-08]`
- Matches 'Unreliable airspeed' (SKYbrary – Unreliable Airspeed): Erroneous or disagreeing airspeed indications, for example from pitot icing, ice crystals or a blocked pitot tube, which can lead to an upset if the crew follows the wrong indication.  `[definition:IND-09]`
- Narrative describes 'rotor' (12 of 12 supporting reports).  `[report:WPR13FA343]`  
  > Probable cause: The pilot's failure to maintain helicopter control while operating in conditions conducive to a loss of tail rotor effectiveness.
- Narrative describes 'tail' (12 of 12 supporting reports).  `[report:WPR13FA343]`  
  > Probable cause: The pilot's failure to maintain helicopter control while operating in conditions conducive to a loss of tail rotor effectiveness.
- Narrative describes 'loss' (9 of 12 supporting reports).  `[report:WPR13FA343]`  
  > Probable cause: The pilot's failure to maintain helicopter control while operating in conditions conducive to a loss of tail rotor effectiveness.

**Exclude when**
- Distinguish from sibling B05 'Stall warning or upset during a go-around' under the same parent.  `[sibling:B05]`
- Distinguish from sibling B23 'Windshear on final approach' under the same parent.  `[sibling:B23]`
- Distinguish from sibling B24 'Landing short of the runway' under the same parent.  `[sibling:B24]`
- Not 'Tail rotor gearbox (90 deg) related event (ATA Code:6520) (6520 Tail rotor gearbox (90 deg))' — that definition is crosswalked to SCF-NP, not LOC-I.  `[definition:ECC-1652000]`
- Not 'Tail rotor gearbox (45 deg) related event (ATA Code:6530) (6530 Tail rotor gearbox (45 deg))' — that definition is crosswalked to SCF-NP, not LOC-I.  `[definition:ECC-1653000]`
- Not 'Tail rotor drive shaft related event (ATA Code:6510)' — that definition is crosswalked to SCF-NP, not LOC-I.  `[definition:ECC-1651000]`
- Events better described by CICTT SCF-NP (System/Component Failure – Non-Powerplant) (runner-up parent, margin 0.60).  `[parent:SCF-NP]`

**Linked example reports**
- WPR13FA343: "Probable cause: The pilot's failure to maintain helicopter control while operating in conditions conducive to a loss of tail rotor effectiveness."
- GAA16LA117: "Loss of Tail Rotor Effectiveness The Federal Aviation Administration has published the Helicopter Flying Handbook FAA-H-8083-21A (2012).This handbook discusses loss of tail rotor effectiveness and states in part: Loss of tail rotor effectiveness (LTE) or an unanticipated yaw is defined as an uncommanded, rapid yaw towards the advancing blade which does not subside of its own accord."
- WPR10FA440: "Specific configuration details included: - A metal "seat deck"' which was the primary structural element of the cabin - Metal-framed left and right side cabin doors - A vertical firewall that also served as the aft cabin wall - A central pilot's seat with an instrument/control pedestal, and flight controls - Left and right external racks (approximately 6 feet long, 2 feet wide, and 4 inches deep, with metal mesh bottoms) - Main rotor rotation counter-clockwise when viewed from above - A metal, semi-monocoque tail boom - Multi-segment tail rotor drive system mounted atop the tail boom - Tail rotor gearbox at the aft end of the tail boom - Tail rotor rotation counter-clockwise when viewed from helicopter left side - Single metal horizontal stabilizer on the right-side end of the tail boom METEOROLOGICAL INFORMATION The 1030 automated weather observation at Kamiah Municipal Airport (S73), Kamiah, included calm winds; clear skies; temperature 16 degrees C; dew point 10 degrees C; and a barometric pressure of 29.99 inches of mercury."
- GAA17CA495: "Federal Aviation Administration's Helicopter Flying Handbook, FAA-H-8083-21A, contains a section titled "Loss of Tail Rotor Effectiveness (LTE)" which states: Loss of tail rotor effectiveness (LTE) or an unanticipated yaw is defined as an uncommanded, rapid yaw towards the advancing blade which does not subside of its own accord."
- CEN15FA003: "Probable cause: The pilot’s failure to maintain yaw control when he applied power to execute a go-around at a low airspeed in dark, night conditions, which resulted in a rapid, uncommanded right yaw due to a loss of tail rotor effectiveness."
- SEA08LA213: "Be aware that if a considerable amount of left pedal is being maintained, that a sufficient amount of left pedal may not be available to counteract an unanticipated right yaw." According to FAA Advisory Circular (AC) 90-95, "Any maneuver which requires the pilot to operate in a high power, low airspeed environment with a left crosswind or tailwind creates an environment where unanticipated right yaw may occur." The AC also advised of greater susceptibility for loss of tail rotor effectiveness (LTE) in right turns and the phenomena may occur in varying degrees in all single main rotor helicopters at airspeeds less than 30 knots."
- ERA22FA207: "The tail rotor was manually rotated through several 360° rotation of the tail rotor gearbox input flange and resulted in a corresponding rotation of the tail rotor."
- ERA11LA409: "The AC stated that the loss of tail rotor effectiveness (LTE) was a critical, low-speed aerodynamic flight characteristic which could result in an uncommanded rapid yaw rate which does not subside of its own accord and, if not corrected, could result in the loss of aircraft control."
- CEN20LA167: "According to the pilot, the helicopter was “spinning like [the] tail was not functioning,” and he responded by performing the emergency procedure for “loss of tail rotor.” He lowered the collective and pushed the cyclic forward “to gain forward airspeed and airflow over the vertical stabilizer.” The helicopter continued to spin “very violently” so he also reduced power."
- WPR16LA056: "Probable cause: The loss of helicopter control as a result of the loss of tail rotor effectiveness."
- ERA12LA282: "The AC stated that the loss of tail rotor effectiveness (LTE) was a critical, low-speed aerodynamic flight characteristic which could result in an uncommanded rapid yaw rate which does not subside of its own accord and, if not corrected, could result in the loss of aircraft control."
- CEN17LA375: "Probable cause: The loss of tail rotor thrust due to a failed tail rotor driveshaft, which resulted in a loss of tail rotor control and a hard landing."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D14 · Low rotor RPM in a helicopter

*Taxonomy version ntsb-draft-45231e0fc8 · status needs review · parent ARC Abnormal Runway Contact*

**Definition.** The helicopter's main rotor speed decays below the normal range because of high power demand, a mishandled throttle or collective, or a late autorotation entry, and the helicopter descends uncontrollably.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: The helicopter's main rotor speed decays below the normal range because of high power demand, a mishandled throttle or collective, or a late autorotation entry, and the helicopter descends uncontrollably.  `[candidate:D14]`
- Matches 'Tail strike' (SKYbrary – Tailstrike): The aft fuselage contacts the runway during takeoff rotation or landing, often after early rotation, wrong takeoff speeds or excessive pitch.  `[definition:IND-35]`

**Exclude when**
- Distinguish from sibling C9 'Hard landing or tail strike' under the same parent.  `[sibling:C9]`
- Distinguish from sibling D06 'Bounced landing and improper recovery' under the same parent.  `[sibling:D06]`
- Distinguish from sibling D07 'Gear-up landing with the landing gear not extended' under the same parent.  `[sibling:D07]`
- Coded LOC-I (Loss of Control – Inflight) rather than ARC: similar wording, different occurrence category.  `[report:ERA13LA242]`  
  > The amount the collective can be lowered depends on altitude…since the tail rotor is geared to the main rotor, low main rotor rpm may prevent the tail rotor from producing enough thrust to maintain direction control…" The recorded wind at an airport located about 25 miles east, at 0853, was from 290 degrees at 3 knots.
- Coded UNK (Unknown or Undetermined) rather than ARC: similar wording, different occurrence category.  `[report:CEN19LA269]`  
  > The PIC initiated a simulated governor failure by rolling the throttle down just enough to take the governor offline, but still maintaining the main rotor rpm in the green (normal) range.
- Not 'Main rotor blade flapping' — that definition is crosswalked to SCF-NP, not ARC.  `[definition:ECC-1620101]`
- Not 'Helicopter's main rotor in general related event (ATA Code:6201)' — that definition is crosswalked to SCF-NP, not ARC.  `[definition:ECC-1620100]`
- Not 'Rotorcraft main rotor systems related event (ATA Code:6200)' — that definition is crosswalked to SCF-NP, not ARC.  `[definition:ECC-1620000]`
- Events better described by CICTT LOC-I (Loss of Control – Inflight) (runner-up parent, margin 0.02).  `[parent:LOC-I]`

**Linked example reports**
- ANC23LA024: "If the helicopter is close to the ground, lowering the collective may be the last thing on a pilot's mind, but simultaneously lowering the collective and applying full throttle is the only sure way to recover the lost rotor rpm."
- CEN21LA187: "The pilot stated that the engine’s free turbine speed and the main rotor speed were “drooped”, and he reduced collective and moved the cyclic control aft to stabilize the main rotor speed."
- WPR17LA143: "If collective pitch is increased excessively, the power required by the main rotor exceeds the full-throttle power available, causing rotor rpm to decrease."
- ERA14TA113: "Power from the turboshaft engine was transmitted through the main drive shaft to the main rotor transmission and from the main transmission through a drive shaft to the tail rotor."
- GAA15CA181: "The above factors should be taken into consideration during the ground run-out phase following an autorotation or while performing certain types of anti-torque failure procedures where rotor speed decay occurs faster than forward speed decay."
- ERA21LA335: "According to the pilot, the helicopter was operating in the shaded area of the helicopter’s height/velocity diagram, and although he rapidly lowered the collective to gain energy in the main rotor blades, there was not enough inertia in them for a normal autorotative landing."
- WPR11CA101: "He rolled the throttle to flight idle, and lowered the collective while gently flaring the nose of the helicopter to set up the appropriate main rotor revolutions per minute (rpm) and airspeed."
- CEN13LA099: "At 3 feet I leveled the helicopter and applied collective to cushion the landing but I had only about 1/3rd of the rotor RPM normally available."
- ERA10LA362: "The collective was lowered to restore rotor rpm, but engine and rotor speed accelerated through the upper limits."
- ERA10LA023: "He then reduced throttle which caused the rotor rpm to deteriorate further resulting in the helicopter descending."
- ERA14LA311: "He lowered the collective, the low rotor rpm horn activated, and the low rotor rpm light illuminated."
- WPR18LA133: "The main rotor blades were in the wreckage debris adjacent to the main rotor mast, which was in its normal position."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 FAIL · G7 FAIL · G8 FAIL · G9 pass

### D15 · Balloon hard landing in high wind

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent ARC Abnormal Runway Contact*

**Definition.** A hot-air balloon lands in strong or gusty surface wind, the basket strikes the ground hard, tips or is dragged, and occupants are injured.

**Include when**
- The occurrence meets the CICTT ARC (Abnormal Runway Contact) definition.  `[parent:ARC]`
- Core definition: A hot-air balloon lands in strong or gusty surface wind, the basket strikes the ground hard, tips or is dragged, and occupants are injured.  `[candidate:D15]`
- Matches 'Hard landing' (ECCAIRS 1.3.0.12 · Events (390) · 2010600 · Aircraft operation general › Aircraft handling): An event involving a hard landing. Hard landing: A landing in which the vertical deceleration encountered required a hard landing check.  `[definition:ECC-2010600]`
- Matches 'Hard landing, tail strike' (SKYbrary – Hard Landing and Tail Strike): A touchdown with a vertical load above limits, a bounced landing, or contact of the tail with the runway during takeoff rotation or landing flare.  `[definition:IND-18]`
- Narrative describes 'hard' (7 of 12 supporting reports).  `[report:CEN18LA006]`  
  > Probable cause: The steep approach and hard landing after the balloon encountered unexpected high wind conditions, which resulted in a serious injury to a passenger.

**Exclude when**
- Distinguish from sibling C9 'Hard landing or tail strike' under the same parent.  `[sibling:C9]`
- Distinguish from sibling D06 'Bounced landing and improper recovery' under the same parent.  `[sibling:D06]`
- Distinguish from sibling D07 'Gear-up landing with the landing gear not extended' under the same parent.  `[sibling:D07]`
- Coded LOC-G (Loss of Control – Ground) rather than ARC: similar wording, different occurrence category.  `[report:CEN17LA223]`  
  > On June 8, 2017, about 1630 central daylight time, a Head Balloons AX 77B balloon, N30721, encountered a wind gust while preparing for takeoff that threw the balloon occupants to the floor of the basket.
- Coded CTOL (Collision with Obstacle(s) During Takeoff and Landing) rather than ARC: similar wording, different occurrence category.  `[report:GAA18CA016/2]`  
  > The Ultramagic balloon pilot reported that, during a balloon festival, after a local sightseeing flight, he landed the balloon and decided to wait for the ground crew to locate the balloon before deflating.
- Not 'Aircraft encounter with turbulence' — that definition is crosswalked to TURB, not ARC.  `[definition:ECC-2220600]`
- Not 'Crosswind landing' — that definition is crosswalked to RE, not ARC.  `[definition:IND-20]`
- Not 'Aircraft encountered vortex/wake turbulence' — that definition is crosswalked to TURB, not ARC.  `[definition:ECC-2220400]`
- Events better described by CICTT LOC-G (Loss of Control – Ground) (runner-up parent, margin 0.34).  `[parent:LOC-G]`

**Linked example reports**
- MIA08CA193: "As he approached the landing site, he allowed the balloon basket to drag through the top of trees in an effort to reduce speed."
- CEN18LA006: "Probable cause: The steep approach and hard landing after the balloon encountered unexpected high wind conditions, which resulted in a serious injury to a passenger."
- CEN09CA358: "The winds on the ground suddenly increased to about 25 mph, and the balloon experienced strong wind gusts."
- CEN09CA018: "The pilot reported that at the time they landed the winds were "gusty" on the surface and the balloon was moving approximately two miles per hour when the basket touched down on the ground."
- CEN19CA128: "Probable cause: The pilot's improper decision to launch the balloon in known high wind conditions, and his failure to fully vent the balloon upon landing, which resulted in the balloon landing hard several times, tipping over, being pushed along uneven ground, and a serious passenger injury."
- CEN15LA300: "Probable cause: The pilot’s improper burner control, which allowed the balloon’s envelope to cool, and the balloon’s subsequent encounter with a drop in wind velocity during a high wind landing approach, both of which resulted in the balloon’s descent rate increasing too rapidly for the pilot to arrest it and led to a hard landing."
- CEN13IA349: "The TAF for Denver International Airport during the period in which the accident took place were as follows: Denver Terminal Area Forecast, July 8, 2013 at 1139 UTC (0539 MDT,) wind 210 degrees at 13 knots, visibility more than 6 statute miles, few clouds at 8,000 feet mean sea level (MSL), scattered clouds at 12,000 feet MSL From 0800, wind 310 degrees at 11 knots, visibility more than 6 statute miles, few clouds at 8,000 feet MSL From 1000, wind 020 degrees at 13 knots, gusts to 23 knots, visibility more than 6 statute miles, few clouds at 8,000 feet MSL From 1700, wind 060 degrees at 13 knots, visibility more than 6 statute miles, few clouds at 8,000 feet MSL, broken ceiling at 15,000 feet MSL From 2000, wind 140 degrees at 5 knots, visibility more than 6 statute miles, few clouds at 8,000 feet MSL From 0000 on June 9, 2013, wind 200 degrees at 7 knots, visibility more than 6 statute miles, few clouds at 10,000 feet MSL From 0700 on June 9, 2013, wind 270 degrees at 5 knots, visibility more than 6 statute miles, few clouds at 10,000 feet MSL An amended TAF was issued for KDEN at 0652, with forecast wind 210 degrees at 13 knots, visibility more than 6 statute miles, few clouds at 8,000 feet MSL, scattered clouds at 12,000 feet MSL, and scattered clouds at 22,000 feet MSL From 0830, wind 010 degrees at 18 knots, gusts to 30 knots, visibility more than 6 statute miles, scattered clouds at 8,000 feet MSL, scattered clouds at 12,000 feet MSL From 1300, wind 020 degrees at 15 knots, gusts to 25 knots, visibility more than 6 statute miles, scattered clouds at 8,000 feet MSL, scattered clouds at 12,000 feet MSL From 1600, wind 060 degrees at 13 knots, visibility more than 6 statute miles, scattered clouds at 8,000 feet MSL, and broken ceiling at 15,000 feet MSL From 2000, wind 140 at 5 knots, visibility more than 6 statute miles, scattered clouds at 8,000 feet MSL From 0000 on June 9, 2013, wind 200 degrees at 7 knots, visibility more than 6 statute miles, few clouds at 10,000 feet MSL From 0700 on June 9, 2013, wind 270 degrees at 5 knots, visibility more than 6 statute miles, few clouds at 10,000 feet MSL The TAF issued at 0539 expected VMC conditions to prevail with a wind from the southwest or 210 degrees at 13 knots shifting northwest or 310 degrees at 11 knots at 0800."
- GAA20CA012: "She had a gradual descent to land, but as the balloon neared the surface, the winds were "in the 20+ mile per hour range." The balloon landed hard and bounced."
- CEN12CA393: "Probable cause: The balloon pilot’s encounter with increased wind during landing, which resulted in a hard landing and a passenger’s injury."
- CEN13CA372: "The passengers advised that the balloon basket hit the ground “very hard” and bounced several times before hitting the slope side of a dirt hill where the basket flipped onto its side and was dragged in the dirt in that tipped-over position."
- CEN14CA215: "The pilot briefed the passenger, who was very familiar with balloon operations, that they were going to make a high wind landing."
- CEN11CA654: "Probable cause: The pilot’s failure to maintain control of the balloon’s descent during the landing, which resulted in the balloon having a hard landing in a ditch and causing a passenger to be seriously injured."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass

### D16 · Taxi collision from inadequate visual lookout

*Taxonomy version ntsb-draft-45231e0fc8 · status grounded · parent GCOL Ground Collision*

**Definition.** While taxiing, the pilot does not maintain an adequate visual lookout and the aircraft strikes another aircraft, a vehicle, a hangar or another object on the ramp or taxiway.

**Include when**
- The occurrence meets the CICTT GCOL (Ground Collision) definition.  `[parent:GCOL]`
- Core definition: While taxiing, the pilot does not maintain an adequate visual lookout and the aircraft strikes another aircraft, a vehicle, a hangar or another object on the ramp or taxiway.  `[candidate:D16]`
- Matches 'Collision of a vehicle with an another vehicle or moveable equipment' (ECCAIRS 1.3.0.12 · Events (390) · 5030701 · Aerodrome & ground aids › Aerodrome services / operations › Vehicle/equipment operations): Collision of a vehicle with an another vehicle or moveable equipment  `[definition:ECC-5030701]`
- Matches 'Collision of a vehicle or moveable equipment with another object / obstacle' (ECCAIRS 1.3.0.12 · Events (390) · 5030703 · Aerodrome & ground aids › Aerodrome services / operations › Vehicle/equipment operations): Collision of a vehicle or moveable equipment with another object / obstacle  `[definition:ECC-5030703]`
- Matches 'Aircraft collision with approach/runway/taxiway lights' (ECCAIRS 1.3.0.12 · Events (390) · 2050403 · Aircraft operation general › Aircraft - collisions with obstacle/terrain/aircraft › Collision aircraft - object ground): An event involving an aircraft collision with approach, runway or taxiway lights.  `[definition:ECC-2050403]`
- Narrative describes 'taxi' (9 of 12 supporting reports).  `[report:WPR15LA154]`  
  > The pilot of the Cessna was cleared by ground control to taxi to runway 16 via taxiways A and C, and communication was maintained with the ground controller during the taxi.
- Narrative describes 'taxiways' (7 of 12 supporting reports).  `[report:WPR15LA154]`  
  > The pilot of the Cessna was cleared by ground control to taxi to runway 16 via taxiways A and C, and communication was maintained with the ground controller during the taxi.

**Exclude when**
- Coded MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) rather than GCOL: similar wording, different occurrence category.  `[report:ANC16FA061]`  
  > Cause: Personnel issues-Psychological-Attention/monitoring-Monitoring other aircraft-Pilot of other aircraft.
- Not 'A standing or parked aircraft was struck/damaged by a vehicle/equipment' — that definition is crosswalked to ADRM, not GCOL.  `[definition:ECC-5030704]`
- Not 'Loss of separation with aircraft - both airborne' — that definition is crosswalked to MAC, not GCOL.  `[definition:ECC-2180101]`
- Not 'Anomaly: Ground Incursion – Runway or Taxiway' — that definition is crosswalked to RI, not GCOL.  `[definition:IND-04]`
- Events better described by CICTT MAC (Airprox / ACAS alert / loss of separation / near midair / midair collision) (runner-up parent, margin 0.54).  `[parent:MAC]`

**Linked example reports**
- WPR15LA154: "The pilot of the Cessna was cleared by ground control to taxi to runway 16 via taxiways A and C, and communication was maintained with the ground controller during the taxi."
- ERA10CA411: "Other workers at the site stated that their rule was to park their vehicles behind the taxiway lights, in order to leave adequate room for aircraft on the taxiway."
- ERA11LA361/2: "Probable cause: The pilots of both airplanes did not maintain adequate visual lookout during taxi, which resulted in an on-ground collision."
- ERA15CA113: "When conducting taxi operations, pilots need to be aware of their proximity to other aircraft and vehicles moving on the airport.""
- ERA20LA247: "Probable cause: The failure of both pilots to see and avoid each other while taxiing, which resulted in a ground collision."
- ERA13CA123: "When the pilot was taxiing back to the hangar she noticed the same parked vehicle in the distance and off to the right of the taxiway she was traveling on."
- GAA18CA568: "While taxiing on delta, another airplane entering taxiway Delta collided with the left side of his airplane."
- DCA15FA004/2: "The intersection of taxiway Alpha and Quebec is a "Y-type" intersection where taxiing northwest on A through the intersection and continuing northwest becomes taxiway Q and a right turn of greater than 25 degrees is required to remain on taxiway A."
- WPR11FA158: "No objects are allowed to be within the Taxi-lane Object Free Area (TOFA) except for those objects that need to be located in the Object Free Area for air navigation or aircraft ground maneuvering purposes."
- CEN11LA099: "Probable cause: The Boeing 747 first officer’s failure to maintain clearance from another airplane while taxiing due to his inadequate judgment of the distance between the airplanes."
- ERA20CA243: "According to the pilot, airplanes were parked along both sides with many parked across the double-yellow taxiway edge lines and into the taxiway object-free movement area.The student pilot said he endeavored to keep the nose wheel on the taxiway centerline as he'd been taught to maintain clearance."
- WPR09LA036: "The captain reported when the airplane was on the taxiway centerline, the first officer asked if he wanted the taxi light turned off, after replying "yes" the first officer turned off the taxi light and the captain "…felt a large impact." In a written statement submitted to the NTSB, the first officer stated while taxiing on taxiway Alpha 5 the airplane's left wing was struck by a service vehicle."

**Checks:** G1 pass · G2 pass · G3 pass · G4 pass · G5 pass · G6 pass · G7 pass · G8 pass · G9 pass
