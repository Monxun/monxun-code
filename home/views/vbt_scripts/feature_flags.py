import os
from distutils.util import strtobool

from dotenv import load_dotenv

env_files = [f for f in os.listdir() if f.endswith(".env")]
if env_files:
    load_dotenv(env_files[0])

# Use tabulate to print dataframes
USE_TABULATE_DF = strtobool(os.getenv("GTFF_USE_CLEAR_AFTER_CMD", "True"))

# Use clear console after each command
USE_CLEAR_AFTER_CMD = strtobool(os.getenv("GTFF_USE_CLEAR_AFTER_CMD", "False"))

# Use coloring features
USE_COLOR = strtobool(os.getenv("GTFF_USE_COLOR", "True"))

# Select console flair (choose from config_terminal.py list)
USE_FLAIR = os.getenv("GTFF_USE_FLAIR") or "stars"

# Enable interactive matplotlib mode
USE_ION = strtobool(os.getenv("GTFF_USE_ION", "True"))

# Enable Prompt Toolkit
USE_PROMPT_TOOLKIT = strtobool(os.getenv("GTFF_USE_PROMPT_TOOLKIT", "True"))

# Enable Prediction features
ENABLE_PREDICT = strtobool(os.getenv("GTFF_ENABLE_PREDICT", "True"))

# Enable plot autoscaling
USE_PLOT_AUTOSCALING = strtobool(os.getenv("GTFF_USE_PLOT_AUTOSCALING", "False"))

# Enable thoughts of the day
ENABLE_THOUGHTS_DAY = strtobool(os.getenv("GTFF_ENABLE_THOUGHTS_DAY", "False"))

# Quick exit for testing
ENABLE_QUICK_EXIT = strtobool(os.getenv("GTFF_ENABLE_QUICK_EXIT", "False"))

# Open report as HTML, otherwise notebook
OPEN_REPORT_AS_HTML = strtobool(os.getenv("GTFF_OPEN_REPORT_AS_HTML", "True"))