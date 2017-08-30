#!/usr/bin/env python3

import sys

try:
    import yaml
except ImportError as exc:
    raise ImportError("Please install PyYAML") from exc


def main():
    result = {}
    
    if len(sys.argv) < 2:
        raise ValueError("No input file privided")

    input_file = sys.argv[1]

    with open(input_file) as f:
        content = yaml.load(f)

    for entry in content.get('result', []):
        if not entry.get('topics'):
            continue

        for topic in entry['topics']:
            result[topic] = {'occurrence_count': result.get(topic, {}).get('occurrence_count', 0) + 1}

    with open('../raw/' + input_file, 'w') as f:
        yaml.dump(result, f)

if __name__ == '__main__':
    sys.exit(main())

