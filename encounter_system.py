# encounter_system.py
import random
from dataclasses import dataclass, asdict
from typing import List, Dict


# =====================================================
# 1. ข้อมูลมอนสเตอร์ (Monster Database)
# =====================================================
@dataclass
class Monster:
    name: str
    level: int | str
    hp: int
    atk: int
    defense: int
    exp: int
    drop: str
    skill: str


MONSTER_DB: Dict[str, Monster] = {
    "Sproutkin": Monster("Sproutkin", 1, 40, 8, 4, 15, "Leaf Seed", "มีโอกาส 10% ทำให้พิษ"),
    "Ironleaf Beetle": Monster("Ironleaf Beetle", 2, 60, 10, 8, 25, "Iron Shard", "ลดดาเมจเวท 20%"),
    "Vine Wolf": Monster("Vine Wolf", 3, 80, 12, 6, 35, "Wolf Pelt", "อาจโจมตี 2 ครั้ง"),
    "Sprout Mage": Monster("Sprout Mage", 3, 55, 8, 5, 30, "Mana Fruit", "ใช้เวท Poison Mist"),
    "Nano Sprig": Monster("Nano Sprig", 2, 50, 9, 5, 20, "Nano Core", "โจมตีแบบพลังนาโน"),
    "Event Beast": Monster("Event Beast", "—", 100, 20, 8, 40, "Rare Component", "หลับลึก 1 ตา"),
}


# =====================================================
# 2. การตั้งค่าโอกาสการสุ่ม
# =====================================================
EVENT_TYPES = ["Monster", "No Encounter"]
EVENT_WEIGHTS = [60, 40]

MONSTER_NAMES = list(MONSTER_DB.keys())
MONSTER_WEIGHTS = [4, 4, 4, 4, 4, 1]  # Event Beast หายาก


# =====================================================
# 3. ฟังก์ชันหลัก
# =====================================================
def draw_encounter() -> str:
    """สุ่มว่าจะเจอเหตุการณ์อะไร (มอนสเตอร์หรือว่างเปล่า)"""
    return random.choices(EVENT_TYPES, weights=EVENT_WEIGHTS, k=1)[0]


def draw_monster() -> Monster:
    """สุ่มมอนสเตอร์จากฐานข้อมูล"""
    name = random.choices(MONSTER_NAMES, weights=MONSTER_WEIGHTS, k=1)[0]
    return MONSTER_DB[name]


def simulate_encounter(verbose: bool = True) -> Dict[str, str]:
    """จำลองการจั่วการ์ด 1 ครั้ง"""
    result_type = draw_encounter()

    if verbose:
        print("---------------------------------")
        print("🎴 ผู้เล่นจั่วการ์ด...")

    if result_type == "No Encounter":
        if verbose:
            print("✨ การ์ดว่างเปล่า (No Encounter) — ไม่เกิดอะไรขึ้น")
        return {"Type": "No Encounter"}

    # ถ้าเจอมอนสเตอร์
    monster = draw_monster()
    if verbose:
        print(f"⚔️ คุณพบกับ {monster.name} (LV: {monster.level})")
        print(f"HP: {monster.hp} | ATK: {monster.atk} | DEF: {monster.defense}")
        print(f"EXP: {monster.exp} | Drop: {monster.drop}")
        print(f"Skill: {monster.skill}")
        print("---------------------------------")

    return {"Type": "Monster", "Monster": monster.name}


# =====================================================
# 4. ฟังก์ชันเสริม (จำลองหลายรอบ)
# =====================================================
def simulate_multiple_draws(rounds: int = 10):
    """จำลองการสุ่มหลายครั้ง"""
    summary = {"Monster": 0, "No Encounter": 0}
    monster_counter: Dict[str, int] = {m: 0 for m in MONSTER_NAMES}

    for i in range(rounds):
        result = simulate_encounter(verbose=False)
        summary[result["Type"]] += 1
        if result["Type"] == "Monster":
            monster_counter[result["Monster"]] += 1

    # แสดงผลรวม
    print(f"\n📊 สรุปการจั่วทั้งหมด {rounds} ครั้ง")
    print(f"- เจอมอนสเตอร์ทั้งหมด: {summary['Monster']} ครั้ง")
    print(f"- การ์ดว่างเปล่า: {summary['No Encounter']} ครั้ง")

    print("\n🐉 รายชื่อมอนสเตอร์ที่พบ:")
    for name, count in monster_counter.items():
        if count > 0:
            print(f"  • {name}: {count} ครั้ง")


# =====================================================
# 5. Main (สำหรับรันใน GitHub / CLI)
# =====================================================
if __name__ == "__main__":
    print("=== ระบบสุ่มการ์ดมอนสเตอร์ (Encounter System) ===\n")

    # สุ่มครั้งเดียว
    simulate_encounter()

    # หรือสุ่มหลายครั้ง (ใส่จำนวนได้)
    simulate_multiple_draws(rounds=10)
