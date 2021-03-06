from google.appengine.api import users
from ferris import Controller, route_with
from ferris import settings
from app.services.user_svc import UserSvc
from app.services.auth import only
from app.models.account import Account
from protorpc import protojson


class Main(Controller):

    @route_with(template='/')
    def show(self):
        self.meta.view.template_name = 'angular/app-index.html'
        active_user = UserSvc.get_current_user()
        user = Account.transform_message(active_user)
        self.context['active_user'] = protojson.encode_message(user)
        self.context['logout_url'] = users.create_logout_url('/')
        self.context['commission'] = settings.get('paypal').get('commission')

    @route_with(template='/account')
    @only("=", "Seller")
    def admin(self):
        self.meta.view.template_name = 'angular/admin-index.html'
        active_user = UserSvc.get_current_user()
        user = Account.transform_message(active_user)
        self.context['active_user'] = protojson.encode_message(user)
        self.context['logout_url'] = users.create_logout_url('/')
        self.context['commission'] = settings.get('paypal').get('commission')
