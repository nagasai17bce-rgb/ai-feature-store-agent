class Service:
    def run(self, value: str):
        features = [
            {"name": "customer_30d_orders", "freshness_min": 12, "quality": "good"},
            {"name": "customer_risk_score", "freshness_min": 45, "quality": "good"},
        ]
        return {
            "query": value,
            "features": features,
            "stale_threshold_min": 60,
            "lineage_available": True,
        }
