import re


class FlagsHelper:
    def remove_flags(self, arguments: str):
        first_flag_match = re.search(r'--\w', arguments)
        command_end_idx = first_flag_match.start() if first_flag_match else None
        return arguments[0:command_end_idx].strip()

    def extract_flags(self, arguments: str, validators: dict = {}):
        flags = {}
        flag_matches = list(re.finditer(r'--[^ ]+', arguments))
        for idx, match in enumerate(flag_matches):
            flag_name = match.group()[2:]
            next_match = flag_matches[idx + 1] if idx + 1 < len(flag_matches) else None
            flag_value_start_idx = match.end() + 1
            flag_value_end_idx = next_match.start() if next_match else None
            flag_value = arguments[flag_value_start_idx:flag_value_end_idx].strip()
            validator = validators.get(flag_name)
            if not validator or validator(flag_value):
                flags[flag_name] = flag_value
        return flags
