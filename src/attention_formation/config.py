"""Projedeki tüm sabitler. Değerler başlangıç tahminidir; implementasyon sırasında ayarlanacak."""

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class WorldConfig:
    """Çember, Gövde ve hareket dinamiği."""

    circle_radius: float = 10.0  # R
    body_radius: float = 0.3  # Gövde yarıçapı (sabit)
    max_accel: float = 2.0  # a_max
    max_speed: float = 3.0  # v_max
    friction: float = 0.5  # hız sönümleme katsayısı (1/s)
    dt: float = 0.1  # simülasyon adımı (s)


@dataclass(frozen=True)
class RewardConfig:
    """Çarpışma eşiği ve ödül ağırlıkları."""

    d0: float = 1.5  # az Agent varken d_min
    alpha: float = 0.5  # kalabalıkta d_min = alpha * eşit aralık
    on_circle_eps: float = 0.2  # Daire Formasyonu için radyal tolerans

    def d_min(self, n_agents: int, circle_radius: float) -> float:
        """Çarpışma eşiği: min(d0, alpha * 2*pi*R / N)."""
        if n_agents <= 1:
            return self.d0
        return min(self.d0, self.alpha * 2 * math.pi * circle_radius / n_agents)


@dataclass(frozen=True)
class TrainConfig:
    """Eğitim ve donanım ayarları."""

    n_max: int = 8  # eğitimde gözlem padding'i için üst sınır
    episode_steps: int = 500  # T
    device: str = "cpu"  # ileride "cuda"
    num_env_runners: int = 4
    num_gpus: int = 0  # GPU'ya geçince 1
