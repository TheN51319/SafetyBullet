from then.utils import get_env,get_params
from safepo.single_agent.ppo_lag import main
if __name__ == "__main__":
    args = get_params()
    main(args=args)