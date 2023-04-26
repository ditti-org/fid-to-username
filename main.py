from farcaster import Warpcast

# Enter your seed phrase here
# You could also use an access token instead of a seed phrase
seed_phrase = "your seed phrase here"

def read_fid_list_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        return [int(line.strip()) for line in lines]

def fetch_usernames(wcc, fid_list):
    username_list = []
    for fid in fid_list:
        try:
            res = wcc.get_user(fid)
            username_list.append((fid, res.username))
        except Exception as e:
            print(e)
            username_list.append((fid, None))
    return username_list

def write_output_to_file(output_data, filename="result.txt"):
    with open(filename, "w") as file:
        for fid, username in output_data:
            file.write(f"{fid}: {username}\n")

wcc = Warpcast(mnemonic=seed_phrase)

default_fid_list = [1, 2, 3, 4]

filename = input("Enter filename to read fids from (or press Enter to use default fids): ")

try:
    fid_list = read_fid_list_from_file(filename) if filename else default_fid_list
except FileNotFoundError:
    print(f"Error: file '{filename}' not found. Using default fids.")
    fid_list = default_fid_list

fetched_usernames = fetch_usernames(wcc, fid_list)

print(dict(fetched_usernames))

write_output_to_file(fetched_usernames)
