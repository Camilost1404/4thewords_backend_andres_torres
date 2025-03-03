from src.app.legends.repository import LegendRepository
from src.app.legends.models import Legend

class LegendService:
    def __init__(self, repository: LegendRepository):
        self.repository = repository
    
    def get_legends(self):
        legends = self.repository.get_all()
        return legends
    
    def create_legend(self, legend: dict):
        data = Legend(**legend)
        return self.repository.insert(data)
    
    def update_legend(self, legend_id: int, legend: dict):
        return self.repository.update(legend_id, legend)