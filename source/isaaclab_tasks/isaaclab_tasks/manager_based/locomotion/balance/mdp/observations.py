import torch
from isaaclab.envs import ManagerBasedRLEnv

def base_orientation(env: ManagerBasedRLEnv) -> torch.Tensor:
    return env.scene["robot"].data.root_quat_w  # shape: [N, 4]

def base_velocity(env: ManagerBasedRLEnv) -> torch.Tensor:
    lin_vel = env.scene["robot"].data.root_lin_vel_w  # shape: [N, 3]
    ang_vel = env.scene["robot"].data.root_ang_vel_w  # shape: [N, 3]
    return torch.cat([lin_vel, ang_vel], dim=-1)  # shape: [N, 6]

def joint_states(env: ManagerBasedRLEnv) -> torch.Tensor:
    joint_pos = env.scene["robot"].data.joint_pos
    joint_vel = env.scene["robot"].data.joint_vel
    return torch.cat([joint_pos, joint_vel], dim=-1)
