class Solution:

    def encode(self, strs: List[str]) -> str:
        orig = ""
        split_info = ""
        origlen = 0
        for each in strs:
            orig += each
            origlen += len(each)
            split_info += str(origlen) + " "
        return str(origlen) + " " + orig + split_info
    def decode(self, s: str) -> List[str]:
        origlen_others = s.split(" ", maxsplit=1)
        origlen = origlen_others[0]

        len_origlen = len(origlen)
        origlen = int(origlen_others[0])
        others = s[len_origlen+1:]
        orig = others[:origlen]
        split_info = others[origlen:]
        split_info = split_info.split(" ")

        ret = []
        curr_pos = 0
        split_info.pop()
        for each in split_info:
            print(split_info)
            sub_len = int(each)
            ret.append(orig[curr_pos:sub_len])
            curr_pos = sub_len
        return ret
