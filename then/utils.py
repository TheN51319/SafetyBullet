import then
import sys
from pathlib import Path
import os
from distutils.util import strtobool
import copy
import argparse
from safety_gymnasium.wrappers import Gymnasium2SafetyGymnasium
import gymnasium as gym
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def get_env(id:str):
    # check_env(env)
    # env = TheNMobileRobotBaseRadarEnv(trainMode = False,radarShowMode=True)
    env = gym.make(id=id)
    safety_gymnasium_env = Gymnasium2SafetyGymnasium(env)
    return safety_gymnasium_env

def get_env_eval():
    # check_env(env)
    # env = TheNMobileRobotBaseRadarEnv(trainMode = False,radarShowMode=True)
    env = gym.make("TheNMobileRobotBaseRadarEnv-v1")
    safety_gymnasium_env = Gymnasium2SafetyGymnasium(env)
    return safety_gymnasium_env

def get_params():
    path = "C:/Users/HP/Desktop/code/python/pycharm/SafePyBullet/runs"
    if os.path.exists(path):
        path=create_incremental_folder(path)
    else:
        path = Path.cwd()
    custom_parameters = [
        {"name": "--seed", "type": int, "default": 0, "help": "Random seed"},
        {"name": "--use-eval", "type": lambda x: bool(strtobool(x)), "default": False,
         "help": "Use evaluation environment for testing"},
        {"name": "--task", "type": str, "default": "SafetyPointGoal1-v0", "help": "The task to run"},
        {"name": "--num-envs", "type": int, "default": 6, "help": "The number of parallel game environments"},
        {"name": "--experiment", "type": str, "default": "single_agent_exp", "help": "Experiment name"},
        {"name": "--log-dir", "type": str, "default":path, "help": "directory to save agent logs"},
        {"name": "--device", "type": str, "default": "cpu", "help": "The device to run the model on"},
        {"name": "--device-id", "type": int, "default": 0, "help": "The device id to run the model on"},
        {"name": "--write-terminal", "type": lambda x: bool(strtobool(x)), "default": True,
         "help": "Toggles terminal logging"},
        {"name": "--headless", "type": lambda x: bool(strtobool(x)), "default": False, "help": "Toggles headless mode"},
        {"name": "--total-steps", "type": int, "default": 10000, "help": "Total timesteps of the experiments"},
        {"name": "--steps-per-epoch", "type": int, "default": 20000,
         "help": "The number of steps to run in each environment per policy rollout"},
        {"name": "--randomize", "type": bool, "default": False,
         "help": "Wheather to randomize the environments' initial states"},
        {"name": "--cost-limit", "type": float, "default": 25.0, "help": "cost_lim"},
        {"name": "--lagrangian-multiplier-init", "type": float, "default": 0.001,
         "help": "initial value of lagrangian multiplier"},
        {"name": "--lagrangian-multiplier-lr", "type": float, "default": 0.035,
         "help": "learning rate of lagrangian multiplier"},
    ]
    # Create argument parser
    parser = argparse.ArgumentParser(description="RL Policy")
    issac_parameters = copy.deepcopy(custom_parameters)
    for param in custom_parameters:
        param_name = param.pop("name")
        parser.add_argument(param_name, **param)

    # Parse arguments
    args = parser.parse_args()
    return args


def create_incremental_folder(base_path=None):
    """
    在指定路径下创建递增的 run_x 文件夹。

    参数:
        base_path (str): 目标目录路径。若未指定，默认为当前工作目录。
    返回:
        str: 新创建的文件夹路径。
    """
    # 设置默认路径为当前工作目录
    if base_path is None:
        base_path = Path.cwd()
    else:
        base_path = Path(base_path)

    # 确保路径存在
    if not base_path.exists():
        raise FileNotFoundError(f"路径不存在: {base_path}")

    # 查找所有以 run_ 开头的文件夹
    existing_folders = [
        d for d in base_path.iterdir()
        if d.is_dir() and d.name.startswith("run")
    ]

    # 提取数字并排序
    max_num = 0
    for folder in existing_folders:
        try:
            num = int(folder.name.split("run")[1])
            if num > max_num:
                max_num = num
        except (IndexError, ValueError):
            continue  # 忽略非规范命名的文件夹（如 run_xxx 非 run_数字）

    # 生成新文件夹名
    new_folder_name = f"run{max_num + 1}"
    new_folder_path = base_path / new_folder_name

    # 创建文件夹（exist_ok=True 防止重复创建时报错）
    new_folder_path.mkdir(parents=True, exist_ok=True)
    return str(new_folder_path)



