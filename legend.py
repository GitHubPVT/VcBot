import os
from config import UPSTREAM_REPO

os.system(f"git clone {UPSTREAM_REPO} VcBot")
os.system("cd VcBot && bash start")
