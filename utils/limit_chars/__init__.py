class LimitBiggerThanString(Exception):
    def __init__(self, msg):
        super().__init__(self, msg)
        self.msg = msg

    def __str__(self):
        return self.msg


def limit_chars(text: str, limit: int, replace: bool, replace_val: str = "...", replace_whitespace: bool = True) -> str:
    if limit > len(text) and not replace_whitespace: raise LimitBiggerThanString(f"\"{text}\" of length {len(text)} is smaller than given limit of {limit}")
    if limit > len(text): return text.ljust(47)  # idk why 47 it just seems to work well

    if replace:
        return text[:limit - len(replace_val)] + replace_val
    return text[:limit]
