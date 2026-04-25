from dataclasses import dataclass

@dataclass
class SystemState:
    ahi: float
    ihi: float
    dhi: float
    score: float = 0.0
    tier: str = ""
    action: str = ""
