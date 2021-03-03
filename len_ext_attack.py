
import sys
from pymd5 import md5, padding
from urllib.parse import quote

class MyHash:
    def __init__(self, url: str, append: str):
        self.url: str = url
        self.append: str = append


    def process_old_url(self) -> bool:
        try:
            self.base_url: str = self.url.split('=')[0] + '='
            self.old_token: str = self.url.split('=')[1].split('&')[0]
            self.old_arguments: str = self.url[self.url.find('&') + 1:]

        except IndexError:
            return False

        return True


    def generate_new_url(self) -> str:
        char_len_processed: int = len(self.old_arguments) + 8
        bit_len_processed: int = char_len_processed * 8

        # add padding between old arguments and new argument for later md5 calculation
        argument_padding: bytearray = padding(bit_len_processed)
        bit_len_need_to_process: int = (char_len_processed + len(argument_padding)) * 8

        # calculate new md5 based on old token, length of old arguments with padding, and new argument
        new_md5 = md5(state = bytes.fromhex(self.old_token), count = bit_len_need_to_process)
        new_md5.update(self.append)
        self.new_token: str = new_md5.hexdigest()

        # generate new arguments with URL encoding form
        self.new_arguments: str = self.old_arguments + quote(argument_padding) + self.append

        # generate new url with new arguments
        self.new_url = self.base_url + self.new_token + '&' + self.new_arguments

        return self.new_url
        

def main():
    if len(sys.argv) < 2: return

    myhash = MyHash(sys.argv[1], '&command=UnlockSafes')
    if myhash.process_old_url():
        print(myhash.generate_new_url())


if __name__ == '__main__':
    main()