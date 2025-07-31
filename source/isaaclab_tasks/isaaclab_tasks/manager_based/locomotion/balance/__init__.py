# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents

gym.register(
    id="Isaac-Balance-Spot-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.spot_balance_env_cfg:SpotBalanceEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:SpotBalancePPORunnerCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_balance_ppo_cfg.yaml",
    },
)

gym.register(
    id="Isaac-Balance-Spot-Play-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.spot_balance_env_cfg:SpotBalanceEnvCfg_PLAY",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:SpotBalancePPORunnerCfg",
        "skrl_cfg_entry_point": f"{agents.__name__}:skrl_balance_ppo_cfg.yaml",
    },
)

print("[DEBUG] Balance task registered.")

