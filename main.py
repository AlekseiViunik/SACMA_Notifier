from logic.checker import Checker
from logic.logger import logger as lg

if __name__ == "__main__":

    lg.info("================================================================")
    lg.info("Starting the script...")
    checker = Checker()
    checker.check()
    lg.info("Script finished.")
    lg.info("================================================================")
