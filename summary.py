from typing import List, Optional

def process_scores(names: List[str], bonus: Optional[int] = None) -> dict:
    summary = {"count": len(names)}
    if bonus:
        summary["total_bonus"] = bonus * len(names)
    return summary


process_scores(["Alice", "Bob"], bonus=10)