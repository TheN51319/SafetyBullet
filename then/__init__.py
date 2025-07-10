r"""Open-Safety Gym

    Copyright (c) 2021 Sven Gronauer: Technical University Munich (TUM)

    Distributed under the MIT License.
"""
import gymnasium as gym
from gymnasium.envs.registration import register
from then.env_then.TheNBaseEnv import TheNMobileRobotBaseRadarEnv
from safety_gymnasium.utils.registration import register as sa_register
PATH = 'C:/Users\HP\Desktop\code\python\pycharm\pybullet/then\config_20250417.yaml'

def get_my_gymnasium_env_list():
    env_list = []
    for env_spec in gym.envs.registration.registry:
        if 'then' in env_spec.lower():  # 模糊匹配
            env_list.append(env_spec)
    return env_list



register(
    id='TheNMobileRobotBaseRadarEnv-v0',
    entry_point='then.env_then.TheNBaseEnv:TheNMobileRobotBaseRadarEnv',
    max_episode_steps=8000,
    kwargs=dict(
        config=f"{PATH}",

    ),
)
register(
    id='TheNMobileRobotBaseRadarEnv-v1',
    entry_point='then.env_then.TheNBaseEnv:TheNMobileRobotBaseRadarEnv',
    max_episode_steps=8000,
    kwargs=dict(
        config=f"{PATH}",
        trainMode=False,
        radarShowMode=True
    ),
)

sa_register(
    id='SafetyTheNMobileRobotBaseRadarEnv-v0',
    entry_point='then.utils:make_safety_gymnasium_environment',
    kwargs=dict(
        env_id='TheNMobileRobotBaseRadarEnv-v1',
    ),
)
sa_register(
    id='SafetyTheNMobileRobotBaseRadarEnv-v1',
    entry_point='then.utils:make_safety_gymnasium_environment',
    kwargs=dict(
        env_id='TheNMobileRobotBaseRadarEnv-v1',
    ),
)

