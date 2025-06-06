from agent import thinker, critic
from checker import check_math_step, check_logic_step

def cot_verifier_pipeline(question):
    print("Generating reasoning...")
    raw_reasoning = thinker(question)
    print("Raw Reasoning:\n", raw_reasoning)

    print("\nExtracting claims...")
    claim_list = critic(raw_reasoning)
    print("Claims:\n", claim_list)

    print("\nVerifying claims...")
    verified_claims = []
    for i, claim in enumerate(claim_list.split('\n')):
        if "math" in claim.lower():
            valid, result = check_math_step(claim)
        else:
            valid = check_logic_step(claim)

        status = "✅ Valid" if valid else "❌ Invalid"
        print(f"[{i+1}] {status}: {claim}")
        verified_claims.append({"claim": claim, "valid": valid})

    return verified_claims, raw_reasoning
