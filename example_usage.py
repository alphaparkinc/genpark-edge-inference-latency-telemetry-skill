from client import EdgeInferenceLatencyTelemetry

def run_example():
    print("=== GenPark Edge Inference Latency Telemetry Example ===")
    ts = [10.0, 10.035, 10.052, 10.070, 10.089, 10.108]
    res = EdgeInferenceLatencyTelemetry.profile(ts)
    print("TTFT (Time To First Token):", res["ttft_ms"], "ms")
    print("TPOT (Time Per Output Token):", res["tpot_ms"], "ms")
    print("Generation Throughput:", res["throughput_tokens_sec"], "tokens/sec")

if __name__ == "__main__":
    run_example()
