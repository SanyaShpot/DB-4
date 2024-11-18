from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.PanelVideo import PanelVideo

class PanelVideoDAO(GeneralDAO):
    _domain_type = PanelVideo

    def create(self, panel_video: PanelVideo) -> None:
        self._session.add(panel_video)
        self._session.commit()

    def find_all(self) -> List[PanelVideo]:
        return self._session.query(PanelVideo).all()

    def find_by_panel_id(self, panel_id: int) -> List[PanelVideo]:
        return self._session.query(PanelVideo).filter(PanelVideo.panel_id == panel_id).all()
