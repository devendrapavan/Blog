import datetime

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.utils import datetime_to_epoch

SUPERUSER_LIFETIME = datetime.timedelta(minutes=1)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['name'] = user.email
        token['user_id'] = user.id

        if user.is_superuser:
            # token.set_exp(from_time=starttime,lifetime=SUPERUSER_LIFETIME)
            token.payload['exp'] = datetime_to_epoch(token.current_time + SUPERUSER_LIFETIME)

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer