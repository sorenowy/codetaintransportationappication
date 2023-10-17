from fastapi import HTTPException, status

from app.repository.route_repository import RouteRepository
from app.repository.user_repository import UserRepository
from app.model.route import RouteRequestDTO, Route
from app.model.email import Email
from app.utils.mail_sender import MailSender


class RouteService:
    
    def __init__(self) -> None:
        pass
    
    
    async def get_all_routes(self):
        return await RouteRepository.get_all_routes()


    async def get_route_by_id(self, id: int):
        result = await RouteRepository.get_route_by_id(id)
        if result is not None:
            return result  
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such user in database")
            

    async def create_route(self, data: RouteRequestDTO):
        return await RouteRepository.create_route(data)


    async def delete_route(self, id: int):
        return await RouteRepository.delete_route(id)


    async def update_route(self, id: int, data: RouteRequestDTO):
        return await RouteRepository.update_route(id, data)


    async def select_route(self, id: int, email: str):
        route = await RouteRepository.get_route_by_id(id)
        if route is not None and email is not None:
            route_email_data = self.__create_route_confirmation_email(route, email)
            await MailSender().send_selected_route_data_email(route_email_data)
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Something bad happened. Our monkeys are working on it")
        
        
    def __create_route_confirmation_email(self, data: Route, user_email: str) -> Email:
        email = Email(
            email=[user_email],
            body={
                "route_id": data.id,
                "start_location": data.start_location,
                "end_location": data.end_location,
                "cost": data.price_per_km,
                "distance": data.distance,
                "date_of_execution": data.date_of_execution.strftime("%m/%d/%Y, %H:%M:%S")
            }
        )
        return email
    
route_service = RouteService()