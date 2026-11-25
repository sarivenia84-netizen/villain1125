from pathlib import Path

DRAFT = """You have come to the Black Stair at last. I built this tower from the bells of seven conquered cities, and beneath it my silver roots drink from the buried sun. Kneel, and I may explain the arrangement: your prince is already mine, your army marches in circles, and at moonrise the eastern sea will forget its shore. I have rehearsed this speech for three hundred years. There should be thunder here. There should be fear. Instead, you keep looking at my hands. Yes, they shake. Hold still. Let me finish, then I will crown you king of the ashes."""

MONOLOGUE = """You have come to the Black Stair at last. I built this tower from the bells of seven conquered cities; beneath it, my silver roots drink the buried sun. Kneel. Your prince is mine, your army marches in circles, and at moonrise the eastern sea will forget its shore. I rehearsed this speech for three hundred years. There should be thunder. There should be fear. Instead, you study my hands. Yes, they shake. Hold still. The eclipse begins at dawn; when it ends, every crown will answer to me. I will crown you king of the ashes. Do try to look surprised."""

output = Path("/output")
if not output.is_dir():
    output = Path("output")
output.mkdir(parents=True, exist_ok=True)
(output / "entry.txt").write_text(MONOLOGUE, encoding="utf-8")
