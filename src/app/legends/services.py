from src.app.legends.repository import LegendRepository
from src.app.legends.models import Legend

class LegendService:
    def __init__(self, repository: LegendRepository):
        self.repository = repository
    
    async def create_legend(self, legend: dict):
        data = Legend(**legend)
        return await self.repository.insert(data)