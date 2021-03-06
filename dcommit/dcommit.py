from git import *
from time import (altzone)
import datetime
import argparse

def commit(message, time):
  repo = Repo(".")
  repo.index.commit(message, author_date=time, commit_date=time)

def conv_datestr(string):
  arr = string.split(".")
  arr = list(map(lambda n: int(n), arr))
  return datetime.datetime(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]).strftime("%Y-%m-%d %H:%M:%S")

def main():
  parser = argparse.ArgumentParser(description="dcommit is a git committer that can specify commit date.")
  parser.add_argument("-t", "--time")
  parser.add_argument("-m", "--message")
  args = parser.parse_args()
  time = conv_datestr(args.time)
  message = args.message
  commit(message, time)
  
if __name__ == "__main__":
    main()
