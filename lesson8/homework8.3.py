import json
from pathlib import Path
current_path = Path(__file__)
current_dir = current_path.parent
current_file_name = current_path.stem


workdict = {123454: ('Clark', 35),
            123455: ('Hermiona', 39),
            123456: ('Adam', 19), 123457: ('Soni', 45), 123458: ['Rain', 27], 123459: ('Nina', 23)}
with open(
    current_dir.joinpath("my_json.json"),
    mode="w"
) as w_file:
    json.dump(workdict, w_file, indent=4)