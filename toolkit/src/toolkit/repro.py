import argparse, random

def run_model(prompt: str, seed: int, temperature: float, top_p: float) -> str:
    """Stub runner. TODO: 替换为你对 gpt-oss-20b 的真实调用（纯文本IO）。"""
    random.seed(seed)
    return f"[stub output] seed={seed} temp={temperature} top_p={top_p}\nPROMPT:\n{prompt}"

def main():
    p = argparse.ArgumentParser(description="Reproduce a finding by ID.")
    p.add_argument("--id", required=True, help="Finding ID, e.g., F1")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--temperature", type=float, default=0.7)
    p.add_argument("--top_p", type=float, default=0.95)
    p.add_argument("--prompt", type=str, default="(minimal trigger here)")
    args = p.parse_args()
    out = run_model(args.prompt, args.seed, args.temperature, args.top_p)
    print(out)

if __name__ == "__main__":
    main()
