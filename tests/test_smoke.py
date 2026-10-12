from attention_formation.config import RewardConfig, TrainConfig, WorldConfig


def test_rllib_and_torch_on_configured_device():
    import ray.rllib  # noqa: F401
    import torch

    assert torch.zeros(1, device=TrainConfig().device).device.type == TrainConfig().device


def test_d_min_shrinks_with_n():
    reward, world = RewardConfig(), WorldConfig()
    assert reward.d_min(2, world.circle_radius) == reward.d0
    assert reward.d_min(100, world.circle_radius) < reward.d0
