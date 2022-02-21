#!/usr/bin/env python3
import sys
from time import sleep
from panda import Panda
from opendbc.can.packer import CANPacker
from opendbc.can.parser import CANParser
from opendbc.can.tests.test_packer_parser import can_list_to_can_capnp
from selfdrive.controls.lib import cluster


DBC_NAME = "ford_lincoln_base_pt"
BUS = 2
DELAY = 0.009

SIGNALS = [
 ("ValetMode_D_Mem", "BodyInfo_3_FD1", 0),
 ("DimmingLvlEvnt_No_Actl", "BodyInfo_3_FD1", 0),
 ("DrStatDrvErrCnt_B_Stat", "BodyInfo_3_FD1", 0),
 ("TurnLghtRight_D_Rq", "BodyInfo_3_FD1", 0),
 ("TurnLghtRightOn_B_Stat", "BodyInfo_3_FD1", 0),
 ("TurnLghtLeftOn_B_Stat", "BodyInfo_3_FD1", 0),
 ("FogLghtRearOn_B_Stat", "BodyInfo_3_FD1", 0),
 ("Backlit_LED_Status", "BodyInfo_3_FD1", 0),
 ("TurnLghtLeft_D_Rq", "BodyInfo_3_FD1", 0),
 ("FogLghtFrontOn_B_Stat", "BodyInfo_3_FD1", 0),
 ("IgnKeyType_D_Actl", "BodyInfo_3_FD1", 0),
 ("Parklamp_Status", "BodyInfo_3_FD1", 0),
 ("Litval", "BodyInfo_3_FD1", 0),
 ("Key_In_Ignition_Stat", "BodyInfo_3_FD1", 0),
 ("Ignition_Status", "BodyInfo_3_FD1", 0),
 ("Dimming_Lvl", "BodyInfo_3_FD1", 0),
 ("Day_Night_Status", "BodyInfo_3_FD1", 0),
 ("Remote_Start_Status", "BodyInfo_3_FD1", 0),
 ("DrStatTgate_B_Actl", "BodyInfo_3_FD1", 0),
 ("DrStatRr_B_Actl", "BodyInfo_3_FD1", 0),
 ("DrStatRl_B_Actl", "BodyInfo_3_FD1", 0),
 ("DrStatPsngr_B_Actl", "BodyInfo_3_FD1", 0),
 ("DrStatInnrTgate_B_Actl", "BodyInfo_3_FD1", 0),
 ("DrStatHood_B_Actl", "BodyInfo_3_FD1", 0),
 ("DrStatDrv_B_Actl", "BodyInfo_3_FD1", 0),
 ("PrkBrkActv_B_Actl", "BodyInfo_3_FD1", 0),
 ("LifeCycMde_D_Actl", "BodyInfo_3_FD1", 0),
 ("Delay_Accy", "BodyInfo_3_FD1", 0),
 ("CrashEvnt_D_Stat", "BodyInfo_3_FD1", 0),
 ("FuelPmpInhbt_B_Stat", "BodyInfo_3_FD1", 0),
 ("BodySrvcRqd_B_Rq", "BodyInfo_3_FD1", 0),
]
CHECKS = []


def steering_data(packer):
  values = {
    "HeadLghtHiFlash_D_Stat": 1,
    "HeadLghtHiCtrl_D_RqAhb": 0,
  }
  return packer.make_can_msg("Steering_Data_FD1", 0, values)

def body_info_3(packer):
  values = {
    "ValetMode_D_Mem": 0,
    "DimmingLvlEvnt_No_Actl": 0,
    "DrStatDrvErrCnt_B_Stat": 0,
    "TurnLghtRight_D_Rq": 0,
    "TurnLghtRightOn_B_Stat": 0,
    "TurnLghtLeftOn_B_Stat": 0,
    "FogLghtRearOn_B_Stat": 0,
    "Backlit_LED_Status": 0,
    "TurnLghtLeft_D_Rq": 0,
    "FogLghtFrontOn_B_Stat": 0,
    "IgnKeyType_D_Actl": 4,
    "Parklamp_Status": 1,
    "Litval": 0,
    "Key_In_Ignition_Stat": 0,
    "Ignition_Status": 4,
    "Dimming_Lvl": 0,
    "Day_Night_Status": 0,
    "Remote_Start_Status": 0,
    "DrStatTgate_B_Actl": 0,
    "DrStatRr_B_Actl": 0,
    "DrStatRl_B_Actl": 0,
    "DrStatPsngr_B_Actl": 0,
    "DrStatInnrTgate_B_Actl": 0,
    "DrStatHood_B_Actl": 0,
    "DrStatDrv_B_Actl": 0,
    "PrkBrkActv_B_Actl": 1,
    "LifeCycMde_D_Actl": 0,
    "Delay_Accy": 0,
    "CrashEvnt_D_Stat": 0,
    "FuelPmpInhbt_B_Stat": 0,
    "BodySrvcRqd_B_Rq": 0,
  }
  return packer.make_can_msg("BodyInfo_3_FD1", 0, values)

def body_info_6(packer):
  values = {
    "IgnPsswrdDsply_B_Rq": 0,
    "ElPwPoint_D_Rq": 0,
    "PoliceIdlMde_D_Stat": 0,
    "DrLatchMsgTxt_D_Rq": 1,
    "SecurityMsgTxt_D_Rq": 3,
    "PrmtrAlrmEvnt_D_Stat": 2,
    "HeadLghtHiPrmsn_D_Stat": 0,
    "SteWhlLckMsgTxt_D_Rq": 0,
    "immoMsgTxt_D_Rq": 0,
    "PrsnlDevcChrgEnbl_B_Rq": 0,
    "TracKeyMde_D_Stat": 0,
    "PEBackupSlot_Stats": 0,
    "KeyMykeyTot_No_Cnt": 0,
    "Keycode_Status": 0,
    "KeyAdmnTot_No_Cnt": 0,
  }
  return packer.make_can_msg("Body_Info_6_FD1", 0, values)

def body_info_9(packer):
  values = {
    "PtWakeReas_D_Stat": 4,  # 6 "ElapsedTime" 5 "ThirdPartyWakeup" 4 "DoorAjar" 3 "EarlyWake" 2 "NonMotiveStart" 1 "MotiveStart" 0 "Null"
    "VehOnSrc_D_Stat": 1,  # 4 "OverTheAir" 3 "RemoteParkAssist" 2 "RemoteStart" 1 "Manual" 0 "Off"
    "StrtrMtrCtlDStat_No_Cs": 0,
    "EngStrtActv_B_Stat": 1,  # 1 "Active" 0 "Inactive"
    "EngStrt_B_Rq": 1,  # 1 "Request" 0 "NoRequest"
    "DrvInCtl_B_Stat": 1,  # 1 "Yes" 0 "No"
    "AdvStrt_D_Stat": 0,  # 0 "NoAction"
    "CrnkInhbt_No_Cs": 0,
    "CrnkInhbt_No_Cnt": 0,
    "CrnkInhbt_B_Stat": 0,  # 1 "Inhibit" 0 "NoInhibit"
    "IgnPreOffActv_B_Stat": 0,  # 1 "Active" 0 "Inactive"
  }
  return packer.make_can_msg("Body_Info_9_FD1", 0, values)

def cluster_info_3(packer):
  values = {
    "HILL_DESC_SW": 1,
    "AutoRgen_D_Rq": 0,
    "W2S_LAMP_OK": 1,
    "OdoTripRx_B_Actl": 1,
    "Veh_V_CompLimMx": 0,
    "DrvSlipCtlMde_B_RqMyKey": 0,
    "FuelLvlWarn_D_Actl": 2,
    "FuelSecndActv_B_Actl": 1,
    "FuelLvlPssvSide_No_Raw": 512,
    "FUEL_SENSOR_NUM": 0,
    "FuelLvlActvSide_No_Raw": 512,
    "FuelLvl_Pc_Dsply": 50.0,
    "DISPLAY_SPEED_SCALING": 100,
    "DISPLAY_SPEED_OFFSET": 0,
  }
  return packer.make_can_msg("Cluster_Info_3_FD1", 0, values)

def locking_systems_2(packer):
  values = {
    "ChildLckMde_B_Stat": 0,
    "VehLckInd_D_Rq": 2,
    "DrTgateOpen_B_Rq": 0,
    "DrTgateExtSwMde_B_Stat": 0,
    "Remote_Device_Feedback": 0,
    "Veh_Lock_Requestor": 3,
    "R_Pwr_Sliding_Dr_Rqst": 0,
    "Power_Liftgate_Rqst": 0,
    "Veh_Lock_EvNum": 0,
    "Power_Decklid_Rqst": 0,
    "L_Pwr_Sliding_Dr_Rqst": 0,
    "Keyfob_Pad_Msg_Count": 0,
    "Veh_Lock_Sub_Id": 0,
    "Veh_Lock_Status": 0,
    "ChildLck_D_Dsply": 0,
    "WindowLockout_B_Stat": 0,
    "RollCodeUnlock": 0,
    "Lockmsgtxt_D_Rq": 2,
    "FobComm_D_Stat": 0,
    "LockInhibit": 0,
  }
  return packer.make_can_msg("Locking_Systems_2_FD1", 0, values)


if __name__ == "__main__":
  packer = CANPacker(DBC_NAME)
  parser = CANParser(DBC_NAME, signals=SIGNALS, checks=CHECKS, enforce_checks=False)

  # msgs = create_body_info_command(packer, key=1, ignition=4, backlight=4, dimming=12)
  # msgs[2] =  b"\x41\x00\x00\x00\x4c\x00\xe0\x00"
  # print("msgs:", msgs)

  # BodyInfo_3_FD1, CGEA 1.3 wake up message
  # msg = [947, 0, b"\x41\x00\x00\x00\x4c\x00\xe0\x00", 0]
  # bts = can_list_to_can_capnp([msg])
  # parser.update_string(bts)
  # print(parser.vl["BodyInfo_3_FD1"])

  # bds_values = parser.vl["BodyInfo_3_FD1"]
  # bds_values["TurnLghtRightOn_B_Stat"] = 0
  # bds_values["TurnLghtLeftOn_B_Stat"] = 0
  # bds_values["DrStatTgate_B_Actl"] = 0
  # bds_values["CrashEvnt_D_Stat"] = 0
  # result = packer.make_can_msg("BodyInfo_3_FD1", 0, bds_values)
  # print(f"result: {result[2]}")

  # bdf_info_addr = 947
  # bdy_info_data = b"\x40\x00\x00\x00\x40\x00\xa0\x00"

  # sys.exit(0)

  p = Panda()
  p.can_clear(0xFFFF)
  p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
  p.set_heartbeat_disabled()

  def send_cmd(packer, command):
    addr, _, data, _ = command(packer)
    print(addr, data)
    p.can_send(addr, data, BUS)
    sleep(DELAY)

  def send_msg(addr, data):
    print(addr, data)
    p.can_send(addr, data, BUS)
    sleep(DELAY)

  print("Is white panda?", p.is_white())

  # while 1:
  #   p.can_send(bdf_info_addr, bdy_info_data, BUS)
  #   print(bdf_info_addr, bdy_info_data)
  #   sleep(0.008)

  # bad_ranges = [
  #   range(0, 500),
  #   range(2000, 10000)
  # ]

  print("Sending commands...")
  try:
    # datas = [0, 255, 136]
    datas = [0, 255, 136] #, 255, 136, 170, 158, 132, 140]
    step = 0

    while 1:
      # can_sends = []

      # Source: https://ffclub.ru/topic/444743/jump_330/
      # print("Wake up messages")
      # p.can_send(0x048, b"\x00\x00\x00\x00\x07\x00\xe0\x00", BUS)  # C1MCA
      # p.can_send(0x044, b"\x88\xC0\x0C\x10\x04\x00\x02\x00", BUS)  # Sync 4

      # p.can_send(0x3B3, b"\x41\x00\x00\x00\x4c\x00\xe0\x00", BUS)  # CGEA 1.3
      # can_sends.append(create_body_info_3_command(packer))  # 947
      # can_sends.append(create_body_info_6_command(packer))  # 909
      # can_sends.append(create_locking_systems_2_command(packer))  # 817
      # can_sends.append(create_cluster_info_3_command(packer))  # 1076

      # around addr 1200? maybe a bit earlier. definitely above 1000.

      # chimes = 1, 2, 3, 8, 16, 48
      #      not 12

      # beep beep = 1, 3

      # nothing happens on addr % 4, 5, 6

      # ranges = itertools.chain(range(500, 1200, 2))
      # for addr in ranges:

      # wake up message less than 500 or more than 1200
      # for addr in range(100, 500, 1):
      #   send = bytearray([data] * 8)
      #   p.can_send(addr, send, BUS)
      #   print(addr, data, send)
      #   sleep(0.004)

      # not wakeup messages:
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
        # 900
        # TODO: test with ignoring these
        # range(909, 909 + 1),  # Body_Info_6_FD1
        # range(931, 931 + 1),  # Body_Info_9_FD1
        # range(947, 947 + 1),  # BodyInfo_3_FD1

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
      # range(900, 925 + 1),  # chimes with FF
      # range(925, 950 + 1),  # lights and screen on (backlight) with FF
      # range(950, 975 + 1),  # Danish language, hazards, alarm ("Start vehicle to stop the alarm")

      idx = 925
      size = 200

      count = 0
      BATCH_SIZE = 25

      data = datas[step]
      send_data = bytearray([data] * 8)

      step += 1
      if step == len(datas):
        step = 0

      for addr in range(idx, idx + size + 1):
        if any(addr in r for r in ignored):
          print("skipping ignored", addr)
          continue
        # if any(addr in r for r in bookmarked):
        #   print("skipping bookmarked", addr)
        #   continue

        wake_up_addr = bookmarked[0][0]
        wake_up_data = b"\x00\x00\x00\x00\x00\x00\x00\x00"
        send_msg(wake_up_addr, wake_up_data)

        send_msg(addr, send_data)

        count += 1
        if count == BATCH_SIZE:
          send_cmd(packer, body_info_3)  # 947
          send_cmd(packer, body_info_6)  # 909
          send_cmd(packer, body_info_9)  # 931
          send_cmd(packer, cluster_info_3)
          print("sent", BATCH_SIZE)
          input()
          count = 0

      # Source: https://www.explorerforum.com/forums/threads/anybody-play-with-arduino-can-bus-looking-for-the-front-camera-trigger.482116/
      # print("Speed message")
      # p.can_send(0x109, b"\x00\x03\x01\x00\x00\x00\x00\x28", BUS)  # BO_ 265
      # can_sends.append(create_speed_command(packer, speed=0))

      # for msg in can_sends:
      #   addr, data = msg[0], msg[2]
      #   try:
      #     p.can_send(addr, data, BUS)
      #     print(f"Sending {addr:04X}")
      #   except RuntimeError as e:
      #     print(f"RuntimeError while sending message {addr}, {data}", e)

      # p.send_heartbeat()
  except Exception as e:
    print(e)
  finally:
    p.close()
