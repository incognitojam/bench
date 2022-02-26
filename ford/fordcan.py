def steering_data(packer):
  values = {
    "HeadLghtHiFlash_D_Stat": 1,
    "HeadLghtHiCtrl_D_RqAhb": 0,
  }
  return packer.make_can_msg("Steering_Data_FD1", 0, values)

def rcm_status_message_2(packer):
  values = {
    "FirstRowBuckleMid": 2,
    "SecondRowBucklePsngr": 2,
    "SecondRowBuckleMid": 2,
    "SecondRowBuckleDriver": 2,
    "FirstRowBuckleDriver": 1,
    "RILReq": 0,
    "FirstRowBucklePsngr": 2,
    "RstrnImpactEvntStatus": 0,
    "PsngrFrntDetct_D_Actl": 2,
    "EDRTriggerEvntSync": 0,
    "PassRstrnInd_Req": 0,
  }
  return packer.make_can_msg("RCMStatusMessage2_FD1", 0, values)

def body_info_data(packer, ignition=0, needle_backlight=0, backlight=16, turn_signal_right=False, turn_signal_left=False):
  values = {
    "Ignition": ignition,
    "RunningLights": 0,
    "FogLightRear": 0,
    "DoorOpen": 0,
    "NeedleBacklight": needle_backlight,
    "Backlight": backlight,
    "TurnSignalRight": 1 if turn_signal_right else 0,
    "TurnSignalLeft": 1 if turn_signal_left else 0,
    "FactoryMode": 0,
    "DoorOpenRr": 0,
    "DoorOpenRl": 0,
    "DoorOpenDrvr": 0,
    "DoorOpenPsngr": 0,
    "DoorOpenLftgt": 0,
    "FogLightFront": 0,
  }
  return packer.make_can_msg("BodyInfo_Data", 0, values)

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
    "Key_In_Ignition_Stat": 1,
    "Ignition_Status": 8,
    "Dimming_Lvl": 6,
    "Day_Night_Status": 2,
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
    "Veh_V_CompLimMx": 20,
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


def mc_send_signals_2(packer):
  values = {
    "Mc_VehTimeFrmtUsrSel_St": 2,  # 2 "24h_mode" 1 "12h_mode" 0 "Invalid"
    "Running_Board_Cmd": 1,  # 3 "Unused" 2 "Manually_Deployed" 1 "All_Enabled" 0 "All_Disabled"
    "EngExhMdeQuiet_D2_Rq": 2,  # 4 "Track" 3 "Sport" 2 "Normal" 1 "Stealth" 0 "Null"
    "EdmSailMde_B_RqDrv": 0,  # 1 "On" 0 "Off"
    "DrvInputRequired_B_Rq": 0,  # 1 "Yes" 0 "No"
    "AwdRnge_D_ActlIpc": 3,  # 6 "High_Range_2wd" 5 "High_Range_Auto" 4 "High_Range_Locked" 3 "Neutral" 2 "Low_Range_2wd" 1 "Low_Range_Auto" 0 "Low_Range_Locked"
    "BalrSwtch_D_Stat": 0,  # 2 "Pressed" 1 "NotPressed" 0 "Null"
    "BalrMde_D_Rq": 0,  # 3 "High" 2 "Medium" 1 "Low" 0 "Null"
    "WaitToStartLamp_D_Falt": 0,  # 2 "Wait_to_start_lamp_failed" 1 "Diagnosis_not_ready" 0 "Wait_to_start_lamp_OK"
    "EsaOn_B_Rq": 0,  # 1 "On" 0 "Off"
    "BttOn_B_Rq": 1,  # 1 "On" 0 "Off"
    "Btt_L_Actl": 125,  # 127 "Faulty" 126 "NoDataExists"
    "SelDrvMdeTxtReset_B_Rq": 0,  # 1 "Yes" 0 "No"
    "SelDrvMdeDsply_B_Avail": 1,  # 1 "Available" 0 "NotAvailable"
    "Mc_VehUntTrpCoUsrSel_St": 1,  # 0 "TripComputer_metric" 1 "TripComputer_imperial"
    "Mc_VehUnitTempUsrSel_St": 0,  # 0 "Temperature_deg_c" 1 "Temperature_deg_f"
    "Mc_VehLangUsrSel_St": 0,  # 30 "Slovak" 29 "Arabic" 28 "Cantonese" 27 "Mandarin_Chinese"
                               # 26 "Korean" 25 "Japanese_Kanji" 24 "Japanese_Katakana" 23 "Braz_Portuguese"
                               # 22 "EU_Portuguese" 21 "Finish" 20 "Norwegian" 19 "Danish" 18 "Swedish"
                               # 17 "Hungarian" 16 "Greek" 15 "Czech" 14 "Polish" 13 "Flemish" 12 "Dutch"
                               # 11 "Russian" 10 "Turkish" 9 "Mex_Spanish" 8 "EU_Spanish" 7 "Cana_French"
                               # 6 "EU_French" 5 "Italian" 4 "German" 3 "NA_English" 2 "UK_English"
  }
  return packer.make_can_msg("Mc_Send_Signals_2_FD1", 0, values)


def battery_mgmt_2(packer):
  values = {
    "EngStrtInhbt_B_RqBatt": 0,  # 1 "Start_Inhibit" 0 "Dont_Care"
    "BattULoChrg_D_Rq": 0,  # 3 "Low_Battery_Temperature" 2 "Charging_Requested" 1 "Chrg_Requested_HighCurrent" 0 "No_Request"
    "PwSysULoFalt_D_Stat": 0,  # 14 "LowBatterySOC" 13 "PSS_Shed2_Contin" 9 "BattMonitoringSensorFault" 8 "LowBattVoltDuringPwSrcOn" 7 "LowBatt2_PowerSaveMode" 6 "LowBatt1_Warning" 5 "Overvoltage" 4 "Fault_NoOutput" 3 "Fault_ReducedOutput" 2 "Fault_Nonspecific" 1 "Cluster_Proveout" 0 "No_Fault"
    "Shed_T_Eng_Off_B": 0,  # 1 "Active" 0 "Inactive"
    "Shed_Feature_Group_ID": 0,  # 31 "All LSHED1 Features"  16 "PtcHeater" 15 "Engine_Coolant_Fan" 14 "HtdMirr"
                                 # 13 "HvacRearBlwr_Third" 12 "HvacRearBlwr_Second" 11 "HvacRearBlwr_First"
                                 # 10 "Htd_Windscrn" 9 "SpltHtdBcklight_HtdMirr" 8 "HtdBcklight_HtdMirr"
                                 # 7 "HtdCoolSeat_FrtDriver" 6 "HtdCoolSeat_FrtPass" 5 "HtdCoolSeat_RearPass"
                                 # 4 "HtdCoolSeat_RearDriver" 3 "SmartTrlrTowBattCharge" 2 "Htd_StrWhl"
                                 # 1 "Htd_Washer_Fluid" 0 "No_LSHED1_Features"
    "Shed_Drain_Eng_Off_B": 0,  # 1 "Active" 0 "Inactive"
    "Shed_Level_Req": 0,  # 6 "Loads_On" 5 "SHED_ENG_OFF" 4 "SOON_ENG_OFF" 3 "SHED2_CONTIN" 2 "SHED2_TRANS" 1 "SHED1" 0 "NO_SHED"
    "BattULoSrvc_T_Actl": 0,
    "ULoRgenTestMde_B_Rq": 0,  # 1 "Request" 0 "NoRequest"
    "ChargeMode": 0,  # 5 "Battery_Identify" 4 "Battery_Refresh" 3 "SlowRegenAllowNoDischarge" 2 "Fast_Regen_Allowed" 1 "Slow_Regen_Allowed" 0 "Conventional_Charging"
    "IdleSpeedIncrease_El": 0,  # 1 "Yes" 0 "No"
    "Batt_Lo_SoC_B": 0,  # 1 "Active" 0 "Inactive"
    "PeriodicElLoad_B_Stat": 0,  # 1 "Active" 0 "Inactive"
    "Batt_Crit_SoC_B": 0,  # 1 "Active" 0 "Inactive"
  }
  return packer.make_can_msg("Battery_Mgmt_2_FD1", 0, values)


def bcm_lamp_stat(packer):
  values = {
    "Illuminated_Entry_Stat": 1,  # 1 "On" 0 "Off"
    "Dr_Courtesy_Light_Stat": 0,  # 1 "On" 0 "Off"
    "Courtesy_Delay_Status": 0,  # 1 "On" 0 "Off"
    "ImpactEvntFdbck_D_Stat": 0,  # 2 "EventComplete" 1 "EventInProgress" 0 "Normal"
    "WrlssAcsyChrgInhbt_B_Rq": 0,  # 1 "Yes" 0 "No"
    "PudLampPsngr_D_Rq": 0,  # 3 "Ramp_Down" 2 "Ramp_Up" 1 "On" 0 "Off"
    "HeadLampLoOut_B_Stat": 0,  # 1 "Out" 0 "Null"
    "CrnrLghtRight_Pc_Rq": 0,  # pct
    "CrnrLghtLeft_Pc_Rq": 0,  # pct
    "HeadLghtHiFdbck_D_Stat": 0,
    "PudLampDrv_D_Rq": 0,
    "TrnNotInPrkChime_B_Rq": 0,
    "PrkLightChime_B_Rq": 0,
    "KeyInIgnWarn_B_Cmd": 0,
    "HomeSafeLtChime_B_Rq": 0,
    "StopLghtOn_B_Stat": 0,
    "RvrseLghtOn_B_Stat": 0,
    "PrkLght_D_Stat": 0,
    "HeadLghtSwtch_D_Stat": 0,
    "HeadLampLoFrOn_B_Stat": 0,
    "HeadLampLoFlOn_B_Stat": 0,
    "HeadLampLoActv_B_Stat": 0,
    "Headlamp_On_Wrning_Cmd": 0,
    "Park_Brake_Chime_Rqst": 0,
    "HeadLghtHiOn_B_Stat": 0,
    "BrkWarnInd_B_Rq": 0,
    "Brk_Fluid_Lvl_Low": 0,
    "ReducedGuard_D_Stat": 0,
    "Perimeter_Alarm_Status": 0,
    "Courtesy_BSave_Stat": 0,
    "DrTgateLck_D_Stat": 0,
    "WndwGlbl_D_Cmd": 0,
    "PudLamp_D_Rq": 0,
    "DayRnngLampOn_B_Stat": 0,
    "PerimeterAlarmChimeRq": 0,
  }
  return packer.make_can_msg("BCM_Lamp_Stat_FD1", 0, values)

def accdata_2(packer, hud_intensity=100, hud_blk3=True, hud_blk2=True, hud_blk1=True, hud_rate=1):
  values = {
    "CmbbBrkDecel_No_Cnt": 0,
    "HudDsplyIntns_No_Actl": hud_intensity,
    "HudBlk3_B_Rq": 1 if hud_blk3 else 0,
    "HudBlk2_B_Rq": 1 if hud_blk2 else 0,
    "HudBlk1_B_Rq": 1 if hud_blk1 else 0,
    "HudFlashRate_D_Actl": hud_rate,
    "CmbbBrkDecel_No_Cs": 0,
    "CmbbBrkDecel_A_Rq": 0,
    "CmbbBrkPrchg_D_Rq": 0,
    "CmbbBrkDecel_B_Rq": 0,
    "CmbbBaSens_D_Rq": 0,
  }
  return packer.make_can_msg("ACCDATA_2", 0, values)

def steering_wheel_data2(packer, ok=False, menu=False, hud=False):
  values = {
    "SelDrvMdeSwtch_D_Stat4": 0,
    "SteWhlSwtchView_B_Stat": 0,
    "SteWhlSwtchSet_B_Stat": 0,
    "SteWhlSwtchPhon_B_Stat": 0,
    "SteWhlSwtchNav_B_Stat": 0,
    "SteWhlSwtchMed_B_Stat": 0,
    "SteWhlSwtchIod_B_Stat": 0,
    "SteWhlSwtchHud_B_Stat": 1 if hud else 0,
    "SteWhlSwtchBack_B_Stat": 0,
    "SteWhlSwtchMenu_B_Stat": 1 if menu else 0,
    "SteEffortInc_B_RqDrv": 0,
    "SelDrvMdeInc_B_RqDrv": 0,
    "SelDrvMdeDec_B_RqDrv": 0,
    "SuspDampInc_B_RqDrv": 0,
    "SteWhlSwtchUp_B_Stat": 0,
    "SteWhlSwtchRght_B_Stat": 0,
    "SteWhlSwtchOk_B_Stat": 1 if ok else 0,
    "SteWhlSwtchLeft_B_Stat": 0,
    "SteWhlSwtchDown_B_Stat": 0,
    "SteWhlSwtchHome_B_Stat": 0,
    "SteWhlSwtchInfo_B_Stat": 0,
  }
  return packer.make_can_msg("Steering_Wheel_Data2_FD1", 0, values)

def eng_vehicle_sp_throttle_2(packer):
  values = {
    "StrtrMtrDlyStrt_B_Stat": 0,
    "VehVTrlrAid_B_Avail": 0,
    "StrtrMtrCtlMsgTxt_D_Rq": 0,
    "VehVActlEng_No_Cs": 0,
    "VehVActlEng_No_Cnt": 0,
    "Veh_V_RqCcSet": 0,
    "VehVActlEng_D_Qf": 0,
    "Veh_V_ActlEng": 50,
    "GearRvrse_D_Actl": 3,
    "StrtrMtrCtlMsgTxt_D2_Rq": 0,
  }
  return packer.make_can_msg("EngVehicleSpThrottle2", 0, values)

def wheel_speed(packer, speed=1000):
  values = {
    "WhlRr_W_Meas": speed,
    "WhlRl_W_Meas": speed,
    "WhlFr_W_Meas": speed,
    "WhlFl_W_Meas": speed,
  }
  return packer.make_can_msg("WheelSpeed", 0, values)

def brake_sn_data_3(packer):
  values = {
    "VehTrvlDir_D_Stat": 1,
    "VehOverGnd_V_Est": 1000,
    "VehLongComp_A_Actl": 0,
    "VehLatComp_A_Actl": 0,
    "VehYawComp_W_Actl": 0,
  }
  return packer.make_can_msg("BrakeSnData_3", 0, values)

def powertrain_data_4(packer, fuel=0, fuelwarn=0, fuelrange=0):
  values = {
    "RearDiffOilTeWarn_B_Rq": 0,
    "RearDiffOil_Te_Actl": 0,
    "BpedDrvMsgTxt_B_Dsply": 0,
    "FuelLvl_Pc_DsplyEng": fuel,
    "FuelLvlWarn_D_ActlEng": fuelwarn,
    "FuelRange_L_DsplyEng": fuelrange,
    "SelDrvMdePt_D_Stat": 0,
  }
  return packer.make_can_msg("Powertrain_Data_4", 0, values)
