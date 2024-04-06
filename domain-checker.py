import sys
import subprocess

def check_domains(wordlist_path, output_file):
    # ドメインリストからドメインを読み取る
    with open(wordlist_path, 'r') as file:
        domains = [domain.strip() for domain in file.readlines()]

    # 結果を画面に出力しつつファイルに保存
    with open(output_file, 'w') as output:
        for domain in domains:
            # DNSルックアップしてAレコードを取得
            dns_result = subprocess.run(['nslookup', '-type=A', domain], capture_output=True, text=True)

            # NXDOMAINが含まれていない場合にのみ出力
            if "NXDOMAIN" not in dns_result.stdout:
                # Aレコードが存在する場合
                if "Address" in dns_result.stdout:
                    # IPアドレスのみを取得
                    ip_address = dns_result.stdout.split("Address: ")[-1].split("\n")[0]
                    result = f"{domain} - {ip_address}\n"
                    print(result)
                    output.write(result)

def main():
    # コマンドライン引数の解析
    if len(sys.argv) < 3 or sys.argv[1] != "-w":
        print("Usage: python3 domain-checker.py -w <wordlist_path> [-o <output_file>]")
        sys.exit(1)

    wordlist_path = sys.argv[2]

    # オプションの解析
    output_file = 'domain_check_results.txt'
    if "-o" in sys.argv:
        output_index = sys.argv.index("-o")
        output_file = sys.argv[output_index + 1]

    # ドメインをチェックして結果を出力
    check_domains(wordlist_path, output_file)

if __name__ == "__main__":
    main()
