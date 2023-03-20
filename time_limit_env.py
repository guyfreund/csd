from gymnasium.wrappers.time_limit import TimeLimit


class TimeLimitEnv(TimeLimit):
    def step(self, action):
        observation, reward, terminated, truncated, info = super().step(action=action)
        done = terminated or truncated
        return observation, reward, done, info
