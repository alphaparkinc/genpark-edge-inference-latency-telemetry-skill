from typing import List, Dict, Any

class EdgeInferenceLatencyTelemetry:
    @staticmethod
    def profile(timestamps_sec: List[float]) -> Dict[str, Any]:
        if len(timestamps_sec) < 2:
            return {"error": "Need at least 2 timestamps"}
        ttft_ms = (timestamps_sec[1] - timestamps_sec[0]) * 1000.0
        inter_lat = [
            (timestamps_sec[i] - timestamps_sec[i - 1]) * 1000.0
            for i in range(2, len(timestamps_sec))
        ]
        tpot_ms = sum(inter_lat) / len(inter_lat) if inter_lat else ttft_ms
        sorted_lat = sorted(inter_lat) if inter_lat else [ttft_ms]
        def pct(data, p):
            idx = int(len(data) * p)
            return data[min(idx, len(data) - 1)]
        gen_time = timestamps_sec[-1] - timestamps_sec[1] if len(timestamps_sec) > 1 else 0.001
        throughput = (len(timestamps_sec) - 1) / max(0.001, gen_time)
        return {
            "ttft_ms": round(ttft_ms, 2),
            "tpot_ms": round(tpot_ms, 2),
            "throughput_tokens_sec": round(throughput, 2),
            "jitter_p50_ms": round(pct(sorted_lat, 0.50), 2),
            "jitter_p90_ms": round(pct(sorted_lat, 0.90), 2),
            "jitter_p99_ms": round(pct(sorted_lat, 0.99), 2),
            "total_tokens_decoded": len(timestamps_sec) - 1
        }

    @staticmethod
    def benchmark_telemetry() -> Dict[str, Any]:
        simulated_ts = [0.00, 0.042, 0.061, 0.082, 0.103, 0.124, 0.145, 0.165, 0.187]
        return EdgeInferenceLatencyTelemetry.profile(simulated_ts)
