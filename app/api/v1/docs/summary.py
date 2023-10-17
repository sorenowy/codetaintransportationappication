class LoginApiSummaryDocs:
    """Documentation descriptions for Login API urls"""
    
    POST_LOGIN = "Login into the system, receive token for user session."
    POST_LOGOUT = "Logout user from the system, end user session."
    
class RegisterApiSummaryDocs:
    """Documentation descriptions for Register API urls"""
    
    POST_REGISTER = "Register user into the system, create an user, send an email to user inbox"
    GET_VERIFY = "Verify the token from the email URL."
    
class RouteApiSummaryDocs:
    """Documentation descriptions for Transport Routes API urls"""
    
    GET_ALL_ROUTES = "Get all routes in system"
    GET_ROUTE_DETAIL = "Get info from selected route"
    POST_NEW_ROUTE = "Add new route into the system"
    POST_SELECT_ROUTE = "Select route and send notification to user with route cost"
    DELETE_ROUTE = "Delete route from system"
    UPDATE_ROUTE = "Update route data"
    
class UsersApiSummaryDocs:
    """Documentation descriptions for Users API urls"""
    
    CREATE_USER = "Create an user into system"
    GET_ALL_USERS = "Return list of all users in system"
    GET_USER = "Return info about selected user"
    DELETE_USER = "Delete user from system"
    UPDATE_USER = "Update user data"
    