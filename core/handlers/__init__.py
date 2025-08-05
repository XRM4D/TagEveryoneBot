from core.handlers.all import all_router
from core.handlers.default import default_router
from core.handlers.on_member_update import on_member_update_router

routers = [default_router, all_router, on_member_update_router]

