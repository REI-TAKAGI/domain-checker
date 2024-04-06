import sys
import subprocess
from datetime import datetime

# コマンドライン引数からワードリストのパスを取得する
if len(sys.argv) != 3 or sys.argv[1] != "-w":
    print("Usage: python3 domain-checker.py -w <wordlist_path>")
    sys.exit(1)

wordlist_path = sys.argv[2]

# 出力ファイルのパス
output_file = f'domain_check_results_{datetime.now().strftime("%Y%m%d%H%M%S")}.txt'

# ドメインリストからドメインを読み取る
with open(wordlist_path, 'r') as file, open(output_file, 'w') as output:
    domains = file.readlines()
    domains = [domain.strip() for domain in domains]

    # 各ドメインに対して処理を実行
    for domain in domains:
        # DNSルックアップしてAレコードを取得
        dns_result = subprocess.run(['nslookup', '-type=A', domain], capture_output=True, text=True)

        # NXDOMAINが含まれていない場合にのみ出力
        if "NXDOMAIN" not in dns_result.stdout:
            # Aレコードが存在する場合
            if "Address" in dns_result.stdout:
                # IPアドレスのみを取得
                ip_address = dns_result.stdout.split("Address: ")[-1].split("\n")[0]
                output.write(f"{domain} - {ip_address}\n")
