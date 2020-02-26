import pandas as pd
import hashlib

def main():
    dat = 'python'
    hs = hashlib.sha256(dat.encode()).hexdigest()
    print(hs)

if __name__ == '__main__':
  main()
