import base64

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '[]'

        for i in range(len(strs)):
            encoded = base64.b64encode(strs[i].encode('latin-1')).decode('ascii')
            strs[i] = encoded

        return ','.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '[]':
            return []

        result = []
        for encoded_str in s.split(','):
            decoded = base64.b64decode(encoded_str).decode('latin-1')
            result.append(decoded)
        
        return result
            
