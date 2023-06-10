import starbound as sb
import sys

try:
    path = sys.argv[1].replace("\"", "")
except IndexError:
    print("Required argument of player path")
    exit(0)

slots = int(input("number of slots (120 in the normal version): "))

# ======================================================================

# Open
with open(path, "rb") as f:
    player = sb.read_sbvj01(f)

# ======================================================================

# Clear the hotbar
player.data["inventory"]["customBar"] = [
    [[None, None] for i in range(0, 6)],
    [[None, None] for i in range(0, 6)]
]

# Change inventory
bag_names = [
	"armoryBag",
	"objectBag",
	"foodBag",
	"farmBag",
	"reagentBag",
	"vehicleBag",
	"mainBag",
	"objectBag2",
	"materialBag",
	"hobbyBag"
]
player.data["inventory"]["itemBags"] = {}
for name in bag_names:
    player.data["inventory"]["itemBags"][name] = [None] * slots

# ======================================================================

# Export
with open(path, "wb") as f:
    player = sb.write_sbvj01(f, player)
