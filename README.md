# domain-checker
This tool checks domains in a wordlist and outputs the domain and IP address if an A record exists. It also includes a script to generate a list of domain candidates based on words and predefined patterns.

Usage:

domain-checker
python3 domain-checker.py -w /path/wordlist

Options:

-w (required): Specifies the wordlist of domain names.
-o: Allows saving the output result as a file.

domain-gen

python3 domain-gen.py -w /path/wordlist -p www.*.com -o /path/output

Options:

-w (required): Specifies the wordlist of strings to include in domain names.
-p (required): Allows specifying multiple patterns separated by "", where * represents the items listed in the wordlist.
-o (required): Allows saving the output result as a file.