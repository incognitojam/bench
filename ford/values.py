DBC_NAME = "ford_lincoln_base_pt"
DELAY = 0.01

BUS_MAP = {
  "HS1": 0,
  "HS2": 1,
  "HS3": 2,
  "HS4": 2,
}

ignored = [
  range(765, 765+1),  # cluster settings, incl. language

  # ###########
  # # WAKE UP #
  # ###########
  # range(800, 1200 + 1),

  # # 1400
  # range(1400, 1407 + 1),  # not wake up

  # # 1500
  # range(1548, 1599 + 1),  # not wake up

  # # 1600
  # range(1600, 1699 + 1),  # not wake up
]

bookmarked = [
  range(76, 76 + 1),    # RCMStatusMessage2_FD1

  # 700
  range(765, 765 + 1),  # Mc_Send_Signals_2_FD1

  # 900
  range(909, 909 + 1),  # Body_Info_6_FD1
  range(931, 931 + 1),  # Body_Info_9_FD1
  range(946, 946 + 1),  # BodyInfo_Data
  range(947, 947 + 1),  # BodyInfo_3_FD1
  range(963, 963 + 1),  # BCM_Lamp_Stat_FD1

  # 1000
  range(1060, 1060 + 1), # Powertrain_Data_4
  # range(1068, 1068 + 1),  # Battery_Mgmt_2_FD1
  # range(1076, 1076 + 1),  # Cluster_Info_3_FD1

  # 1400
  range(1408, 1427 + 1),  # wake up
  range(1428, 1449 + 1),  # wake up (untested)
  range(1450, 1450 + 1),  # wake up
  range(1451, 1499 + 1),  # wake up (untested)

  # 1500
  range(1500, 1502 + 1),  # wake up
  range(1503, 1517 + 1),  # wake up (batched)
  range(1518, 1532 + 1),  # wake up (batched)
  range(1533, 1547 + 1),  # wake up (batched)
]

# range(500, 550 + 1),  # park brk + fault? warnings flashed with FF. sometimes chime too.
# range(900, 925 + 1),  # chimes with FF, "vehicle switched off"
# range(925, 950 + 1),  # lights and screen on (backlight) with FF, "vehicle switched off"
# range(950, 975 + 1),  # Danish language, hazards, alarm ("Start vehicle to stop the alarm")
