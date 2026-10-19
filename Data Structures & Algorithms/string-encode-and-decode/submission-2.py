class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}>{s}" for s in strs)
            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # find where > is
            j = s.find('>', i + 1)
            # decode from previous tag to > as an int
            elem_len = int(s[i:j])
            # capture the next N elements of the string as a new element
            start_of_slice = j + 1
            end_of_slice = start_of_slice + elem_len
            res += [s[start_of_slice:end_of_slice]]
            i = end_of_slice
        return res


