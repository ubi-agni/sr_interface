#!/usr/bin/env python

# Script to move the left hand with biotacs into store position.

import rospy
from sr_robot_commander.sr_hand_commander import SrHandCommander


rospy.init_node("store_left_hand", anonymous=True)

hand_commander = SrHandCommander(name="left_hand", prefix="lh")

open_hand = {'lh_FFJ1': 0.0, 'lh_FFJ2': 0.0, 'lh_FFJ3': 0.0, 'lh_FFJ4': 0.0,
             'lh_MFJ1': 0.0, 'lh_MFJ2': 0.0, 'lh_MFJ3': 0.0, 'lh_MFJ4': 0.0,
             'lh_RFJ1': 0.0, 'lh_RFJ2': 0.0, 'lh_RFJ3': 0.0, 'lh_RFJ4': 0.0,
             'lh_LFJ1': 0.0, 'lh_LFJ2': 0.0, 'lh_LFJ3': 0.0, 'lh_LFJ4': 0.0,
             'lh_THJ1': 0.0, 'lh_THJ2': 0.0, 'lh_THJ3': 0.0, 'lh_THJ4': 0.0, 'lh_THJ5': 0.0}

pack_hand = {'lh_FFJ1': 0.35, 'lh_FFJ2': 1.5707, 'lh_FFJ3': 1.5707, 'lh_FFJ4': 0.0,
             'lh_MFJ1': 0.35, 'lh_MFJ2': 1.5707, 'lh_MFJ3': 1.5707, 'lh_MFJ4': 0.0,
             'lh_RFJ1': 0.35, 'lh_RFJ2': 1.5707, 'lh_RFJ3': 1.5707, 'lh_RFJ4': 0.0,
             'lh_LFJ1': 0.35, 'lh_LFJ2': 1.5707, 'lh_LFJ3': 1.5707, 'lh_LFJ4': 0.0,
             'lh_THJ1': 0.35, 'lh_THJ2': 0.58, 'lh_THJ3': 0.0, 'lh_THJ4': 0.39, 'lh_THJ5': 0.19}


# Move hand to open position
joint_states = open_hand
rospy.loginfo("Moving hand to open position")
hand_commander.move_to_joint_value_target_unsafe(joint_states, 2.0, True)

# Move hand to closed position
joint_states = pack_hand
rospy.loginfo("Moving hand to pack position")
hand_commander.move_to_joint_value_target_unsafe(joint_states, 2.0, True)
