from src.app.legends.repository import LegendRepository, CategoryRepository
from src.app.legends.models import Legend


class LegendService:
    def __init__(self, repository: LegendRepository):
        self.repository = repository

    def get_legends(self, title: str = None, category: int = None):
        legends = self.repository.get_all(title, category)
        return legends
    
    def get_legend(self, legend_id: int):
        legend = self.repository.get_by_id(legend_id)
        return legend

    def create_legend(self, legend: dict):
        data = Legend(**legend)
        return self.repository.insert(data)

    def update_legend(self, legend_id: int, legend: dict):
        return self.repository.update(legend_id, legend)
    
    def delete_legend(self, legend_id: int):
        return self.repository.delete(legend_id)


class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def get_categories(self):
        legends = self.repository.get_all()
        return legends
