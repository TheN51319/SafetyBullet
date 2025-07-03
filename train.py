from then.utils import get_env,get_params
from safepo.single_agent.ppo_lag import main
if __name__ == "__main__":
    env = get_env("TheNMobileRobotBaseRadarEnv-v0")
    args = get_params()
    main(args=args ,cfg_env=env)