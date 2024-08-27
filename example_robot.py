

import os
import pybullet_utils.bullet_client as bc
import pybullet as p
import pb_utils as pbu
import random

if __name__ == '__main__':

    PANDA_PATH = os.path.join("./models/franka_panda/panda.urdf")
    client = bc.BulletClient(connection_mode=p.GUI)
    robot = pbu.load_pybullet(PANDA_PATH, fixed_base=True, client=client)

    for _ in range(10):
        joints = pbu.get_movable_joints(robot, client=client)
        ranges = [pbu.get_joint_limits(robot, joint, client=client) for joint in joints]
        initialization_sample = [random.uniform(r[0], r[1]) for r in ranges]
        pbu.set_joint_positions(robot, joints, initialization_sample, client=client)
        print("Joint angles:", initialization_sample)
        pbu.wait_if_gui("Next?", client=client)

