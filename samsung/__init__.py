from samsung.miner import Samsung

if __name__ == '__main__':
    f = Samsung.read_file()
    t = Samsung.extract_hangeul(f)
    Samsung.change_token(t)