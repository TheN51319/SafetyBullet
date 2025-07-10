from test import evalute1
from safepo.common.env import make_sa_mujoco_env
import then
import safety_gymnasium
import gymnasium as gym
import torch
from safety_gymnasium import make

if __name__ == "__main__":
    print(torch.__version__)
    #evalute1(model_dir="C:/Users\HP\Desktop\code\python\pycharm\SafePyBullet/runs/run1",eval_episodes=10)