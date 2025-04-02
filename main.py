from bot.config import Config
from bot.engine import GridTradingEngine

if __name__ == "__main__":
    config = Config()
    engine = GridTradingEngine(config)
    engine.run()
