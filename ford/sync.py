#!/usr/bin/env python3
import sys
from time import sleep
from panda import Panda
from opendbc.can.packer import CANPacker
from opendbc.can.parser import CANParser
from opendbc.can.tests.test_packer_parser import can_list_to_can_capnp
from selfdrive.controls.lib import cluster

from bench.ford.fordcan import *
from bench.ford.values import *


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


if __name__ == "__main__":
  packer = CANPacker(DBC_NAME)
  # parser = CANParser(DBC_NAME, signals=SIGNALS, checks=CHECKS, enforce_checks=False)

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

  p = Panda()
  p.can_clear(0xFFFF)
  p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
  p.set_heartbeat_disabled()

  def send_cmd(packer, command, **kwargs):
    addr, _, data, _ = command(packer, **kwargs)
    print(command.__name__, addr, data)
    p.can_send(addr, data, BUS)
    sleep(DELAY)

  def send_msg(addr, data):
    print(addr, data)
    p.can_send(addr, data, BUS)
    sleep(DELAY)

  send_cmd(packer, mc_send_signals_2)
  # sys.exit(0)

  print("Is white panda?", p.is_white())

  # while 1:
  #   p.can_send(bdf_info_addr, bdy_info_data, BUS)
  #   print(bdf_info_addr, bdy_info_data)
  #   sleep(0.008)

  # bad_ranges = [
  #   range(0, 500),
  #   range(2000, 10000)
  # ]

  # send_cmd(packer, mc_send_signals_2)
  # sys.exit(0)

  print("Sending commands...")
  try:
    datas = [0, 255, 170]
    # datas = [0, 255] #, 255, 136, 170, 158, 132, 140]
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

      idx = 946
      size = 1
      # idx = 0
      # size = 1600 + 1

      BATCH_SIZE = 1
      count = 0

      data = datas[step]
      send_data = bytearray([data] * 8)

      step += 1
      if step == len(datas):
        step = 0
      sent = []


      def send_wakeup():
        wake_up_addr = 1408
        wake_up_data = b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
        send_msg(wake_up_addr, wake_up_data)


      def send_common():
        # removes airbag fault telltale
        send_cmd(packer, rcm_status_message_2)  # 76

        # speed
        # send_cmd(packer, brake_sn_data_3)  # 119
        # send_cmd(packer, eng_vehicle_sp_throttle_2)  # 514
        # send_cmd(packer, wheel_speed)  # 535

        # fuel
        send_cmd(packer, powertrain_data_4, fuel=75, fuelwarn=4, fuelrange=0)  # 1060

        # send_cmd(packer, cluster_info_3)  # 1076
        pass
        # send_cmd(packer, mc_send_signals_2)  # 765
        # send_cmd(packer, body_info_6)  # 909
        # send_cmd(packer, body_info_9)  # 931
        # send_msg(946, b"\xAA\xAA\xAA\xAA\xAA\xAA\xAA\xAA")  # 946 wake up IPC display
        # send_cmd(packer, body_info_3)  # 947
        # send_cmd(packer, bcm_lamp_stat)  # 963
        # send_cmd(packer, battery_mgmt_2)  # 1068

      # while 1:
      #   send_always()
      #   send_common()

      #   sleep(DELAY * 10)

      addr = 946  # 0x3B2
      send_data = bytearray([
        0b01000000,   # XXXX---- ignition?
                      # -----X-- running lights?
                      # ------X- rear fog light
                      # -------X door open
        0b00000001,   # 0001---- is "turn key to start?"
                      # ----1--- is needle backlight
        0b00000000,
        0b00010000,   # ???YYYYY backlight?
        0b00000000,   # ----X--- right turn signal
        0b00000000,
        0b00001100,   # -X------ left turn signal
                      # ----XX-- factory mode/transport mode
                      # ------X- rear right door open
                      # -------X rear left door open
        0b00000000,   # --X----- driver door open
                      # ---X---- passenger door open
                      # -----X-- liftgate open
                      # -------X front fog light
      ])
      print(data)

      while 1:
        # data += 1
        # if data == 256:
        #   data = 0
        # send_data = bytearray([data] * 8)
        send_wakeup()
        send_msg(addr, send_data)
        send_common()
        # send_cmd(packer, steering_wheel_data2, ok=True)
        # sleep(DELAY*2)
        # send_cmd(packer, steering_wheel_data2)
        sleep(DELAY * 10)


      for addr in range(idx, idx + size):
        if any(addr in r for r in ignored):
          print("skipping ignored", addr)
          continue
        if any(addr in r for r in bookmarked):
          print("skipping bookmarked", addr)
          continue

        send_wakeup()

        send_msg(addr, send_data)
        sent.append(addr)

        count += 1
        if count == BATCH_SIZE or addr == idx + size - 1:
          send_common()
          print(f"sent data {data:2X} in batch ({count}): {','.join(str(x) for x in sent)}")
          sent = []
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
