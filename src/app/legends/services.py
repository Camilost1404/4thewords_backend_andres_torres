from src.app.legends.repository import LegendRepository

class LegendService:
    def __init__(self, repository: LegendRepository):
        self.repository = repository
    
    async def create_legend(self, legend):
        return await self.repository.insert(legend)