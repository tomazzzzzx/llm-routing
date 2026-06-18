class LLMRouter:
    def __init__(self): self.models = {}
    def register(self, name, provider, cost, caps):
        self.models[name] = {"provider": provider, "cost": cost, "caps": caps}
    def route(self, task):
        cands = [m for m in self.models.values() if self._ok(m, task)]
        return min(cands, key=lambda m: m["cost"]) if cands else None
    def _ok(self, m, t): return True
