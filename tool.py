#!/usr/bin/env python3
from time import sleep
from panda import Panda

if __name__ == "__main__":
  p = Panda()
  p.can_clear(0xFFFF)
  p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
  p.set_heartbeat_disabled()

  BUS = 1
  DELAY = 0.1

  print("Sending commands...")
  try:
    while 1:
      try:
        # Source: https://ffclub.ru/topic/444743/jump_330/
        print("Wake up messages")
        p.can_send(0x048, b"\x00\x00\x00\x00\x07\x00\xe0\x00", BUS)  # C1MCA
        p.can_send(0x044, b"\x88\xC0\x0C\x10\x04\x00\x02\x00", BUS)  # Sync 4
        p.can_send(0x3B3, b"\x41\x00\x00\x00\x4c\x00\xe0\x00", BUS)  # CGEA 1.3

        # Source: https://www.explorerforum.com/forums/threads/anybody-play-with-arduino-can-bus-looking-for-the-front-camera-trigger.482116/
        print("Speed message")
        p.can_send(0x109, b"\x00\x03\x01\x00\x00\x00\x00\x28", BUS)
      except RuntimeError as e:
        print("RuntimeError", e)
        pass

      # p.send_heartbeat()
      sleep(DELAY)
  except Exception as e:
    print(e)
  finally:
    p.close()
