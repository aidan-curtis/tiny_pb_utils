

import pybullet_utils.bullet_client as bc
import pybullet as p
import pb_utils as pbu


if __name__ == '__main__':
    client = bc.BulletClient(connection_mode=p.DIRECT)

    box1 = pbu.create_box(0.2, 0.2, 0.2, client=client)
    pbu.set_pose(box1, ((0, 0, 0), (0, 0, 0, 1)), client=client)

    box2 = pbu.create_box(0.2, 0.2, 0.2, client=client)
    pbu.set_pose(box2, ((0.1, 0.1, 0.1), (0, 0, 0, 1)), client=client)

    print(pbu.get_closest_points(box1, box2, client=client))