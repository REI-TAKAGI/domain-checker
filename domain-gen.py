import sys

def generate_hostnames(wordlist_path, patterns):
    # ワードリストからワードを読み取る
    with open(wordlist_path, 'r') as file:
        words = file.readlines()
    words = [word.strip() for word in words]

    # パターンごとにホスト名を生成する
    hostnames = []
    for pattern in patterns:
        for word in words:
            hostname = pattern.replace('*', word)
            hostnames.append(hostname)

    return hostnames

def write_to_file(hostnames, output_file):
    # ホスト名の候補リストをファイルに書き込む
    with open(output_file, 'w') as file:
        for hostname in hostnames:
            file.write(hostname + '\n')

def main():
    # コマンドライン引数の解析
    if len(sys.argv) < 6 or sys.argv[1] != "-w" or sys.argv[-2] != "-o":
        print("Usage: python3 domain-gen.py -w <wordlist_path> -p <pattern1> <pattern2> ... -o <output_file>")
        sys.exit(1)

    wordlist_path = sys.argv[2]
    patterns = sys.argv[4:-2]
    output_file = sys.argv[-1]

    # ホスト名の候補リストを生成
    hostnames = generate_hostnames(wordlist_path, patterns)

    # ファイルに書き込む
    write_to_file(hostnames, output_file)

if __name__ == "__main__":
    main()
