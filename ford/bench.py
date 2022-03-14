#!/usr/bin/env python3
from time import sleep
from panda import Panda
from opendbc.can.packer import CANPacker

from bench.ford.fordcan import *
from bench.ford.values import *


class FordBench():
  def __init__(self):
    self.panda = Panda()
    self.panda.can_clear(0xFFFF)
    self.panda.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
    self.panda.set_heartbeat_disabled()

  def send_cmd(self, packer, command, bus=None, **kwargs):
    addr, _, data, _ = command(packer, **kwargs)
    if bus is None:
      sent_bus = "0, 1, 2"
      for bus in (0, 1, 2):
        print(bus)
        self.panda.can_send(addr, data, bus)
    elif isinstance(bus, str):
      bus = BUS_MAP[bus]
      sent_bus = str(bus)
      self.panda.can_send(addr, data, bus)
    else:
      sent_bus = str(bus)
      self.panda.can_send(addr, data, bus)
    print(f"({addr})\t{command.__name__}\t\tbus {sent_bus}:\t\t{data}")
    sleep(DELAY)

  def send_msg(self, addr, data):
    print(addr, data)
    for bus in (0, 1, 2):
      self.panda.can_send(addr, data, bus)
    print(f"{addr}\t sent on bus 0, 1, 2: {data}")
    sleep(DELAY)


if __name__ == "__main__":
  packer = CANPacker(DBC_NAME)

  bench = FordBench()

  bench.send_cmd(packer, mc_send_signals_2)
  # sys.exit(0)

  print("Is white panda?", bench.panda.is_white())

  # while 1:
  #   p.can_send(bdf_info_addr, bdy_info_data, BUS)
  #   print(bdf_info_addr, bdy_info_data)
  #   sleep(0.008)

  # send_cmd(packer, mc_send_signals_2)
  # sys.exit(0)


  print("Sending commands...")
  try:
    datas = [0, 255, 170, 132]
    # datas = [0, 255] #, 255, 136, 170, 158, 132, 140]
    step = 0
    button_counter = 0

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

      idx = 1
      size = 2000
      # idx = 0
      # size = 1600 + 1

      BATCH_SIZE = 250000
      count = 0

      data = datas[step]
      send_data = bytearray([data] * 8)

      step += 1
      if step == len(datas):
        step = 0
      sent = []


      def send_bdycm():
        bench.send_cmd(packer, body_info_data, bus=2, ignition=4)

      send_bdycm()


      def send_common():
        # removes airbag fault telltale
        # send_cmd(packer, rcm_status_message_2, bus="HS2")  # 76

        # if button_counter % 20 == 0:
        #   print("BUTTON!")
        #   print("BUTTON!")
        #   print("BUTTON!")
        #   print("BUTTON!")
        #   print("BUTTON!")
        # send_cmd(packer, steering_wheel_data2, bus="HS2", hud=True, ok=True)
        # else:
        #   send_cmd(packer, steering_wheel_data2)

        # hud
        # send_cmd(packer, accdata_2)  # 391

        # speed
        # send_cmd(packer, brake_sn_data_3)  # 119
        # send_cmd(packer, eng_vehicle_sp_throttle_2)  # 514
        # send_cmd(packer, wheel_speed)  # 535

        # fuel
        # send_cmd(packer, powertrain_data_4, bus="HS1", fuel=75, fuelwarn=0, fuelrange=0)  # 1060

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

      # addr = 946  # 0x3B2
      # send_data = bytearray([
      #   0b01000000,   #  7 XXXX---- ignition?
      #                 #    -----X-- running lights?
      #                 #    ------X- rear fog light
      #                 #    -------X door open
      #   0b00000000,   # 15 0001---- is "turn key to start?"
      #                 #    ----XXXX needle backlight
      #   0b00000000,   # 23
      #   0b00010000,   # 31 ---YYYYY backlight?
      #   0b00000000,   # 39 ----X--- right turn signal
      #   0b00000000,   # 47
      #   0b00000000,   # 55 -X------ left turn signal
      #                 #    ----XX-- factory mode/transport mode
      #                 #        11   transport mode
      #                 #        10   ?
      #                 #        01   factory mode
      #                 #        00   ?
      #                 #    ------X- rear right door open
      #                 #    -------X rear left door open
      #   0b00000000,   # 63 --X----- driver door open
      #                 #    ---X---- passenger door open
      #                 #    -----X-- liftgate open
      #                 #    -------X front fog light
      # ])
      # print(data)

      while 1:
        button_counter += 1

        # data += 1
        # if data == 256:
        #   data = 0
        # send_data = bytearray([data] * 8)

        send_bdycm()
        # send_msg(addr, send_data)
        send_common()
        sleep(DELAY * 10)


      for addr in range(idx, idx + size):
        if any(addr in r for r in ignored):
          print("skipping ignored", addr)
          continue
        if any(addr in r for r in bookmarked):
          print("skipping bookmarked", addr)
          continue

        if idx % 25 == 0:
          send_bdycm()

        bench.send_msg(addr, send_data)
        sent.append(addr)

        count += 1
        if count == BATCH_SIZE or addr == idx + size - 1:
          # send_wakeup()
          send_bdycm()
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
    bench.panda.close()
