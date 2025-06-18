class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string.
        
        The encoding format is: <lengths>#<strings>
        where lengths is comma-separated list of string lengths
        and strings is concatenation of all strings
        
        Example:
        ["neet","code"] -> "4,4#neetcode"
        
        Args:
            strs: List of strings to encode
            
        Returns:
            Encoded string
        """
        if not strs:
            return ""
        sizes, res = [], ""
        # Get lengths of all strings
        for s in strs:
            sizes.append(len(s))
        # Add lengths separated by commas
        for sz in sizes:
            res += str(sz)
            res += ','
        # Add delimiter
        res += '#'
        # Add all strings
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        
        Reverses the encoding by:
        1. Parsing lengths before '#' delimiter
        2. Using lengths to split remaining string
        
        Example:
        "4,4#neetcode" -> ["neet","code"]
        
        Args:
            s: String to decode
            
        Returns:
            List of decoded strings
        """
        if not s:
            return []
        sizes, res, i = [], [], 0
        # Parse lengths until '#' delimiter
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        # Split remaining string using lengths
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res